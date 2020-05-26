# print(random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*()', 5))
import random


def ranstr(num):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt


salt = ranstr(100)
print(salt)
