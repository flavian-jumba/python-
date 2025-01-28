phonenumbers = ['2442526362','2025551212','2545551212','2315551212','2455551212','2315551212']

def format_phone (phonenumbers):
    codes = []
    for e in phonenumbers:
        ans = '+'+e[:3]
        codes.append(ans)
    return codes
area_codes = format_phone(phonenumbers)
print("The country codes are:",area_codes)