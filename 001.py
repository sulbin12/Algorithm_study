list_a=[1,1,1,2,2,2,2,2,2,3,4,5]

check_num_list=[0]*1000

for data in list_a:
    check_num_list[data]+=1

max_idx=check_num_list.index(max(check_num_list))

idx=0
max_data_num=0
for num in check_num_list:
    if(max(check_num_list)==num):
        max_data_num+=1

if(max_data_num>1):
    check=-1
else:
    check=max_idx

print(check)