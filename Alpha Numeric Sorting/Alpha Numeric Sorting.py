def alnumsort(text):
    text=text.split()
    if text[0].isalpha():
        p=1
    else:
        p=2
    nums=[]
    words=[]
    for i in text:
        if i.isdigit():
            nums.append(i)
        else:
            words.append(i.lower())
    words.sort()
    nums.sort()
    output=[]
    if p==2:
        for i in range(len(words)):
            output.append(nums[i])
            output.append(words[i])
    else:
        for i in range(len(words)):
            output.append(words[i])
            output.append(nums[i])
    return ' '.join(output)
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        text=input()
        print(alnumsort(text))
