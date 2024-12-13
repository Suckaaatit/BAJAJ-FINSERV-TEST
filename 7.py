total_medicines = sum(len(record['consultationData']['medicines']) for record in data)
average_medicines = total_medicines / len(data)

average_medicines
