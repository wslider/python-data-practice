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


# fill null country entries with unknown 
print(hotel_bookings[hotel_bookings['country'].isna()][['hotel', 'is_canceled', 'country']])
hotel_bookings['country'] = hotel_bookings['country'].fillna('unknown')
hotel_bookings.to_csv('hotel_bookings.csv', index=False)

# drop rows with null children entries (since only 4)
hotel_bookings = hotel_bookings.dropna(subset=['num_children'])
hotel_bookings.to_csv('hotel_bookings.csv', index=False)

# drop company column
# company column not found in original - likely in messier version on github

# print data types of columns 
print(hotel_bookings.dtypes)


hotel_bookings = hotel_bookings.astype({'is_canceled': 'boolean', 'is_repeated_guest': 'boolean', 'num_children': 'int64'})


# bin cols 
print(hotel_bookings['lead_time'].unique())
print(hotel_bookings['lead_time'].describe())

bins = [0, 100, 200, 300, 400, 500, 600, 700, 800]
labels = ['0-100', '101-200', '201-300', '301-400', '401-500', '501-600', '601-700', '701-800']

hotel_bookings['lead_time_binned'] = pd.cut(hotel_bookings['lead_time'], bins=bins, labels=labels)
print(hotel_bookings[['lead_time', 'lead_time_binned']])

# split arrival date (already split in dataset)
    # hotel_bookings['arrival_date_month'] = hotel_bookings['arrival_date'].str.split('-', expanded=True)[0]
    # hotel_bookings['arrival_date_year'] = hotel_bookings['arrival_date'].str.split('-', expanded=True)[1]

# string cleaning via regex
# strings already clean in existing dataset
hotel_bookings['hotel'] = hotel_bookings['hotel'].replace(r"[\*\n\^]", '', regex=True)
print(hotel_bookings['hotel'].unique())

# Remove Duplicates 
hotel_bookings.loc[hotel_bookings.duplicated(keep=False)]
# Remove duplicates where entire rows match
hotel_bookings.drop_duplicates(keep="first", inplace=True)
# Confirm no duplicates exist
print(hotel_bookings.loc[hotel_bookings.duplicated(keep=False)])