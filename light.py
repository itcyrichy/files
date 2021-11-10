import pandas as pd
data = [['BMW','X3',1000000],['BMW','X5',2000000],['BMW','X6',3000000]]
df = pd.DataFrame(data=data,columns=['Brand','Model','Price'])

df.to_csv('cars_dz_light.csv')
df.to_json('cars_dz_light.json')