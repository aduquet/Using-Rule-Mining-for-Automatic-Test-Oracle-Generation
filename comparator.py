import warnings
import os
import pathlib

warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob as gl

plt.rcParams.update({'font.size': 10})

if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-m', '--second file', 'rules', help='Path for getting the data')
    @click.option('-f', '-- file', 'file', help='Name of the directory')
    @click.option('-o', '--out file', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, file_in2, file, file_out):
        training = pd.read_csv(file_in, index_col=None)
        testing = pd.read_csv(file_in2, index_col=None)
        testingErrors = testing.copy()
        print('*** Reading Data ***')

        paths = str(pathlib.Path().absolute()) + '\\' + file

        if not os.path.exists(paths):
            os.mkdir(file)
        # testId, instanceId, size, isEmpty, peek, peek_obj_type, calledMethod

        training.drop(columns=['testId', 'instanceId'], inplace=True)
        testing.drop(columns=['testId', 'instanceId'], inplace=True)
        # print(training.head(10))
        # print(testing.head(10))
        # print(testingErrors.head(10))
        df = training.eq(testing)
        # print(df.head(60))

        if len(training) == len(testing):

            testingErrors['diff'] = 'No'

            for index, row in df.iterrows():
                if not row['peek_obj_type']:
                    testingErrors['diff'][index] = 'Yes'

                if not row['isEmpty']:
                    testingErrors['diff'][index] = 'Yes'

                if not row['size']:
                    testingErrors['diff'][index] = 'Yes'

                # if testingErrors['size'][index] == 2:
                #     testingErrors['errors'][index] = 'Yes'

        else:
            testingErrors['diff'] = 'Yes'
            testingErrors.loc[(testingErrors['size'] != 2) & (testingErrors['isEmpty'] != 'TRUE'), 'diff'] = 'No'
            # testingErrors.loc[(testingErrors['size'] < 2) & (testingErrors['isEmpty'] != 'TRUE'), 'diff'] = 'No'
            testingErrors.loc[(testingErrors['size'] > 2), 'diff'] = 'Yes'
        name = file_out + '.csv'
        file_out_aux = paths + '\\'
        testingErrors.to_csv(file_out_aux + name)

main()
