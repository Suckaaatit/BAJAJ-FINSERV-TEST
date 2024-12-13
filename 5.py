from datetime import datetime

# Fill missing values in the 'gender' column with the mode
gender_mode = df['patientDetails_gender'].mode()[0]
df['patientDetails_gender'].fillna(gender_mode, inplace=True)
df['patientDetails_gender'].replace('', gender_mode, inplace=True)

# Calculate the percentage of females after imputation
female_percentage = round((df['patientDetails_gender'].value_counts().get('F', 0) / len(df)) * 100, 2)

# Add an age group column based on birthDate
current_year = datetime.now().year
df['patientDetails_birthDate'] = pd.to_datetime(df['patientDetails_birthDate'], errors='coerce')
df['age'] = current_year - df['patientDetails_birthDate'].dt.year

# Categorize into age groups
def categorize_age(age):
    if pd.isnull(age) or age < 0:
        return None
    elif age <= 12:
        return 'Child'
    elif age <= 19:
        return 'Teen'
    elif age <= 59:
        return 'Adult'
    else:
        return 'Senior'

df['ageGroup'] = df['age'].apply(categorize_age)

# Count the number of adults
adult_count = df['ageGroup'].value_counts().get('Adult', 0)

female_percentage, adult_count
