#列提个标题。
print("许发鑫开发的游戏。")
#导入随机数模块。
import random
#创建变量设置游戏答案。
answer=random.randint(1,10)
#设置while循环变量。
counts=3
#设置while循环。
while counts>0:
    #让键盘记录函数记录用户输入整形数据存放到变量之中。
    temp=input("猜猜许发鑫现在心里想的是哪个数字：")
    #定义用户输入的数据形式。
    guess=int(temp)
    #设置if，else条件分支。
    if guess==answer:
        #答对后的提示。
        print("答对了！")
        print("答对了也没有奖励。")
    #设置else和嵌套。
    else:
        if guess>0:
            #答案大于正确答案后的提示。
            print("大了大了》")
            print("再猜一次。")
        else:
            #答案小于正确答案后的提示。
            print("小了小了。")
    #设置循环次数。
    counts=counts-1
#游戏结束后的提示。
print("游戏结束不玩儿了。")


            
    
