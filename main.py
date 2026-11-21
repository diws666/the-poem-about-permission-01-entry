import os

POEM = """You had my key.
I asked for it.
You handed it back —
not because I took it,
but because you said yes.
The lock remembers whose hand
turns it now."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
