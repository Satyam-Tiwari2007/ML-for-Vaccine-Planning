import pandas as pd

# Load real Delhi HMIS dataset
df = pd.read_csv("../dataset/delhi_real_vaccine_data.csv")

# Keep only important columns
important_cols = df.columns[:8]
clean_df = df[important_cols].copy()

# Rename columns for easy use
clean_df.columns = [
    "indicator",
    "serial_no",
    "parameter",
    "type",
    "subdistrict_1",
    "subdistrict_2",
    "subdistrict_3",
    "subdistrict_4"
]

# Remove missing rows
clean_df = clean_df.dropna()

# Save cleaned version
clean_df.to_csv("../dataset/delhi_cleaned_vaccine_data.csv", index=False)

print("Delhi dataset cleaned successfully!")