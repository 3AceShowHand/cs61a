test = {
  'name': 'nest',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          logic> (query (nest (6 1 a) (6 (1 (a ())))))
          Success!
          logic> (query (nest () ?done-nesting))
          Success!
          done-nesting: ()
          logic> (query (nest (1 2 3) ?nested))
          Success!
          nested: (1 (2 (3 ())))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      logic> (load lab14.logic)
      """,
      'teardown': '',
      'type': 'logic'
    }
  ]
}
