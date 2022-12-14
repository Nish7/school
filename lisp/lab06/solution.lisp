(defun next-state (alist st)
  (cdr (assoc st alist)))

(defun jump-state (alist s x)
  (let ((x_val (next-state alist x)) (s_val (next-state alist s)))
    (if (null s_val) (return-from jump-state x))
    
    (if (typep x_val 'list)
        (dolist (i x_val)
          (if (eq i s) (return-from jump-state s_val)))
        (if (eq s x_val) (return-from jump-state s_val) (return-from jump-state x)))))


(defun next-fork (alist st)
  (if (typep st 'list) (return-from next-fork st))
  (let ((st_val (next-state alist st)))
    (if (or (null st_val) (typep st_val 'list))
        (return-from next-fork st_val) 
        (next-fork alist (jump-state alist st_val st)))))


(defun interleave (a b)
  (cond ((null a)
         (return-from interleave b))
        ((null b)
         (return-from interleave a)))
  (append (list (car a) (car b)) (interleave (cdr a) (cdr b) )))


(defun comb (n k)
  (if (> k n)
      (return-from comb nil))
  (if (or (eq k 0) (eq k n))
      (return-from comb 1))
  (+ (comb (- n 1) (- k 1)) (comb (- n 1) k)))



  
