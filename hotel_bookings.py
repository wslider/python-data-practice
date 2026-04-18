import pandas as pd

# Now your normal code
hotel_bookings = pd.read_csv('hotel_bookings.csv')

hotel_bookings = hotel_bookings.rename(columns={
    'adults': 'num_adults',
    'children': 'num_children',
    'babies': 'num_babies'
})

hotel_bookings.to_csv('hotel_bookings.csv', index=False)

