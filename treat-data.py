import pandas as pd
import glob
import os
import sys
import re

from timeit import default_timer as timer

# Eliminate checks in the loop to make this as fast as possible
def make_dfs_list(file_paths, dtypes, cols_to_drop):
    dfs = []
    for file in file_paths:
        print(file)
        df = pd.read_csv(file, dtype=dtypes)
        df = df.drop(columns=cols_to_drop, errors='ignore')
        dfs.append(df)
    return dfs

def make_dfs_list_q(file_paths, dtypes, cols_to_drop):
    dfs = []
    for file in file_paths:
        df = pd.read_csv(file, dtype=dtypes)
        df = df.drop(columns=cols_to_drop, errors='ignore')
        dfs.append(df)
    return dfs

def make_dfs_list_c(file_paths, dtypes):
    dfs = []
    for file in file_paths:
        print(file)
        df = pd.read_csv(file, dtype=dtypes)
        dfs.append(df)
    return dfs

def make_dfs_list_qc(file_paths, dtypes):
    dfs = []
    for file in file_paths:
        df = pd.read_csv(file, dtype=dtypes)
        dfs.append(df)
    return dfs


if (len(sys.argv) < 3):
    print(f'Usage: python {sys.argv[0]} CSV_DIRECTORY_PATH OUTPUT_FILE [OPTIONS]\n' +
          '    CSV_DIRECTORY_PATH: Path to directory contining all .csv files to be included\n' +
          '    OUTPUT_FILE: File to save treated data in\n\n' +

          '    Options:\n' +
          '    -c, --combine-parts: Don\'t clean any data, just combine files that match \'*.part*.csv\' in CSV_DIRECTORY_PATH\n' +
          '    -q, --quiet: Disable non-essential output\n' +
          '    --strict=[1-2]: Strictness level, higher means more columns are removed (default: 1)\n\n' +

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

# parse short options and strictness
short_opts = ''
strictness = 1
for i, arg in enumerate(sys.argv[1:], 1):
    if re.match(r'-[a-z]+', arg):
        short_opts = sys.argv[i][1:]
    if re.match(r'--strict=[0-9]', arg):
        strictness = int(sys.argv[i][9])
SHORT_OPTS = short_opts
STRICTNESS = strictness

QUIET_RUN = ('--quiet' in sys.argv or 'q' in SHORT_OPTS)
COMBINE_PARTS = ('--combine-parts' in sys.argv or 'c' in SHORT_OPTS)

START_TIME = timer()

# Find all matching CSV files in the path/directory
if COMBINE_PARTS:
    file_paths = glob.glob(f'{CSV_DIR_PATH}/*.part*.csv')
else:
    file_paths = glob.glob(f'{CSV_DIR_PATH}/ETLSIH.ST_DF*.csv')
    file_paths += glob.glob(f'{CSV_DIR_PATH}/ETLSIH.ST_GO*.csv')
    file_paths += glob.glob(f'{CSV_DIR_PATH}/ETLSIH.ST_MT*.csv')
    file_paths += glob.glob(f'{CSV_DIR_PATH}/ETLSIH.ST_MS*.csv')

    # Define which columns to remove from dataset
    cols_to_drop = ['CGC_HOSP', 'N_AIH', 'IDENT', 'CEP', 'UTI_MES_IN', 'UTI_MES_AN', 'UTI_MES_AL', 'UTI_INT_IN', 'UTI_INT_AN', 'UTI_INT_AL', 'UTI_INT_TO', 
                    'DIAR_ACOM', 'PROC_SOLIC', 'PROC_REA', 'VAL_SH', 'VAL_SP', 'VAL_SADT', 'VAL_RN', 'VAL_ACOMP', 'VAL_ORTP', 'VAL_SANGUE', 'VAL_SADTSR', 'VAL_TRANSP', 
                    'VAL_OBSANG', 'VAL_PED1AC', 'US_TOT', 'NATUREZA', 'NAT_JUR', 'GESTAO', 'RUBRICA', 'IND_VDRL', 'NUM_PROC', 'TOT_PT_SP', 'CPF_AUT', 'HOMONIMO', 
                    'NUM_FILHOS', 'CID_NOTIF', 'CONTRACEP1', 'CONTRACEP2', 'GESTRISCO', 'INSC_PN', 'SEQ_AIH5', 'CBOR', 'CNAER', 'VINCPREV', 'GESTOR_COD', 'GESTOR_TP', 
                    'GESTOR_CPF', 'GESTOR_DT', 'CNES', 'CNPJ_MANT', 'INFEHOSP', 'FINANC', 'FAEC_TP', 'REGCT', 'RACA_COR', 'ETNIA', 'SEQUENCIA', 'REMESSA', 'AUD_JUST', 
                    'SIS_JUST', 'VAL_SH_FED', 'VAL_SP_FED', 'VAL_SH_GES', 'VAL_SP_GES', 'res_AMAZONIA', 'res_FRONTEIRA', 'res_CAPITAL', 'res_MSAUDCOD', 'res_RSAUDCOD', 'res_CSAUDCOD', 
                    'res_AREA', 'res_codigo_adotado', 'int_AMAZONIA', 'int_FRONTEIRA', 'int_CAPITAL', 'int_MSAUDCOD', 'int_RSAUDCOD', 'int_CSAUDCOD', 'int_AREA', 
                    'int_codigo_adotado', 'def_cir_res', 'def_cir_int', 'def_aglr_res', 'def_aglr_int', 'def_rsaud_res', 'def_rsaud_int', 'def_csaud_res', 'def_csaud_int', 
                    'def_esferajur', 'def_etnia', 'def_cbo', 'def_cnae', 'def_identific', 'def_n_aih', 'def_ident', 'def_regime', 'def_nat_jur', 'def_gestao', 'def_ind_vdrl', 
                    'def_homonimo', 'def_num_filhos', 'def_contracep1', 'def_contracep2', 'def_gestrisco', 'def_seq_aih5', 'def_vincprev', 'def_infehosp', 'def_financ', 
                    'def_faec_tp', 'def_regct', 'def_raca_cor', 'codidade', 'dia_semana_internacao', 'dia_semana_saida', 'ano_internacao', 'ano_saida', 'mes_internacao',
                    'mes_saida', 'def_idade_bas', 'def_idade_pub', 'def_idade_18', 'INSTRU', 'def_instru']
    
    if STRICTNESS >= 2:
        cols_to_drop += ['UF_ZI', 'ESPEC', 'MUNIC_RES', 'MUNIC_MOV', 'res_MUNCOD', 'res_CODIGO_UF', 'int_MUNCOD', 'int_CODIGO_UF', 'res_coordenadas', 'int_coordenadas']

    if STRICTNESS >= 3:
        cols_to_drop += []
    
dtypes = 'object'

# Eliminate checks in the loop to make this part as fast as possible
if not COMBINE_PARTS:
    if not QUIET_RUN:
        dfs = make_dfs_list(file_paths, dtypes, cols_to_drop)
    else:
        dfs = make_dfs_list_q(file_paths, dtypes, cols_to_drop)
elif not QUIET_RUN:
    dfs = make_dfs_list_c(file_paths, dtypes)
else:
    dfs = make_dfs_list_qc(file_paths, dtypes)

# Concatenate all DataFrames into one
combined_df = pd.concat(dfs, ignore_index=True)

# Filter rows where 'def_diag_princ_cap' matches 'X. Doenças do aparelho respiratório
filtered_df = combined_df if COMBINE_PARTS else combined_df[combined_df['def_diag_princ_cap'] == 'X. Doenças do aparelho respiratório']

# Save the filtered DataFrame to CSV of specified filename
filtered_df.to_csv(OUT_FILE, index=False)

END_TIME = timer()
print(f'Done! Execution time: {END_TIME - START_TIME}s')

# Display the first few rows of the filtered DataFrame
if not QUIET_RUN:
    print(filtered_df.head())
