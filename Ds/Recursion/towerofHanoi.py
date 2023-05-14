#Thre tower given 
# Tower A have some disc in ascending order of there size
# now we have to move the disc from tower a to tower b and c 
# According to the ques so that it bigger tower always remain at top
# you can only take out one disc at a time

def Toh(n,A,B,C):
    if n==1:
        print("Move from 1 to A to C")
    else:
        Toh(n-1,A,C,B)
        print("Move n from A To C")
        Toh(n-1,B,A,C)
