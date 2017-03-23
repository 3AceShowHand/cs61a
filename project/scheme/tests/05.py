test = {
  'name': 'Question 5',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> expr = read_line('(+ 2 2)')
          >>> expr
          Pair('+', Pair(2, Pair(2, nil)))
          >>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
          4
          >>> expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
          >>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
          12
          >>> expr = read_line('(yolo)')
          >>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
          SchemeError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (+ 2 3) ; Type SchemeError if you think this errors
          5
          scm> (* (+ 3 2) (+ 1 7)) ; Type SchemeError if you think this errors
          40
          scm> (1 2) ; Type SchemeError if you think this errors
          SchemeError
          scm> (1 (print 0)) ; check_procedure should be called before operands are evaluated
          SchemeError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
