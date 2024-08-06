x,y,z= 1,2,3
s1,a,b=4,5,6
u = 7,8,9
print(u)
A=[1,2,
3]
B='XYZ'
Res=(zip(A,B))# list of tuples
print(Res)
A*=3
print(A)
# Function to print full pyramid pattern
def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()
   
full_pyramid(5)

