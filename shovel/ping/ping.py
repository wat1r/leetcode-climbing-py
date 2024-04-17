import ping3
import time
import datetime


def ping_test(target, count=4):
    """  
    发送ping请求并统计丢包和超时的次数。  
  
    参数:  
        target (str): 要ping的IP地址或域名。  
        count (int): 要发送的ping请求数量。默认为4。  
  
    返回:  
        dict: 包含丢包和超时的统计信息。  
    """
    results = {}
    results['timeout'] = 0
    results['packet_loss'] = 0
    # ping_count(count, results, target)
    ping_forever(results, target)
    return results


def ping_forever(results, target):
    while True:
        time.sleep(30)  # 等待30秒再发送下一个ping请求
        print(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'), " ping ", target)
        response = ping3.ping(target)
        if response is None:
            results['timeout'] += 1
        elif type(response) is float:
            continue
        elif response.do_not_fragment and response.packet_loss:
            results['packet_loss'] += 1



def ping_count(count, results, target):
    for _ in range(count):
        time.sleep(30)  # 等待30秒再发送下一个ping请求
        response = ping3.ping(target)
        if response is None:
            results['timeout'] += 1
        elif type(response) is float:
            continue
        elif response.do_not_fragment and response.packet_loss:
            results['packet_loss'] += 1



if __name__ == "__main__":
    # target = input("请输入要ping的IP地址或域名: ")
    # count = int(input("请输入要发送的ping请求数量 (默认为4):")) or 4
    target = '8.8.8.8'
    count = 10
    stats = ping_test(target, count)
    print(f"超时次数: {stats['timeout']}")
    print(f"丢包次数: {stats['packet_loss']}")
