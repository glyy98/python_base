shen=str(input("学历："))
ti=int(input("工作年限"))
#以下代码的意思就是本科or经验，有一个达标就行
# if shen == "本科" :#条件1  #如果是本科，直接就通过了，最后打印本科通过
#     print("offer")
# elif ti>=3:  #条件2   #如果上一个条件通过了，这个没通过，但还是打印上一个的
#     print("offer")  #如果上一个没过，就到下一个条件，要是过了就打印这个
# else:    #以上条件都不成立执行的
#     print("不符合用人标准")   #以上条件都不过就执行这个的东西

#以下代码   本科and经验  缺一就回家种地
if shen =='本科':     
    if ti >3:
        print('通过收offer')
    else:
        print(f'您的{ti}年经验不够哦')
else:
    print(f'由于你您的学历为{shen},我司只招本科')




