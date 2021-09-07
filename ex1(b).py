import re


def counter_word_html(word, tag):
    with open("sample.html") as f:
        res = re.findall(rf'<{tag}.*>.*</{tag}>', f.read())
        s = 0
        for tag in res:
            s += len(re.findall(rf'\b{word}\b', tag))
        return s


if __name__ == '__main__':
    print(counter_word_html("default", 'a'))
