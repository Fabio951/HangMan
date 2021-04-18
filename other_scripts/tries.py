import time
import sys

print("ciao", end="\r")

time.sleep(1)

print("ciao2")

time.sleep(1)

print("ciao3", end="\r")
sys.stdout.flush()

time.sleep(1)

print("ciao4", end="\r")
