'''
karri korsu
cleans data not found when migrating your library between streaming services on soundiiz
ie: Domino (expanded edition) -> Domino
usage: python ./clean_soundiiz_csv.py filepath (optional:) > cleaned.csv
'''
from re import sub
from sys import argv
if len(argv) > 1:
    path = argv[1].strip()
else:
    exit(print("nobueno"))

with open(path, "r", encoding="utf-8") as f:
    for row in f:
        if row.endswith(",1\n"):
            continue
        elif "(" or "[" or "{" in row:
            clean_curly = sub(r"\s*\{[^}]*\}", "", row)
            clean_square = sub(r"\s*\[[^]]*\]", "", clean_curly)
            cleaned = sub(r"\s*\([^)]*\)", "", clean_square)
            print(cleaned)
