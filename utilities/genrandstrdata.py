import random
import string
class Rdmdata:
    @staticmethod
    def generate_random_string():
    #Generate a random string of letters (default length = 8)
        ranstrdata=''.join(random.choices(string.ascii_letters, k=8))
        rdm_mail=ranstrdata+"@gmail.com"
        return rdm_mail
