import pandas as pd
import sys, os, re

if (len(sys.argv) < 2):
    print(f'Usage: python {sys.argv[0]} IN_FILE [OUT_FILE] [OPTIONS]\n' +
          '    IN_FILE: Path to .csv data file\n' +
          '    OUT_FILE: File to save treated data in\n\n' +

          '    Options:\n' +
          '    -k, --keep-names: Keep original column names\n\n' +

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

# Read the CSV with semicolon separator
df = pd.read_csv(IN_FILE, sep=';')

if '--keep-names' not in sys.argv and '-k' not in SHORT_OPTS:
    df.columns = NEW_COLS # Rename columns
DATE_COL = df.columns[0]

# Replace commas with dots + convert to numeric 
for col in df.columns:
    if col not in ('Data', 'data', 'Hora UTC', 'hora_utc'):
        df[col] = (df[col].astype(str)
                   .str.replace(',', '.')
                   .replace({'': float('nan'), 'nan': float('nan')}))
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert 'Data' to datetime for grouping
df[DATE_COL] = pd.to_datetime(df[DATE_COL], format='%Y/%m/%d', errors='coerce')

# Drop rows with invalid dates (if any)
df = df.dropna(subset=[DATE_COL])

# Group by 'Data' and compute mean for numeric columns only
df_daily_avg = df.groupby(DATE_COL).mean(numeric_only=True).round(2)

# Save to new CSV (index as 'Data')
df_daily_avg.to_csv(OUT_FILE)

print(f'Generated {OUT_FILE} with daily averages.')