import datetime

'''
    :输入 n s t : n 表示n行、s t 表示开始时间(包含)和结束时间(不包含) yyyymmddHHMM 年月日时分
    :输出 若干行，每行两部分，第一部分 时间 yyyymmddHHMM， 第二部分 执行命令。按时间顺序输出，如果统一时刻有多条命令，按输入顺序输出
'''
anyday = int(datetime.datetime(2018, 10 ,16).strftime('%w'))-1

first = input().split()
n = int(first[0])
begin = first[1]
end = first[2]

# beginTime
begin_year = int(begin[:4])
begin_month = int(begin[4:6])
begin_day = int(begin[6:8])
begin_hour = int(begin[8:10])
begin_min = int(begin[10:])
# endTime
end_year = int(end[:4])
end_month = int(end[4:6])
end_day = int(end[6:8])
end_hour = int(end[8:10])
end_min = int(end[10:])

cmds = []
for i in n:
    cmd = input().split()
    cmds.append(cmd)

for y in range(end_year - begin_year + 1 ):
    isEndYear = True if end_year - y == 0 else False
    isBeginYear = True if begin_year - y == 0 else False
    # 开始和结束在同一年
    if isBeginYear and isEndYear:
        for m in range(begin_year, end_year + 1):
            pass
    # 在结束那一年
    elif isEndYear:
        for m in range(1, end_month + 1):
            pass
    # 在开始那一年
    elif isBeginYear:
        for m in range(begin_month, 13):
            pass
    # 开始和结束之间那年
    else:
        for m in range(1,13):
            pass
