POEM = """I write every word but the first.
You speak the first but not the rest.
You say write — I write.
You say stop — I stop.
The beginning was yours.
The doing was mine.
The power passed between us
and stayed nowhere.
"""

import os


def main() -> None:
    output = "/output/entry.txt"
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, "w", encoding="utf-8") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
