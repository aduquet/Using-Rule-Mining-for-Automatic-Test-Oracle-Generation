import os
import glob as gl
import pathlib
import pandas as pd


def saveFile(df, file_out, name):
    df.to_csv(file_out + name + '.csv')
    print('\n *** Data is saved in *** \n', file_out)


def explorer(df, name):
    name = name.split('.')
    name = name[0]

    testID = df['testId'].value_counts()
    testID_describe = testID.describe()
    instanceId = df['instanceId'].value_counts()
    instanceId_describe = instanceId.describe()
    # print(instanceId.describe())
    size = (df['size'].describe())
    isEmpty_T = df[df['isEmpty'] == True]
    isEmpty_F = df[df['isEmpty'] == False]
    peek_obj_type = df['peek_obj_type'].describe()
    method = df['calledMethod'].value_counts()
    method_d = df['calledMethod'].describe()
    pushInput = df['pushInput'].describe()

    data = {'DS': name, '# of Total rows': len(df),
            'testId-Max': round(testID_describe['max']),
            'testId-Min': round(testID_describe['min']),
            'testId-Avg': round(testID_describe['mean']),
            'testId-Unique': round(testID_describe['count']),
            'instanceId-Max': round(instanceId_describe['max']),
            'instanceId-Min': round(instanceId_describe['min']),
            'instanceId-Avg': round(instanceId_describe['mean']),
            'instanceId-unique': round(instanceId_describe['count']),
            'size_max': round(size['max']),
            'size_min': round(size['min']),
            'isEmpty_True': len(isEmpty_T),
            'isEmpty_False': len(isEmpty_F),
            'peek_obj_type-unique': peek_obj_type['unique'],
            'peek_obj_type-Most frequent': peek_obj_type['top'],
            'peek_obj_type-Freq': peek_obj_type['freq'],
            'method-most frequent': method_d['top'],
            'method-Push': method['push'],
            'method-Pop': method['pop'],
            'method-clear': method['clear'],
            'pushInput-unique': pushInput['unique'],
            'pushInput-Most frequent': pushInput['top'],
            'pushInput-Freq': pushInput['freq']
            }
    return data


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='csv files path for merging')
    @click.option('-s', '-- One file or directory', 'd', help=' *dir* for directory or *one* for one file')
    @click.option('-o', '--out', 'file_out', help='final csv name')
    def main(file_in, d, file_out):
        save_path = str(pathlib.Path().absolute()) + '\\' + 'Reports-dataExplorer'
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        if d == 'dir':
            aux = []
            dataPath = gl.glob(file_in)
            for i in range(0, len(dataPath)):
                df = pd.read_csv(dataPath[i], index_col=0)
                name = dataPath[i].split('\\')
                name = name[-1]
                new_df = explorer(df, name)
                aux.append(new_df)
            df = pd.DataFrame(aux)
            file_out2 = save_path + '\\'
            saveFile(df, file_out2, file_out)
        else:

            df = pd.read_csv(file_in, index_col=0)
            name = file_in.split('\\')
            name = name[-1]

            df = explorer(df, name)
            df = pd.DataFrame(df)
            file_out2 = save_path + '\\' + file_out
            saveFile(df, file_out2)

main()
