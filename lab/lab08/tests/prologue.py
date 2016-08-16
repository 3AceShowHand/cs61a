test = {
  'name': 'Prologue',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> brians_car = Car('Tesla', 'Model S')
          >>> brians_car.color
          80d498e7f8cbec95df437d78b524521a
          # locked
          >>> brians_car.paint('black')
          1b93d7f83f69e1b06c11954d997cf04f
          # locked
          >>> brians_car.color
          9ccdc90cb9022261857bac913f59ab65
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> brians_car = Car('Tesla', 'Model S')
          >>> brians_truck = MonsterTruck('Monster Truck', 'XXL')
          >>> brians_car.size
          8b1b16415e2c0ff19bfb5c4e54f6f878
          # locked
          >>> brians_truck.size
          c5ace7df7c7b66fd8733af007dd50564
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
