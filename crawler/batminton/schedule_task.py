import logging
import time
from concurrent.futures import Future, ThreadPoolExecutor

from apscheduler.schedulers.background import BackgroundScheduler


executor = ThreadPoolExecutor(10)
logger = logging.getLogger(__name__)


def job():
    req = {
        "taskId": "-1",
        "taskCode": "ANT_SPIDER",
        "funcId": 3,
        "funcCode": "SPIDER_RUN",
        "bizData": {
            "batchNo": "100000000000009",
            "code": [
                "270023",
                "004243",
                "270042",
                "005224",
                "008702",
                "011369",
                "011236",
                "012805",
                "001092",
                "012337",
                "011364",
                "021370"
            ]
        }
    }
    logger.info(f"-----------------schedule job-----------------req:{req}")
    # future: Future = executor.submit(, req)


def start_job():
    logger.info("nothing to do")
    # start_job_core()


def start_job_core():
    # logger.info("------------------timer:start------------------")
    #     # 创建后台调度器
    #     scheduler = BackgroundScheduler()
    #     # 添加任务，interval参数表示间隔时间，单位为秒
    #     scheduler.add_job(job, 'interval', seconds=60 * 30)
    #     # 启动调度器
    #     scheduler.start()
    pass
    # 为了防止程序退出，主线程在这里等待
    # try:
    #     while True:
    #         time.sleep(2)
    # except KeyboardInterrupt:
    #     # 关闭调度器
    #     scheduler.shutdown()
