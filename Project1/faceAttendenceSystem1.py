import cv2
import dlib
import numpy as np
import os

# Path to the directory containing the student images
directory = "C:\\Users\\A1 Computer\\Desktop\\faceAttendanceSystem\\students"
shape_predictor_path = 'shape_predictor_5_face_landmarks.dat'
face_rec_model_path = 'dlib_face_recognition_resnet_model_v1.dat'

# Initialize the face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor_path)
face_rec_model = dlib.face_recognition_model_v1(face_rec_model_path)

def get_face_encoding(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    if len(faces) == 0:
        return None
    shape = predictor(gray, faces[0])
    face_descriptor = face_rec_model.compute_face_descriptor(image, shape)
    return np.array(face_descriptor)

# Load and encode all student images
student_encodings = []
student_names = []  # List to store the filenames without extensions
student_images = os.listdir(directory)
for filename in student_images:
    img_path = os.path.join(directory, filename)
    image = cv2.imread(img_path)
    if image is not None:
        encoding = get_face_encoding(image)
        if encoding is not None:
            student_encodings.append(encoding)
            student_names.append(os.path.splitext(filename)[0])  # Store the filename without extension

# Function to compare faces
def compare_faces(encoding1, encoding2, tolerance=0.6):
    return np.linalg.norm(encoding1 - encoding2) <= tolerance

# Flag to control scanning
scan_enabled = False
present_students = []  # List to track students who have been marked present

def on_mouse_click(event, x, y, flags, param):
    global scan_enabled
    if event == cv2.EVENT_LBUTTONDOWN:
        scan_enabled = True

# Capture video from the webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow("Face Attendance System")
cv2.setMouseCallback("Face Attendance System", on_mouse_click)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image from webcam.")
        break

    if scan_enabled:
        test_encoding = get_face_encoding(frame)
        if test_encoding is not None:
            match_found = False
            for i, student_encoding in enumerate(student_encodings):
                if compare_faces(test_encoding, student_encoding):
                    if student_names[i] not in present_students:
                        global name_present
                        name_present = student_names[i]
                        print(student_names[i], "is present")  # Print the name of the matched image without extension
                        present_students.append(student_names[i])
                        match_found = True
                        break
            if not match_found:
                print("not a student ")
        else:
            print("No face detected in the scanned photo.")
        
        scan_enabled = False

    cv2.imshow("Face Attendance System", frame)
    
    # Exit if 'ESC' is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Determine the absent students
global absent_students
absent_students = [student for student in student_names if student not in present_students]

cap.release()
cv2.destroyAllWindows()
