import random

def id_gen(length):
    key = ""
    file = open("base-16.txt","r")
    chars = file.read()
    for i in range(length):
        key += chars[random.randint(0, len(chars)-1)]
    return key

print(id_gen(9))