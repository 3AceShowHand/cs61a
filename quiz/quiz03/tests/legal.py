test = {
  'name': 'legal',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (legal '(3 7) 5)
          fe0d386b7c8a9c8c0bae1111d11e5df1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (legal '(5 2 4 3) 4)
          ((5 . True) (2 . False) (4 . True))
          scm> (legal '(4 2 4 3) 4)
          ((4 . True) (2 . False) (4 . True))
          scm> (legal '(5 2 4 4 3) 5)
          ((5 . True) (2 . False))
          scm> (legal '(5 2 4 4 3) 6)
          ((2 . False))
          scm> (legal '(5 4) 3)
          ((5 . True) (4 . True))
          scm> (legal '(5 4 4 3) 6)
          ((3 . False))
          scm> (legal '(4 8 9) 5)
          ((4 . False) (8 . True) (9 . True))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'quiz03)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}