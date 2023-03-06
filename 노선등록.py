'''
BMS테스트를 위한 테스트용 노선 등록 파일

서울열린 데이터광장에서 
서울시버스노선별정류소 정보를 구하여 사용함


'''


import pymysql as pysql
import pandas as pd


data= pd.read_csv("./서울시버스노선별정류소 정보(20221202).csv",encoding="euc-kr")

conn=None
cur=None
sql=""
conn=pysql.connect(host='localhost',user='root',password='비밀번호',db='bms',charset='utf8')
cur= conn.cursor()


Enterprise_name="seoul_bus"
route=""
route_name=""


for i in range(0,len(data)):
    
    if i!=0 and data.iloc[i]["노선명"]==data.iloc[i-1]["노선명"]:
        
        route+="-"+data.iloc[i]["정류소명"]
    else:
        if i!=0:
            sql="INSERT INTO route_info (id,route_name,route,Enterprise_name) VALUES ('"+Enterprise_name+route_name+"','"+route_name+"','"+route+"','"+Enterprise_name+"')"
            cur.execute(sql)
            conn.commit()
        route=data.iloc[i]["정류소명"]
        route_name=data.iloc[i]["노선명"]

conn.close()

