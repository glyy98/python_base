shen=str(input("学历："))
ti=float(input("工作年限"))
if shen == "本科" :#条件1
    print("本科通过")
elif ti>=3:  #条件2
    print("经验也够")
else:    #以上条件都不成立执行的
    print("不符合用人标准")

