import pandas as pd
import sys, os, re

if (len(sys.argv) < 2):
    print(f'Usage: python {sys.argv[0]} IN_FILE [OUT_FILE] [OPTIONS]\n' +
          '    IN_FILE: Path to .csv data file\n' +
          '    OUT_FILE: File to save treated data in\n\n' +

          'Not enough arguments, exiting')
    sys.exit(0)


IN_FILE = sys.argv[1]
if (not os.path.exists(IN_FILE)):
    print(f'File not found: \'{IN_FILE}\', exiting')
    sys.exit(0)

if len(sys.argv) >= 3:
    OUT_FILE = sys.argv[2]
else:
    OUT_FILE = os.path.splitext(IN_FILE)[0] + '_avg' + os.path.splitext(IN_FILE)[1]
if os.path.exists(OUT_FILE):
    if (input('File already exists! Overwrite? [y/N]:') not in ['y', 'Y']):
        sys.exit(0)

# Read the CSV with semicolon separator
df = pd.read_csv(IN_FILE, sep=';')

# Replace commas with dots in potential numeric columns (exclude 'Data' and 'Hora UTC')
numeric_cols = df.columns.drop(['Data', 'Hora UTC'])
for col in numeric_cols:
    if df[col].dtype == 'object':  # Only for string-like columns
        df[col] = df[col].str.replace(',', '.').replace('', float('nan'))
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to float, NaN for non-numeric

# Convert 'Data' to datetime for grouping
df['Data'] = pd.to_datetime(df['Data'], format='%Y/%m/%d', errors='coerce')

# Drop rows with invalid dates (if any)
df = df.dropna(subset=['Data'])

# Group by 'Data' and compute mean for numeric columns only
daily_avg = df.groupby('Data').mean(numeric_only=True)

# Save to new CSV (index as 'Data')
daily_avg.to_csv(OUT_FILE)

print(f'Generated {OUT_FILE} with daily averages.')