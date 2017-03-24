(define (reduce f s start)
 (if (null? s)
    start
    (reduce f (cdr s) (f start (car s)))))

(define (range a b)
 (if (>= a b) nil (cons a (range (+ a 1) b))))

(define (sum s)
 (reduce + s 0))

(define (prime? x)
 (if (<= x 1)
    false
    (null? (filter (lambda (y) (= 0 (remainder x y)))
                   (range 2 x)))))

(define (sum-prime a b)
 (sum (filter prime? (range a b))))
