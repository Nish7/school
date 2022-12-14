(defun arith-eval (expr)
  "EXPR is a list of symbols that may include:
square brackets, arithmetic operations, and numbers."
  (let ((acc_a 0) (acc_b 0))
    (dolist (i expr)
      (case i
        (([) (incf acc_a))
        ((]) (incf acc_b))))

    (if (not (equal acc_a acc_b))
        (return-from arith-eval "Error")))
  
  (let ((ops ())
        (vals ())
        (op nil)
        (val nil))
    (dolist (item expr)
      (case item
        ([ ) ; do nothing
        ((+ - * / ^ SDIV MAXF FACT) (push item ops))
        (] (setf op (pop ops) val (pop vals))
         (case op
           (+ (setf val (+ val (pop vals))))
           (- (setf val (- (pop vals)  val)))
           (* (setf val (* val (pop vals))))
           (/ (setf val (/ (pop vals)  val)))
           (^ (setf val (expt (pop vals) val)))
           (SDIV (setf val (/ (+ (* -1 (pop vals)) (pop vals)) val)))
           (MAXF (setf val (max (pop vals) (pop vals) val)))
           (FACT (setf val (factorial val))))
         (push val vals))
        (otherwise (push item vals))))
    (pop vals)))

(defun factorial (n &optional (acc 1))
  (if (<= n 1) acc
      (factorial (- n 1) (* acc n))))


  
