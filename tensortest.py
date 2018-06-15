import tensorflow as tf
from keras.models import Sequential
import pymysql 

try:
    database = pymysql.connect(user="root",passwd="password", host="ec2-52-79-75-141.ap-northeast-2.compute.amazonaws.com",db="test")
    print("good")
    cursor = database.cursor()
    sql = "select * from user"
    cursor.execute(sql)
except:
    print("error")
    
