
;; (use extras)

(import (scheme base)
        (scheme write)
        ;; (chicken io)
        )


(define (READ x)
  x)

(define (EVAL x)
  x)

(define (PRINT x)
  x)

(define (rep x)
  (PRINT (EVAL (READ x))))

(define (main)
  (display "user> ")
  (let ([line (read-line)])
    (if (eof-object? line)
        #f
        (let ([rep-res (rep line)])
          (display rep-res)
          (newline)
          (main)))))

(main)
