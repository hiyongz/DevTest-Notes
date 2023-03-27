# -*-coding:utf-8-*-

import configparser


def get_variables(filename):
    config = configparser.ConfigParser()
    config.read(filename)

    variables = {}
    for section in config.sections():
        for key, value in config.items(section):
            var = "%s.%s" % (section, key)
            variables[var] = value
    return variables

filename = 'D:\pythonproj\DevTest-Notes\RobotFramework\scripts\config.ini'
variables = get_variables(filename)
print(variables)