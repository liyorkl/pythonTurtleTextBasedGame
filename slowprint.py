import sys
import time


def slow_print(text, t=0.0):  # slowprinting
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(t)
