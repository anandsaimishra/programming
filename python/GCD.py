#  Property of Godslayer™
#  Code wirtten by Anand Sai Mishra
#  On : 12/16/19, 5:54 PM

def gcd(a,b):
    while (b !=0 ):
        t = a
        a = b
        b = t % b
    return a
a = int(input("Please enter the first Number : "))
b = int(input("Please enter the second number : "))
# print(a , b)
c = gcd(a,b)
print("The GCD of " + str(a) + " and " + str(b) + " is " + str(c))