test = {
  'name': 'Odds and Evens',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class OddNaturalsIterator():
          ...     def __init__(self):
          ...         self.current = 1
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current += 2
          ...         return result
          ...     def __iter__(self):
          ...         return self
          >>> odds = OddNaturalsIterator()
          >>> odd_iter1 = iter(odds)
          >>> odd_iter2 = iter(odds)
          >>> next(odd_iter1)
          7cd20da6435c318b417f99ab831ac85e
          # locked
          >>> next(odd_iter1)
          7cce957d5689f75737e35919f54283e1
          # locked
          >>> next(odd_iter1)
          8d3d95b1350833ea7b81c9454d1af611
          # locked
          >>> next(odd_iter2)
          54038328fa76561333de39372fc08510
          # locked
          >>> next(odd_iter1)
          24501e5e22e5149e7702cb00bdfc079c
          # locked
          >>> next(odd_iter2)
          0365077a13b0df347c6b012c9ef93a7c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> class EvenNaturalsIterator():
          ...     def __init__(self):
          ...         self.current = 0
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current += 2
          ...         return result
          ...     def __iter__(self):
          ...         return EvenNaturalsIterator()
          >>> evens = EvenNaturalsIterator()
          >>> even_iter1 = iter(evens)
          >>> even_iter2 = iter(evens)
          >>> next(even_iter1)
          7fc207623480272cc31bc20c8f8c512e
          # locked
          >>> next(even_iter1)
          32cd207d18df99546ca7a56bc36ed715
          # locked
          >>> next(even_iter1)
          a1e11865670a42d05e20b9a3455dc457
          # locked
          >>> next(even_iter2)
          7fc207623480272cc31bc20c8f8c512e
          # locked
          >>> next(even_iter2)
          32cd207d18df99546ca7a56bc36ed715
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
          >>> class DoubleIterator():
          ...     def __init__(self):
          ...         self.current = 2
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current += result
          ...         return result
          ...     def __iter__(self):
          ...         return DoubleIterator()
          >>> doubleI = DoubleIterator()
          >>> dIter = iter(doubleI)
          >>> next(doubleI)
          32cd207d18df99546ca7a56bc36ed715
          # locked
          >>> next(doubleI)
          a1e11865670a42d05e20b9a3455dc457
          # locked
          >>> next(dIter)
          32cd207d18df99546ca7a56bc36ed715
          # locked
          >>> next(dIter)
          a1e11865670a42d05e20b9a3455dc457
          # locked
          >>> next(doubleI)
          2bfcd627609c82ebd017c2edfad00c89
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> class ThreeIterator():
          ...     def __init__(self):
          ...         self.current = 10
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current -= 3
          ...         return result
          ...     def __iter__(self):
          ...         return self
          >>> threeI = ThreeIterator()
          >>> tIter = iter(threeI)
          >>> next(threeI)
          6ed2911f88b2fb526846619209f10214
          # locked
          >>> next(threeI)
          54038328fa76561333de39372fc08510
          # locked
          >>> next(tIter)
          a1e11865670a42d05e20b9a3455dc457
          # locked
          >>> next(tIter)
          7cd20da6435c318b417f99ab831ac85e
          # locked
          >>> next(threeI)
          7a429f5c68b108c220ab5adf7b558ce2
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
