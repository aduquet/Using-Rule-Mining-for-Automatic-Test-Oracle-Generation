import warnings
import os
import pathlib
from collections import Counter

warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob as gl

plt.rcParams.update({'font.size': 10})


def rhsAnal(rhs):
    print(rhs['RHS'].value_counts())


def ruleA2(df, k, rhs2):
    rhs_values = df['RHS'].drop_duplicates()
    global aux_global
    global bigRule
    global aux_RHS

    for row in rhs_values:

        dfAux = df[df['RHS'] == row]
        dfAux = dfAux.sort_values(by='LHS_size', ascending=True)
        # print('******', row)
        # print(row.find(",)"))

        if row.find(",)") == -1:

            auxRHS = row.replace('(', '')
            auxRHS = auxRHS.replace(')', '')
            auxRHS = auxRHS.replace(", '", ",")
            auxRHS = auxRHS.replace("'", "")
            auxRHS = auxRHS.split(',')
        else:
            auxRHS = row.replace('(', '')
            auxRHS = auxRHS.replace(',)', '')
            auxRHS = auxRHS.replace(", '", ",")
            auxRHS = auxRHS.replace("'", "")
            auxRHS = auxRHS.split(',')
        for n in auxRHS:
            aux_RHS.append(n)

        for index, row2 in dfAux.iterrows():
            if row2['LHS_size'] != 1:
                lhs_aux = row2.at['LHS']
                aux = lhs_aux.replace('(', '')
                aux = aux.replace(')', '')
                aux = aux.replace(", '", ",")
                aux = aux.replace("'", "")
                aux = aux.split(',')
                # print(lhs_aux, type(lhs_aux))
                # print(aux)
                # print()
            else:
                lhs_aux = row2.at['LHS']
                aux = lhs_aux.replace('(', '')
                aux = aux.replace(',)', '')
                aux = aux.replace(", '", ",")
                aux = aux.replace("'", "")
                aux = aux.split(',')
                # print(lhs_aux, type(lhs_aux))
                # print(aux)
                # print()
            for j in aux:
                # print(j)
                bigRule.append(j)
            # print(list(set(bigRule)), auxRHS )
        br = list(set(bigRule))
        Nrule = {'br_LHS': br, 'LHS_size': len(list(set(bigRule))), 'RHS': auxRHS, 'RHS_size': len(auxRHS)}
        aux_global.append(Nrule)
        dfRule = pd.DataFrame(aux_global)

    if k == len(rhs2):

        cRHS = Counter(aux_RHS)
        print(cRHS)
        print(cRHS.values())
        cLHS = Counter(bigRule)
        print(cLHS)
        print(cLHS.values())

        print((set(aux_RHS)))
        print((set(bigRule)))
        print('union:  \n', (set(aux_RHS)).union((set(bigRule))))
        print('inter:  \n',(set(aux_RHS)).intersection((set(bigRule))))

    # dfRule.to_csv('es.csv')

    # print(dfRule)

    # print(rhs_values[])
    # print('***', rhs_values)


def ruleAnilsator(dfr, rv):
    aux = []
    rv.sort()
    for index in rv:
        res = dfr.iloc[index, :]
        aux.append(res)
    df = pd.DataFrame(aux)
    df = df.sort_values(by='LHS_size', ascending=False)

    lhs = np.arange(1, (df['LHS_size'].max()) + 1, 1)
    rhs = np.arange(1, (df['RHS_size'].max()) + 1, 1)
    aux2 = []

    for i in rhs:
        dfAux = df[df['RHS_size'] == i]
        ruleA2(dfAux, i, rhs)
        # print('***', dfRules)
        # aux2.append(dfRules)
    # dfinal = pd.DataFrame(aux2)
    # print(dfinal)
    # return dfinal


if __name__ == '__main__':
    import click

    global aux_RHS
    aux_RHS = []

    global aux_global
    aux_global = []

    global bigRule
    bigRule = []


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-r', '--second file', 'rules', help='Path for getting the rules set')
    @click.option('-f', '-- file', 'file', help='Name of the directory')
    @click.option('-o', '--out file', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, rules, file, file_out):
        data = pd.read_csv(file_in, index_col=0)
        rules = pd.read_csv(rules, index_col=0)

        print('*** Reading Data ***')

        paths = str(pathlib.Path().absolute()) + '\\' + file

        if not os.path.exists(paths):
            os.mkdir(file)

        report = data.drop(data[(data['Matched'] == 0) & (data['Violated'] == 0)].index)
        report = report.drop(report[(report['Violated'] == 0)].index)

        rulesV = report['RuleViolated']
        rv = []
        df_Aux = []
        for row in rulesV:
            aux = row.replace(']', '')
            aux = aux.replace('[', '')
            aux = aux.replace(" ", "")
            aux = aux.replace(", '", ",")
            aux = aux.replace("'", "")
            rulesVio = aux.split(',')
            for num in rulesVio:
                num = int(num)
                rv.append(num)
        rv = list(set(rv))
        ruleAnilsator(rules, rv)

        name = file_out + '.csv'
        file_out_aux = paths + '\\'
        # df_final.to_csv(file_out_aux + name)

main()
