test = {
  'name': 'map',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (map '(1 2 3) (lambda (x) (* x x)))
          528bb0e0761f6149ee147850370d176a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (map '(6 1) (lambda (x) (+ x 1)))
          dc235c94b2aefd44cd748a7d283db593
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
