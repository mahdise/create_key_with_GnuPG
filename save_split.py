import csv
import pandas as pd


def save_split_file(list_of_split, file_name):

    try :
        file_name_list = file_name.split(".")
        file_name_list = file_name_list[0].split("\\")
        processed_file_name = file_name_list[-1]

    except:
        processed_file_name = "newly_encrypt_file"

    file_name = processed_file_name

    length_of_key = len(list_of_split)

    filename = file_name + ".csv"
    '../GnuPG/bin/gpg.exe'

    plot_file_name_dir = '../store_share_code/' + filename
    list_part = list()

    for index in range(0, length_of_key):
        name = "part_" + str(index)

        list_part.append(name)

    fieldnames = list_part

    try:

        with open(plot_file_name_dir) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
        new_plot = False

    except OSError as e:
        new_plot = True

    if new_plot:
        with open(plot_file_name_dir, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fieldnames)

    data = pd.read_csv(plot_file_name_dir)

    for index, value in enumerate(list_of_split):
        name = "part_" + str(index)
        data[name] = [value]
    data.to_csv(plot_file_name_dir, index=False, header=True)

    return "Passed"






if __name__ == '__main__':
    save_split_file(["asss", "hhhhh", "kkkkkk", "zzzzzz", "ooooooo"], "a")
