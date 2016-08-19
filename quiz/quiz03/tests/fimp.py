test = {
  'name': 'fimp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (fimp '(5 2 4 3) 4)
          2761b7d033932cee9dd78a34dd554f08
          # locked
          scm> (fimp '(5 2 4 4 3) 4)
          2761b7d033932cee9dd78a34dd554f08
          # locked
          scm> (fimp '(5 2 4 4 3) 5)
          2e8b7b726c25cd3ba99adda8bbb3fea7
          # locked
          scm> (fimp '(5 2 4 4 3) 6)
          97f7ea0bb9bb6ef002baa72d4b074a37
          # locked
          scm> (fimp '(5 4 4) 3)
          2761b7d033932cee9dd78a34dd554f08
          # locked
          scm> (fimp '(6 5 5) 4)
          2e8b7b726c25cd3ba99adda8bbb3fea7
          # locked
          scm> (fimp '(6 4 2) 3)
          2761b7d033932cee9dd78a34dd554f08
          # locked
          scm> (fimp '(6 4 2) 8)
          97f7ea0bb9bb6ef002baa72d4b074a37
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