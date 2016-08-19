test = {
  'name': 'all',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (all number? '(1 2 3 4))     ; True or False
          345264a1d0d514282219f2cb5e0d6289
          # locked
          scm> (all list? '(1 2 3 4))       ; True or False
          2aaeb70b41cb4614f62005db39466157
          # locked
          scm> (all list? '((1 2) (3 4))))  ; True or False
          345264a1d0d514282219f2cb5e0d6289
          # locked
          scm> (all list? '((1 2 3) 4))     ; True or False
          2aaeb70b41cb4614f62005db39466157
          # locked
          scm> (all (lambda (x) (> x 5)) '(7 8 3 9))
          2aaeb70b41cb4614f62005db39466157
          # locked
          """,
          'hidden': False,
          'locked': True
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