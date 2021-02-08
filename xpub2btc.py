#!./venv/bin/python

from electrum import bitcoin, bip32, util

import sys

lines = [x.strip() for x in sys.stdin.readlines()]

if len(lines) !=1:
    print("wrong input")
    sys.exit(1)

node = bip32.BIP32Node.from_xkey(lines[0])
type = "p2pkh"
if len(sys.argv) == 2:
    type = sys.argv[1]
pubkey = bitcoin.pubkey_to_address(type, util.bh2u(node.eckey.get_public_key_bytes()))

print(pubkey)
