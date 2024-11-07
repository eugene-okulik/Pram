import os
from collections.abc import Iterator
from typing import List

import argparse

find_next = True

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="Full path to the logs files", type=str)
parser.add_argument("-t", "--text", help="Text for search", default="", type=str)
parser.add_argument("-f", "--first", help="Show the first match", action="store_true", default=False)
args = parser.parse_args()


def read_file(filename: Iterator[str]) -> Iterator[List[str]]:
    for line in filename:
        yield line


def find_text(line: str, find_text: str, first: bool) -> List[str] | None:
    if find_text in line:
        words = line.split()
        find_words_index = []
        results = []
        for i, word in enumerate(words):
            if find_text in word:
                find_words_index.append(i)
                if first:
                    break
        for index in find_words_index:
            start = max(0, index - 5)
            end = min(len(words), index + 6)
            result = ' '.join(words[start:end])
            results.append(result)
        return results
    else:
        return None


for root, dirs, log_files in os.walk(args.directory):
    for log_file in log_files:
        if find_next:
            with open(f"{root}\\{log_file}", "r") as f:
                for index, line in enumerate(read_file(f)):
                    if not find_next:
                        break
                    results = find_text(line, args.text, args.first)
                    if results is not None and find_next:
                        for result in results:
                            print(f"File: {log_file}, line: {index} - {result}")
                            if args.first:
                                find_next = False
