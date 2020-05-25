#names of funcytions should be in lower case
#use an under score if u have two words


def say_hi():
    print("hello user")
print("top")
say_hi()
print("bottom")

#u can make functions more powerful using parameters

def say_hello(name , age):
    print("hello " + name + " you are " + age)

say_hello("bill", "77")