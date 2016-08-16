test = {
  'name': 'Problem 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Simple test for Place
          >>> place0 = Place('place_0')
          >>> print(place0.exit)
          044ef3c0c6fd739b6260fe6f6cae71dd
          # locked
          >>> print(place0.entrance)
          044ef3c0c6fd739b6260fe6f6cae71dd
          # locked
          >>> place1 = Place('place_1', place0)
          >>> place1.exit is place0
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> place0.entrance is place1
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
