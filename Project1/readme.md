
# Face Attendance System

A Python-based **Face Attendance System** using **Dlib** and **OpenCV** to detect and recognize student faces in real-time via webcam.

## Project Structure

This is how your folder should be organized:

faceAttendanceSystem/  
├── students/  
│   ├── john_doe.jpg  
│   ├── jane_smith.jpg  
│   └── ...  
├── shape_predictor_5_face_landmarks.dat  
├── dlib_face_recognition_resnet_model_v1.dat  
├── face_attendance.py  
└── README.md  

## Features

- Real-time face detection via webcam  
- Face recognition using Dlib face encodings  
- One-click scan triggered by mouse  
- Marks students as **present**  
- Shows **absent** students after session ends  

## Requirements

Install the necessary Python packages:

```
pip install dlib opencv-python numpy
```

**Note:** Dlib may require CMake and Visual Studio Build Tools on Windows. Use Anaconda or prebuilt wheels if installation fails.

## Preparing Student Images

- Place images inside the `students/` folder.
- Filenames (without extension) are treated as student names.

**Example:**

students/  
├── ali_khan.jpg → "ali_khan"  
├── sara_malik.png → "sara_malik"

Use **clear, front-facing** images.

## How to Run

Run the following command:

```
python face_attendance.py
```

- A webcam window titled **Face Attendance System** will appear.
- **Click anywhere in the window** to trigger a face scan.
- If a known face is matched, the name will be printed as **present**.
- If not matched, it will print **not a student**.
- If no face is detected, it will print **No face detected in the scanned photo.**
- Press **ESC** key to exit the application.

## Code Summary

1. Load Dlib models.
2. Encode all student images in the `students/` folder.
3. On each webcam frame + mouse click:
   - Detect and encode face.
   - Compare with known student encodings.
   - If matched → mark student as **present**.
   - Others are marked **absent** after exit.

## Adjust Match Sensitivity

Inside the code:

```python
def compare_faces(encoding1, encoding2, tolerance=0.6):
```

- Lower **tolerance** = stricter match  
- Higher **tolerance** = more lenient match

## Sample Output

```
ali_khan is present  
sara_malik is present  
not a student  
No face detected in the scanned photo.
```

After pressing ESC:

```
Absent students: ['john_doe', 'hamza_raza']
```

## Future Improvements

- Export attendance to CSV  
- Multi-face detection  
- GUI interface with buttons  
- Google Sheets integration  
- Auto-download models  

## Author

**Author:** Muhammed Mohsin  
**Title:** The best software engineer in the whole world  

## References

- Dlib: http://dlib.net/  
- OpenCV Docs: https://docs.opencv.org/  
- NumPy Docs: https://numpy.org/doc/  
- Dlib Pretrained Models: http://dlib.net/files/
