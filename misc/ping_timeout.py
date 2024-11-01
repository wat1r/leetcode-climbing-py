#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ping3
import time
import datetime

encoding = 'utf-8'

fi = open('/Users/frankcooper/Data/20tmp/ping_timeout.txt', 'w+')

cnt = 0


def ping(host, time_out=1):
    """
    检查ip是否能被ping通，time_out为超时时间，单位为秒，默认为1秒
    """
    print(f'host = {host}, time_out = {time_out}')
    fi.write(f'host = {host}, time_out = {time_out}\n')
    try:
        response_time = ping3.ping(host, timeout=time_out)
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print(f'[{current_time}] response_time: [{response_time}]')
        fi.write(f'[{current_time}] response_time: [{response_time}]\n')
        #  如果能ping通（测试发现ping不通时函数有一定几率不到超时时间就提前返回）
        if response_time is not False and response_time is not None:
            print(
                f'ping3.ping({host}, timeout={time_out}) response_time: [{response_time}]')
            fi.write(f'ping3.ping({host}, timeout={time_out}) response_time: [{response_time}]\n')
            return True

    except Exception as e:
        print(f"检测Ping发生错误：{e}")
        print(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') + " ping " + host)
        # raise Exception(f"Error，检测 IP[{ip}] 检测Ping发生错误：{e}")
        fi.write(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') + " ping " + host)
        fi.write(f"检测Ping发生错误：{e}")
        pass

    # 不能ping通（超时或异常）
    return False


def main(cnt: int):
    host = '202.108.22.5'
    while not ping(host):
        time.sleep(1)
        cnt += 1
        if cnt > 10:
            fi.flush()
            cnt = 0


if __name__ == "__main__":
    main(cnt)
