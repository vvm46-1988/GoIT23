import re

phone_number = "38050-111-22-22"
# TODO: def normalize_phone()...
cleaned_number = re.sub(r'[^0-9+]', '', phone_number)
if not cleaned_number.startswith('+'):
    if cleaned_number.startswith('380'):
        cleaned_number = "+" + cleaned_number
    else:
        cleaned_number = "+38" + cleaned_number
print(cleaned_number)
