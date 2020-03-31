import os


def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def write_file(path, data, mode='w'):
    f = open(path, mode)
    f.write(data)
    f.close()


def append_file(path, data, mode='a'):
    with open(path, mode) as file:
        file.write(data + '\n')


def delete_file(path, mode='w'):
    with open(path, mode):
        pass


def file_to_set(filename):
    result = set()
    with open(filename, 'rt') as file:
        for link in file:
            result.add(link.replace('\n', ''))

    return result


def set_to_file(data, filename):
    delete_file(filename)
    for link in sorted(data):
        append_file(filename, link)