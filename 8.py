from collections import Counter


all_medicines = [medicine['medicineName'] for record in data for medicine in record['consultationData']['medicines']]

medicine_frequency = Counter(all_medicines)

third_most_common_medicine = medicine_frequency.most_common()[2] if len(medicine_frequency) >= 3 else None

third_most_common_medicine
