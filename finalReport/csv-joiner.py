import os
import glob as gl
import pathlib
import pandas as pd

# set working directory
# os.chdir("/mydir")


# find all csv files in the folder
# use glob pattern matching -> extension = 'csv'
# save result in list -> all_filenames
def joiner(path, save_path, file_out):
    extension = 'csv'
    all_filenames = [i for i in gl.glob(path)]
    # print(all_filenames)

    # combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    # export to csv
    name = save_path + '\\' + file_out + '.csv'
    combined_csv.to_csv(name, index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='csv files path for merging')
    @click.option('-o', '--out', 'file_out', help='final csv name')
    def main(file_in, file_out):
        save_path = str(pathlib.Path().absolute()) + '\\' + 'merged_files'
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        joiner(file_in, save_path, file_out)

main()
