test = {
  'name': 'Problem 5B',
  'partner': 'B',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing ScubaThrower parameters
          >>> scuba = ScubaThrower()
          >>> ScubaThrower.food_cost
          6
          >>> scuba.armor
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing if ScubaThrower is watersafe
          >>> water = Water('Water')
          >>> ant = ScubaThrower()
          >>> water.add_insect(ant)
          >>> ant.place is water
          True
          >>> ant.armor
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing ScubaThrower Inheritance from ThrowerAnt
          >>> def new_action(self, colony):
          ...     raise NotImplementedError()
          >>> def new_throw_at(self, target):
          ...     raise NotImplementedError()
          >>> ThrowerAnt.action = new_action
          >>> test_scuba = ScubaThrower()
          >>> passed = 0
          >>> try:
          ...     test_scuba.action(colony)
          ... except NotImplementedError:
          ...     passed += 1
          >>> ThrowerAnt.action = old_thrower_action
          >>> ThrowerAnt.throw_at = new_throw_at
          >>> test_scuba = ScubaThrower()
          >>> try:
          ...     test_scuba.throw_at(Bee(1))
          ... except NotImplementedError:
          ...     passed += 1
          >>> ThrowerAnt.throw_at = old_throw_at
          >>> passed
          2
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
      >>> old_thrower_action = ThrowerAnt.action
      >>> old_throw_at = ThrowerAnt.throw_at
      """,
      'teardown': r"""
      >>> ThrowerAnt.action = old_thrower_action
      >>> ThrowerAnt.throw_at = old_throw_at
      """,
      'type': 'doctest'
    }
  ]
}
