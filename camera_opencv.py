import os
import cv2
from base_camera import BaseCamera


class Camera(BaseCamera):
    
    @staticmethod
    def frames():        
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError('Error en el streaming')

        while True:
            # read current frame
            success, img = camera.read()

            # encode as a jpeg image and return it
            if success:
                yield cv2.imencode('.jpg', img)[1].tobytes()
