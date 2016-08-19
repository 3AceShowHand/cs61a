test = {
  'name': 'every',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (every >= '(2 3 4 1))
          4fadd151239fbffca0ed8730912ef464
          # locked
          scm> (every >= '(4 2 3 4))
          53d8882431fb1cbe0973ef989dc0376f
          # locked
          scm> (every = '(4 2 3 4))
          b6f3f9774f6939a3640bab704a59d7d8
          # locked
          scm> (every (lambda (x y) (<= (abs (- x y)) 1)) '(4 2 3 4))
          aa5f852aaa515734c55f1ebad51c2f94
          # locked
          scm> (every <= '(2 1 3 4 1))
          acea5146d0f877eeb8c69bc5b3a1dab1
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'quiz03)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}