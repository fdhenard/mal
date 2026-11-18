
(module reader ()

 (import (scheme base)
         srfi-69
         (scheme write))

 ;; (define (next (reader-obj)))

 ;; (define (peek (reader-obj)))


 (define something (alist->hash-table '((a "b") (c "d"))))

 (display something)

 )
