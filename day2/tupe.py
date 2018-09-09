
product_list = [
    ('Iphone', 5800),
    ('Mac Pro', 9800),
    ('Bike', 800),
    ('Watch', 3800),
    ('Coffee', 4800),
    ('Alex Python', 1800),
]
shoplist = []
salary = input("Input your salary:")

if salary.isdigit() :
    salary = int(salary)
    while True :
        # enumerate 数组的index值取出来

        for index,item in enumerate(product_list) :
            print(index, item)

        user_choice = input("选择要买吗？>>>: ")
        if user_choice.isdigit () : 
            user_choice = int(user_choice)

            if user_choice < len(product_list) and user_choice >= 0 :
                p_item = product_list[user_choice]

                if p_item[1] < salary :
                    shoplist.append(p_item)
                    salary -= p_item[1]
                    print('Add $ into shopping cart', (p_item, salary))
                else :
                    print("\033[41: 您的余额不足 \033[31] %(salary)", salary)

            else :
                print("product code [%s] is not exist!"% user_choice)

        elif user_choice == 'q' : 
            print('-------shopping_list-----------')

            for p in shoplist :
                print(p)
            
            print("your current balance", salary)

            exit()
        else :
            print("invalid option")
