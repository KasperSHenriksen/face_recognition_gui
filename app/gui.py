import tkinter as tk
from src.facevision import FaceVision
from src.videostream import VideoStream


if __name__ == '__main__':
    # Tkinter window
    root_window = tk.Tk()

    # Window settings
    root_window.title('Face Recognition')
    root_window.geometry('500x540')  # widthxheight+x+y
    root_window.configure(background='#353535')

    # Panel for webcam visualization
    panel = tk.Label(root_window)
    panel.pack(side='top', fill='none')

    # FaceVision init
    face_vision = FaceVision()

    # Webcam stream init
    vs = VideoStream(panel=panel, face_vision=face_vision)
    vs.stream()

    # Button for face recognition
    button_face_recognition = tk.Button(root_window, text='Activate Face Recognition', command=lambda: face_vision.change_facerec_state(button_face_recognition))
    button_face_recognition.pack()

    # Main loop
    root_window.mainloop()
