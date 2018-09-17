info = {
    'st1': "xin",
    'st2': "lin",
    'st3': "lin"
}
b = {
    "st1": '宝',
    1: 1
}
# print(info)
# info['st1'] = "广信"
# del info["st1"] # 删除 
# info.pop("st1") # 删除
# print(info.get('st2')) # 查找
info.update(b)
# print(info)
print(info.items())