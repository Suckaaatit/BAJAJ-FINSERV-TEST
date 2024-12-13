active_count = sum(1 for record in data for medicine in record['consultationData']['medicines'] if medicine['isActive'])
inactive_count = sum(1 for record in data for medicine in record['consultationData']['medicines'] if not medicine['isActive'])
total_medicines = active_count + inactive_count

# Calculate percentages
active_percentage = (active_count / total_medicines) * 100 if total_medicines > 0 else 0
inactive_percentage = (inactive_count / total_medicines) * 100 if total_medicines > 0 else 0

active_percentage, inactive_percentage
