test = {
  'name': 'Coroutines',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def search(pattern):
          ...     print("Looking for", pattern)
          ...     while True:
          ...         line = (yield)
          ...         if pattern in line:
          ...             print(line)
          ...         else:
          ...             print("Nope!")
          >>> s = search('cs61a') # what type of object is this?
          >>> next(s)
          4b22bd7fb2b1b5f93e629b4da5d74e0b
          # locked
          >>> s.send('cs61b is the best class!')
          f8f78cc510b4af630680175dd40b68b1
          # locked
          >>> s.send('I love cs61a')
          035047f84aa70efd0bf44e1293739336
          # locked
          >>> s.close()
          >>> s.send('cs61a rocks.') # what is raised if the coroutine has been closed?
          667e07a49189d29f2260a9d4c5b618fb
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def truthy():
          ...     print("Starting...")
          ...     num_truths = 0
          ...     while num_truths < 3:
          ...         print("Give me a truth!")
          ...         truth = (yield)
          ...         if truth:
          ...             num_truths += 1
          ...             print("Nice truth.")
          ...         else:
          ...             print("Liar!")
          >>> t = truthy()
          >>> next(t)
          b014445d0c34960e32219ebf79b73dd5
          baabb611fa700f0b5e68eed6eb7fa2bc
          # locked
          >>> t.send(True)
          b6fee5c1830b1c752925f8920fd7ecaf
          baabb611fa700f0b5e68eed6eb7fa2bc
          # locked
          >>> t.send([])
          96a3ea114dad710a2a6649da1c2dcba8
          baabb611fa700f0b5e68eed6eb7fa2bc
          # locked
          >>> t.send(4)
          b6fee5c1830b1c752925f8920fd7ecaf
          baabb611fa700f0b5e68eed6eb7fa2bc
          # locked
          >>> next(t)
          96a3ea114dad710a2a6649da1c2dcba8
          baabb611fa700f0b5e68eed6eb7fa2bc
          # locked
          >>> t.send([1, 2, 3]) # we break out of the loop
          b6fee5c1830b1c752925f8920fd7ecaf
          667e07a49189d29f2260a9d4c5b618fb
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
