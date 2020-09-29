import pandas as pd
import numpy as np
import glob as gl
import os
import pathlib
import warnings

warnings.filterwarnings('ignore')


def saveFile(df, file_out):
    df.to_csv(file_out)
    print('\n *** Data is saved in *** \n', file_out)


def analisator(df, df_unique, name, r):
    df_tam = len(df)
    df_no = df['diff'].value_counts()

    try:
        df_yes = df_no['Yes']
    except:
        df_yes = 0

    ur_tam = len(df_unique)
    ur_no = df_unique['diff'].value_counts()
    try:
        ur_yes = ur_no['Yes']

    except:
        ur_yes = 0
    # print(df_unique)
    ur_noCovered = df_unique[df_unique['Matched'] == 0]

    dataError = df_unique.copy()
    ur_Covered = dataError.drop(dataError[(dataError['Matched'] == 0) & (dataError['Violated'] == 0)].index)
    ur_Violated = df_unique[df_unique['Violated'] != 0]
    Violated = df_unique[df_unique['Violated'] != 0]
    v = list(Violated['Violated'])
    Matched = df_unique[df_unique['Matched'] != 0]
    M = Matched['Matched'].sum()
    # print(Matched)

    count = 0
    auxcount = []
    auxcount2 = []

    df_unique2 = df_unique.copy()
    df_unique2['RuleMatched'].replace('', np.nan, inplace=True)
    df_unique2.dropna(subset=['RuleMatched'], inplace=True)

    for i in range(0, int(r)):
        for index, row in df_unique2.iterrows():
            auxlis = row['RuleMatched']
            a = "'" + str(i) + "'"
            if a in auxlis:
                auxcount2.append(i)
                break
            else:
                count = count + 1
                auxcount.append(i)

    auxset = set(auxcount)
    auxset2 = set(auxcount2)
    unionset = (auxset.union(auxcount2))
    # print(auxset)
    # print(unionset)

    # RuleViolated
    vauxcount = []
    vauxcount2 = []
    df_unique3 = df_unique.copy()
    df_unique3['RuleViolated'].replace('', np.nan, inplace=True)
    df_unique3.dropna(subset=['RuleViolated'], inplace=True)
    for k in range(0, r):
        for index, row in df_unique3.iterrows():
            auxlis = row['RuleViolated']
            b = "'" + str(k) + "'"
            if b in auxlis:
                vauxcount2.append(k)
                break
            else:
                vauxcount.append(k)
    # print(r)
    vauxset = set(vauxcount)
    vauxset2 = set(vauxcount2)
    vunionset = (vauxset.union(vauxcount2))
    # print(vauxset2)
    unionMV = list(unionset.union(vauxset2))
    intmv = list(vauxset2.intersection(vunionset))

    l = 0
    for i in range(0, r):
        if str(i) in unionMV:
            l = l + 1

    data = {'DS': name, '# of Total rows': df_tam,
            '# of rows that are NOT different from Non-mod (correct values)': int(df_no['No']),
            '# of rows that are different from Non-mod (incorrect values)': int(df_yes),
            '# of uniques rows': ur_tam,
            '# of unique rows that are NOT different from Non-mod (correct values)': int(ur_no['No']),
            '# of unique rows that are different from Non-mod (incorrect values)': int(ur_yes),
            '# of unique rows that are NOT covered by rules': len(ur_noCovered),
            '# of unique rows  that are covered by rules': len(ur_Covered),
            '# of unique rows that VIOLATE rules': len(ur_Violated),
            '% coverage': ((len(ur_Covered) / len(df_unique)) * 100),
            '# of Rules': r,
            'Total # of rules Matched (LHS and RHS)': len(unionset),
            'Total # of rules Violated (LHS match but NOT RHS)': len(vauxset2),
            'M-intersection-V': len(intmv),
            'Total # of rules used (MUV)': len(unionMV),
            'Total # of rules NOT used': l}

    return data


if __name__ == '':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-ur', '--unique Rows', 'uniqueRows', help='path for getting the data with unique rows')
    @click.option('-r', '--rules', 'rule', help='rules')
    @click.option('-s', '-- One file or directory', 'direc', help=' *direc* for directory or *one* for one file')
    @click.option('-f', '-- file', 'file', help='Name of the directory')
    @click.option('-o', '--out', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, uniqueRows, rule, direc, file, file_out):
        print('*** Reading Data ***')
        paths = str(pathlib.Path().absolute()) + '\\' + file

        if not os.path.exists(paths):
            os.mkdir(file)

        df_rules = pd.read_csv(rule, index_col=0)
        r = len(df_rules)

        if direc == 'directory':
            dataPath = gl.glob(file_in)
            dataPath.sort()
            dataPath_ur = gl.glob(uniqueRows)
            aux = []
            j = 0

            for i in range(0, len(dataPath_ur)):
                ur = pd.read_csv(dataPath_ur[i], index_col=0)
                if j > len(dataPath) - 1:
                    df = pd.read_csv(dataPath[j - 1], index_col=0)
                    name = dataPath_ur[i].split('-')

                    for n in name:
                        if 'fs' in n:
                            name = n
                    new_df = analisator(df, ur, name, r)
                    aux.append(new_df)
                    j = 0
                else:
                    df = pd.read_csv(dataPath[j], index_col=0)

                    name = dataPath_ur[i].split('-')
                    for n in name:
                        if 'fs' in n:
                            name = n
                    # print(name)
                    new_df = analisator(df, ur, name, r)
                    aux.append(new_df)
                    j = j + 1

            df = pd.DataFrame(aux)
            file_out = paths + '\\' + file_out
            saveFile(df, file_out)

        else:
            df = pd.read_csv(file_in, index_col=0)
            ur = pd.read_csv(uniqueRows, index_col=0)
            new_df = analisator(df, ur, name='asd')
            df = pd.DataFrame(new_df, index=[0])
            file_out = paths + '\\' + file_out
            # print(file_out)
            saveFile(df, file_out)

main()
