import pandas as pd

hotel_bookings = pd.read_csv('hotel_bookings.csv')


# rename columns
hotel_bookings = hotel_bookings.rename(columns={
    'adults': 'num_adults',
    'children': 'num_children',
    'babies': 'num_babies'
})

hotel_bookings.to_csv('hotel_bookings.csv', index=False)

# % of rows with null values
print(hotel_bookings.isnull().sum() *100 / len(hotel_bookings))

print (hotel_bookings['agent'].unique())
print (hotel_bookings[hotel_bookings['agent'] == 5])

# fill null agent entries with -1
hotel_bookings['agent'] = hotel_bookings['agent'].fillna(-1)
hotel_bookings.to_csv('hotel_bookings.csv', index=False)

print(hotel_bookings[hotel_bookings['agent'] == -1].head())

