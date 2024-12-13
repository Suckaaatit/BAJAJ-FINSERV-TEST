import pandas as pd
from scipy.stats import pearsonr


# Convert birthDate to age
current_year = 2024
df = pd.DataFrame(data)
df["birthDate"] = pd.to_datetime(df["birthDate"], errors="coerce")
df["age"] = current_year - df["birthDate"].dt.year

# Remove entries with missing ages or medicines
df_cleaned = df.dropna(subset=["age"])

# Calculate Pearson correlation
correlation, p_value = pearsonr(df_cleaned["age"], df_cleaned["medicines"])

correlation, p_value
