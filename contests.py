import csv

from cs50 import SQL

db = SQL("sqlite:///contests.db")

answer = input("Answer: ").strip()

rows = db.execute("SELECT COUNT(*) AS counter FROM contests WHERE Answer LIKE ?", answer)

row = rows[0]

print(row["counter"])