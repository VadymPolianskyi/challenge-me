from configparser import ConfigParser


def read(config, section):
    parser = ConfigParser()
    parser.read(config + '.ini')

    res = {}
    if parser.has_section(section):
        for param in parser.items(section):
            res[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, config))

    return res
