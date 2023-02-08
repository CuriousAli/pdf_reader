import re
import fitz
from static_data import path



def get_dict(raw_text:str, info:dict):
    """Gives processed data of given data-defined PDF file"""
    title, start = get_title(raw_text)
    data = re.findall(r"(.*):(.*[^\n]*)", raw_text[start:])
    for key, value in data:
         info[key.strip()] = value

    info["NOTES"] = get_notes_value(raw_text)
    return info


def get_dict_with_numerated_keys(raw_text:str):
    """Gives processed and numerated data of given data-defined PDF file"""
    info = {}
    i = 2
    title, start = get_title(raw_text)
    info[("Voucher title", 1)] = title
    data = re.findall(r"(.*):(.*[^\n]*)", raw_text[start:])
    for key, value in data:
         info[(key.strip(), i)] = value
         i += 1
    info[("NOTES", 20)] = get_notes_value(raw_text)
    print(info)
    return info


def get_notes_value(raw_text):
    """Extracts value from raw text for NOTES field"""
    notes_value = raw_text[raw_text.rfind("NOTES:")+7::]
    return notes_value.strip()


def get_title(text:str):
    """Extracts title of the voucher"""
    end_of_title = text.find("\n")
    company = text[:end_of_title].strip()
    return company, end_of_title


def open_pdf_file():
    with fitz.open(path) as doc:
        for page in doc:
            raw_text = page.get_text()
        return raw_text


def save_pdf_file_as_image():
    '''Converting pdf file into image'''
    with fitz.open(path) as doc:
        page = doc.load_page(0)  # number of page
        zoom = 3    # zoom factor
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        output = "outfile.png"
        pix.save(output)
        return output
