my_string="hello"
n=3

list_string=list(my_string)

answer=[]
idx=0
for i in list_string:
    answer+=(list_string[idx]*n)
    idx+=1
answer=''.join(answer)
print(answer)