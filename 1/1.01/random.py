import random
import string
import time

def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

random_string = generate_random_string()

while True:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Random String: {random_string}")
    time.sleep(5)
