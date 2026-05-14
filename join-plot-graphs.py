import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('Qt5Agg')  # or 'TkAgg' 
import matplotlib.pyplot as plt
import os, re, sys
import palettable.lightbartlein.diverging as pbl_lbt_dmaps
import palettable.colorbrewer.diverging as pbl_cbwr_dmaps

if (len(sys.argv) < 3):
    print(f'Usage: python {sys.argv[0]} SUS_CSV_PATH WTR_CSV_PATH [OPTIONS]\n' + 
           '    SUS_CSV_PATH: Path to SUS .csv data file\n' +
           '    WTR_CSV_PATH: Path to weather .csv data file\n\n' +
          
           '    Options:\n' +
           '    -j, --joined-csv: Generate joined data CSV\n\n'+

           'Not enough arguments, exiting')
    sys.exit(0)

SUS_CSV = sys.argv[1]
WTR_CSV = sys.argv[2]

# File checking
for path in [SUS_CSV, WTR_CSV]:
    if (not os.path.exists(path)):
        print(f'File not found: \'{path}\', exiting')
        sys.exit(0)

df_sus = pd.read_csv(SUS_CSV)
df_wtr = pd.read_csv(WTR_CSV)

# Parse short options
short_opts = ''
for i, arg in enumerate(sys.argv[1:], 1):
    if re.match(r'-[a-z]+', arg):
        short_opts = sys.argv[i][1:]
SHORT_OPTS = short_opts

## Convert the dates to proper datetime objects
df_sus['DT_INTER'] = pd.to_datetime(df_sus['DT_INTER'], format='%Y%m%d', errors='coerce')
df_sus['DT_SAIDA'] = pd.to_datetime(df_sus['DT_SAIDA'], format='%Y%m%d', errors='coerce')
df_wtr['data'] = pd.to_datetime(df_wtr['data'], errors='coerce')

# Remove rows where the date could not be parsed (should be none)
df_sus = df_sus.dropna(subset=['DT_INTER'])
df_sus = df_sus.dropna(subset=['DT_SAIDA'])
df_wtr = df_wtr.dropna(subset=['data'])

## Create a hospitalizations count column for each date
inter_counts = df_sus.groupby('DT_INTER').size().reset_index(name='numero_internacoes')

# Left join wtr -> sus
df = df_wtr.merge(
    df_sus,
    left_on='data',
    right_on='DT_INTER',
    how='left'
)

# Merge the count column into the main dataframe
df = df.merge(inter_counts, on='DT_INTER', how='left')
df['numero_internacoes'] = df['numero_internacoes'].fillna(0).astype(int)

# Move numero_internacoes to a specific position
dt_inter_count = df.pop('numero_internacoes')
ref_col_idx = df.columns.get_loc('data')
df.insert(ref_col_idx, 'numero_internacoes', dt_inter_count)
            
## Create a column for age in years, starting with NaN
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

if ('j' in SHORT_OPTS or '--joined-csv' in sys.argv):
    joined_csv_path = './joined_data.csv'
    df.to_csv(joined_csv_path, index=False)
    print(f"Joined CSV saved to {joined_csv_path}")

numeric_df = df.select_dtypes(include=['number']) #, 'datetime'
numeric_df = numeric_df.dropna(axis=1, how='all') # Drop columns that became all-NaN after the join

hm_df = numeric_df.drop(columns=['SEXO','VAL_UCI'], errors='ignore')

renames = {
    'idade_anos':           'Idade em anos',
    'SEXO':                 'Sexo do paciente',
    'numero_internacoes':   'Número de internações',
    'precip_mm':            'Precipitação média',
    'precip_tot_mm':        'Precipitação total',
    'precip_max_mm':        'Precipitação máxima',
    'press_nvl_estac_mb':   'Pressão atmosférica',
    'press_max_mb':         'Pressão atm. máx.',
    'press_min_mb':         'Pressão atm. mín.',
    'radiac_kjm2':          'Radiação global',
    'temp_seco_c':          'Temperatura do ar',
    'temp_orv_c':           'Temp. do ponto de orvalho',
    'temp_max_c':           'Temperatura máxima',
    'temp_min_c':           'Temperatura mínima',
    'temp_orv_max_c':       'Temperatura orvalho máx.',
    'temp_orv_min_c':       'Temperatura orvalho mín.',
    'umd_r_max_pct':        'Umidade rel. máx.',
    'umd_r_min_pct':        'Umidade rel. mín.',
    'umd_r_pct':            'Umidade relativa do ar',
    'vento_dir_gr':         'Vento, direção média',
    'vento_raj_max_mps':    'Vento, rajada máxima',
    'vento_vel_mps':        'Vento, velocidade média',
    'temp_var_c':           'Variação de temperatura',
    'temp_med_10d':         'Temp. média, últ. 10d',
    'temp_min_10d':         'Temp. mínima, últ. 10d',
    'temp_max_10d':         'Temp. máxima, últ. 10d',
    'temp_var_ext_10d':     'Var. temp. máx-mín últ. 10d',
    'temp_var_med_10d':     'Var. méd. da temp. últ. 10d',
    'umd_med_10d':          'Umidade rel. méd. últ. 10d',
    'precip_med_10d':       'Precipitação méd. últ. 10d',
    'press_med_10d':        'Pressão média, últ. 10d'
}
numeric_df.rename(mapper=renames, axis='columns', inplace=True)
hm_df.rename(mapper=renames, axis='columns', inplace=True)

# Compute correlation matrix
corr = hm_df.corr(min_periods=1)

# Hide mirrored values and the diagonal on the heatmap
mask = np.triu(np.ones_like(corr, dtype=bool))

## Create heatmap
plt.figure(figsize=(26, 16))
# colormap = pbl_cbwr_dmaps.RdBu_10_r
colormap = pbl_cbwr_dmaps.RdBu_11_r
sns.heatmap(corr, mask=mask, annot=True, cmap=colormap.mpl_colormap, vmin=-1, vmax=1, center=0, fmt='.2f')
if '_' in colormap.name and '_r' not in colormap.name:
    plt.title(f'Heatmap da correlação entre dados diários do SUS e clima (cmap: {colormap.name})')
else:
    plt.title(f'Heatmap da correlação entre dados diários do SUS e clima (cmap: {colormap.name}_{colormap.number})')
plt.tight_layout()
# plt.style.use('dark_background')
save_path = 'generated-graphs/heatmap'
plt.savefig(save_path, dpi=140, bbox_inches='tight') # plt.show()
print(f"Heatmap saved to {save_path}")


plt.figure()
sns.relplot(data=numeric_df, x='Umidade rel. méd. últ. 10d', y='Número de internações')
plt.tight_layout()

save_path = 'generated-graphs/umd-10d-intrn'
plt.savefig(save_path, dpi=160, bbox_inches='tight')
print(f"Scatterplot saved to {save_path}")