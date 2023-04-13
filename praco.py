import numpy as np
import pandas as pd

raw_data = {'bond_name': ['govt_bond_1', 'govt_bond_2', 'govt_bond_3', 'pvt_bond_1', 'pvt_bond_2', 'pvt_bond_3', 'pvt_bond_4'],
             'risk_score': [1.6, 0.9, 2.3, 3.0, 2.7, 1.8, 4.1]}
df = pd.DataFrame(raw_data, columns = ['bond_name', 'risk_score'])
    
print(df)

rating = []
for row in df['risk_score']:
    if row < 1.0 :
            rating.append('AA')
    elif row < 2.0:
           rating.append('A')
    elif row < 3.0:
          rating.append('BB')
    elif row < 4.0:
              rating.append('B')
    elif row < 5.0:
              rating.append('C')
        
    else: 
        rating.append('Not_Rated')

df['rating'] = rating
print(df) 


import pandas as pd
import numpy as np

# Import the file
df = pd.read_excel (r'/home/brian/Documents/Schoolwork/3rd year/MCS_3.1_7.xlsx')
df.head()

# Impose a condition on the AVERAGE column
grade = []
if (df['AVERAGE'] >= 60):
    grade.append('A')
elif(df['AVERAGE'] >= 50):
    grade.append('B')
elif(df['AVERAGE'] >= 40):
    grade.append('C')
elif(df['AVERAGE'] >= 30):
    grade.append('D')
else:
    grade.append('E')


# create a list of the values we want to assign for each condition
grade = ['E', 'D', 'C', 'B', 'A']

# create a new column and use np.select to assign values to it using our lists as arguments
df['Grade'] = np.select(grade)

# display updated DataFrame
print(df)


wrkbk = openpyxl.load_workbook(filename="MCS_3.1_7.xlsx")
wrkbk.sheetnames()
wrksht = wrkbk['MCS 3.1']

grade = []
for row in df[wrksht['AVERAGE']]:
    if row < 60:
        grade.append('A')
    elif row < 50:
        grade.append('B')
    elif row < 40:
        grade.append('C')
    elif row < 30:
        grade.append('D')
    else:
        grade.append('E')

df['grade'] = grade
print(df)