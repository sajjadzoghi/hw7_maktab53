import re


def counter(word, case_sensitive=False):
    with open("sample.html") as f:
        if case_sensitive:
            return len(re.findall(rf'\b{word}\b', f.read()))
        else:
            return len(re.findall(rf'\b{word}\b', f.read(), re.I))


if __name__ == '__main__':
    print(counter("Python"))
    print(counter("Python", case_sensitive=True))
