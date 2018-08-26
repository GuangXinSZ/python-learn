# 函数如何返回2个值 tupe类型(元组)

def resval(skill1, skill2) :
    resp1 = skill1 * 3
    resp2 = skill2 * 2 + 10
    return resp1, resp2

skill = resval(1, 2)
# 结果: 3 14
print(skill[0], skill[1])
print(type(skill))