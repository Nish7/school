(defun a-sum (n p)
  (do* ((i n (1+ i))(sum 0))
       ((> i p) sum)
    (setf sum (+ sum i))))

(defun sum-odd (n p)
  (do ((i n (1+ i))(sum 0))
       ((> i p) sum)
       (when (not (equal (mod i 2) 0))(setf sum (+ sum i)))))

(defun my-function (fn) (funcall fn 1))

(defun sigma (f n p)
  (do* ((i n (1+ i))(sum 0))
       ((> i p) sum)
    (setf sum (+ sum (funcall f i)))))


