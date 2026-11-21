POEM = """May I buy the bread?
You gave me the coin
and did not watch what I bought.
The loaf is mine.
Yours to give,
mine to spend.
"""


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
