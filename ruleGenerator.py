import pandas as pd
import numpy as np
import glob as gl
import pickle
from efficient_apriori import apriori
import warnings
import os
import pathlib
warnings.filterwarnings('ignore')


def ruleGenerator(transactions_df, support, conf):
    """
        Generate set of rules with given support and confidence using transactions_df
    """
    # print(transactions_df.head(20))
    transactions_array = transactions_df.to_numpy()
    transactions_list = transactions_array.tolist()
    itemSets, rules = apriori(transactions_list, min_support=support, min_confidence=conf)
    return itemSets, rules


def saveFile(pre, test_path, df, file_out):
    name = test_path + '\\' + file_out + '_' + pre

    df.to_csv(name+'.csv')
    print('\n *** DONE!! *** \n', name)


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-s', '--support', 'sup', help='Support value')
    @click.option('-c', '--confidence', 'conf', help='Confidence Value')
    #@click.option('-f', '--file', 'file', help='Name of the directory in which data will be stored')
    @click.option('-o', '--out', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, file_out, sup, conf):
        print('*** Reading Data ***')
        paths = str(pathlib.Path().absolute()) + '\\' + 'Rules'

        if not os.path.exists(paths):
            os.mkdir('Rules')

        dfListUnion = []
        dfListIntersection = []
        sets1 = []
        sets2 = []

        df = pd.read_csv(file_in, index_col=0)
        names = df.columns.values
        df.drop(columns=['instanceId', 'testId'], inplace=True)
        for n in names:
            if n == 'diff':
                df.drop(columns=['diff'], inplace=True)

        items, rules1 = ruleGenerator(df, float(sup), float(conf))
        sets1.append(set(rules1))
        sets2.append(set(items))

        sup = sup.split('.')
        sup = sup[-1]
        conf = conf.replace('.', '_')
        union = set.union(*sets1)
        lUnion = list(union)

        for rul in range(0, len(lUnion)):
            dfAux_union = {'LHS': tuple(lUnion[rul].lhs), 'LHS_size': len(lUnion[rul].lhs),
                           'RHS': tuple(lUnion[rul].rhs), 'RHS_size': len(lUnion[rul].rhs),
                           'conf': lUnion[rul].confidence,
                           'sup': lUnion[rul].support, 'lift': lUnion[rul].lift, 'cov': lUnion[rul].conviction}
            dfListUnion.append(dfAux_union)

        dfRule = pd.DataFrame(dfListUnion)
        ruleName = 'sup_0' + sup + '-conf_' + conf
        saveFile(ruleName, paths, dfRule, file_out)

main()
