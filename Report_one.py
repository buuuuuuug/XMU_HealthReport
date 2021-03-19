import time
import datetime

import schedule
import requests

from Utils.health_report_api import health_report

# 自定义参数(请填写)
USERNAME = ''  # 统一身份认证账号
PASSWORD = ''  # 统一身份认证密码
N = 1  # 你要打卡的天数,1为只打今天，2为打昨天和今天.....以此类推
webhook = ''
dingding_patern = "【每日打卡信息：】"


def job():
    a = health_report(USERNAME, PASSWORD, N)
    # 把消息传给钉钉
    dingding_report(a, webhook)


def get_current_time():
    timestamp = time.time()
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    time_local = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return time_local


def dingding_report(message, webhook):
    time_local = get_current_time()
    data = {
        "msgtype": "text",
        "text": {
            "content": dingding_patern + ' ' + message + '\n' + time_local

        }
    }
    requests.post(webhook, json=data)
    return


# schedule.every().day.at("08:00").do(job)

if __name__ == '__main__':
    schedule.every().day.at("07:52").do(job)
    while True:
        schedule.run_pending()
        time.sleep(60)
