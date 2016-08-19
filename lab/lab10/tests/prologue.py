test = {
  'name': 'Prologue',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a73208f54c693e08d6671873ec5c680d',
          'choices': [
            'Turns input into tokens',
            'Tries to beat Superman',
            'Organizes tokens in a data structure',
            'Makes sure that there are no parentheses errors'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the lexer do?'
        },
        {
          'answer': '5b1b7da5cb56c4ea1c82e9ef2422b59b',
          'choices': [
            'Turns input into tokens',
            'Organizes tokens in a data structure',
            'Evaluates the input'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the parser do?'
        },
        {
          'answer': '8006978b69e088213a68a29f96d158db',
          'choices': [
            'Read-Eval-Print-Loop',
            'Really-Enormous-Purple-Llamas',
            'Read-Eval-Parse-Lex'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does REPL stand for?'
        },
        {
          'answer': 'c8719397b67eeba8c4826370e9fcc052',
          'choices': [
            'Literal(1)',
            '1',
            "Name('1')",
            'Name(1)'
          ],
          'hidden': False,
          'locked': True,
          'question': "What will read('1') output?"
        },
        {
          'answer': 'fd0cb816ca4bc1c16a1b18d7c9899909',
          'choices': [
            'Literal(x)',
            'x',
            'Name(x)',
            "Name('x')"
          ],
          'hidden': False,
          'locked': True,
          'question': "What will read('x') output?"
        },
        {
          'answer': '9964a5ee1d418d42c046ba51a5d20093',
          'choices': [
            "CallExpr(Literal('add'), Literal(3), Literal(4))",
            "CallExpr('add', [Literal(3), Literal(4)])",
            "CallExpr(Name('add'), Literal(3), Literal(4))",
            "CallExpr(Name('add'), [Literal(3), Literal(4)])"
          ],
          'hidden': False,
          'locked': True,
          'question': "What will read('add(3, 4)') output?"
        },
        {
          'answer': '3bb14b5a933e76f7fae5f2cb7ba763a1',
          'choices': [
            "CallExpr(CallExpr(Name('f'), []), [])",
            "CallExpr(CallExpr(Name('f'))",
            "CallExpr(Name('f'), [])",
            "CallExpr(Name('f'), [CallExpr(Name('f'), [])])"
          ],
          'hidden': False,
          'locked': True,
          'question': "What will read('f()()') output?"
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}