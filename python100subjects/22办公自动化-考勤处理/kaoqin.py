'''
迟到早退：
  5<time> 10 20
  10<time 50
只一次卡 扣20
不打卡 扣1.5
调休   当月天数够不扣，不够扣1.5
'''
import xlrd #操作ecxel工具

def rans(num): #判断有多少违规记录
    temp_rs = [0,0,0,0] #迟到5min的次数，迟到10分钟以上，只打一次卡，没打卡
    for j in range(1,15):
        t = sheet.cell_value(num,j)
        all_time = t.split('\n') if len(t) !=0 else []
        count = len(all_time)
        #print(all_time)
        if count == 0: #没有打卡
            temp_rs[3] += 1
        else: #已经打卡
            start = all_time[0]
            t_start = transforms(start)
            if count == 1:  #只打了一次卡
                temp_rs[2] += 1 #记录只打一次卡
                c= compare(t_start)

            else: #打了多次卡
                end = all_time[-1]
                t_end = transforms(end)
                if t_end[0]-t_start[0]<4:
                    temp_rs[2] += 1 #记录只打一次卡
                    if t_end[0]<12: #判断多次打卡是不是上午卡
                        c = compare(t_start)
                    else:
                        c = compare(t_end)
                        statistics(c,temp_rs)
                else:
                    a = compare(t_start)
                    p = compare(t_end)
                    statistics(a,temp_rs)
                    statistics(p,temp_rs)
    return temp_rs

def statistics(c,temp_rs):
    if c >5 and c < 10:
        temp_rs[0] += 1
    elif c>=10:
        temp_rs[1] += 1

def transforms(tmp_time):  # 处理时间
    hour,minute = tmp_time.split(':')
    sum_minute = int(hour)*60 + int(minute)
    return [int(hour),int(minute),sum_minute]

def compare(tmp_time): #判断是否有迟到或者早退
    if tmp_time[0] <12:  #打了上午卡
        c = tmp_time[2] - 9*60 
    else: #签退
        c = 18*60 -tmp_time[2]
    return c if c >0 else 0

#读取数据
if __name__ == "__main__":
    excel = xlrd.open_workbook('./22办公自动化-考勤处理/kq.xlsx')
    sheet = excel.sheets()[0]
    # for i in range(1,sheet.nrows):
    #     print(sheet.cell_value(i,0))
    for i in range(1,sheet.nrows):
        one_rs = rans(i)
        #print(one_rs)
        print({'姓名':sheet.cell_value(i,0),'迟到5分钟':one_rs[0],'迟到10分钟':one_rs[1],'只打一次卡':one_rs[2],'矿工':one_rs[3],})