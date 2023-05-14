
def natural(n):
    if n<1:
        return n
    return n + natural(n-1)












if __name__=="__main__":
    natural(20)

