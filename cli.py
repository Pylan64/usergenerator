import random

a = random.randint(0,2048)
b_list = ['parabola', 'equation', 'eagle', 'bird', 'girl', 'boy', 'blacksmith', 'miner', 'chest', 'computer', 'pass', 'fox', 'goat', 'pillow', 'man', 'python']
c_list = ['sleepy', 'furry', 'big', 'nerdy', 'tiny', 'stupid', 'english', 'french', 'deadly', 'violent', 'musical',
         'whimsical', 'scaly', 'yellow', 'maroon', 'feminine']
r = random.randint(0, 15)
d = c_list[r]
x = b_list[r]
b = random.randint(0, 15)
c = b_list[b]


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR



print("Your new username: " + str(d)+str(c)+str(a))
print("Your New password: " + str(random.randint(0, 2048)) + str(x))
