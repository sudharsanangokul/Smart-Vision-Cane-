import cv2
import pygame
import numpy as np
import torch
import RPi.GPIO as GPIO
import pyttsx3
import time
from picamera2 import Picamera2

# === YOLOv5 Model Load ===

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force\_reload=True)

# === PiCamera2 Setup ===

picam2 = Picamera2()
picam2.preview\_configuration.main.size = (640, 480)
picam2.preview\_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

# === Ultrasonic Sensor Setup ===

TRIG = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# === TTS (Text-to-Speech) ===

engine = pyttsx3.init()
engine.setProperty('rate', 150)

# === Measure Distance ===

def measure\_distance():
GPIO.output(TRIG, False)
time.sleep(0.05)
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

```
while GPIO.input(ECHO) == 0:
    pulse_start = time.time()
while GPIO.input(ECHO) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start
return round(pulse_duration * 17150, 2)
```

# === Speak ===

def speak(msg):
engine.say(msg)
engine.runAndWait()

# === PyGame Setup ===

pygame.init()
screen = pygame.display.set\_mode((640, 480))
pygame.display.set\_caption("Smart Vision Cane - PyGame Stream")

running = True

while running:
frame = picam2.capture\_array()
results = model(frame)
labels = results.names
preds = results.pred\[0]

```
# Render image
results.render()
frame = results.ims[0]  # Already annotated

# Convert to RGB for pygame
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
frame = np.rot90(frame)
frame = pygame.surfarray.make_surface(frame)

screen.blit(frame, (0, 0))
pygame.display.update()

# Voice alert if object detected
if len(preds):
    for det in preds:
        conf = det[4].item()
        if conf > 0.5:
            cls_id = int(det[5])
            label = labels[cls_id]
            distance = measure_distance()

            if distance < 80:
                message = f"{label} ahead at {distance} centimeters"
                print("🔊", message)
                speak(message)
                time.sleep(1.5)  # Avoid repeating too fast
            break

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
        break
```

cv2.destroyAllWindows()
picam2.stop()
GPIO.cleanup()
pygame.quit()
