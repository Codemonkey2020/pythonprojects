print('if statements')
#boolean variable
#(1) simple if statements
is_male = False

if is_male:
    print("you are a male")


#(2) if else statements
is_male = False

if is_male:
    print("you are a male ")
else:
    print("you are a female")

#(3) if else statements using "or " or "and" operator..

is_male = True
is_tall = True

if is_male and is_tall:
    print("your are a tall male ")
else:
    print("you are neither male nor tall")

#(4) the ifelse and else if statemets

is_man = False
is_young = False

if is_man and is_young:
    print("you are a young man ")
elif is_man and not(is_young):
    print("you are an old man ")
elif not(is_man) and is_young:
    print("you are a young woman ")
else:
    print("you are an  old woman ")


