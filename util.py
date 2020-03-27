_CHARMAP = {
        "to_upper": {
            u"ı": u"I",
            u"i": u"İ",
        },
        "to_lower": {
            u"I": u"ı",
            u"İ": u"i",
        }
    }

def lower_tr(text):
        for key, value in _CHARMAP.get("to_lower").items():
            text = text.replace(key, value)
        return text.lower()

def upper_tr(text):
    for key, value in _CHARMAP.get("to_upper").items():
        text = text.replace(key, value)
    return text.upper()