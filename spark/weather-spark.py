from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext,Row
import re


def test(p):
    if len(p) == 33:
	    val = Row(YRMODAHRMN = p[2][0:10],TEMP=p[21],VSB=p[11],PCP01=p[28],SD=p[32])
	    return val
    else:
        return Row()
conf = SparkConf().setAppName("SQlSELECT")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
weather = sc.textFile("hdfs:///user/rg2856/weather-data.txt")
parts0 = weather.map(lambda l:l.split())
#weatherInfo2 = parts0.map(lambda p: Row(USAF=p[0],WBAN = p[1],YRMODAHRMN = p[2][0:10],DIR=p[3],SPD=p[4],GUS =p[5],CLG=p[6],SKC=p[7],L=p[8],M=p[9],H=p[10],VSB=p[11],MW0=p[12],MW1=p[13],MW2=p[14],MW3=p[15],AW0=p[16],AW1=p[17], AW2=p[18],AW3=p[19],W=p[20],TEMP=p[21],DEWP=p[22],SLP=p[23] ,ALT=p[24], STP=p[25],MAX=p[26],MIN=p[27],PCP01=p[28],PCP06=p[29],PCP24=p[30], PCPXX=p[31],SD=p[32]))
#weatherInfo = parts0.map(lambda p: Row(YRMODAHRMN = p[2][0:10],TEMP=p[21],VSB=p[11],PCP01=p[28],SD=p[32]))

weatherInfo = parts0.map(lambda p: Row(YRMODAHRMN = p[2][0:10],TEMP=p[21],VSB=p[11],PCP01=p[28],)) 
#weatherInfo = parts0.map(lambda p: Row(YRMODAHRMN = p[2][0:10],TEMP=p[21],VSB=p[11],PCP01=p[28]))
schemaWeather = sqlContext.createDataFrame(weatherInfo)
schemaWeather.registerTempTable("weatherTable")

outRdd = sqlContext.sql(" SELECT TEMP as Temp, YRMODAHRMN as Time, VSB as VSB, PCP01 as PCP01 FROM weatherTable WHERE weatherTable.TEMP NOT LIKE '%*%' AND weatherTable.VSB NOT LIKE '%*%' AND weatherTable.PCP01 NOT LIKE '%*%'  ")
outRdd.registerTempTable("outTable")

m = sqlContext.sql(" SELECT Time,AVG(CAST(Temp as decimal(10,3))) as TempPerHour,AVG(CAST(VSB as decimal(10,3))) as VSBPerHour,AVG(CAST(PCP01 as decimal(10,3))) as PCP01PerHour FROM outTable GROUP BY Time ORDER BY Time")
m.registerTempTable("outTable1")
n = sqlContext.sql(" SELECT Time,CAST(TempPerHour as decimal(6,3)) as TempPerHour1,CAST(VSBPerHour as decimal(6,3)) as VSBPerHour1,CAST(PCP01PerHour as decimal(6,3)) as PCP01PerHour1 FROM outTable1  ORDER BY Time")
n.rdd.map(lambda r:",".join([str(c) for c in r])).coalesce(1).saveAsTextFile("hdfs:///user/rg2856/selectweather8")
#m.registerTempTable("weathTable")

#taxi = sc.textFile("hdfs:///user/lh1891/project/yellow_tripdata_test.csv")
#parts1 = taxi.map(lambda l:l.split(','))
#taxiInfo2 = parts1.map(Conv)
#taxiInfo = taxiInfo2 .map(lambda p: Row(VendorID= p[0],pickup_datetime=p[1],dropoff_datetime=p[2],passenger_count=p[3],trip_distance=p[4],pickup_longitude = p[5],pickup_lattitude=p[6],RateCodeID=p[7],store_and_fwd_flag=p[8],dropoff_longitude=p[9],dropoff_lattitude=p[10],payment_type=p[11],fare_amount=p[12],extra=p[13],mta_tax=p[14],tip_amount=p[15],tolls_amount=p[16],improvement_surcharge=p[17],total_amount=p[18]))

#schemaTaxi = sqlContext.createDataFrame(taxiInfo)
#schemaTaxi.registerTempTable("taxiTable")

#taxiWeatherJoin = sqlContext.sql("SELECT DISTINCT VendorID,pickup_datetime,dropoff_datetime,passenger_count,trip_distance,pickup_longitude,pickup_lattitude,RateCodeID,store_and_fwd_flag,dropoff_longitude,dropoff_lattitude,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount,weathTable.TempPerHour FROM taxiTable JOIN weathTable ON weathTable.Time=taxiTable.pickup_datetime ORDER BY pickup_datetime") 

#taxiWeatherJoin.rdd.map(lambda r:",".join([str(c) for c in r])).coalesce(1).saveAsTextFile("hdfs:///user/lh1891/project/JOIN")

