test = {
  'name': 'Structure',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'e7df6bc0dc456d2631ac280dcebe1e2d',
          'choices': [
            'tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])',
            'tree(1, (tree(2), tree(3, (tree(5))), tree(5)))',
            'tree(2, [tree(1, tree(3, tree(5)))], tree(4))',
            'tree(1, [tree(2), tree(3), tree(4)], tree(5))'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          The tree structure for the following is:
              1
            / | \
           2  3  4
             /
            5
          """
        },
        {
          'answer': 'b87929dc6098331f794e03405a9c6e64',
          'choices': [
            '1, 6, 5',
            '1, 6, 5, 4',
            '7, 6, 1, 5, 4',
            'None of the above'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Given the following tree structure, what are all the leaves?
                7
              / | \
             3  2  4
            /  /|
           6  1 5
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}