import pandas as pd
import numpy as np
import glob as gl
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv('LabeledDS\mod1_R3.csv', index_col=0)

df = df.sort_values(by=['testId', 'instanceId'], ascending=False)
df = df.reset_index()
df.drop(columns=['index'], inplace=True)
# df.to_csv('test.csv')
new_df = df.assign(size_p=0, isEmpty_p='True', peek_p=str(0), peek_obj_type_p=str(0), calledMethod_p=str(0),
                   pushInput_p=str(0))
#
index_aux = 0
for index, row in df.iterrows():
    if index_aux == len(df):
        break
    a = df.at[index_aux, 'instanceId']
    df_aux = df.loc[df['instanceId'] == a]
    # print('tamano', len(df_aux), '\n', df_aux['instanceId'], '\n index', index_aux)
    count = 0
    i = 0
    for j, row2 in df_aux.iterrows():
        # print('===')
        # print(len(df_aux), count)
        # print(row2['index'])
        if count == (len(df_aux) - 1):
            # print(index, index + count)

            if i == 0:
                new_df.at[index_aux + count, 'size_p'] = df_aux.at[j, 'size']
                new_df.at[index_aux + count, 'isEmpty_p'] = df_aux.at[j, 'isEmpty']
                new_df.at[index_aux + count, 'peek_p'] = df_aux.at[j, 'peek_obj_type']
                new_df.at[index_aux + count, 'peek_obj_type_p'] = df_aux.at[j, 'peek_obj_type']
                new_df.at[index_aux + count, 'calledMethod_p'] = df_aux.at[j, 'calledMethod']
                new_df.at[index_aux + count, 'pushInput_p'] = 'none'

            else:
                # print(index, index + count)
                new_df.at[index_aux + count, 'size_p'] = df_aux.at[j - 1, 'size']
                new_df.at[index_aux + count, 'isEmpty_p'] = df_aux.at[j - 1, 'isEmpty']
                new_df.at[index_aux + count, 'peek_p'] = df_aux.at[j - 1, 'peek']
                new_df.at[index_aux + count, 'peek_obj_type_p'] = df_aux.at[j - 1, 'peek_obj_type']
                new_df.at[index_aux + count, 'calledMethod_p'] = df_aux.at[j - 1, 'calledMethod']
                new_df.at[index_aux + count, 'pushInput_p'] = df_aux.at[j - 1, 'pushInput']
            # print(index_aux + count)
            index_aux = index_aux + len(df_aux)
            # print('*****')
            # print(index_aux)
            # new_df.to_csv('test.csv')
            break

        if i != (len(df_aux)):
            # print('*')
            # print(i)
            # print(index_aux, index_aux+count)
            if i == 0:
                new_df.at[index_aux + count, 'size_p'] = df_aux.at[j, 'size']
                new_df.at[index_aux + count, 'isEmpty_p'] = df_aux.at[j, 'isEmpty']
                new_df.at[index_aux + count, 'peek_p'] = df_aux.at[j, 'peek_obj_type']
                new_df.at[index_aux + count, 'peek_obj_type_p'] = df_aux.at[j, 'peek_obj_type']
                new_df.at[index_aux + count, 'calledMethod_p'] = df_aux.at[j, 'calledMethod']
                new_df.at[index_aux + count, 'pushInput_p'] = 'none'

            else:
                # print(index, index + count)
                new_df.at[index_aux + count, 'size_p'] = df_aux.at[j - 1, 'size']
                new_df.at[index_aux + count, 'isEmpty_p'] = df_aux.at[j - 1, 'isEmpty']
                new_df.at[index_aux + count, 'peek_p'] = df_aux.at[j - 1, 'peek']
                new_df.at[index_aux + count, 'peek_obj_type_p'] = df_aux.at[j - 1, 'peek_obj_type']
                new_df.at[index_aux + count, 'calledMethod_p'] = df_aux.at[j - 1, 'calledMethod']
                new_df.at[index_aux + count, 'pushInput_p'] = df_aux.at[j - 1, 'pushInput']
            i = i + 1
        count = count + 1
print('done!!!')
new_df.to_csv('test.csv')
