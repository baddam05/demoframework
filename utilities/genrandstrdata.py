import random
import string

def generate_random_string(length=8):
    """Generate a random string of letters (default length = 8)"""
    ranstrdata=''.join(random.choices(string.ascii_letters, k=length))
    return ranstrdata
