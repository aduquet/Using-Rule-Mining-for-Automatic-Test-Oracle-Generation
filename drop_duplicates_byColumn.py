import os
import glob as gl
import pathlib
import pandas as pd


# set working directory
# os.chdir("/mydir")


# find all csv files in the folder
# use glob pattern matching -> extension = 'csv'
# save result in list -> all_filenames
def dropper(df, save_path, file_out):
    df2=df.drop_duplicates(subset=['LHS', 'RHS'], keep='last')
    df2 = df2.reset_index(drop=True)
    file_out2 = save_path + file_out
    df2.to_csv(file_out2+'.csv')
    print('\n *** Data is saved in *** \n', file_out2)


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='csv files path for merging')
    @click.option('-s', '-- One file or directory', 'd', help=' *dir* for directory or *one* for one file')
    @click.option('-o', '--out', 'file_out', help='final csv name')
    def main(file_in, d, file_out):
        save_path = str(pathlib.Path().absolute()) + '\\' + 'without-duplicates'
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        if d == 'dir':
            dataPath = gl.glob(file_in)
            for i in range(0, len(dataPath)):
                df = pd.read_csv(dataPath[i], index_col=0)
                name = dataPath[i].split('.')
                name =name[0]
                sa = save_path + '\\' + name + '_'
                dropper(df, sa, file_out)

        else:
            df = pd.read_csv(file_in, index_col=0)
            file_out = save_path + '\\' + file_out + '.csv'
            dropper(df, save_path, file_out)

        # joiner(file_in, save_path, file_out)

main()
