test = {
  'name': 'foldl',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (foldl (lambda (x y) (+ x y)) 0 '(1 2 3))
          b139541df661b7797a062bd06fae7d77
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (foldl (lambda (x y) (* x y)) 1 '(1 2 3))
          b139541df661b7797a062bd06fae7d77
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab14)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
