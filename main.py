import random as r
from time import*


def checkerror(userin,test):
    error=0
    for a in range(len(test)):
       try:
           if test[a]!=userin[a]:
                error= error+1
       except:
          error = error + 1
    return error
def time_speed(time_s,time_e,userinput):
    time_delay=time_e-time_s
    roundtime=round(time_delay,2)
    speed=len(userinput)/roundtime
    return round(speed)


test=['hello saqib',"My name is Saqib Hussain, and I am currently pursuing a Bachelor of Science in Computer Science (BSCS).","I am focused on honing my skills in Python, a versatile and powerful programming language. My studies include various aspects of computer science, and I am particularly interested in web development, data analysis, and artificial intelligence. I am passionate about leveraging technology to solve real-world problems. I look forward to contributing to innovative projects and continuously expanding my knowledge in the field" ]

test1=r.choice(test)
print(test1)
print()
print()
time1=time()
userinput=input("***Type*** ")
time2=time()
print("speed",time_speed(time1,time2,userinput))
print("error",checkerror(test1,userinput))