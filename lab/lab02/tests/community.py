test = {
  'name': 'Community',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def troy():
          ...     abed = 0
          ...     while abed < 3:
          ...         britta = lambda: abed
          ...         print(abed)
          ...         abed += 2
          ...     annie = abed
          ...     annie += 1
          ...     abed = 6 # seasons and a movie
          ...     return britta
          >>> jeff = troy()
          0
          2
          >>> shirley = lambda: jeff
          >>> pierce = shirley()
          >>> pierce()
          6
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}