from worker import *

from validator import comparing_sequence_with_standart, validating_barcode


def get_voucher_info_as_dictionary():
    VOUCHER_INFO = {}
    raw_text = open_pdf_file()
    result = get_dict(raw_text, VOUCHER_INFO)
    print(result)
    return result


def checking_the_compliance_of_the_structure_with_the_requirements():
    raw_text = open_pdf_file()
    sequence = get_dict_with_numerated_keys(raw_text).keys()
    comparing_sequence_with_standart(sequence)


def checking_barcode(display=False):
    validating_barcode(display)


get_voucher_info_as_dictionary()
checking_the_compliance_of_the_structure_with_the_requirements()
checking_barcode(True)
