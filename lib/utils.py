import hashlib
import sys

def sha256(b: bytes) -> bytes:
    return hashlib.sha256(b).digest()

def fb(b: bytes) -> int:
    return int.from_bytes(b, "big")

def tb(i: int, l: int) -> bytes:
    return int.to_bytes(i, length =l, byteorder = "big")

def one_line_from_stdin() -> str:
    lines = [x.strip() for x in sys.stdin.readlines()]

    if len(lines) !=1:
        print("wrong input")
        sys.exit(1)

    return lines[0]