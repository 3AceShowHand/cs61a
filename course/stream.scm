(define (int-stream start)
    (cons-stream start (int-stream (+ 1 start)))
)

(define (prefix s k)
    (if (= k 0)
        ()
        (cons (car s) (prefix (cdr-stream s) (- k 1))))
)

(define ones (cons-stream 1 ones))

(define (add-streams s t)
 (cons-stream (+ (car s) (car t))
              (add-streams (cdr-stream s) (cdr-stream t))))

(define ints (cons-stream 1 (add-streams ones ints)))

(define (map-stream f s)
 (if (null? s) nil
     (cons-stream (f (car s))
                (map-stream f (cdr-stream s)))))

(define (filter-stream f s)
 (if (null? s)
    nil
    (if (f (car s))
        (cons-stream (car s)
                (filter-stream f (cdr-stream s)))
        (filter-stream f (cdr-stream s)))))

(define (reduce-stream f s start)
 (if (null? s)
     start
     (reduce-stream f (cdr-stream s) (f start (car s)))))

(define (sieve s)
    (cons-stream (car s)
                (sieve (filter-stream (lambda (x) (not (= 0 (remainder x (car s)))))
                                      (cdr-stream s)))))

(define primes (sieve (int-stream 2)))