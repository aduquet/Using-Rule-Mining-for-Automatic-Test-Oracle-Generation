import os
import pathlib
import pandas as pd
import numpy as np
import glob as gl
import warnings

warnings.filterwarnings('ignore')


def saveFile(df, file_out):
    df.to_csv(file_out)
    print('\n *** Encode Data is saved in *** \n', file_out)


def encoder(df):
    """
    Encode the Stack dataframe features to make is readable after the rule mining
    """
    data = df.copy()

    data['peek_obj_type'] = np.where(df['peek'] == 'EmptyObject', 'EmptyObject',
                                     df['peek_obj_type'])
    data['peek_obj_type_p'] = np.where(df['peek_p'] == 'EmptyObject_p', 'EmptyObject',
                                       df['peek_obj_type_p'])
    data.drop(columns=['peek', 'peek_p'], inplace=True)

    data['size'] = df['size'].astype(float)
    data['isEmpty'] = df['isEmpty'].astype(str).str.lower()
    data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
    transactions_df = data.copy()

    names = transactions_df.columns.values
    for n in names:
        if n == 'testId' or n == 'instanceId' or n == 'diff':
            transactions_df[n] = df[n]
        else:
            transactions_df[n] = str(n) + ' == ' + '"' + df[n].astype(str) + '"'

    for index, row in transactions_df.iterrows():
        if row['calledMethod_p'] == 'calledMethod_p == "CTOR"':
            transactions_df.at[index, 'size_p'] = 'x'
            transactions_df.at[index, 'isEmpty_p'] = 'x'
            transactions_df.at[index, 'peek_p'] = 'x'
            transactions_df.at[index, 'peek_obj_type_p'] = 'x'
            transactions_df.at[index, 'calledMethod_p'] = 'x'
            transactions_df.at[index, 'pushInput_p'] = 'x'
    return transactions_df


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-s', '-- One file or directory', 'direc', help=' *direc* for directory or *one* for one file')
    @click.option('-o', '--out', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, direc, file_out):
        print('*** Reading Data ***')
        paths = str(pathlib.Path().absolute()) + '\\' + 'EncodeDS'

        if not os.path.exists(paths):
            os.mkdir('EncodeDS')

        if direc == 'directory':
            dataPath = gl.glob(file_in)
            for i in range(0, len(dataPath)):
                df = pd.read_csv(dataPath[i], index_col=0)
                name = dataPath[i].split('\\')
                name = name[-1]
                new_df = encoder(df)
                file_out_a = paths + '\\' + file_out
                name = file_out_a + name
                saveFile(new_df, name)

        else:
            df = pd.read_csv(file_in, index_col=0)
            new_df = encoder(df)
            saveFile(new_df, file_out)

main()
