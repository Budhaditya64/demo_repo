def arrange(l):
    z=''
    o=''
    t=''
    for i in l:
        if i=='1':
            o+='1'
        elif i=='0':
            z+='0'
        elif i=='2':
            t+='2'
    return o+z+t
if __name__=='__main__':
    n=int(input())
    l=input().split()[:n]
    print(arrange(l))
