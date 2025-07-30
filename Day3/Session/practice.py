
#for loop
for i in range(6):
    print("Hello World")

#While loop
i = 0
while(i<5):
    print("Hello")
    i += 3

#Nested for loop
for i in range(2):
    print("Andrea")
    for i in range(3):
        print("Brown")
        for i in range(3):
            print("Hello World")

#Nested for loop with multiple variables
for i in range(1,6):
    for j in range(1,6):
        for k in range(1,6):
            for l in range(1,6):
                for m in range(1,6):
                    for n in range(1,6):
                        for o in range(1,6):
                            for p in range(1,6):
                                for q in range(1,6):
                                    for r in range(1,6):
                                        for s in range(1,6):
                                            for t in range(1,6):
                                                for u in range(1,6):
                                                    for v in range(1,6):
                                                        for w in range(1,6):
                                                            for x in range(1,6):
                                                                for y in range(1,6):
                                                                    for z in range(1,6):
                                                                        print(i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)

#Print two functions 1st conditional if else if true get into a for loop and print hello world 5 times





# Function to print "Hello World" or "Not Hello World" based on the condition
def print_hello_world(a,b):
    if(a < b): 
        for i in range(5):
            print("Hello World")
    else:
        for i in range(5):
            print("Not Hello World")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
result = print_hello_world(a,b)