STANDART_SAMPLE = [('Voucher title', 1), ('PN', 2), ('SN', 3), ('DESCRIPTION', 4), ('LOCATION', 5),
     ('CONDITION', 6), ('RECEIVER#', 7), ('UOM', 8), ('EXP DATE', 9), ('PO', 10),
     ('CERT SOURCE', 11), ('REC.DATE', 12), ('MFG', 13), ('BATCH# ', 14), ('DOM', 15),
     ('REMARK', 16), ('LOT# ', 17), ('TAGGED BY', 18), ('Qty', 19), ('NOTES', 20)]


def comparing_sequence_with_standart(sequence):
     sequence = list(sequence)
     assert sequence == STANDART_SAMPLE, "PDF file don't satisfy the standart"
     print("Everything is ok")