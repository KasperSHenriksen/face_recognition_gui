import face_recognition
import pickle
import cv2
import numpy as np


class FaceVision():
    def __init__(self):
        # Load encodings once
        data = pickle.loads(open('./data/encodings.pkl', 'rb').read())
        self.encoded_data = data['encodings']
        self.name_data = data['names']
        self.use_face_recognition = False

    def process_image(self, img):
        # Detect and locate faces
        face_locations = self.__locate_faces(img)

        # If no faces are found, return with the original image
        if not face_locations:
            return img

        # Encodings from input image
        encodings = face_recognition.face_encodings(face_image=img, known_face_locations=face_locations, model='small')

        # Identify faces by comparing the new encoding with the previously encoded pickle file
        self.__identify_faces(image=img, face_locations=face_locations, encodings=encodings)

        return img

    def __locate_faces(self, image):
        if self.use_face_recognition is True:

            # Detect faces and recieve their locations
            face_locations = face_recognition.face_locations(img=image, number_of_times_to_upsample=1, model='cnn')
            return face_locations

    def __identify_faces(self, image, face_locations, encodings):
        # Compares saved encodings with new encoding
        for face_bbox, encoding in zip(face_locations, encodings):

            # Find matches
            matches = face_recognition.compare_faces(known_face_encodings=self.encoded_data, 
                                                     face_encoding_to_check=encoding, 
                                                     tolerance=0.01)

            # Calculate votes and find best match
            votes = [np.count_nonzero(m==True) for m in matches]
            highest_vote = max(votes)
            highest_vote_idx = votes.index(highest_vote)
            person_match = self.name_data[highest_vote_idx]

            # Vote threshold, if it doesn't exceed, the voted name will be unknown
            if highest_vote < 20:
                person_match = 'Unknown'

            # Add visualization to image
            t, r, b, l = face_bbox
            cv2.rectangle(image, (l, t), (r, b), (0, 255, 0), 2)        
            cv2.putText(image, person_match, (l, t-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1)
    
    def change_facerec_state(self, button):
        # Inverse boolean
        self.use_face_recognition = not self.use_face_recognition

        # Change text of button depending on its state
        if self.use_face_recognition is True:
            button.configure(text='Disable Face Recognition')
        else:
            button.configure(text='Activate Face Recognition')
