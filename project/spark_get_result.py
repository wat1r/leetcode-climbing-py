# -*- coding: utf8 -*-
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import *
import pandas
import datetime, time


class SparkGetResultClz:

    def spark_get_result(self, SparkSql, return_format='json'):
        """
         spark异步请求接口
        :param SparkSql:
        :param return_format: 默认JSON,dataframe
        :return:
        """
        post_url = 'http://116.211.12.109:19002/apollo/api/spark/submit/v1'  # V2版本的url

        print("sql:" + SparkSql)
        params = {
            "sql": SparkSql,
            "token": "d061c776"
        }
        params = json.dumps(params)
        headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
        params = bytes(params, 'utf8')
        try:
            req = urllib.request.Request(url=post_url, data=params, headers=headers, method='POST')
            response = urllib.request.urlopen(req).read()

            json_data = json.loads(response)
            taskId = json_data['taskId']
            print("taskId:" + taskId)
            fetch_url = "http://116.211.12.109:19002/apollo/api/spark/fetch/v1/%s" % (taskId)  # V2版本的url
            print(fetch_url)
            params = {
                "token": "d061c776"
            }
            params = json.dumps(params)
            headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
            params = bytes(params, 'utf8')
            while True:
                req = urllib.request.Request(url=fetch_url, data=params, headers=headers, method='POST')
                response = urllib.request.urlopen(req).read()
                json_data = json.loads(response)
                if json_data['state'] == 'FINISH':
                    break
                time.sleep(1)

            if return_format == 'DataFrame':
                columns = list(map(lambda x: x['name'], json_data['data']['schema']))
                databody = json_data['data']['body']
                data = pandas.DataFrame(databody, columns=columns)
                return data

        except Exception as e:
            print(e.read())
            raise e

        return json_data['data']['body']
