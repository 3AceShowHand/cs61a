test = {
  'name': 'fruits',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          logic> (query (fruits-tail date elderberry fig guava))
          Success!
          logic> (query (fruits-tail banana . ?after-banana))
          Success!
          after-banana: (cherry date elderberry fig guava)
          logic> (query (fruits-tail ?e fig guava))
          Success!
          e: elderberry
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
