(defun check-loop (g s acc)
  (let ((s_val (next-state g s)))
    (push s acc)
    (cond ((listp s_val)
           (dolist (i s_val)
             (if (eq (check-loop g i acc) t) (return-from check-loop t))))
          ((or (null s_val) (member s_val acc)) (return-from check-loop t))
          (t (check-loop g s_val acc)))))


(defvar *acc* ())

(defun has-loop (g s)
  (check-loop g s *acc*))

(defun next-state (alist st)
  (cdr (assoc st alist)))
