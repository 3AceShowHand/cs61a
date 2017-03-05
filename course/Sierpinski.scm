(define (repeat k fn)
    ;Reapt fn k times.
    (if (> k 1)
        (begin (fn) (repeat (- k 1) fn)
        (fn)))
)


(define (tri fn)
    (repeat 3 (lambda () (fn) (lt 120))) 
)

(define (sier d k)
    (tri (lambda () (if (= k 1) (fd d) (leg d k)))))


(define define(leg d x):
        (sier (/ d 2) (k-1))
        (penup)
        (fd d)
        (pendown))
