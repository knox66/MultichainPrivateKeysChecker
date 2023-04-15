# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 00:00:00 2023
Multichain Private Keys Checker v0.1
Secret random generator version
@author: https://github.com/seega
"""
from datetime import datetime
import hashlib
import secrets
import sys
import time
from bitcoinlib.encoding import pubkeyhash_to_addr_bech32
from bitcoinlib.keys import Address
from bloomfilter import BloomFilter
from cashaddress import convert
from eth_hash.auto import keccak
import bit
print('[$] Multichain Private Keys Checker v0.1')
print('[*] Secret random generator version')
if len(sys.argv) < 3:
    RANGESTART = 1
    RANGEEND = 115792089237316195423570985008687907852837564279074904382605163141518161494336
    print('[!] The range is not set, the values are set by default (1-256 bits)')
else:
    RANGESTART = int(sys.argv[1])
    RANGEEND = int(sys.argv[2])
try:
    RESULTFILE = 'found_secret_range.txt'
    print('[~] Loading Bitcoin bloomfilter...')
    BTC_BF_FILE = 'btc.bf'
    with open(BTC_BF_FILE, "rb") as fp:
        btc_bf = BloomFilter.load(fp)
    print(f'[>] Bitcoin bloomfilter loaded, {BTC_BF_FILE} lines: {btc_bf.size}')
    print('[~] Loading Ethereum bloomfilter...')
    ETH_BF_FILE = 'eth.bf'
    with open(ETH_BF_FILE, "rb") as fp:
        eth_bf = BloomFilter.load(fp)
    print(f'[>] Ethereum bloomfilter loaded, {ETH_BF_FILE} lines: {eth_bf.size}')
    print('[~] Loading Dogecoin bloomfilter...')
    DOGE_BF_FILE = 'doge.bf'
    with open(DOGE_BF_FILE, "rb") as fp:
        doge_bf = BloomFilter.load(fp)
    print(f'[>] Dogecoin bloomfilter loaded, {DOGE_BF_FILE} lines: {doge_bf.size}')
    print('[~] Loading Litecoin bloomfilter...')
    LTC_BF_FILE = 'ltc.bf'
    with open(LTC_BF_FILE, "rb") as fp:
        ltc_bf = BloomFilter.load(fp)
    print(f'[>] Litecoin bloomfilter loaded, {LTC_BF_FILE} lines: {ltc_bf.size}')
    print('[~] Loading Dash bloomfilter...')
    DASH_BF_FILE = 'dash.bf'
    with open(DASH_BF_FILE, "rb") as fp:
        dash_bf = BloomFilter.load(fp)
    print(f'[>] Dash bloomfilter loaded, {DASH_BF_FILE} lines: {dash_bf.size}')
    print('[~] Loading Zcash bloomfilter...')
    ZEC_BF_FILE = 'zec.bf'
    with open(ZEC_BF_FILE, "rb") as fp:
        zec_bf = BloomFilter.load(fp)
    print(f'[>] Zcash bloomfilter loaded, {ZEC_BF_FILE} lines: {zec_bf.size}')
    print('[~] Loading Bitcoin Cash bloomfilter...')
    BCH_BF_FILE = 'bch.bf'
    with open(BCH_BF_FILE, "rb") as fp:
        bch_bf = BloomFilter.load(fp)
    print(f'[>] Bitcoin Cash bloomfilter loaded, {BCH_BF_FILE} lines: {bch_bf.size}')
    total_bf_size = btc_bf.size + eth_bf.size + doge_bf.size \
                    + ltc_bf.size + dash_bf.size + zec_bf.size + bch_bf.size
    print(f'[~] Total lines from bloomfilers loaded: {total_bf_size}')
    def hash_160(pubk_bytes):
        """hash_160 from public key bytes"""
        return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()
    def eth_address(un_pubk_bytes):
        """Convert uncompressed public keys bytes to Ethereum address"""
        return '0x' + keccak(un_pubk_bytes[1:])[-20:].hex()
    def pub_to_hash_160(pubk_bytes):
        """Convert public key bytes to hash 160"""
        return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()
    start_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f'[~] [{start_time}] Checking private keys begins...')
    start_time = time.time()
    TOTAL_CHECKED = 0
    LAST_TOTAL_CHECKED = 0
    FOUNDED = 0
    TOTAL_KEYS = 1000000000
    for i in range(TOTAL_KEYS):
        random_int = secrets.randbelow(RANGEEND - RANGESTART) + RANGESTART
        hexkey = hex(random_int)[2:]
        #print(hexkey) # generator check
        pk = bit.Key.from_hex(hexkey)
        # pylint: disable=W0212
        upub = pk._pk.public_key.format(compressed=False)
        # pylint: disable=W0212
        cpub = pk._pk.public_key.format(compressed=True)
        crmd = pub_to_hash_160(cpub)
        urmd = pub_to_hash_160(upub)
        A1 = 'Bitcoin compressed address (P2PKH)'
        ADDR1 = bit.base58.b58encode_check(b'\x00' + crmd)
        A2 = 'Bitcoin uncompressed address (P2PKH)'
        ADDR2 = bit.base58.b58encode_check(b'\x00' + urmd)
        A3 = 'Bitcoin compressed address SegWit Base58 (P2SH)'
        ADDR3 = bit.base58.b58encode_check(b'\x05' + hash_160(b'\x00\x14' + crmd))
        A4 = 'Bitcoin address SegWit Bech32 (P2WPKH)'
        ADDR4 = pubkeyhash_to_addr_bech32(crmd, prefix='bc', witver=0, separator='1')
        A5 = 'Bitcoin address SegWit Bech32 (P2WSH)'
        btcp2wsh =  Address(cpub, encoding='bech32', script_type='p2wsh')
        ADDR5 = btcp2wsh.address
        A6 = 'Ethereum standard address'
        ADDR6 = eth_address(upub)
        A7 = 'Dogecoin compressed address (P2PKH)'
        ADDR7 = bit.base58.b58encode_check(b'\x1e' + crmd)
        A8 = 'Dogecoin uncompressed address (P2PKH)'
        ADDR8 = bit.base58.b58encode_check(b'\x1e' + urmd)
        A9 = 'Dogecoin compressed address SegWit Base58 (P2SH)'
        ADDR9 = bit.base58.b58encode_check(b'\x16' + hash_160(b'\x00\x14' + crmd))
        A10 = 'Litecoin compressed address (P2PKH)'
        ADDR10 = bit.base58.b58encode_check(b'\x30' + crmd)
        A11 = 'Litecoin uncompressed address (P2PKH)'
        ADDR11 = bit.base58.b58encode_check(b'\x30' + urmd)
        A12 = 'Litecoin compressed address SegWit Base58 (P2SH)'
        ADDR12 = bit.base58.b58encode_check(b'\x32' + hash_160(b'\x00\x14' + crmd))
        A13 = 'Litecoin address SegWit Bech32 (P2WPKH)'
        ADDR13 = pubkeyhash_to_addr_bech32(crmd, prefix='ltc', witver=0, separator='1')
        A14 = 'Litecoin address SegWit Bech32 (P2WSH)'
        ltcp2wsh =  Address(cpub, network='litecoin', encoding='bech32',
                            script_type='p2wsh')
        ADDR14 = ltcp2wsh.address
        A15 = 'Dash compressed address (P2PKH)'
        ADDR15 = bit.base58.b58encode_check(b'\x4c' + crmd)
        A16 = 'Dash uncompressed address (P2PKH)'
        ADDR16 = bit.base58.b58encode_check(b'\x4c' + urmd)
        A17 = 'Dash compressed address SegWit Base58 (P2SH)'
        ADDR17 = bit.base58.b58encode_check(b'\x10' + hash_160(b'\x00\x14' + crmd))
        A18 = 'Zcash compressed address (P2PKH)'
        ADDR18 = bit.base58.b58encode_check(b'\x1c\xb8' + crmd)
        A19 = 'Zcash uncompressed address (P2PKH)'
        ADDR19 = bit.base58.b58encode_check(b'\x1c\xb8' + urmd)
        A20 = 'Zcash compressed address SegWit Base58 (P2SH)'
        ADDR20 = bit.base58.b58encode_check(b'\x1c\xbd' + hash_160(b'\x00\x14' + crmd))
        A21 = 'Bitcoin Cash compressed address (P2PKH)'
        ADDR21OLD = bit.base58.b58encode_check(b'\x00' + crmd)
        ADDR21 = convert.to_cash_address(ADDR21OLD)[12:]
        A22 = 'Bitcoin Cash uncompressed address (P2PKH)'
        ADDR22OLD = bit.base58.b58encode_check(b'\x00' + urmd)
        ADDR22 = convert.to_cash_address(ADDR22OLD)[12:]
        A23 = 'Bitcoin Cash compressed address SegWit Base58 (P2SH)'
        ADDR23OLD = bit.base58.b58encode_check(b'\x05' + hash_160(b'\x00\x14' + crmd))
        ADDR23 = convert.to_cash_address(ADDR23OLD)[12:]
        CHAINEXPLORER ='https://blockchair.com/search?q='
        for i, (address, blockchain) in enumerate([(ADDR1, btc_bf),
                                                   (ADDR2, btc_bf),
                                                   (ADDR3, btc_bf),
                                                   (ADDR4, btc_bf),
                                                   (ADDR5, btc_bf),
                                                   (ADDR6[2:], eth_bf),
                                                   (ADDR7, doge_bf),
                                                   (ADDR8, doge_bf),
                                                   (ADDR9, doge_bf),
                                                   (ADDR10, ltc_bf),
                                                   (ADDR11, ltc_bf),
                                                   (ADDR12, ltc_bf),
                                                   (ADDR13, ltc_bf),
                                                   (ADDR14, ltc_bf),
                                                   (ADDR15, dash_bf),
                                                   (ADDR16, dash_bf),
                                                   (ADDR17, dash_bf),
                                                   (ADDR18, zec_bf),
                                                   (ADDR19, zec_bf),
                                                   (ADDR20, zec_bf),
                                                   (ADDR21, bch_bf),
                                                   (ADDR22, bch_bf),
                                                   (ADDR23, bch_bf)]):
            if address in blockchain:
                with open(RESULTFILE, 'a', encoding="utf-8") as f:
                    FOUNDED += 1
                    a = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11,
                         A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22, A23]
                    atype = a[i]
                    if i == 5:
                        f.write(f'{atype},{hexkey.zfill(64)},{CHAINEXPLORER}0x{address}\n')
                    else:
                        f.write(f'{atype},{hexkey.zfill(64)},{CHAINEXPLORER}{address}\n')
        TOTAL_CHECKED += 1
        elapsed_time = time.time() - start_time
        if elapsed_time > 1:
            rate = (TOTAL_CHECKED - LAST_TOTAL_CHECKED) / elapsed_time
            CHECKED = TOTAL_CHECKED
            COMPLETE = (CHECKED / TOTAL_KEYS) * 100
            elapsed_seconds = (TOTAL_KEYS - CHECKED) / rate
            hours, remainder = divmod(elapsed_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f'\r[~] [F:{FOUNDED}]'
                  f'[K:{CHECKED:.0f}/{TOTAL_KEYS}]'
                  f'[K:{rate:.0f}keys/s]'
                  f'[A:{CHECKED*23:.0f}/{TOTAL_KEYS*23}]'
                  f'[A:{rate*23:.0f}adr/s]'
                  f'[{COMPLETE:.2f}%]'
                  f'[E:{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}]',
                  end='', flush=True)
            start_time = time.time()
            LAST_TOTAL_CHECKED = TOTAL_CHECKED
    end_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f'\n[!] [{end_time}] Task COMPLETED, matches found: {FOUNDED}')
    if FOUNDED > 0:
        print(f'[$] FOUNDED addresses and private keys wrote in {RESULTFILE}')
except KeyboardInterrupt:
    print(f'\n[#] [{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] Program interrupted by user')
    sys.exit()
