


def sub(input,output):
    if len(input)<=0:
        print(output," ") 
        return
    
    sub(input[1:],output+input[0])
    
    sub(input[1:],output)# it will give bcd+a 2 -iteration 
    # input ==cd+b


    
#a
#ab
#abc
#abc




if __name__=="__main__":

    output=" "
    input="abcd"
    sub(input,output)