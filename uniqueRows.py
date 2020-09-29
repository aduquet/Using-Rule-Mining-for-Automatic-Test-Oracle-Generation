import glob as gl
import warnings
import os
import pathlib
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams.update({'font.size': 10})


def saveFile(df, file_out, file):
    df.to_csv(file+'\\'+file_out)
    print('\n *** The Data is saved in *** \n', file_out)


def uniqueRows(data):
    names = data.columns.values
    df = data.copy()
    df.drop(columns=['instanceId', 'testId'], inplace=True)
    for n in names:
        if n == 'diff':
            df.drop(columns=['diff'], inplace=True)

    df_unique = df.drop_duplicates()
    df_unique['diff'] = 'No'
    df_unique['testId'] = 'No'
    df_unique['instanceId'] = 'No'

    for index, row in df_unique.iterrows():
        df_unique.at[index, 'testId'] = data.at[index, 'testId']
        df_unique.at[index, 'instanceId'] = data.at[index, 'instanceId']
        for n in names:
            if n == 'diff':
                df_unique.at[index, 'diff'] = data.at[index, 'diff']

    return df_unique


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-s', '-- One file or directory', 'dire', help=' *dire* for directory or *one* for one file')
    @click.option('-f', '--file', 'file', help='Name of the directory in which data will be stored')
    @click.option('-o', '--out', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, dire, file_out,file):
        print('*** Reading Data ***')
        paths = str(pathlib.Path().absolute()) + '\\' + file

        if not os.path.exists(paths):
            os.mkdir(file)

        if dire == 'dire':
            dataPath = gl.glob(file_in)
            for i in range(0, len(dataPath)):
                df = pd.read_csv(dataPath[i], index_col=0)
                name = dataPath[i].split('\\')
                name = name[-1]
                name = file_out + name
                new_df = uniqueRows(df)
                saveFile(new_df, name, paths)

        else:
            df = pd.read_csv(file_in, index_col=0)
            new_df = uniqueRows(df)
            saveFile(new_df, file_out, paths)

main()
