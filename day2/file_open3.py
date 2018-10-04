import sys, time

for i in range(50):
    sys.stdout.write('#')
    sys.stdout.flush() # 更新缓冲
    time.sleep(0.1)