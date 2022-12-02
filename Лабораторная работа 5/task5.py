import random
from random import sample
def get_random_password(n=8) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyz0123456789'
    password = ''
    i = ''.join(random.sample(alphabet, n))
    password += str(i)
    return (password)

print(get_random_password(n=8))

