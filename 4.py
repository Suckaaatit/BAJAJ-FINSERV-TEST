columns_to_check = ['patientDetails_firstName', 'patientDetails_lastName', 'patientDetails_birthDate']
missing_percentage = {}

for column in columns_to_check:
 
    total_missing = df[column].isnull().sum() + (df[column] == '').sum()
 
    missing_percentage[column] = round((total_missing / len(df)) * 100, 2)

missing_values_output = ', '.join(str(value) for value in missing_percentage.values())

missing_values_output
