import configparser


def read_section(config, section):
    parser = configparser.ConfigParser()
    parser.read(f'project/config/{config}.ini')
    res = {}
    if parser.has_section(section):
        for param in parser.items(section):
            res[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, config))

    return res


print("Initializing configs...")
auth = read_section('server', 'auth')
db = read_section('database', 'postgresql')
