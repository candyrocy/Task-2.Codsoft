import random as rd

def password_length():
    global x1A, x1a, x2, x3
    x1A = int(input("How many upper case alphabets? "))
    x1a = int(input("How many lower case alphabets? "))
    x2 = int(input("How many numbers? "))
    x3 = int(input("How many symbols? "))
    return x1A, x1a, x2, x3

def random_generator(n,n1A,n1a,n2,n3):
    password = ""
    for i in range(0,n1A,1):
        password = password + chr(rd.randrange(65,91,1))
    for i in range(0,n1a,1):
        password = password + chr(rd.randrange(97,123,1))
    for i in range(0,n2,1):
        password = password + chr(rd.randrange(48,58,1)) 
    for i in range(0,n3,1):
        password = password + (chr(rd.randrange(33,48,1)) or chr(rd.randrange(58,65,1)) or chr(rd.randrange(123,127,1)))
    L = list(password)
    rd.shuffle(L)
    for x in range(0,len(L),1):
        print(L[x],end = '')
    
def main():
    x = int(input("Enter length of password: "))
    while x <= 1:
        print("Invalid Input!")
        print("Try again")
        x = int(input("Enter length of password: "))
    password_length()
    
    while x != (x1A+x1a+x2+x3):
        print("Invalid Input!")
        print("Try again")
        x = int(input("Enter length of password: "))
        password_length()
    random_generator(x, x1A, x1a, x2, x3)

main()