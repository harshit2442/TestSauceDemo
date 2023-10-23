import csv

import allure

from Config import config_data


def get_data(data_file_path):
    data_path = (config_data.folder_data_file_path + data_file_path)
    with open(data_path, 'r') as f:
        reader = csv.reader(f)
        # skipping first row as header
        next(reader)
        data = [tuple(row) for row in reader]
    return data
