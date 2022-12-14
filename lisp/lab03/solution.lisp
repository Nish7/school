(defstruct movie
  title  director year type)

(defparameter *size* 3) 

(defvar *db*)

(setf *db* (make-array *size*  :initial-element nil))

(defun add-movie (m)
  "Adds a movie to *db* and returns *db*"
  (dotimes (i *size*)
    (when (and (not (aref *db* i)) (not (in-db? (movie-title m))))
      (setf (aref *db* i) m)
      (return-from add-movie *db*)))
  
  (return-from add-movie nil)
  )

(defun in-db? (title)
  "Returns *db* if movie title is in the database; otherwise returns NIL"
  (dotimes (i *size*)
    (when (and (typep (aref *db* i) 'movie)
               (Equal (movie-title (aref *db* i)) title))
      (return *db*))))


(defun delete-movie (title)
  "Delete a move to *db* and return *db*"
  (dotimes (i *size*)
    (when
        (and (typep (aref *db* i) 'movie)
             (equal (movie-title (aref *db* i)) title)
             (equal (+ *size* -1) i) (> i 0))
      
      (setf (aref *db* i) nil)
      (return *db*)))


  (when (in-db? title)
    (setf *db* (remove-if #'(lambda (i) (if (not (eq i nil)) (eq (movie-title i) title) nil)) *db*))
    (decf *size*)))

(defun replace-movie (m nm)
  (if  (or (not (in-db? (movie-title m))) (in-db? (movie-title nm))) (return-from replace-movie nil))
  
  (dotimes (i *size*)
    (when (and (typep (aref *db* i) 'movie) (eq (movie-title (aref *db* i)) (movie-title m)))
      (setf (aref *db* i) nm)
      (return-from replace-movie t))))

 
(defun num-movies ()
  (do ((i 0 (1+ i))(sum 0))
      ((= i (length *db*)) sum)
    (when (typep (aref *db* i) 'movie) (setf sum (+ sum 1)))))


