import pandas as pd
import glob as gl
import os
import pathlib

import warnings

warnings.filterwarnings('ignore')


def histoData(df):
    df = df.sort_values(by=['testId', 'instanceId'], ascending=False)
    df = df.reset_index()
    names = df.columns.values
    if 'index' in names:
        df.drop(columns=['index'], inplace=True)
    # df.to_csv('test.csv')
    new_df = df.assign(size_p=0, isEmpty_p='True', peek_p=str(0), peek_obj_type_p=str(0), calledMethod_p=str(0),
                       pushInput_p=str(0))

    index_aux = 0
    for index, row in df.iterrows():
        if index_aux < len(df):
            a = df.at[index_aux, 'instanceId']
            df_aux = df.loc[df['instanceId'] == a]
            count = 0
            i = 0
            for j, row2 in df_aux.iterrows():
                if count == (len(df_aux) - 1):
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

                    index_aux = index_aux + len(df_aux)
                    break

                if i != (len(df_aux)):
                    if i == 0:
                        new_df.at[index_aux + count, 'size_p'] = df_aux.at[j, 'size']
                        new_df.at[index_aux + count, 'isEmpty_p'] = df_aux.at[j, 'isEmpty']
                        new_df.at[index_aux + count, 'peek_p'] = df_aux.at[j, 'peek_obj_type']
                        new_df.at[index_aux + count, 'peek_obj_type_p'] = df_aux.at[j, 'peek_obj_type']
                        new_df.at[index_aux + count, 'calledMethod_p'] = df_aux.at[j, 'calledMethod']
                        new_df.at[index_aux + count, 'pushInput_p'] = 'none'

                    else:
                        new_df.at[index_aux + count, 'size_p'] = df_aux.at[j - 1, 'size']
                        new_df.at[index_aux + count, 'isEmpty_p'] = df_aux.at[j - 1, 'isEmpty']
                        new_df.at[index_aux + count, 'peek_p'] = df_aux.at[j - 1, 'peek']
                        new_df.at[index_aux + count, 'peek_obj_type_p'] = df_aux.at[j - 1, 'peek_obj_type']
                        new_df.at[index_aux + count, 'calledMethod_p'] = df_aux.at[j - 1, 'calledMethod']
                        new_df.at[index_aux + count, 'pushInput_p'] = df_aux.at[j - 1, 'pushInput']
                    i = i + 1
                count = count + 1
        else:

            new_df = new_df[new_df['calledMethod'] != 'CTOR']
            return new_df


def saveFile(df, file_out, name):
    df.to_csv(file_out + name)
    print('\n *** Historical Data is saved in *** \n', file_out+name)


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-s', '-- One file or directory', 'd', help=' d for directory or *one* for one file')
    @click.option('-f', '-- file', 'file', help='Name of the directory')
    @click.option('-o', '--out', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, d, file, file_out):
        print('*** Reading Data ***')
        paths = str(pathlib.Path().absolute()) + '\\' + file

        if not os.path.exists(paths):
            os.mkdir(file)

        if d == 'dir':
            dataPath = gl.glob(file_in)
            for i in range(0, len(dataPath)):
                df = pd.read_csv(dataPath[i], index_col=0)
                # print(dataPath[i])
                name = dataPath[i].split('\\')
                name = name[-1]
                name = name.split('_')
                name = name[0]
                name = file_out + name + '.csv'
                file_out_aux = paths + '\\'
                new_df = histoData(df)
                # print(file_out)
                saveFile(new_df, file_out_aux, name)

        else:
            df = pd.read_csv(file_in, index_col=0)
            new_df = histoData(df)
            file_out = paths + '\\' + file_out
            saveFile(new_df, file_out, name='.csv')

main()
