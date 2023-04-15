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
- Run with HEXes from file, input name after request:
```
python mpkc_from_file.py
```
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
python mpkc_random_range.py for default settings (1-256 bits)
```
- Run with range set in DEC, using python secrets generator
```
python mpkc_secrets_range.py 10000000000000000 90000000000000000
```
- Run with default settings (1-256 bits)
```
python mpkc_secrets_range.py
```

# Credits
Some pieces of https://github.com/iceland2k14 code were used (I would like to see an updated version of his secp256k1 library)

Cbloom.py by Noname400

# Q&A
Q: Why so slow?

A: If you know a library that supports all 23 types of addresses that are used here and works quickly, I will be happy to test it.

# Buy me a coffee
Bitcoin `1Cofee1xwYkeJydiUS9yG1ofcucMKFXVEY`
