import re


def capital_space(string):
    return re.sub(r'(\S)([A-Z])', r'\1 \2', string)


if __name__ == '__main__':
    print(capital_space("TheFirstProgrammingBootcamp"))
    print(capital_space("TheFirst ProgrammingBootcamp"))
    print(capital_space("TheFirst?ProgrammingBootcamp"))
