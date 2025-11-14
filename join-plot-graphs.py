import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('Qt5Agg')  # or 'TkAgg' 
import matplotlib.pyplot as plt
import os
import sys

if (len(sys.argv) < 3):
    print(f'Usage: python {sys.argv[0]} SUS_CSV_PATH WTR_CSV_PATH\n' + 
          '    SUS_CSV_PATH: Path to SUS .csv data file\n' +
          '    WTR_CSV_PATH: Path to weather .csv data file\n\n' +
          
          'Not enough arguments, exiting')
    sys.exit(0)

SUS_CSV = sys.argv[1]
if (not os.path.exists(SUS_CSV)):
    print(f'File not found: \'{SUS_CSV}\', exiting')
    sys.exit(0)

WTR_CSV = sys.argv[2]
if (not os.path.exists(WTR_CSV)):
    print(f'File not found: \'{WTR_CSV}\', exiting')
    sys.exit(0)

df_sus = pd.read_csv(SUS_CSV)
df_wtr = pd.read_csv(WTR_CSV)

# Convert the join keys to proper datetime objects
df_sus['DT_INTER'] = pd.to_datetime(df_sus['DT_INTER'], format='%Y%m%d', errors='coerce')
df_wtr['data'] = pd.to_datetime(df_wtr['data'], errors='coerce')

# Remove rows where the date could not be parsed (should be none)
df_sus = df_sus.dropna(subset=['DT_INTER'])
df_wtr = df_wtr.dropna(subset=['data'])

# Create a count column for each DT_INTER date
inter_counts = df_sus.groupby('DT_INTER').size().reset_index(name='numero_internacoes')

# Left join sus -> wtr
df = df_sus.merge(
    df_wtr,
    left_on='DT_INTER',
    right_on='data',
    how='left'
)

# Merge the count column into the main dataframe
df = df.merge(inter_counts, on='DT_INTER', how='left')

# Move numero_internacoes to a specific position
dt_inter_count = df.pop('numero_internacoes')
ref_col_idx = df.columns.get_loc('data')
df.insert(ref_col_idx, 'numero_internacoes', dt_inter_count)
            
# Create a column for age in years, starting with NaN
df.insert(0, 'idade_anos', np.nan)
# Use years if available and >= 1
mask_years = df['def_idade_anos'].notna() & (df['def_idade_anos'] >= 1)
df.loc[mask_years, 'idade_anos'] = df['def_idade_anos'] # select only the rows where mask_years is True, in the 'idade_anos' column
# Use months if years < 1 (or missing) and months available
mask_months = ((df['def_idade_anos'].isna()) | (df['def_idade_anos'] < 1)) & df['def_idade_meses'].notna() & (df['def_idade_meses'] >= 1)
df.loc[mask_months, 'idade_anos'] = df['def_idade_meses'] / 12
# Use days if both years and months < 1 (or missing) and days available
mask_days = ((df['def_idade_anos'].isna()) | (df['def_idade_anos'] < 1)) & ((df['def_idade_meses'].isna()) | (df['def_idade_meses'] < 1)) & df['def_idade_dias'].notna()
df.loc[mask_days, 'idade_anos'] = df['def_idade_dias'] / 365.25

# Drop all other redundant age columns
df = df.drop(columns=['NASC', 'COD_IDADE', 'IDADE', 'def_cod_idade', 'def_idade_anos', 'def_idade_meses', 'def_idade_dias'], errors='ignore')

df.to_csv('joined_data.csv', index=False)

numeric_df = df.select_dtypes(include=['number', 'datetime'])
numeric_df = numeric_df.dropna(axis=1, how='all') # Drop columns that became all-NaN after the join

# Compute correlation matrix
corr = numeric_df.corr(min_periods=1)

# Hide mirrored values and the diagonal on the heatmap
mask = np.triu(np.ones_like(corr, dtype=bool))

# Create heatmap
plt.figure(figsize=(24, 14))
sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, fmt='.2f')
plt.title('Heatmap da correlação entre dados do SUS e clima (diário)')
plt.show()