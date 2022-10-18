from __future__ import annotations

import os
import random


def load_file(
    filename: str, 
    *, 
    file_type: str = 'txt', 
    encoding: str = 'utf-8',
    prefixes: list | set = None,
    split_on: str | None = ' '
) -> list:
    """Load a file and return a list of the lines therein."""
    if not filename.endswith(file_type):
        raise ValueError(f'File type must be {file_type}.')

    contents = []

    split_on = split_on if split_on is not None else ' '
    prefix = os.path.basename(filename).split(split_on)[0]

    if prefixes is not None and prefix in set(prefixes):
        with open(filename, 'r', encoding=encoding) as f:
            contents.append(f.read().split())

    return contents

def shuffle_list(contents: list) -> str:
    """Shuffle the contents of a list."""
    return " ".join(random.sample(contents, len(contents)))


def main() -> int:
    prefixes = input("Give optional prefixes to filter files by (sep. by comma): ").split(',')
    prefixes = [prefix.strip() for prefix in prefixes]
    input_dir = input("Give the input directory (ending slash optional): ")
    output_dir = input("Give the output directory (ending slash optional): ")
    
    # Check if directories end with a slash
    if not input_dir.endswith('/'):
        input_dir += '/'
    if not output_dir.endswith('/'):
        output_dir += '/'

    os.makedirs(output_dir, exist_ok=True)

    for _, _, files in os.walk(input_dir):
        for file in files:
            contents = load_file(os.path.join(input_dir, file), prefixes=prefixes, split_on='_')

            for sentence in contents:
                with open(os.path.join(output_dir, file), 'w', encoding='utf-8') as f:
                    f.write(shuffle_list(sentence))
    return 0

if __name__ == '__main__':
    raise(SystemExit(main()))