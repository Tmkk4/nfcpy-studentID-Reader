# -*- coding:utf-8 -*-
# Attempt to Read Student ID(SID) Demo
"""
nfcpy v1.0.4 in Python 3.8.3
ref:
    - https://qiita.com/h_tyokinuhata/items/2733d3c5bc126d5d4445
    - https://qiita.com/Requin/items/206ce5fdf6b4644fd149
"""
import re
import sys
import time
import nfc
from parse_id import enrollment_year, faculty_department

# Student ID : System 809E > Random Service 128 > Service Code 0x200B
SID_SERVICE_CODE = 0x200B


def shape_sid(sid):
    ug_sid_pattern = r'^[0-9]{1}[A-Z]{3,4}[0-9]{4}'
    p_cmp = re.compile(ug_sid_pattern)
    s = p_cmp.search(sid)
    sid = s.group()
    if sid:
        return sid


def show_student_info(sid):
    flg, g = enrollment_year.verify_id(sid)

    e_info = enrollment_year.get_enrollment_year(sid)
    fd_info = faculty_department.get_fac_dept(sid)
    print(f"isStudentIDCard:{flg}\ngrade:{g}\nenrollment year:{e_info['enrollment_year']}\nsemester:{e_info['enrollment_semester']}\nbelonging:{fd_info}")


def on_connected(tag):
    # Try to read the card's Student ID on Connected
    if isinstance(tag, nfc.tag.tt3.Type3Tag):
        # NFCカードのNDEF TypeがFeliCa(Type3)であるかどうか 型check
        try:
            # SID(16bit)から 上位10bitを取り出す(SERVICE_CODE >> 6)
            # 下位6bitをマスクして取り出す(SERVICE_CODE && 0x3f(0b 0011 1111))
            srv_cd = nfc.tag.tt3.ServiceCode(SID_SERVICE_CODE >> 6, SID_SERVICE_CODE & 0x3f)
            # service : index of arguments 'service_list' of read_w/o_encryption
            blk_cd = nfc.tag.tt3.BlockCode(0, service=0)
            # read blk_cd's block data
            blk_data = tag.read_without_encryption([srv_cd], [blk_cd])
            # fetch SID
            sid = str(blk_data[0:9].decode("utf-8")).upper()
            sid = shape_sid(sid)
            print('SID:', sid)
            show_student_info(sid)
        except Exception as e:
            print("Error:%s" % e, file=sys.stderr)
    else:
        print("Error:Not Type3Tag", file=sys.stderr)
    return True  # connect event handlerへTrue返すと, カード触れてから離すまでに"1回だけ"処理する


if __name__ == '__main__':
    clf = nfc.ContactlessFrontend('usb')
    try:
        while 1:
            # set callback to event handler on connected
            clf.connect(rdwr={'on-connect': on_connected})

    except KeyboardInterrupt:
        print('[Quited] By KeyboardInterruption')
        clf.close()
        sys.exit(0)
