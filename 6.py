
for record in data:
    birthdate_str = record['patientDetails'].get('birthDate')
    age = calculate_age(birthdate_str)
    if age is not None:
        if age <= 12:
            record['ageGroup'] = 'Child'
        elif 13 <= age <= 19:
            record['ageGroup'] = 'Teenage'
        elif 20 <= age <= 59:
            record['ageGroup'] = 'Adult'
        else:
            record['ageGroup'] = 'Senior'
    else:
        record['ageGroup'] = 'Unknown' 

updated_adult_count = sum(1 for record in data if record.get('ageGroup') == 'Adult')

updated_adult_count

