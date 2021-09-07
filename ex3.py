import argparse
import os


def get_size_dir(mypath):
    size = 0
    for path, dirs, files in os.walk(mypath):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp) // 1024
    return f'{size} KB'


def get_size_suffix(mypath, suffix):
    size = 0
    for path, dirs, files in os.walk(mypath):
        for f in files:
            if f.endswith(suffix):
                fp = os.path.join(path, f)
                size += os.path.getsize(fp) // 1024
    return f'{size} KB'


def get_size_file(mypath):
    size = os.path.getsize(mypath) // 1024
    return f'{size} KB'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='get size of a directory or a file')
    parser.add_argument('-F', '--filesuffix', type=str, help='get size of a specific file')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--directory', type=str, help='get size of a directory')
    group.add_argument('-f', '--file', type=str, help='get size of a file')

    args = parser.parse_args()
    if args.filesuffix:
        if args.directory:
            print(get_size_suffix(args.directory, args.filesuffix))
    else:
        if args.file:
            print(get_size_file(args.file))
        elif args.directory:
            print(get_size_dir(args.directory))
