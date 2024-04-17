import time
import schedule
from txlct import run


if __name__ == '__main__':
    # 定时器
    schedule.every().hour.at(":30").do(run)

    # 无限循环检查任务
    while True:
        schedule.run_pending()
        time.sleep(1)
