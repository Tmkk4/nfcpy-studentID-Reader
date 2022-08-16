# -*- coding:utf-8 -*-
"""
Read SuiCa / PASMO Demo
* nfcpy v.1.0.3+で, 比較的新しい Suica, PASMO等交通系ICカードを読み取ろうとすると
  Error "This is not an NFC Forum Tag."が出る場合の対処法
  nfcpy v1.0.4 in Python 3.8.3
ref:

    - Read SuiCa Tips : https://www.slideshare.net/m2wasabi/nfcpy-0100
                        https://qiita.com/h-hata/items/f9632b4005fc3a1a8ed1
                        https://nfcpy.readthedocs.io/en/latest/modules/tag.html
                        https://buildmedia.readthedocs.org/media/pdf/nfcpy/latest/nfcpy.pdf
"""
# SuiCa : tag obj : nfc.tag.tt3_sony.FelicaStandard
import sys
import nfc

SERVICE_CODE = 0x090F
NUM_BLOCKS = 20

def connected(tag):
    if isinstance(tag, nfc.tag.tt3_sony.FelicaStandard):
        try:
            for i in range(NUM_BLOCKS):
                sc = nfc.tag.tt3.ServiceCode(SERVICE_CODE >> 6, SERVICE_CODE & 0x3F)
                bc = nfc.tag.tt3.BlockCode(i, service=0)
                data = tag.read_without_encryption([sc], [bc])  # :: bytearray
                print("".join(['%02x' % s for s in data]))
        except Exception as e:
            print('error: %s' % e, file=sys.stderr)
    else:
        print('error: tag isn\'t SONY Felica', file=sys.stderr)
if __name__ == '__main__':
    clf = nfc.ContactlessFrontend('usb')
    print('>> ')
    clf.connect(rdwr={'on-connect': connected})


