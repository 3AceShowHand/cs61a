test = {
  'name': 'Coroutines',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
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
          Looking for cs61a
          >>> s.send('cs61b is the best class!')
          Nope!
          >>> s.send('I love cs61a')
          I love cs61a
          >>> s.close()
          >>> s.send('cs61a rocks.') # what is raised if the coroutine has been closed?
          StopIteration
          """,
        }
      ]
    }
  ]
}
