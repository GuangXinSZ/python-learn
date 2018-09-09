product_list = [
    ('Iphone', 5800),
    ('Mac Pro', 9800),
    ('Bike', 800),
    ('Watch', 3800),
    ('Coffee', 4800),
    ('Alex Python', 1800),
]

salary = input("Input your salary: ")
shop_list = []

if salary.isdigit() :
    salary = int(salary)
    while True :
        for index,item in  enumerate(product_list) :
            print(index, item)
        user_choice = input("input your choice?>>>>")

        if user_choice.isdigit() :
            user_choice = int(user_choice)

            if user_choice < len(product_list) and user_choice >= 0 :
                user_temp = product_list[user_choice]

                if user_temp[1] < salary :
                    shop_list.append(user_temp)

                    salary -= user_temp[1]
                    print("购买成功剩余余额", salary)
                else :
                    print("您的余额不够", salary)
            else :
                print("您选择的商品不存在")
        elif user_choice == 'q' :
            print('-------shopping_list-----------')

            for p in shop_list :
                print(p)
            
            print("your current balance", salary)

            exit()

else :
    print("请输入正确的数值!")