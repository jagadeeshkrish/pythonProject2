# OS modules
# OS Modules use to interact with the operating system
# get working dir, change dir, file exist, file name,size file, Evnvironment
import math
import os
import datetime

print(os.name)
print(math.pi)
print(os.getcwd())
#os.mkdir("Jaga")
#os.remove("Jaga")
print(datetime.datetime.now())
for root,dir,files in os.walk(" Users\jagad\PycharmProjects\pythonProject2\ex05072024"):
#print(os.listdir("Users\jagad\PycharmProjects\pythonProject2\ex07062024"))
#os.chdir(" C:\Users\jagad\PycharmProjects\pythonProject2\ ")
#print(os.getcwd())