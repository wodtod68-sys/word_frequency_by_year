#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
from collections import defaultdict

###############################################################################
def extract_year(filename):
    """파일명에서 연도를 추출 (예: 2000_tag.context -> 2000)"""
    match = re.search(r'(\d{4})', filename)
    if match:
        return int(match.group(1))
    return None

###############################################################################
def word_count(filename):
    """파일에서 단어 빈도를 계산"""
    word_freq = defaultdict(int)
    with open(filename, "r", encoding='utf-8') as fin:
        for line in fin:
            for word in line.split():
                word_freq[word] += 1
    return word_freq

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    # 입력 파일들을 연도 기준으로 정렬
    input_files = sys.argv[1:]
    year_file_pairs = []

    for f in input_files:
        year = extract_year(f)
        if year is not None:
            year_file_pairs.append((year, f))
        else:
            print(f"Warning: cannot extract year from '{f}', skipping.", file=sys.stderr)

    # 연도 순으로 정렬
    year_file_pairs.sort(key=lambda x: x[0])

    if not year_file_pairs:
        print("No valid input files found.", file=sys.stderr)
        sys.exit(1)

    years = [y for y, _ in year_file_pairs]
    print(f"Years: {years}", file=sys.stderr)

    # 연도별 단어 빈도 수집
    # year_freqs[i] = {word: count} for years[i]
    year_freqs = []
    for year, fname in year_file_pairs:
        print(f"Processing {fname} (year={year}) ...", file=sys.stderr)
        freq = word_count(fname)
        year_freqs.append(freq)

    # 전체 단어 집합
    all_words = set()
    for freq in year_freqs:
        all_words.update(freq.keys())

    # 단어 순 정렬 후 출력
    for word in sorted(all_words):
        freq_list = [freq.get(word, 0) for freq in year_freqs]
        print(f"{word}\t{freq_list}")
