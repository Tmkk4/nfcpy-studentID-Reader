# -*- coding:utf-8 -*-
# Check the connection to NFC Reader and Read Demo
"""
nfcpy v1.0.4 in Python 3.8.3
ref:
    - https://qiita.com/h_tyokinuhata/items/2733d3c5bc126d5d4445
    - https://qiita.com/Requin/items/206ce5fdf6b4644fd149
"""
import nfc

def is_recognized_reader():
    clf = nfc.ContactlessFrontend()
    return clf.open('usb')  # ** found usb:~ at usb:001:004 <- $ python -m nfc

def fetch_card_info():
    # Show the card's info:
    # Type3Tag:NDEF Type, RC-SAXX/X:IC Chip No., ID:IDm(2byte-6byte), PMM, SYS
    clf = nfc.ContactlessFrontend('usb')
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
    print('>> ', tag)
    return tag.dump()


if __name__ == '__main__':
    print('connected: ', is_recognized_reader())
    tag_dump = fetch_card_info()
    print(('  \n  '.join(tag_dump)))  # Nested : System > Area > Service > Block, Random Service


