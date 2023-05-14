

def prac(n):
    if n<0:
        return
    print(n)
    prac(n-1)
    
if __name__=="__main__":
    prac(10)