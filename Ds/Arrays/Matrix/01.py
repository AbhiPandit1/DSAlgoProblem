"""def matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
            inp=int(input(f"Enter O[{i}][{j}]=  "))
            row.append(inp)

        o.append(row)
    return o
"""



def add(A,B):
    o=[]
    for i in range(len(A)):
        n=[]
        for j in range(len(A[0])):
            sum=A[i][j]+B[i][j]
            o.append(sum)
        n.append(o)
        print(n)







#m=int(input("Enter the value of m\n"))
#n=int(input("Enter the value of n\n"))


if __name__=='__main__':
    A=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


    add(A,B)



    



    





