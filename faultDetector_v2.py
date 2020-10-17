import warnings

warnings.filterwarnings('ignore')
import os
import pandas as pd
import numpy as np
from collections import defaultdict


def preProsDF(df):
    df = df.drop(df[df['Violated'] == 0].index)
    df = df.drop_duplicates(subset=['Violated'], keep='last')
    return df


def takeViolations(set_rule):
    # print(type(setRule))
    set_rule = set_rule.replace(' ', '')
    set_rule = set_rule.replace("'", '')
    set_rule = set_rule.replace(']', '')
    set_rule = set_rule.replace('[', '')
    set_rule = set_rule.split(',')

    return set_rule


def preProsRules(set_rule, dfr):
    set_rule = [int(x) for x in set_rule]
    Filter_dfr = dfr[dfr.index.isin(set_rule)]
    return Filter_dfr
    # RHS[]


def counterItem(item, rows, fin, WHS):
    times = 0
    if WHS == 'RHS':
        for i in rows:
            if i.find(item) != -1:
                times += 1
                mainDictRHS[item] = times
            else:
                mainDictRHS[item] = 20
        if fin == 10:
            return mainDictRHS

    if WHS == 'LHS':
        for i in rows:
            if i.find(item) != -1:
                times += 1
                mainDictLHS[item] = times
            else:
                mainDictLHS[item] = 1000

        if fin == 10:
            return mainDictLHS


def counter(set_rule):
    items = list(mainDictLHS.keys())
    RHS = set_rule['RHS']
    LHS = set_rule['LHS']
    rhs_aux = []
    lhs_aux = []

    for row in RHS:
        # print('****',row)
        if row.find(',)') == -1:
            rhs = row.replace(' ', '')
            rhs = rhs.replace("'", '')
            # print(rhs)
            rhs = rhs.replace('(', '')
            rhs = rhs.replace(')', '')
            rhs = rhs.split(',')
            rhs_aux.extend(rhs)
        else:
            rhs_1 = row.replace('(', '')
            rhs_1 = rhs_1.replace("'", '')
            rhs_1 = rhs_1.replace(',', '')
            rhs_1 = rhs_1.replace(')', '')
            rhs_aux.append(rhs_1)

    for row in LHS:
        # print('****',row)
        if row.find(',)') == -1:
            lhs = row.replace(' ', '')
            lhs = lhs.replace("'", '')
            # print(rhs)
            lhs = lhs.replace('(', '')
            lhs = lhs.replace(')', '')
            lhs = lhs.split(',')
            lhs_aux.extend(lhs)
        else:
            lhs_1 = row.replace('(', '')
            lhs_1 = lhs_1.replace("'", '')
            lhs_1 = lhs_1.replace(',', '')
            lhs_1 = lhs_1.replace(')', '')
            lhs_aux.append(lhs_1)
    fin = 0

    for i in items:
        fin += 1
        t = counterItem(i, rhs_aux, fin, 'RHS')
        tl = counterItem(i,lhs_aux, fin, 'LHS')

    return tl, t, len(RHS)


def lhs_rhs(df, file_out):
    df['lhs_rhs-peek'] = df['LHS_peek_obj_type']/df['RHS_peek_obj_type']
    df['lhs_rhs-isEmpty'] = df['LHS_isEmpty']/df['RHS_isEmpty']
    df['lhs_rhs-size'] = df['LHS_size']/df['RHS_size']
    df['lhs_rhs-calledMethod'] = df['LHS_calledMethod']/df['RHS_calledMethod']
    df['lhs_rhs-pushInput'] = df['LHS_pushInput']/df['RHS_pushInput']
    df['lhs_rhs-peek_p'] = df['LHS_peek_p'] / df['RHS_peek_p']
    df['lhs_rhs-isEmpty_p'] = df['LHS_isEmpty_p'] / df['RHS_isEmpty_p']
    df['lhs_rhs-size_p'] = df['LHS_size_p'] / df['RHS_size_p']
    df['lhs_rhs-calledMethod_p'] = df['LHS_calledMethod_p'] / df['RHS_calledMethod_p']
    df['lhs_rhs-pushInput_p'] = df['LHS_pushInput_p'] / df['RHS_pushInput_p']
    df.replace(50, 'No item', inplace=True)
    df.replace(1000, 'No item', inplace=True)
    df.replace(20, 'No item', inplace=True)

    df.to_csv(file_out)
    print('Done')


if __name__ == '__main__':
    import click

    global mainDictRHS
    # mainDictRHS = defaultdict()
    mainDictRHS = {'peek_obj_type': 0, 'isEmpty': 0, 'size': 0, 'calledMethod': 0, 'pushInput': 0,
                   'peek_p': 0, 'isEmpty_p': 0, 'size_p': 0, 'calledMethod_p': 0, 'pushInput_p': 0}

    global itemCount
    itemCount = {}

    global mainDictLHS
    mainDictLHS = {'peek_obj_type': 0, 'isEmpty': 0, 'size': 0, 'calledMethod': 0, 'pushInput': 0,
                   'peek_p': 0, 'isEmpty_p': 0, 'size_p': 0, 'calledMethod_p': 0, 'pushInput_p': 0}


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-r', '--rules', 'rules', help='set of rules')
    @click.option('-o', '--out file', 'file_out', help='output name')
    def main(file_in, rules, file_out):
        item_count = pd.DataFrame()
        col = list(mainDictRHS.keys())
        print('*** Reading Data ***')
        df = pd.read_csv(file_in, index_col=0)

        dfr = pd.read_csv(rules, index_col=0)

        df = preProsDF(df)
        df = df.reset_index()
        rulesV = df['RuleViolated']
        aux = []
        if rulesV.empty:
            print(rulesV)

        else:
            for row in rulesV:
                setRule = takeViolations(row)
                set_ruleF = preProsRules(setRule, dfr)
                set_ruleF = set_ruleF[['LHS', 'RHS']]
                lhs, rhs, tam = counter(set_ruleF)
                item_count = {'Number_of_Rules': tam, 'LHS_peek_obj_type': lhs['peek_obj_type'], 'LHS_isEmpty': lhs['isEmpty'], 'LHS_size': lhs['size'], 'LHS_calledMethod': lhs['calledMethod'], 'LHS_pushInput': lhs['pushInput'],
                        'LHS_peek_p': lhs['peek_p'], 'LHS_isEmpty_p': lhs['isEmpty_p'], 'LHS_size_p': lhs['size_p'], 'LHS_calledMethod_p': lhs['calledMethod_p'], 'LHS_pushInput_p': lhs['pushInput_p'],
                        'RHS_peek_obj_type': rhs['peek_obj_type'], 'RHS_isEmpty': rhs['isEmpty'], 'RHS_size': rhs['size'], 'RHS_calledMethod': rhs['calledMethod'], 'RHS_pushInput': rhs['pushInput'],
                        'RHS_peek_p': rhs['peek_p'], 'RHS_isEmpty_p': rhs['isEmpty_p'], 'RHS_size_p': rhs['size_p'], 'RHS_calledMethod_p': rhs['calledMethod_p'], 'RHS_pushInput_p': rhs['pushInput_p']}
                aux.append(item_count)
            final = pd.DataFrame(aux)
            lhs_rhs(final, file_out)

main()
