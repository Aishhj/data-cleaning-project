import pandas as pd


df = pd.read_csv('marketing_campaign.csv', sep='\t') 

# 2. Clean column names: lowercase, remove spaces, replace with underscores
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

# 3. Show column names
print("Cleaned column names:", df.columns.tolist())

# 4. Check and display missing values
print("\nMissing values per column:\n", df.isnull().sum())

# 5. Drop rows with any missing values (or use fillna if preferred)
df = df.dropna()

# 6. Remove duplicate rows
df = df.drop_duplicates()

# 7. Standardize text fields (e.g., education, marital_status)
df['education'] = df['education'].str.lower().str.strip()
df['marital_status'] = df['marital_status'].str.lower().str.strip()

# 8. Convert 'dt_customer' to datetime format
df['dt_customer'] = pd.to_datetime(df['dt_customer'], dayfirst=True, errors='coerce')

# Check if any dates failed to convert
print("\nUnparseable dates in dt_customer:", df['dt_customer'].isnull().sum())

# 9. Check and convert data types
# Convert income to numeric if it's not already
df['income'] = pd.to_numeric(df['income'], errors='coerce')
df = df.dropna(subset=['income'])  # Drop rows where income couldn't be converted

# Convert 'year_birth' to int
df['year_birth'] = df['year_birth'].astype(int)

# 10. Preview cleaned data
print("\nCleaned Data Sample:\n", df.head())

# 11. Save cleaned dataset to a new CSV
df.to_csv('cleaned_data.csv', index=False)

