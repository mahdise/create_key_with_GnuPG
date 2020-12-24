import csv
import pandas as pd


def save_split_file(list_of_split, file_name):
    """
    This method used for save the part share into csv.
    :param list_of_split: split part , type list of string
    :param file_name: absolute file path with name
    :return:
    """
    # we used here try and except to ignore error in file name
    try:
        # preprocessed file name
        file_name_list = file_name.split(".")
        file_name_list = file_name_list[0].split("\\")
        processed_file_name = file_name_list[-1]

    except:
        # if failed to prepossess, we will use here by default name
        processed_file_name = "newly_encrypt_file"

    file_name = processed_file_name
    length_of_key = len(list_of_split)
    filename = file_name + ".csv"
    # file_name_dir = '../store_share_code/' + filename
    file_name_dir = 'store_share_code/' + filename

    # create column name
    list_part = list()
    for index in range(0, length_of_key):
        name = "part_" + str(index + 1)

        list_part.append(name)
    fieldnames = list_part

    # check file name exist or not, if not create file
    try:
        with open(file_name_dir) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
        new_file_ = False
    except OSError as e:
        new_file_ = True
    if new_file_:
        with open(file_name_dir, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fieldnames)
    # write data into csv
    data = pd.read_csv(file_name_dir)
    for index, value in enumerate(list_of_split):
        name = "part_" + str(index + 1)
        data[name] = [value]
    data.to_csv(file_name_dir, index=False, header=True)

    return "Passed"

