test = {
  'name': 'Problem 3B',
  'partner': 'B',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'ff4b29a10bb0da79aa8ae6ca275be201',
          'choices': [
            'random_or_none, defined in ant.py',
            'random.random(), defined in the "random" module',
            'getitem, defined in the "operators" module'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What function selects a random bee from a list of bees, or
          None, if an empty list is passed in?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing nearest_bee
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> place = colony.places['tunnel_0_0']
          >>> near_bee = Bee(2)
          >>> far_bee = Bee(2)
          >>> colony.places["tunnel_0_3"].add_insect(near_bee)
          >>> colony.places["tunnel_0_6"].add_insect(far_bee)
          >>> hive = colony.hive
          >>> thrower.nearest_bee(hive) is far_bee
          03456a09f22295a39ca84d133a26f63d
          # locked
          >>> thrower.nearest_bee(hive) is near_bee
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> thrower.action(colony)    # Attack!
          >>> near_bee.armor            # Should do 1 damage
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> thrower.place is place    # Don't change self.place!
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Test that ThrowerAnt attacks bees on its own square
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> near_bee = Bee(2)
          >>> colony.places["tunnel_0_0"].add_insect(near_bee)
          >>> thrower.nearest_bee(colony.hive) is near_bee
          True
          >>> thrower.action(colony)   # Attack!
          >>> near_bee.armor           # should do 1 damage
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
