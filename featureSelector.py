import pandas as pd
import os
import pathlib
import numpy as np
import glob as gl
import os
import pathlib
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings('ignore')


def saveFile(df, file_out):
    df.to_csv(file_out)
    print('\n ***  Data is saved in *** \n', file_out)


def fs_1(df, file_out, path):
    df = df[
        ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "diff"]]

    if os.path.exists(path):
        name = 'FS-1' + '\\' + file_out
        saveFile(df, name)
    else:
        os.mkdir('FS-1')
        name = 'FS-1' + '\\' + file_out
        saveFile(df, name)


def fs_2(df, file_out, path):
    df = df[
        ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "calledMethod", "diff"]]

    if os.path.exists(path):
        name = 'FS-2' + '\\' + file_out
        saveFile(df, name)
    else:
        os.mkdir('FS-2')
        name = 'FS-2' + '\\' + file_out
        saveFile(df, name)


def fs_3(df, file_out, path):
    df = df[
        ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "calledMethod", "size_p", "isEmpty_p",
         "peek_obj_type_p", "calledMethod_p", "diff"]]
    if os.path.exists(path):
        name = 'FS-3' + '\\' + file_out
        saveFile(df, name)
    else:
        os.mkdir('FS-3')
        name = 'FS-3' + '\\' + file_out
        saveFile(df, name)


def fs_4(df, file_out, path):
    df = df[
        ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "calledMethod", "pushInput", "size_p", "isEmpty_p",
         "peek_obj_type_p", "calledMethod_p", "diff"]]
    if os.path.exists(path):
        name = 'FS-4' + '\\' + file_out
        saveFile(df, name)
    else:
        os.mkdir('FS-4')
        name = 'FS-4' + '\\' + file_out
        saveFile(df, name)


def fs_5(df, file_out, path):
    df = df[
        ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "calledMethod", "pushInput", "size_p", "isEmpty_p",
         "peek_obj_type_p", "calledMethod_p", "pushInput_p", "diff"]]

    if os.path.exists(path):
        name = 'FS-5' + '\\' + file_out
        saveFile(df, name)
    else:
        os.mkdir('FS-5')
        name = 'FS-5' + '\\' + file_out
        saveFile(df, name)


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-s', '-- One file or directory', 'direc', help=' *direc* for directory or *one* for one file')
    @click.option('-o', '--out', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, direc, file_out):
        print('*** Reading Data ***')

        if direc == 'directory':
            dataPath = gl.glob(file_in)
            for i in range(0, len(dataPath)):
                df = pd.read_csv(dataPath[i], index_col=0)
                name = dataPath[i].split('\\')
                name = name[-1]
                name = file_out + name
                paths = str(pathlib.Path().absolute()) + '\\FS-1'
                fs_1(df, name, path=paths)
                paths = str(pathlib.Path().absolute()) + '\\FS-2'
                fs_2(df, name, path=paths)
                paths = str(pathlib.Path().absolute()) + '\\FS-3'
                fs_3(df, name, path=paths)
                paths = str(pathlib.Path().absolute()) + '\\FS-4'
                fs_4(df, name, path=paths)
                paths = str(pathlib.Path().absolute()) + '\\FS-5'
                fs_5(df, name, path=paths)

        else:
            df = pd.read_csv(file_in, index_col=0)

            paths = str(pathlib.Path().absolute()) + '\\FS-1'
            fs_1(df, file_out, path=paths)
            paths = str(pathlib.Path().absolute()) + '\\FS-2'
            fs_2(df, file_out, path=paths)
            paths = str(pathlib.Path().absolute()) + '\\FS-3'
            fs_3(df, file_out, path=paths)
            paths = str(pathlib.Path().absolute()) + '\\FS-4'
            fs_4(df, file_out, path=paths)
            paths = str(pathlib.Path().absolute()) + '\\FS-5'
            fs_5(df, file_out, path=paths)

main()
