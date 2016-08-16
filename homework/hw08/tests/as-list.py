test = {
  'name': 'as-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (as-list (leaf 3))
          769d41632a5c82230b000ccca54bbb1f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (as-list ())
          7e44d32911eb855f7a970358ab156a57
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (as-list (tree 20 (leaf 19) (leaf 30)))
          51adaa030929c8d7c4d64845477fadad
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (as-list (tree 20 (tree 19 (leaf 10) ()) (tree 30 (leaf 25) (leaf 35))))
          7a0c04c7e74125d733ec2cbe08416a21
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
