# -*- coding: utf8 -*-
import json
from datetime import *
import sys
import datetime, time
import hashlib
import requests
import urllib.request, urllib.parse, urllib.parse, urllib.error, urllib.error
# import common.loadconfig as cfg
import traceback
import pandas


class clsSparkDal:
    #    def __init__(self, objLogger):
    #        self.objLogger = objLogger

    def ExecuteJsonQuerySql(self, SparkSql, return_format='json'):
        """
         spark异步请求接口
        :param SparkSql:
        :param return_format: 默认JSON,dataframe
        :return:
        """

        post_url = ' http://116.211.12.109:19002/tasks/req/v2/interactive/api/d061c776/sql'  # 正式环境url

        print("sql:" + SparkSql)
        params = {
            "sql": SparkSql,
            "mode": "ASYNC"
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
            get_url = "http://116.211.12.109:19002/tasks/req/v2/fetch/%s?token=d061c776" % (taskId)  # 正式环境url
            #            self.objLogger.info(get_url)
            while True:
                response = urllib.request.urlopen(get_url)
                json_data = json.loads(response.read())
                if json_data['state'] == 'FINISH':
                    break
                time.sleep(0.1)

            if return_format == 'DataFrame':
                columns = list(map(lambda x: x['name'], json_data['data']['schema']))
                # print(a)
                databody = json_data['data']['body']
                # print(b)
                data = pandas.DataFrame(databody, columns=columns)
                return data

        except Exception as e:
            #            self.objLogger.error(traceback.format_exc() + ":" + SparkSql)
            print(e.read())
            raise e

        return json_data['data']['body']

    def ExecuteJsonQuerySqlV2(self, SparkSql, return_format='json'):
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
            fetch_url = "http://116.211.12.109:19002/apollo/api/spark/fetch/v1/%s" % (taskId)
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
                time.sleep(0.1)

            if return_format == 'DataFrame':
                columns = list(map(lambda x: x['name'], json_data['data']['schema']))
                # print(a)
                databody = json_data['data']['body']
                # print(b)
                data = pandas.DataFrame(databody, columns=columns)
                return data

        except Exception as e:
            print(e.read())
            raise e

        return json_data['data']['body']
