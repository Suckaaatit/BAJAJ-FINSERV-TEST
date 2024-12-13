import pandas as pd
import json

# Reloading the JSON data
file_path = "/mnt/data/DataEngineeringQ2.json"
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert JSON data to a pandas DataFrame
df = pd.json_normalize(data, sep='_')

# Define a function to validate phone numbers based on the given rules
def is_valid_phone_number(phone):
    if not isinstance(phone, str):
        return False
    if phone.startswith('+91') or phone.startswith('91'):
        # Remove the prefix for further validation
        phone = phone.lstrip('+91').lstrip('91')
    # Check if the remaining number is numeric and within the valid range
    return phone.isdigit() and 6000000000 <= int(phone) <= 9999999999

# Apply the validation logic to the phoneNumber column
df['isValidMobile'] = df['phoneNumber'].apply(is_valid_phone_number)

# Count the number of valid phone numbers
valid_phone_count = df['isValidMobile'].sum()

valid_phone_count
