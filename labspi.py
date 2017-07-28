import hashlib
import os
import picamera
from gcloud import storage
from google.cloud import vision

## snap picture...

with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.capture('foo.jpg')
#    camera.close()

## hash for upload name

block_size=65536
sha256 = hashlib.sha256()
with open('foo.jpg', 'rb') as f:
    for block in iter(lambda: f.read(block_size), b''):
        sha256.update(block)
    uploadhash = sha256.hexdigest()
uploadname = '%s.jpg' % uploadhash

## upload file to gcp...

client = storage.Client()
bucket = client.get_bucket('labelmaker')
blob2 = bucket.blob('incoming/%s' % uploadname)
blob2.upload_from_filename(filename='foo.jpg')

os.remove('foo.jpg')

### construct gs uri

newURI = 'gs://labelmaker/incoming/%s' % uploadname

## get labels

vision_client = vision.Client(project='lablemaker')
image = vision_client.image(source_uri = newURI)
labels = image.detect_labels()
print('Labels:')
for label in labels:
    print(label.description)

