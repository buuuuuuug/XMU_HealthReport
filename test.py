import time

import schedule

# 自定义参数(请填写)
USERNAME = ''  # 统一身份认证账号
PASSWORD = ''  # 统一身份认证密码
N = 1  # 你要打卡的天数,1为只打今天，2为打昨天和今天.....以此类推


def job():
    print("job working!")


if __name__ == '__main__':
    # schedule.every().day().at("12:30").do(job)
    schedule.every().day.at("12:43").do(job)
    # schedule.every(10).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(30)
