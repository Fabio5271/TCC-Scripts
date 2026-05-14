import pandas as pd
import sys, os, re, glob

# Eliminate checks in the loop to make this as fast as possible
def make_dfs_list(file_paths):
    dfs = []
    for file in file_paths:
        print(file)
        df = pd.read_csv(file, sep=';', na_values=[-9999, -9999.0, '-9999', '-9999.0'])
        df = df.drop(columns=[col for col in df.columns if col.startswith('Unnamed')])
        df.rename(columns={'DATA (YYYY-MM-DD)': 'Data'}, inplace=True)
        df.rename(columns={'HORA (UTC)': 'Hora UTC'}, inplace=True)
        df.rename(columns={'RADIACAO GLOBAL (Kj/m²)': 'RADIACAO GLOBAL (KJ/m²)'}, inplace=True)
        dfs.append(df)
    return dfs

def make_dfs_list_q(file_paths):
    dfs = []
    for file in file_paths:
        df = pd.read_csv(file, sep=';', na_values=[-9999, -9999.0, '-9999', '-9999.0'])
        df = df.drop(columns=[col for col in df.columns if col.startswith('Unnamed')])
        df.rename(columns={'DATA (YYYY-MM-DD)': 'Data'}, inplace=True)
        df.rename(columns={'HORA (UTC)': 'Hora UTC'}, inplace=True)
        df.rename(columns={'RADIACAO GLOBAL (Kj/m²)': 'RADIACAO GLOBAL (KJ/m²)'}, inplace=True)
        dfs.append(df)
    return dfs

if (len(sys.argv) < 3):
    print(f'Usage: python {sys.argv[0]} CSV_DIR_PATH [OUT_FILE] [OPTIONS]\n' +
          '    CSV_DIR_PATH: Path to directory contining all .csv files to be included\n' +
          '    OUT_FILE: File to save treated data in\n\n' +

          '    Options:\n' +
          '    -k, --keep-names: Keep original column names\n' +
          '    -q, --quiet:      Don\'t show file names as they are processed\n\n' +

          'Not enough arguments, exiting')
    sys.exit(0)

if (sys.argv[1][-1] == '/'): # Path to directory that contains all extracted CSVs, remove '/' from end of path
    CSV_DIR_PATH = sys.argv[1][:-1]
else:
    CSV_DIR_PATH = sys.argv[1]
if (not os.path.exists(CSV_DIR_PATH)):
    print(f'Path not found: \'{CSV_DIR_PATH}\', exiting')
    sys.exit(0)

OUT_FILE = sys.argv[2]
if os.path.exists(OUT_FILE):
    if (input('File already exists! Overwrite? [y/N]:') not in ['y', 'Y']):
        sys.exit(0)

short_opts = ''
for i, arg in enumerate(sys.argv[1:], 1):
    if re.match(r'-[a-z]+', arg):
        short_opts = sys.argv[i][1:]
SHORT_OPTS = short_opts

NEW_COLS = [
    'data',                   # Data
    'hora_utc',               # Hora UTC
    'precip_mm',              # PRECIPITAÇÃO TOTAL, HORÁRIO (mm)
    'press_nvl_estac_mb',     # PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)
    'press_max_mb',           # PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)
    'press_min_mb',           # PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)
    'radiac_kjm2',            # RADIACAO GLOBAL (Kj/m²)
    'temp_seco_c',            # TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)
    'temp_orv_c',             # TEMPERATURA DO PONTO DE ORVALHO (°C)
    'temp_max_c',             # TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)
    'temp_min_c',             # TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)
    'temp_orv_max_c',         # TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C)
    'temp_orv_min_c',         # TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C)
    'umd_r_max_pct',          # UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)
    'umd_r_min_pct',          # UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)
    'umd_r_pct',              # UMIDADE RELATIVA DO AR, HORARIA (%)
    'vento_dir_gr',           # VENTO, DIREÇÃO HORARIA (gr) (° (gr))
    'vento_raj_max_mps',      # VENTO, RAJADA MAXIMA (m/s)
    'vento_vel_mps'           # VENTO, VELOCIDADE HORARIA (m/s)
]

file_paths = glob.glob(f'{CSV_DIR_PATH}/INMET_*.csv') + glob.glob(f'{CSV_DIR_PATH}/INMET_*.CSV')
if '--quiet' in sys.argv or 'q' in SHORT_OPTS:
    dfs = make_dfs_list_q(file_paths)
else:
    dfs = make_dfs_list(file_paths)

# Concatenate all DataFrames into one
df = pd.concat(dfs, ignore_index=True)

# Rename columns, optionally keep old names
if '--keep-names' in sys.argv or 'k' in SHORT_OPTS:
    KEEP_NAMES = True
    OLD_COL_NAMES = dict(zip(NEW_COLS, df.columns))
else:
    KEEP_NAMES = False
if len(NEW_COLS) < len(df.columns):
    NEW_COLS = NEW_COLS + df.columns.tolist()[len(NEW_COLS):]
df.columns = NEW_COLS
COL_DATE = df.columns[0]

# Replace commas with dots + convert to numeric 
for col in df.columns:
    if col not in ('Data', 'data', 'Hora UTC', 'hora_utc'):
        df[col] = (df[col].astype(str)
                   .str.replace(',', '.')
                   .replace({'': float('nan'), 'nan': float('nan')}))
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert 'Data' to datetime for grouping
df[COL_DATE] = pd.to_datetime(df[COL_DATE], format='mixed', errors='raise')

# Drop rows with invalid dates (if any)
df = df.dropna(subset=[COL_DATE])
df = df[df[COL_DATE] < pd.to_datetime('2025-12-01')] # Because we only have SUS data up to 2025-11-30

# Group by 'Data' and compute min, mean, max for numeric columns only
cols_avg = [COL_DATE, 'precip_mm', 'press_nvl_estac_mb', 'radiac_kjm2', 'temp_seco_c', 'temp_orv_c', 'umd_r_pct', 'vento_dir_gr', 'vento_vel_mps']
cols_min = [COL_DATE, 'precip_mm', 'press_min_mb', 'temp_min_c', 'temp_orv_min_c', 'umd_r_min_pct']
cols_max = [COL_DATE, 'precip_mm', 'press_max_mb', 'temp_max_c', 'temp_orv_max_c', 'umd_r_max_pct', 'vento_raj_max_mps']
cols_sum = [COL_DATE, 'precip_mm']
df_daily_avg = df[cols_avg].groupby(COL_DATE).mean(numeric_only=True).round(2)
df_daily_min = df[cols_min].groupby(COL_DATE).min(numeric_only=True).round(2)
df_daily_max = df[cols_max].groupby(COL_DATE).max(numeric_only=True).round(2)
df_daily_sum = df[cols_sum].groupby(COL_DATE).sum(numeric_only=True).round(2)
# Rejoin data
df_daily = df_daily_avg
df_daily.insert(df_daily.columns.get_loc('precip_mm') + 1, 'precip_tot_mm', df_daily_sum['precip_mm'])
df_daily.insert(df_daily.columns.get_loc('precip_mm') + 2, 'precip_max_mm', df_daily_max['precip_mm'])
df_daily.insert(df_daily.columns.get_loc('press_nvl_estac_mb') + 1, 'press_min_mb', df_daily_min['press_min_mb'])
df_daily.insert(df_daily.columns.get_loc('press_nvl_estac_mb') + 2, 'press_max_mb', df_daily_max['press_max_mb'])
df_daily.insert(df_daily.columns.get_loc('temp_seco_c') + 1, 'temp_min_c', df_daily_min['temp_min_c'])
df_daily.insert(df_daily.columns.get_loc('temp_seco_c') + 2, 'temp_max_c', df_daily_max['temp_max_c'])
df_daily.insert(df_daily.columns.get_loc('temp_orv_c') + 1, 'temp_orv_min_c', df_daily_min['temp_orv_min_c'])
df_daily.insert(df_daily.columns.get_loc('temp_orv_c') + 2, 'temp_orv_max_c', df_daily_max['temp_orv_max_c'])
df_daily.insert(df_daily.columns.get_loc('umd_r_pct') + 1, 'umd_r_min_pct', df_daily_min['umd_r_min_pct'])
df_daily.insert(df_daily.columns.get_loc('umd_r_pct') + 2, 'umd_r_max_pct', df_daily_max['umd_r_max_pct'])
df_daily.insert(df_daily.columns.get_loc('vento_vel_mps') + 1, 'vento_raj_max_mps', df_daily_max['vento_raj_max_mps'])
# Alternate method (unordered join)
# df_daily = df_daily_avg.join(df_daily_min, on=COL_DATE, how='inner', validate='1:1')
# df_daily = df_daily.join(df_daily_max, on=COL_DATE, how='inner', validate='1:1')

# Add calculated columns
# Add temp variation first so we can already use it
temp_diff = (df_daily['temp_max_c'] - df_daily['temp_min_c']).round(2)
temp_min_idx = df_daily.columns.get_loc('temp_min_c')
df_daily.insert(temp_min_idx + 1, 'temp_var_c', temp_diff)

avg_temp_last_10 = df_daily['temp_seco_c'].rolling(10, min_periods=1).mean().round(2)
avg_temp_var_last_10 = df_daily['temp_var_c'].rolling(10, min_periods=1).mean().round(2)
min_temp_last_10 = df_daily['temp_min_c'].rolling(10, min_periods=1).min()
max_temp_last_10 = df_daily['temp_max_c'].rolling(10, min_periods=1).max()
xtr_temp_var_last_10 = (max_temp_last_10 - min_temp_last_10).round(2)
avg_hum_last_10 = df_daily['umd_r_pct'].rolling(10, min_periods=1).mean().round(2)
avg_prec_last_10 = df_daily['precip_mm'].rolling(10, min_periods=1).mean().round(2)
avg_press_last_10 = df_daily['press_nvl_estac_mb'].rolling(10, min_periods=1).mean().round(2)

df_daily.insert(temp_min_idx + 2, 'temp_med_10d', avg_temp_last_10)
df_daily.insert(temp_min_idx + 3, 'temp_min_10d', min_temp_last_10)
df_daily.insert(temp_min_idx + 4, 'temp_max_10d', max_temp_last_10)
df_daily.insert(temp_min_idx + 5, 'temp_var_ext_10d', xtr_temp_var_last_10)
df_daily.insert(temp_min_idx + 6, 'temp_var_med_10d', avg_temp_var_last_10)
df_daily.insert(df_daily.columns.get_loc('umd_r_pct') + 1, 'umd_med_10d', avg_hum_last_10)
df_daily.insert(df_daily.columns.get_loc('precip_max_mm') + 1, 'precip_med_10d', avg_prec_last_10)
df_daily.insert(df_daily.columns.get_loc('press_min_mb') + 1, 'press_med_10d', avg_press_last_10)

# Restore old naming scheme if requested
if KEEP_NAMES:
    renames = {**OLD_COL_NAMES, # dict unpacking with **
        'temp_var_c': 'VARIAÇÃO DE TEMPERATURA, DIÁRIA (°C)',
        'temp_med_10d': 'TEMPERATURA MÉDIA DO AR, ÚLTIMOS 10 DIAS (°C)',
        'temp_min_10d': 'TEMPERATURA MÍNIMA DO AR, ÚLTIMOS 10 DIAS (°C)',
        'temp_max_10d': 'TEMPERATURA MÁXIMA DO AR, ÚLTIMOS 10 DIAS (°C)',
        'temp_var_ext_10d': 'VARIAÇÃO ENTRE TEMPERATURA MÁX E MÍN NOS ÚLTIMOS 10 DIAS (°C)',
        'temp_var_med_10d': 'VARIAÇÃO MÉDIA DE TEMPERATURA, ÚLTIMOS 10 DIAS (°C)',
        'umd_med_10d': 'UMIDADE RELATIVA MÉDIA, ÚLTIMOS 10 DIAS (%)',
        'precip_med_10d': 'PRECIPITAÇÃO MÉDIA, ÚLTIMOS 10 DIAS (mm)',
        'press_med_10d': 'PRESSÃO MÉDIA, ÚLTIMOS 10 DIAS (mB)'
    }
    df_daily.rename(mapper=renames, axis='columns', inplace=True)

# Save to new CSV (index as 'Data')
df_daily.to_csv(OUT_FILE)

print(f'Generated {OUT_FILE} with daily weather data.')