# Section 1 - submitted on TopHat previously 

# Section 2 
import pandas as pd

data = {
"Name": ["Alice", "Bob", "Charlie", "David"],
"Age": [25, 30, 35, 40],
"City": ["NYC", "LA", "Chicago", "Miami"],
"Email": ["a@example.com", "b@example.com", "c@example.com", "d@example.com"],
}

df = pd.DataFrame(data)

# ex 1 : drop email column and store as a new variable 

new_data = df.drop(['Email'], axis=1)
print(new_data)

# ex 2 : drop row 2 from original dataframe in place 

less2_data = df.drop(index=2, axis=0)
print(less2_data)

# ex 3: 

data = df.drop(columns = ['City', 'Email'], inplace=True)
print(df)

# ex 4: drop first and last rows and store as df_trimmed

df_trimmed = df.drop(index = [0, df.index[-1]], axis=0)
print(df_trimmed)