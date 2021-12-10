import pandas as pd

data = pd.read_csv('test_data.csv', header = None)


# Get data into workable format. Create df of appropriate value positions
data[0] = data[0].astype('str').str.zfill(5)
df = []
for item in data[0]:
    digits = [int(x) for x in str(item)]
    df.append(digits)

print(df)
# df = pd.DataFrame(df)

# # Find most common occuring value
# maximum_val = []
# minimum_val = []

# for col in df.columns:

#     if (len(df) == 1):
#         break

#     val = df.groupby(col).size().idxmax()
#     small_val = df.groupby(col).size().idxmin()

#     if (val == small_val):
#         df = df.loc[df[col] == 1,:]

#     df = df.loc[df[col] == val, :]