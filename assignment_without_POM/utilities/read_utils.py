import pandas


def get_csv_as_list(file_path):
    csv_file = pandas.read_csv(filepath_or_buffer=file_path)
    return csv_file.values.tolist()


def get_excel_as_list(io, sheet_name):
    excel_file = pandas.read_excel(io=io, sheet_name=sheet_name)
    return excel_file.values.tolist()


def get_json_file():
    json_file = pandas.read_json(path_or_buf='../test_data/data.json')
    print(json_file.values)
