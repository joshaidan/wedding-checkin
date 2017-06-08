import picamera

class Camera:

    def __init__(self):
        self.camera = picamera.PiCamera()

    def snap_photo(self, photo_count, name):
        filename = str(photo_count) + '_' + name + '.jpg'
        self.camera.capture('photos/' + filename)