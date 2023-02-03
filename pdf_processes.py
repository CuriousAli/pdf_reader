import fitz

from parser import *
from path_holder import path
from validator import comparing_sequence_with_standart, validating_barcode


VOUCHER_INFO = {}


def get_voucher_info_as_dictionary():
    with fitz.open(path) as doc:
        for page in doc:
            raw_text = page.get_text()
            result = get_dict(raw_text, VOUCHER_INFO)
        return result


def checking_the_compliance_of_the_structure_with_the_requirements():
    with fitz.open(path) as doc:
        for page in doc:
            raw_text = page.get_text()
            sequence = get_dict_with_numerated_keys(raw_text, VOUCHER_INFO).keys()
            comparing_sequence_with_standart(sequence)


def checking_barcode(display=False):
    validating_barcode(display)


checking_barcode(True)