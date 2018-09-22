
data = {
    '北京': {
        "东莞": {},
        "佛山": {},
        "常州": {}
    },
    '广东': {
        "东莞": {
            "沙河": ["oldbody", "test"],
            "沙河2": ["oldb222", "我爱江西"]
        },
        "佛山": {
            "沙河444": ["oldbody", "test"],
            "沙河23": ["oldb222", "我爱江西"]
        },
        "常州": {}
    }
}

exit_enable = False

while not  exit_enable:
    for i in data:
        print(i)
    choice = input("请选择进入>>>:")
    if choice in data:
        while not exit_enable:
            for i2 in data[choice]:
                print(i2)
            choice2 = input("请选择进入>>>:")
            if choice2 in data[choice]:
                while not exit_enable:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input('最后一层了, 按d返回上一层 按q退出: ')
                    if choice3 == "d":
                        break
                    elif choice3 == "q":
                        exit_enable = True
            if choice2 == "d":
                break
            elif choice2 == "q":
                exit_enable = True