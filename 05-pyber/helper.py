def get_ride_count_avg_fare_and_driver_count_by_city(df):
    ride_count = df.groupby(["city"]).count()['ride_id']
    avg_fare = df.groupby(['city']).mean()['fare']
    driver_count = df.groupby(['city']).mean()['driver_count']
    return ride_count, avg_fare, driver_count