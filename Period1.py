import random
import time

def rand_boo():
    rand_num = random.randint(0,10)
    time.sleep(int(rand_num))
    print("boo")


def rand_trt():
    rand_numb = random.randint(1,2)
    if rand_numb == 1:
        print("TRICK")
    if rand_numb == 2:
        print("TREAT")

def string(sentence):
    full_sentence = ("spooky" + str(sentence))
    print(full_sentence)



