import pandas as pd
year_index = { 'Year' :[y for y in range( 2010 , 2031 )],'Index' :[i for i in range( 21 )],}
df = pd.DataFrame(year_index)
print(df.head())
