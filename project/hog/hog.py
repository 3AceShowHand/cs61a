"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    points = []
    while num_rolls > 0:
        point = dice()
        num_rolls -= 1
        points.append(point)
    if 1 in points:
        return 1
    return sum(points)

    # END PROBLEM 1


def split(n):
    """
    Split positive n into all but its last digit and its last digit.
    """
    return n // 10, n % 10


def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon).
    >>> free_bacon(12)
    3
    >>> free_bacon(7)
    8
    >>> free_bacon(49)
    10
    """
    # BEGIN PROBLEM 2
    high, low = split(opponent_score)
    return 1 + max(high, low)
    # END PROBLEM 2


def is_prime(n):
    """
    Return true if n is prime number else False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(100)
    False
    >>> is_prime(13)
    True
    """
    if n < 2:
        return False
    elif n % 2 == 0:
        if n == 2:
            return True
        return False
    mid = n // 2
    for i in range(1, mid):
        if n % (2 * i + 1) == 0:
            return False
    return True


def next_prime(n):
    """
    Return next smallest prime bigger than n
    >>> next_prime(2)
    3
    >>> next_prime(3)
    5
    >>> next_prime(11)
    13
    """
    next = n + 1
    while not is_prime(next):
        next += 1
    return next


def hogtimus_prime(n):
    """
    return next larger prime number if n is a prime number
    else, return n
    >>> hogtimus_prime(2)
    3
    >>> hogtimus_prime(4)
    4
    >>> hogtimus_prime(1)
    1
    """
    if is_prime(n):
        return next_prime(n)
    return n


# Write your prime functions here!

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    if num_rolls == 0:
        score = free_bacon(opponent_score)
    else:
        score = roll_dice(num_rolls, dice=dice)
    score = hogtimus_prime(score)
    return score
    # END PROBLEM 2


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog Wild).
    """
    # BEGIN PROBLEM 3
    sum = score + opponent_score
    if sum % 7 == 0:
        return four_sided
    return six_sided
    # END PROBLEM 3


def max_dice(score, opponent_score):
    """Return the maximum number of dice the current player can roll. The
    current player can roll at most 10 dice unless the sum of SCORE and
    OPPONENT_SCORE ends in a 7, in which case the player can roll at most 1.
    """
    # BEGIN PROBLEM 3
    sum = score + opponent_score
    high, low = split(sum)
    if low == 7:
        return 1
    return 10
    # END PROBLEM 3


def is_swap(score):
    """Returns whether the SCORE contains only one unique digit, such as 22.
    """
    # BEGIN PROBLEM 4
    if score < 10:
        return True
    elif score < 100:
        high, low = split(score)
        return high == low
    high, low = split(score)
    high, mid = split(high)
    return high == mid == low
    # END PROBLEM 4


def swine_swap(score, opponent_score):
    """
    swap score if current score only contains unique digit.
    >>> swine_swap(11, 23)
    23, 11
    >>> swine_swap(5, 11)
    11, 5
    """
    if is_swap(score):
        score, opponent_score = opponent_score, score
    return score, opponent_score


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    while score0 < goal and score1 < goal:
        if player == 0:
            # get the number of dices
            num_rolls = strategy0(score0, score1)
            # get score
            score0 += take_turn(num_rolls, score1, dice=select_dice(score0, score1))
            score0, score1 = swine_swap(score0, score1)
            if score0 >= goal:
                break
            player = other(player)
        else:
            num_rolls = strategy1(score1, score0)
            score1 += take_turn(num_rolls, score0, dice=select_dice(score1, score0))
            score1, score0 = swine_swap(score1, score0)
            if score1 >= goal:
                break
            player = other(player)

    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    @check_strategy
    def strategy(score, opponent_score):
        return n

    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid strategy
    output. All strategy outputs must be non-negative integers less than or
    equal to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert 0 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the 
    strategy returns a valid input. Use `check_strategy_roll` to raise 
    an error with a helpful message if the strategy returns an invalid 
    output.

    >>> always_roll_5 = always_roll(5)
    >>> always_roll_5 == check_strategy(always_roll_5)
    True
    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> fail_15_20 == check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> fail_102_115 == check_strategy(fail_102_115)
    True
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM
    "*** REPLACE THIS LINE ***"
    # END PROBLEM 6

# Experiments


def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    """
    # BEGIN PROBLEM 7
    def average(*args):
        sum = 0
        for i in range(num_samples):
            sum += fn(*args)
        return sum / num_samples
    return average
    # END PROBLEM 7


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN PROBLEM 8
    max_score = 0
    for i in range(1, 11):
        # return a roll dice strategy
        average_roll = make_averaged(roll_dice, num_samples)
        # return average score.
        average_score = average_roll(i, dice)
        if average_score > max_score:
            max_score = average_score
            max_roll = i
    return max_roll
    # END PROBLEM 8


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 9
    if take_turn(0, opponent_score, dice=select_dice(score, opponent_score)) >= margin:
        return 0
    return num_rolls
    # END PROBLEM 9


def swap_strategy(score, opponent_score, margin=5, num_rolls=6):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points and doesn't trigger a
    swap. Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 10
    zero_score = take_turn(0, opponent_score, dice=select_dice(score, opponent_score))
    if is_swap(zero_score):
        if opponent_score > (zero_score + score):
            return 0
    elif zero_score >= margin and not is_swap(zero_score):
        return 0
    return num_rolls
    # END PROBLEM 10


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    This strategy combines these ideas and any other ideas have to achieve a win rate of at least 0.70
    against the baseline always_roll(6) strategy.
    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 10
    # END PROBLEM 10


##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()