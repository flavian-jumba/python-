phonenumbers = ['2442526362', '2025551212', '2545551212', '2545551212', '2455551212', '2315551212']

def format_phone(phonenumbers):
    codes = []  # Creates an empty list to store codes
    kenya_found = False  # Flag to track if Kenya code is found
    for e in phonenumbers:  # Loops through each phone number
        ans = '+' + e[:3]   # Takes first 3 digits and adds '+' prefix
        if ans == '+254':   # Checks if the code IS '+254'
            codes.append(ans)  # Adds the code if it IS '+254'
            kenya_found = True  # Set the flag to True if Kenya code is found
    if not kenya_found:  # If no Kenya code was found
        print('Kenya is not found here')  # Print message if no '+254'
    return codes

area_codes = format_phone(phonenumbers)
print("The country code is:", area_codes)
