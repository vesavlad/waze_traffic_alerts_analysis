import ctypes
import time

mouse_event = ctypes.windll.user32.mouse_event
MOUSEEVENTF_MOVE = 0x0001

while True:
    mouse_event(MOUSEEVENTF_MOVE, 10, 10, 0, 0)
    time.sleep(5)#sleep for 60 seconds