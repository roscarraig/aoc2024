def read_file_line(filename):
    with open(filename, 'r') as fhan:
        return fhan.readlines()
