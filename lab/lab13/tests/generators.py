test = {
  'name': 'Generators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def generator():
          ...     print("Starting here")
          ...     i = 0
          ...     while i < 6:
          ...         print("Before yield")
          ...         yield i
          ...         print("After yield")
          ...         i += 1
          >>> g = generator() # what type of object is this?
          >>> g == iter(g) # equivalent of g.__iter__()
          f3731fc96153a8eaada2c20cb22d07df
          # locked
          >>> next(g) # equivalent of g.__next__()
          e14e4414d2022fd2c1e7e4ffeb9234bb
          bd74cc2cf4494446db895dbd0601cac5
          6c87bbe507608c0c4faab4c3ca4fd206
          # locked
          >>> next(g)
          ae2216fcf09fbddc20c351efd0ffd42b
          bd74cc2cf4494446db895dbd0601cac5
          7d8d680b0d4d5098bec563bb33a0782e
          # locked
          >>> next(g)
          ae2216fcf09fbddc20c351efd0ffd42b
          bd74cc2cf4494446db895dbd0601cac5
          c8e68b9d4bc0f96d2e9c47efcc96a11d
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
          >>> def generator():
          ...     print("Starting")
          ...     i = 2
          ...     while i < 6:
          ...         print("foo", i)
          ...         yield i
          ...         i += 1
          ...         print("bar")
          ...         yield i*2
          ...         i += 2
          >>> h = generator()
          >>> iter(h) == h
          f3731fc96153a8eaada2c20cb22d07df
          # locked
          >>> next(h)
          61f77c6c049e8ff53505aae5265b9523
          4c59b2d8f829bfe875a0ade4f77736ab
          c8e68b9d4bc0f96d2e9c47efcc96a11d
          # locked
          >>> next(h)
          484c1d6dd76dfab2e340b06231c61b70
          4362caea990cde67231b119def59dc09
          # locked
          >>> next(h)
          7c1412e9638c6ca7916d7978221accf3
          9d13ddbbfee3afc75c1e66e13e5db407
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
