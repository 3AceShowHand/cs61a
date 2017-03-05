(define (cddr s)
  (cdr (cdr s))
)

(define (cadr s)
  (car (cdr s)) 
 )

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond
      ((< 0 x) 1)
      ((> 0 x) -1)
      (else 0)
))

(define (square x) (* x x))

(define (pow b n)
  (cond 
      ((= 1 n) b)
      ((= 2 n) (square b))
      ((even? n) square(pow b (/ n 2)))
      (else (* b (square(pow b (/ (- n 1) 2)))))
  )
)

(define (ordered? s)
    (cond
       ((or (= 0 (length s)) (= 1 (length s))) (True))
       ((= 2 (length s)) (cond
                               ((< (cadr s) (car s)) False)
                               (else True)))
       (else (and (ordered? (list(car s) (cadr s))) (ordered? (cdr s)))))
)


(define (nodots s)
    (define (dotted? s) 
                (and (pair? s) (not (or (pair? (cdr s))
                                        (null? (cdr s))
                                        ))))
    (cond
      ((null? s) s)
      ((dotted? s) (list (nodots (car s)) (cdr s)))
      ((pair? s) (cons (nodots (car s)) (nodots (cdr s))))
      (else s)
    )
)


; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond 
        ((empty? s) false)
        ((> (car s) v) False)
        ((= (car s) v) True)  
        (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond 
        ((empty? s) (list v))
        ((contains? s  v) s)
        (else
            (cond
                ((< v (car s)) (cons v s))
                (else (cons (car s) (add (cdr s) v)))
        ))))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          'YOUR-CODE-HERE
          (else nil) ; replace this line
          ))


; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          'YOUR-CODE-HERE
          (else nil) ; replace this line
          ))


(define (extend s t)
    (cond ((empty? s) t)
          (else (list (car s) (extend (cdr s) t)))
    )
)

(define (keep s fn)
    (cond ((empty? s) s)
          (else
          (define kept (keep (cdr s) fn))
          ((not (if (empty? (fn (car s)))))
            (list (car s) kept))
          (else kept)))
)