import requests  # 第三方模块 pip install requests
import json
import os
from sqlalchemy import Column, String, create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import column


engine= create_engine('postgresql://postgres:123456@127.0.0.1:5432/schooldb')

Base = declarative_base()


# 定义school对象:
class school(Base):
    # 表的名字:
    __tablename__ = 'schooldb'

    # 表的结构:
    lineid = Column(String(10), primary_key=True)
    code = Column(String(40))
    schoolname = Column(String(40))
    link = Column(String(80))
    province = Column(String(80))
    city = Column(String(80))
    department = Column(String(80))
    level = Column(String(40))
    type = Column(String(40))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db=Session()
# 请求url地址
url = 'https://www.cingta.com/school/api/name_uni_list/'
# 添加headers,把python伪装成浏览器，对服务器发送请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.5211 SLBChan/30'
    }
response = requests.get(url=url, headers=headers)
# pprint.pprint(response)
# 解析数据
info = response.json()['data']['list']
# pprint.pprint(info)
for index in info:
    lineid = index['lineid']  # 序号
    code = index['code']  # 学校标识码
    schoolname = index['schoolname']  # 学校名称
    link = index['link']    # 学校链接
    province = index['province']  # 所在地区
    city = index['city']    # 所在城市
    department = index['department']    # 主管部门
    level = index['level']  # 办学层次
    type = index['type']    # 高校类型
    # print(lineid, code, schoolname, link, province, city, department, level, type)
    school_data = school(lineid=lineid,
                        code= code,
                        schoolname= schoolname,
                        link= link,
                        province= province, 
                        city=city,
                        department= department,
                        level= level, 
                        type=type)
    db.add(school_data)
    db.commit()


