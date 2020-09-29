import warnings
import os
import pathlib

import click

warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob as gl

plt.rcParams.update({'font.size': 10})


def saveFile(df, file_out, name):
    df.to_csv(file_out + name + '.csv')
    print('\n *** Data is saved in *** \n', file_out)


def confusionM(df, name):
    name = name.split('.')
    name = name[0]
    name = name.split('-')
    name = name[1]
    # print(name)

    trP = df.copy()
    trP = trP.drop(trP[(trP['Violated'] == 0)].index)

    trN = df.copy()
    trN = trN.drop(trN[(trN['Violated'] != 0)].index)
    # print(trP)
    TRP = trP['diff'].value_counts()
    TRN = trN['diff'].value_counts()

    try:
        trP_yes = TRP['Yes']

    except:
        trP_yes = 0

    try:
        trP_no = TRP['No']
    except:
        trP_no = 0

    try:
        trN_yes = TRN['Yes']
    except:
        trN_yes = 0

    try:
        trN_no = TRN['No']
    except:
        trN_no = 0

    try:
        trp = trP_yes / (trP_yes+trN_yes)
    except:
        trp = 0
    try:
        tnr = trN_no / (trN_no+trP_no)
    except:
        tnr = 0

    mcr = (trP_no + trN_yes)/(trP_yes+trN_no+trP_no+trN_yes)

    try:
        prs = trP_yes / (trP_yes+trP_no)
    except:
        prs = 0

    try:
        acc = trP_yes + trN_no/ (trP_yes+trN_no+trP_no+trN_yes)
    except:
        acc = 0

    try:
        recall = trP_yes + trN_no/ (trP_yes+trN_no+trP_no+trN_yes)
    except:
        recall = 0

    try:
        fdr = trP_no/ (trP_no+trP_yes)
    except:
        fdr = 0

    try:
        For = trN_yes/ (trN_yes+trN_no)
    except:
        For = 0

    try:
        fm = 2*((prs*tnr)/(prs+tnr))
    except:
        fm = 0

    data = {'DataSet': name, '# of unique rows covered by at least one rule': len(df),
            'TP': trP_yes,
            'TN': trN_no,
            'FP': trP_no,
            'FN': trN_yes,
            'TPR': trp,
            'TNR': tnr,
            'FPR': 1 - tnr,
            'FNR': 1 - trp,
            'FDR (false discovery rate)': fdr,
            'FOR (false omition rate)': For,
            'Accuracy': acc,
            'Misclassification Rate': mcr,
            'Precision': prs,
            'Recall': tnr,
            'f-measure': fm
            }
    return data


if __name__ == '__main__':


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-s', '-- One file or directory', 'd', help=' *dir* for directory or *one* for one file')
    @click.option('-f', '-- file', 'file', help='Name of the directory')
    @click.option('-o', '--out file', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, d, file, file_out):

        print('*** Reading Data ***')

        paths = str(pathlib.Path().absolute()) + '\\' + file

        if not os.path.exists(paths):
            os.mkdir(file)
        # testId, instanceId, size, isEmpty, peek, peek_obj_type, calledMethod

        if d == 'dir':
            aux = []
            dataPath = gl.glob(file_in)
            for i in range(0, len(dataPath)):
                df = pd.read_csv(dataPath[i], index_col=0)
                dataError = df.copy()
                dataE = dataError.drop(dataError[(dataError['Matched'] == 0) & (dataError['Violated'] == 0)].index)
                name = dataPath[i].split('\\')
                name = name[-1]
                new_df = confusionM(dataE, name)
                aux.append(new_df)
            df = pd.DataFrame(aux)
            # print('*****', df)
            file_out2 = paths + '\\'
            saveFile(df, file_out2, file_out)
        else:

            data = pd.read_csv(file_in, index_col=None)
            dataError = data.copy()
            dataE = dataError.drop(dataError[(dataError['Matched'] == 0) & (dataError['Violated'] == 0)].index)
            new_df = confusionM(dataE, file_out)
            name = file_in.split('\\')
            name = name[-1]
            file_out2 = save_path + '\\' + file_out
            saveFile(new_df, file_out2)

main()