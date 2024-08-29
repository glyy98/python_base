i=1  
j=1   
while i<=10 :
    while j<5:
        print(f'符合两个条件i是{i},j是{j}')
        j=j+1
    print(f'只符合一个条件i是{i},j是{j}')
    i=i+1
    
print(f'都不符合,i是{i},j是{j}')