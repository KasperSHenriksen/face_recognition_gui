import face_recognition
import cv2
from pathlib import Path
import pickle

if __name__ == '__main__':
    print('Starting Encoding..')

    data = {'names': [], 'encodings': []}

    # Path to dataset
    path = Path.cwd() / './data/dataset/'
    
    # Go through each image
    for file_name in path.rglob('*.jpg'):

        # Read image from dataset
        img = cv2.imread(str(file_name))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Locate face
        face_location = face_recognition.face_locations(img, number_of_times_to_upsample=1, model='cnn')

        # Encoding describtions of found face
        encoding = face_recognition.face_encodings(face_image=img, known_face_locations=face_location, model='small')

        # Save info
        data['names'].append(file_name.parent.name)
        data['encodings'].append(encoding)

    # Save encodings in pickle files
    with open('./data/encodings.pkl', 'wb') as f:
        pickle.dump(data, f)

    print('Completed Encoding!')