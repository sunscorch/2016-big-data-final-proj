
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row



def DatetimeConv(DT):
    Day      = DT.split(' ')
    TimeList = Day[1].split(':')
    DayList  = Day[0].split('-')  
    Year     = DayList[0]
    Month    = DayList[1] 
    Day      = DayList[2]
    Hour     = TimeList[0]
    if len(Month)==1:
        Month = '0'+Month
    if len(Day)==1:
        Day = '0'+Day
    if len(Hour)==1:
        Hour = '0'+Hour
    return Year+Month+Day+Hour

def Conv(line):
    line[1]=DatetimeConv(line[1])
    
    return line
    

def ToString(line):
    for i in range(len(line)):
        line[i] = str(line[i])
    return line

conf = SparkConf().setAppName("SQlSELECT")
sc = SparkContext(conf=conf)


sqlContext = SQLContext(sc)
# Load a text file and convert each line to a Row.
taxi = sc.textFile("hdfs:///user/rg2856/yellow_tripdata_2015-12.csv")
header = taxi.first()
taxi = taxi.filter(lambda x:x !=header) 
parts1 = taxi.map(lambda l:l.split(','))


taxiInfo2 = parts1.map(Conv)
taxiInfo = taxiInfo2 .map(lambda p: Row(VendorID= p[0],pickup_datetime=p[1],dropoff_datetime=p[2],passenger_count=p[3],trip_distance=p[4],pickup_longitude = p[5],pickup_lattitude=p[6],RateCodeID=p[7],store_and_fwd_flag=p[8],dropoff_longitude=p[9],dropoff_lattitude=p[10],payment_type=p[11],fare_amount=p[12],extra=p[13],mta_tax=p[14],tip_amount=p[15],tolls_amount=p[16],improvement_surcharge=p[17],total_amount=p[18]))

schemaTaxi = sqlContext.createDataFrame(taxiInfo)
schemaTaxi.registerTempTable("taxiTable")
selectedtaxi = sqlContext.sql("SELECT DISTINCT VendorID,pickup_datetime,pickup_longitude,pickup_lattitude,fare_amount,tip_amount,passenger_count,trip_distance FROM taxiTable ORDER BY pickup_datetime") 

selectedtaxi.rdd.map(lambda r:",".join([str(c) for c in r])).coalesce(1).saveAsTextFile("hdfs:///user/rg2856/taxi12")
