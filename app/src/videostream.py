import cv2
from PIL import Image, ImageTk


class VideoStream():
    def __init__(self, panel, face_vision):
        self.cap = cv2.VideoCapture(0) # Parameter should correspond to your device


        self.panel = panel
        self.face_vision = face_vision

    def stream(self):
        # Fetch image from camera
        _, frame = self.cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Face recognition 
        img = self.face_vision.process_image(img=img)

        # To Tkinter
        img = Image.fromarray(img)
        tk_img = ImageTk.PhotoImage(img)
        self.panel.imgtk = tk_img
        self.panel.configure(image=tk_img)

        # Run itself again
        self.panel.after(ms=1, func=self.stream)
