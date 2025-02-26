open_list=['[','{','(']
close_list=[']','}',')']
def balance(string):
    stack=[]
    countStars=0
    flag=0
    for i in range(len(string)):
        if string[i] in open_list:
            stack.append(string[i])
            flag=1
        elif string[i] in close_list:
            pos=close_list.index(string[i])
            if ((len(stack) > 0) and (open_list[pos]==stack[len(stack)-1])):
                stack.pop()
                flag=1
            else:
                flag=0
                break
        elif string[i]=='*':
            if string[i+1]=='*':
                if len(stack)>0:
                    if stack[-1] in open_list:
                        countStars+=1
    if len(stack)==0 and flag==1:
        return 'Yes '+str(countStars)
    else:
        return 'No '+str(countStars)
string=input()
print(balance(string))

    
    
            
            
        
