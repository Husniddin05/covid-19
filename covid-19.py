# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YZl5fT9lObjUVWwSMDPlKYAmkR0FqK_e
"""

!pip install pandas

import pandas as pd
df=pd.read_excel("covid.xlsx")
df_sorted=df.sort_values(by='Country').reset_index(drop=True)
print(df_sorted)



filtered = df[df['Country'] == 'Afghanistan']
filtered_sorted = filtered.sort_values(by="Country_code").reset_index(drop=True)
print(filtered_sorted)

print("Afghanistandagi kasallar soni:" + str(len(filtered_sorted)))