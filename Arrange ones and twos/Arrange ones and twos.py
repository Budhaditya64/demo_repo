def arrange(n,l):
    li=[]
    n=list(n)
    if len(n)>l:
        return 'Length Error'
    o=''
    t=''
    z=''
    for i in n:
        if i=='1':
            o+='1'
        elif i=='2':
            t+='2'
        elif i=='0':
            z+='0'
    return o+z+t
if __name__=='__main__':
    l=int(input())
    n=input()
    print(arrange(n,l))
