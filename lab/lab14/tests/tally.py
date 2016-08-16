test = {
  'name': 'tally',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (assert-equal '((obama . 1)) '(tally '(obama)))
          f9e706169d2749c2205b7f7f50980fd9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (assert-equal '((taft . 3)) '(tally '(taft taft taft)))
          f9e706169d2749c2205b7f7f50980fd9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (assert-equal '((jerry . 2) (brown . 1)) '(tally '(jerry jerry brown)))
          f9e706169d2749c2205b7f7f50980fd9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (assert-equal '((jane . 5) (jack . 2) (jill . 1)) '(tally '(jane jack jane jane jack jill jane jane)))
          f9e706169d2749c2205b7f7f50980fd9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (assert-equal '((jane . 5) (jack . 2) (jill . 1)) '(tally '(jane jack jane jane jill jane jane jack)))
          f9e706169d2749c2205b7f7f50980fd9
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
