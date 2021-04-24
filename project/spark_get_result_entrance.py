# -*- coding: utf8 -*-
# %%
import json
import pandas as pd
import numpy as np
from spark_get_result import SparkGetResultClz

from datetime import datetime as dt

# %%
# 活跃的服务器和版本
#


sql22 = f'''select case when game_id = 991003632 then '39' when game_id = 991003614 then '安峰' else '其他' end game_id, part_date, area_id, resource_version from dw.ahrxhero_character_login_glog where part_date >= '2021-01-25' and part_date <= '2021-01-31' and area_id > 10000 and game_id in (991003632, 991003614) group by game_id, area_id, resource_version, part_date order by part_date, area_id, resource_version'''


# sql22 = f'''create table temp.bb_area_ah_test0206 as select case when game_id=991003632 then '39' when game_id=991003614 then '安峰' else '其他' end game_id, part_date, area_id, resource_version from dw.ahrxhero_character_login_glog where part_date>= '2021-01-25' and part_date <= '2021-01-31' and area_id > 10000 and game_id in (991003632,991003614) group by game_id, area_id, resource_version, part_date order by part_date, area_id, resource_version;'''


# %%
# 区服和版本信息
spark = SparkGetResultClz()
# json_data = spark.ExecuteJsonQuerySql(sql22)
json_data = spark.spark_get_result(sql22)

# %%
print(json_data)


# %%
