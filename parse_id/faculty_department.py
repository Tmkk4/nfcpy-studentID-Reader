# -*- coding: utf-8 -*-
"""
This code is to parse and skim the student's faculty and department information from Student ID
e.g., Student ID : 0CXX0000 or 0XXXX0000

ref:
    - csv : https://www.delftstack.com/ja/howto/python/python-read-file-into-dictionary/
    - fac dept code : http://www.tsc.u-tokai.ac.jp/risyuu_syllabus/syllabus_g.html,
                      TIPS > Cabinet > 各学科時間割PDF,
                      https://www.tokai-pe.com/2022%E6%98%A5%E5%AD%A6%E6%9C%9F%E6%8E%88%E6%A5%AD%E3%81%AE%E3%83%A1%E3%83%8B%E3%83%A5%E3%83%BC/%E5%AD%A6%E9%83%A8%E5%AD%A6%E7%A7%91%E4%B8%80%E8%A6%A7/
"""
import re

def get_fac_dept(student_id):
    """
    Return the student's faculty and department from the student ID
    :param student_id: Student ID  e.g., 0CXX0000 or 0XXXX0000
    :return: the student's faculty and department information
    """
    student_id = student_id.upper()
    dept_initials = {}
    with open('parse_id/Initials_Fac_Dept_Tokai_Univ_2022.csv', 'r', encoding='utf-8') as f:
        for line in f:
            (i, f, d) = line.split(',')
            dept_initials[i] = f + ' ' + d

#    print(dept_initials)

    fd_code = student_id[2:4]
#    print(fd_code)
    try:
        fd_info = dept_initials[fd_code]
    except:
        return 'NotFound'
    else:
        return fd_info


if __name__ == '__main__':
    id = '0cdi2299'
    belonging = get_fac_dept(id)
    print(f'ID:{id} is belong to {belonging}.')



