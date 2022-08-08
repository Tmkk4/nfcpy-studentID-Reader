# -*- coding: utf-8 -*-
"""
This code is to parse and skim the student's faculty and department information from Student ID
e.g., Student ID : 0CXX0000 or 0XXXX0000

ref:
    - csv : https://www.delftstack.com/ja/howto/python/python-read-file-into-dictionary/
    - fac dept code : http://www.tsc.u-tokai.ac.jp/risyuu_syllabus/syllabus_g.html
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
    with open('parse_id/initial_fac_dept_Tokai_Univ.csv', 'r', encoding='utf-8') as f:
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



