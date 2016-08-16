test = {
  'name': 'Prologue',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '8402a466d219e0b92718fea73daa96f1',
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
          'answer': 'a9212bbb8755bd592e3837e405e7d86a',
          'choices': [
            'Turns input into tokens',
            'Organizes tokens in a data structure',
            'Evaluates the input',
            'Print the result of evaluation'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the parser do?'
        },
        {
          'answer': '81b67964e20b57f553422bbd313c85c5',
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
          'answer': 'bd6a6ff72b06bb0031dd0cca6d48cb67',
          'choices': [
            'literal, name, call expression, lambda expression',
            'number, lambda function, primitive function, string',
            'value, expression, function, number',
            'name, function, number, literal'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What are all the types of expressions in PyCombinator?'
        },
        {
          'answer': 'f82d43eb3eb50a0dee6335e026518795',
          'choices': [
            'number, lambda function, primitive function',
            'number, string, function',
            'name, number, lambda function',
            'number, lambda expression, primitive function'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What are all the types of values in PyCombinator?'
        },
        {
          'answer': '31c5a74b6677eaefe263a04c9fb4459b',
          'choices': [
            'a Number',
            'a String',
            'a Function',
            'an Expression'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does a Literal evaluate to?'
        },
        {
          'answer': 'dbf9769a92374d34e31f4010b8a4ee78',
          'choices': [
            'They are the same thing',
            'A lambda expression is the result of evaluating a lambda function',
            'A lambda function is the result of evaluating a lambda expression',
            'A lambda expression is a call to a lambda function'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What is the difference between a lambda expression and a lambda function?'
        },
        {
          'answer': 'f520b32a65ddff47192e1bb8903eb950',
          'choices': [
            'A method of Expr objects that evaluates the Expr and returns a Value',
            'A method of Expr objects that evaluates a call expression and returns a Number',
            'A method of LambdaExpression objects that evaluates a function call',
            'A method of Literal objects that returns a Name'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which of the following describes the eval method?'
        },
        {
          'answer': 'f96ede45aa43dc3e3a937c190ad4aa6c',
          'choices': [
            'As dictionaries that map variable names (strings) to Value objects',
            'As sequences of Frame objects',
            'As dictionaries that map Name objects to Value objects',
            'As linked lists containing dictionaries'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How are environments represented in our interpreter?'
        },
        {
          'answer': '5ebba5348fc6d0e85fd39023632defc4',
          'choices': [
            'Literal(1)',
            'Number(1)',
            "Name('1')",
            'Name(1)'
          ],
          'hidden': False,
          'locked': True,
          'question': "What will read('1') output?"
        },
        {
          'answer': 'e060f0d7986150912d102d3db300a17b',
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
          'answer': '653e3db72739a557759ade3088b95b82',
          'choices': [
            "CallExpr(Literal('add'), Literal(3), Literal(4))",
            "CallExpr('add', [Literal(3), Literal(4)])",
            "CallExpr(Name('add'), Literal(3), Literal(4))",
            "CallExpr(Name('add'), [Literal(3), Literal(4)])"
          ],
          'hidden': False,
          'locked': True,
          'question': "What will read('add(3, 4)') output?"
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
