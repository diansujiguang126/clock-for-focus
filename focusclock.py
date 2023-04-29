import time

# 定义常量
WORK_TIME = 25 * 60  # 25分钟工作时间
BREAK_TIME = 5 * 60  # 5分钟休息时间
LONG_BREAK_TIME = 20 * 60  # 20分钟长时间休息

# 定义计数器
work_count = 0

while True:
    work_count += 1
    
    # 工作时间
    print("工作开始！")
    for i in range(WORK_TIME, 0, -1):
        print(f"倒计时: {i // 60} 分钟 {i % 60} 秒", end='\r')
        time.sleep(1)
    
    # 休息时间
    if work_count % 4 == 0:
        print("休息结束，可以开始一段长时间休息了！")
        for i in range(LONG_BREAK_TIME, 0, -1):
            print(f"倒计时: {i // 60} 分钟 {i % 60} 秒", end='\r')
            time.sleep(1)
    else:
        print("休息结束，可以开始工作了！")
        for i in range(BREAK_TIME, 0, -1):
            print(f"倒计时: {i // 60} 分钟 {i % 60} 秒", end='\r')
            time.sleep(1)
