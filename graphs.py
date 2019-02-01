import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_pickle('/var/www/html/ML/flight_low_fare_prediction/fare_prediction.pkl')

X = df[['requested_date',
		  'requested_month',
		  'requested_year',
		  'airline_code', 
		  'origin_airport_code', 
		  'dest_airport_code', 
		  'num_passenger',
		  'departure_hour',
		  'departure_minute',
		  'departure_date',
		  'departure_month',
		  'departure_year'
		 ]]
		 
#X = df.drop(columns=['base_fare'])		 
y = df['base_fare'] 

df = df.loc[(df['airline_code']=='6E')&(df['orgin-dest']=='DEL BOM')&(df['departure_date']==24)&(df['departure_month']==1)&(df['departure_hour']==9)&(df['days_to_depature']==4)]
#print(df['departure_hour'].value_counts())
print(df.shape)
#df.to_csv('/var/www/html/ML/flight_low_fare_prediction/graph.csv')

plt.plot(df['departure_timestamp'],df['base_fare'])
plt.show()
#print(df['requested_timestamp'])
#print(df['base_fare'])


plt.show()