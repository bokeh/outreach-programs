import pandas as pq
trips = pq.read_parquet('yellow_tripdata_2022-01.parquet')
t=trips.head(50)
print(t)
print("Done")
