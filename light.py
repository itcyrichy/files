import pandas as pd
import datetime
import time
import os

data = [['BMW','X3',1000000],['BMW','X5',2000000],['BMW','X6',3000000]]
df = pd.DataFrame(data=data,columns=['Brand','Model','Price'])

start1 = time.time()
df.to_csv('cars_dz_light.csv')
time1 = time.time() - start1

start2 = time.time()
df.to_json('cars_dz_light.json')
time2 = time.time() - start2

os.rename('C:\\Users\\Asus-pc\\PycharmProjects\\files\\cars_dz_light.csv','C:\\Users\\Asus-pc\\PycharmProjects\\files\\'+str(time1)+'cars_dz_light.csv')
os.rename('C:\\Users\\Asus-pc\\PycharmProjects\\files\\cars_dz_light.json','C:\\Users\\Asus-pc\\PycharmProjects\\files\\'+str(time2)+'cars_dz_light.json')