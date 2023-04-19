# Multichain Private Keys Checker
This is a tool for checking private keys for presence in the databases used, supports 7 types of coins (BTC, ETH, DOGE, LTC, DASH, ZEC, BCH) and 23 types of addresses.

# Prepare to work
1. Install Python (tested on 3.10)
2. Install Python modules:

```
pip install bitcoinlib bloomfilter cashaddress eth_hash bit secrets
```

3. Download databases from https://t.me/+5KYdGpreTuI2MTli
```
btc.bf eth.bf doge.bf ltc.bf dash.bf zec.bf bch.bf
```

# Usage
The main purpose is to check the database of keys you have
- Run with HEXes from file, input name after request:
```
python mpkc_from_file.py
```

Additional modes for testing
- Run with range set in DEC, sequental:
```
python mpkc_dec_range.py 1 100000
```
- Run for test (1-32 bits):
```
python mpkc_dec_range.py
```
- Run with range set in DEC, using python random generator
```
python mpkc_random_range.py 10000000000000000 90000000000000000
```
- Run with default settings (1-256 bits)
```
python mpkc_random_range.py
```
- Run with range set in DEC, using python secrets generator
```
python mpkc_secrets_range.py 10000000000000000 90000000000000000
```
- Run with default settings (1-256 bits)
```
python mpkc_secrets_range.py
```

If matches are found, the result will be written to a file.

# Screenshot

![Screenshot of mpkc_from_file.py](https://github.com/seega/MultichainPrivateKeysChecker/blob/main/screenshot_mpkc_from_file.png)

# List of addresses to check 
```
PRIVATE KEY HEX: 0000000000000000000000000000000000000000000000000000000000000001
Bitcoin compressed address (P2PKH) 1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH
Bitcoin uncompressed address (P2PKH) 1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm
Bitcoin compressed address SegWit Base58 (P2SH) 3JvL6Ymt8MVWiCNHC7oWU6nLeHNJKLZGLN
Bitcoin address SegWit Bech32 (P2WPKH) bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4
Bitcoin address SegWit Bech32 (P2WSH) bc1qpac4ht6afshdx2tctnhjnetz7u6g3j9zhwwmc4cqkdsa2jumq42qd3drf7
Ethereum standard address 0x7e5f4552091a69125d5dfcb7b8c2659029395bdf
Dogecoin compressed address (P2PKH) DFpN6QqFfUm3gKNaxN6tNcab1FArL9cZLE
Dogecoin uncompressed address (P2PKH) DJRU7MLhcPwCTNRZ4e8gJzDebtG1H5M7pc
Dogecoin compressed address SegWit Base58 (P2SH) A9faqPqnCRNQcZjkcFTviEQiLrkLPctjsJ
Litecoin compressed address (P2PKH) LVuDpNCSSj6pQ7t9Pv6d6sUkLKoqDEVUnJ
Litecoin uncompressed address (P2PKH) LYWKqJhtPeGyBAw7WC8R3F7ovxtzAiubdM
Litecoin compressed address SegWit Base58 (P2SH) MR8UQSBr5ULwWheBHznrHk2jxyxkHQu8vB
Litecoin address SegWit Bech32 (P2WPKH) ltc1qw508d6qejxtdg4y5r3zarvary0c5xw7kgmn4n9
Litecoin address SegWit Bech32 (P2WSH) ltc1qpac4ht6afshdx2tctnhjnetz7u6g3j9zhwwmc4cqkdsa2jumq42qw4rnnm
Dash compressed address (P2PKH) XmN7PQYWKn5MJFna5fRYgP6mxT2F7xpekE
Dash uncompressed address (P2PKH) XoyDQM3xGhFW5JqYBwTLckjqZ67Q3jZfAL
Dash compressed address SegWit Base58 (P2SH) 7jdxvk43wLb9hxuETjU1oUmzZqCg5D1fGv
Zcash compressed address (P2PKH) t1UYsZVJkLPeMjxEtACvSxfWuNmddpWfxzs
Zcash uncompressed address (P2PKH) t1X9yaRpCHJpWX1HrGUxEu39xyQinmo3Ana
Zcash compressed address SegWit Base58 (P2SH) t3bnw6tC26gH7JqRB8YcdbutFtwZP4Xp5o5
Bitcoin Cash compressed address (P2PKH) qp63uahgrxged4z5jswyt5dn5v3lzsem6cy4spdc2h
Bitcoin Cash uncompressed address (P2PKH) qzgmyjle755g2v5kptrg02asx5f8k8fg55zdx7hd4l
Bitcoin Cash compressed address SegWit Base58 (P2SH) pz70adegkkzz202l8acteduqa8hjrzng7s9tg65l3m
```
# Credits
Some pieces of https://github.com/iceland2k14 code were used (I would like to see an updated version of his secp256k1 library)

Cbloom.py by Noname400

# Q&A
Q: Why so slow?

A: If you know a library that supports all 23 types of addresses that are used here and works quickly, I will be happy to test it.

# Buy me a coffee
Bitcoin `1Cofee1xwYkeJydiUS9yG1ofcucMKFXVEY`
