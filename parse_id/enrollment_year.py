# -*- coding: utf-8 -*-
"""
This code is to parse and skim the student's enrollment year and semester information from Student ID
e.g., Student ID : 0CXX0000 or 0XXXX0000
ref:
    - enrollment year code :http://www.pr.tokai.ac.jp/gsc/pdf/ARCHIVES_NEWS_14.pdf
"""
import re
import datetime

def get_enrollement_year(student_id):
    """
    Return the enrollment year and semester on the student ID's student
    :param student_id: e.g., 0XXX0000 or 0XXXX0000 :: str
    :return: student info : {enrollment year, semester} :: dict
    """
    A2Z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    student_id = student_id.upper()
    enrollment_code = student_id[0:2]
#    print(enrollment_code)
    this_year = str(datetime.datetime.now().year)
#    print(this_year)
    if int(enrollment_code[0]) <= int(this_year[-1]):
        enrollment_year = this_year[0:3] + enrollment_code[0]
    else:
        enrollment_year = str(int(this_year[0:3]) - 1) + enrollment_code[0]

    if A2Z.index(enrollment_code[1]) <= 9:
        # Spring Semester
        enrollment_semester = 'Spring'
    elif 10 <= A2Z.index(enrollment_code[1]) <= 19:
        # Fall Semester
        enrollment_semester = 'Fall'

    enroll_info = {'enrollment_year': int(enrollment_year), 'enrollment_semester': enrollment_semester}

    return enroll_info


def verify_id(student_id):
    student_grade = None
    student_id = student_id.upper()
    id_pattern = r'^[0-9]{1}[A-Z]{3,4}[0-9]{3,4}'
    p_cmp = re.compile(id_pattern)
    m = p_cmp.match(student_id)
    if m:
        is_ok = True
        if re.search(r'\d{4}$', student_id):
            # undergraduate
            student_grade = 'undergraduate'
        elif re.search(r'\d{3}$', student_id):
            # graduate
            student_grade = 'graduate'
    else:
        is_ok = False

    return is_ok, student_grade


if __name__ == '__main__':
    # main
    # test code
    id = '0CDA9999'
    flg, g = verify_id(id)
    print(f'flag:{flg}\ngrade:{g}')

    info = get_enrollemnt_year(id)
    print(info)

    info = get_enrollemnt_year('6MDA2900')
    print(info)

