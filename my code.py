import os 
import pandas as pd


data={
    "name":['manish','suraj','ram','shyam'],
    "age":[15,16,17,18],
    'city':['mumbai','dehli','up','bihar']
}
df=pd.DataFrame(data)

# Adding new row to df for V2
new_row_loc = {'Name': 'V2', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

# Adding new row to df for V3
new_row={'Name':'Usagi','Age':30,'City':'City2'}
df.loc[len(df.index)]=new_row

data_dir="data"
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample.csv')
df.to_csv(file_path,index=False)

print(f'CSV FILE SAVE TO {file_path}')

