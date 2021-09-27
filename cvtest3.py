from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
from pupil_apriltags import Detector
import time

def time_ms():
	return time.time() * 1000

w, h = (320, 240)
f = 18

old_time = time_ms()
start_time = time_ms()

camera = PiCamera()
camera.resolution = (w, h)
camera.framerate = f
rawCapture = PiRGBArray(camera, size=(w, h))

time.sleep(0.1)

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), f, (w, h))

detector = Detector(families='tag36h11', nthreads=1)

print("started")

for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
	image = frame.array

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	fps = round(1000 / (time_ms() - old_time))
	old_time = time_ms()
	
	results = detector.detect(gray)
	print("Tags detected: ", len(results))

	for tag in results:
		c = tag.corners
		cv2.line(image, (round(c[0][0]), round(c[0][1])), (round(c[1][0]), round(c[1][1])), (0, 0, 255))
		cv2.line(image, (round(c[1][0]), round(c[1][1])), (round(c[2][0]), round(c[2][1])), (0, 0, 255))
		cv2.line(image, (round(c[2][0]), round(c[2][1])), (round(c[3][0]), round(c[3][1])), (0, 0, 255))
		cv2.line(image, (round(c[3][0]), round(c[3][1])), (round(c[0][0]), round(c[0][1])), (0, 0, 255))

	cv2.putText(image, str(fps), (10, h-2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

	out.write(image)
	
	rawCapture.truncate(0)

	if time_ms() - start_time > 10000:
		break

out.release()
cv2.destroyAllWindows()
