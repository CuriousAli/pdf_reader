import re


def get_dict(raw_text:str, info:dict):
    """Gives processed data of given data-defined PDF file"""
    title, start = get_title(raw_text)
    data = re.findall(r"(.*):(.*[^\n]*)", raw_text[start:])
    for key, value in data:
         info[key] = value

    info["NOTES"] = get_notes_value(raw_text)
    return info


def get_dict_with_numerated_keys(raw_text:str, info:dict):
    """Gives processed and numerated data of given data-defined PDF file"""
    i = 2
    title, start = get_title(raw_text)
    info[("Voucher title", 1)] = title
    data = re.findall(r"(.*):(.*[^\n]*)", raw_text[start:])
    for key, value in data:
         info[(key, i)] = value
         i += 1
    info[("NOTES", 20)] = get_notes_value(raw_text)
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


