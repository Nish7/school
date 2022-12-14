(defstruct movie
  title  director year type)

(defparameter *size* 3)

(defvar *db* (make-array *size*  :initial-element nil))

(defvar *db-list* nil)  

(defun quicksort (vec comp)
  (when (> (length vec) 1)
    (let ((pivot-i 0)
          (pivot (aref vec (1- (length vec)))))
      (dotimes (i (1- (length vec)))
        (when (funcall comp (aref vec i) pivot)
          (rotatef (aref vec i)
                   (aref vec pivot-i))
          (incf pivot-i)))
      (rotatef (aref vec (1- (length vec)))
               (aref vec pivot-i))
      (quicksort (rtl:slice vec 0 pivot-i) comp)
      (quicksort (rtl:slice vec (1+ pivot-i)) comp)))
  vec)

(defun add-movie (m)
  "Adds a movie to the DB and returns true"
  (dotimes (i *size*)
    (when (null (aref *db* i))
      (setf (aref *db* i) m)
      (return *db*))))

(defun add-movie-list (m)
  "Adds a movie to the end of *db-list* and returns the list"
  (when (not (and (typep m 'movie) (in-db-list? (movie-title m)))) (:= *db-list* (cons m *db-list*))
  )) 

(defun in-db-list? (title)
  (dolist (elem *db-list*)
    (when (equal (movie-title elem) title) (return-from in-db-list? *db-list*)))
  
  (return-from in-db-list? nil))

(defun from-year (y)
  (let ((acc nil))
    (dolist (elem *db-list* acc)
      (when (and (typep elem 'movie) (eq (movie-year elem) y)) (:= acc (cons elem acc))))))
  
(defun sort-title ()
  (setf *db* (remove-if #'(lambda (i) (eq i nil)) *db*))
  (when (eq 0 (length *db*)) (return-from sort-title nil))
  (quicksort *db* #'(lambda (x y)
                      (string< (movie-title x) (movie-title y)))))

(defun sort-year ()
  (setf *db* (remove-if #'(lambda (i) (eq i nil)) *db*))
  (when (eq 0 (length *db*)) (return-from sort-year nil))
  (quicksort *db* #'(lambda (x y)
                      (< (movie-year x) (movie-year y)))))
