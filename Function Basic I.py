#1
def a():
    return 5
print(a())
#prediction
5; # prints 5 since there is no argument to pass
#output
5

#2
def a():
    return 5
print(a()+a())
#prediction
10; #since there is no argument in either parameter both parameters will return 5 ; 5 + 5 = 10
#output
10

#3
def a():
    return 5
    return 10
print(a())
#prediction
5; #when running a function and the return statement is used the function will return the first value and exit making the 5 to be the printed value
#output
5

#4
def a():
    return 5
    print(10)
print(a())
#prediction
5;# again once return is called inside a function it will exit and since the print(10) isn't listed first the computer will not print value 10
#output
5

#5
def a():
    print(5)
x = a()
print(x)
#prediction
5; None; # x will not return a value since the return statement was not called thus, making 5 to be the only number printed; 5, none
#output
5 
None

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#prediction
3, 5; #since there is no var to add both functions together the total of 8 will not print - leaving only 3 and 5 to be printed
#output
3, 5, #Type Error:unsupported operand type(s) for +: 'NoneType' and 'NoneType'

#7
def a(b,c):
    return str(b)+str(c)

print(a(2,5))
#prediction
#this will not return the total of 2 + 5 since they are strings
#output
25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#prediction
100, 10; #since the if and else statements are true this return value will not be printed -  100 will be printed first since print(b) was called inside the function followed by the else statement printing 10
#output
100, 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#prediction
7, 14, 21 # since we never told the function to add 2 +3 or 5 + 3 this will print both return statements; 21
#output
7, 14, 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#prediction
8; #10 will not print since the first return exits the function once ran
#output
8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#prediction
500, 500, 300, 500; # 500 is printed twice since b = 500 and print b is called before the function - then it will print 500 again after printing 300(within function)
#output
500, 500, 300, 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#prediction
500; 500; 300; 300; 500
#output
500, 500, 300, 500
#return of 300 did not run because the function was only called - not instructed to print

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#prediction
500; 500; 300, 300 #500 is printed twice since b = 500 and print b is called before the function - then 300 twice since b was set to equal the function and set to print
#output
500; 500; 300, 300 

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#prediction
1, 3, 2; #since b() is called within a() function it will print between the two print statements within a() function
#output
1, 3, 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
#prediction
1, 3, 5, 10; #this is similar to #14 however this function also has two return statements 
#output
1, 3, 5, 10