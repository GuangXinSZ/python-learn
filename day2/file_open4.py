f = open("yesterday.txt", "r", encoding="utf-8")
f_new = open("yesterday_1.txt", "w", encoding="utf-8")

for line in f:
    if '江西' in line:
        line  = line.replace('江西', '广东')
    f_new.write(line)

f.close()
f_new.close() 
