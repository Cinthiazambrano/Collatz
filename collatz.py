#Cinthia Zambrano, 2018-11-02
#The Collatz conjecture program

n=int(input("Give number: "))
while n!=1:
    if n%2==0:
        n=n/2
        print(n)
    else:
        n=(n*3)+1
        print(n)

