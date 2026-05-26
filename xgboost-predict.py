import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns
import os, sys, re, optuna

# ==================== PARAMETER TESTING UTILITIES ====================

def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 70, 1500),
        'learning_rate': trial.suggest_float('learning_rate', 0.005, 0.1),
        'max_depth': trial.suggest_int('max_depth', 6, 10),
        'subsample': trial.suggest_float('subsample', 0.7, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.9, 1.0),
        'min_child_weight': trial.suggest_int('min_child_weight', 1, 10),
    }
    
    model = xgb.XGBRegressor(objective='reg:squarederror', **params, random_state=42)
    score = cross_val_score(model, X_train, y_train, cv=TimeSeriesSplit(5), scoring='neg_root_mean_squared_error')
    return -score.mean()

def test_params():
    study = optuna.create_study(direction='minimize')
    study.optimize(objective, n_trials=100)
    print("Best params:", study.best_params)
    return f'Best value: {study.best_value}, Params: {study.best_params}'

# ==================== PARSE INPUT ====================

if (len(sys.argv) < 3):
    print(f'Usage: python {sys.argv[0]} SUS_CSV_PATH WTR_CSV_PATH\n' + 
           '    SUS_CSV_PATH: Path to SUS .csv data file\n' +
           '    WTR_CSV_PATH: Path to weather .csv data file\n\n' +
          
           '    Options:\n' +
           '    -t, --test: Test different XGBoost parameters\n'+
           '    --rf <file>, --resultsfile <file>: Append best result to <file>\n\n' +

           'Not enough arguments, exiting')
    sys.exit(0)

SUS_CSV = sys.argv[1]
WTR_CSV = sys.argv[2]

# File checking
for path in [SUS_CSV, WTR_CSV]:
    if (not os.path.exists(path)):
        print(f'File not found: \'{path}\', exiting')
        sys.exit(0)

weather_df = pd.read_csv(WTR_CSV)
hospital_df = pd.read_csv(SUS_CSV)

short_opts = ''
for i, arg in enumerate(sys.argv[1:], 1):
    if re.match(r'-[a-z]+', arg):
        short_opts = sys.argv[i][1:]
SHORT_OPTS = short_opts

# ==================== LOAD AND PREPARE DATA ====================
# Parse dates
weather_df['data'] = pd.to_datetime(weather_df['data'])
hospital_df['date'] = pd.to_datetime(hospital_df['DT_INTER'], format='%Y%m%d')

print(f"Dados do clima: {weather_df.shape[0]} dias ({weather_df['data'].min()} a {weather_df['data'].max()})")
print(f"Casos respiratórios: {hospital_df.shape[0]} registros")

# Aggregate daily respiratory disease occurrences (hospital admissions)
daily_cases = hospital_df.groupby('date').size().reset_index(name='cases')

# Merge weather + daily cases (left join so we keep ALL weather days, fill 0 cases when no admissions)
merged_df = pd.merge(weather_df, daily_cases, left_on='data', right_on='date', how='left')
merged_df['cases'] = merged_df['cases'].fillna(0).astype(int)
merged_df = merged_df.drop(columns=['date'])  # remove duplicate column

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
    'press_med_10d':        'Pressão média, últ. 10d',
    'UTI_MES_TO':           'Dias de UTI no mês',
    'QT_DIARIAS':           'Quantidade de diárias',
    'VAL_TOT':              'Valor total do tratamento',
    'VAL_UTI':              'Valor de UTI',
    'DIAS_PERM':            'Dias no hospital',
    'MORTE':                'Morte (sim/não)',
    'COMPLEX':              'Complexidade da doença',
    'res_LATITUDE':         'Latitude do paciente',
    'res_LONGITUDE':        'Longitude do paciente',
    'res_ALTITUDE':         'Altitude do paciente'
}

merged_df.rename(mapper=renames, axis='columns', inplace=True)

print(f"Conjunto de dados final: {merged_df.shape[0]} dias")
print(f"Dias com 0 casos respiratórios: {(merged_df['cases'] == 0).sum()}")
print(f"Média de casos diária: {merged_df['cases'].mean():.2f}")
print(f"Desvio padrão - n° de casos: {merged_df['cases'].std():.2f}")

# ==================== FEATURE SELECTION ====================
# All weather columns except the date and target
exclude_cols = ['data', 'cases']
feature_cols = [col for col in merged_df.columns if col not in exclude_cols]

X = merged_df[feature_cols]
y = merged_df['cases']

print(f"Features usadas ({len(feature_cols)}): {feature_cols}")

# Lag features (for better time-series performance)
merged_df = merged_df.sort_values('data')
for lag in [1, 3, 7]:
    merged_df[f'n_internacoes_lag_{lag}'] = merged_df['cases'].shift(lag)
    merged_df[f'temp_lag_{lag}'] = merged_df[renames['temp_seco_c']].shift(lag)

# Drop rows with NaN from lags (first few days)
merged_df = merged_df.dropna().reset_index(drop=True)

# Update X and y after lags
feature_cols = [col for col in merged_df.columns if col not in exclude_cols]
X = merged_df[feature_cols]
y = merged_df['cases']

# ==================== TRAIN/TEST SPLIT (TIME-SERIES AWARE) ====================
# Sort by date (already done) and use chronological split (80% train, 20% test)
split_idx = int(len(merged_df) * 0.8)
X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

print(f"Treino: {len(X_train)} dias | Teste: {len(X_test)} dias")

# ==================== OPTIONAL: TEST XGBOOST PARAMETERS AND EXIT ====================

if 't' in SHORT_OPTS or '--test' in sys.argv:
    result = test_params()

    def getargfilename(arg):
        if arg in sys.argv:
            return sys.argv[sys.argv.index(arg) + 1]
        else:
            return None
        
    for arg in ('--rf', '--resultsfile'):
        if getargfilename(arg):
            resultsfile = getargfilename(arg)

    if resultsfile:
        with open(resultsfile, 'a') as f:
            f.write(f'{result}\n')
    
    sys.exit(0)

# ==================== XGBoost REGRESSOR ====================
# We use regression because the target is count of daily occurrences (can be 0, 1, 5+)
model = xgb.XGBRegressor(
    objective='reg:squarederror',   # standard regression
    n_estimators=621, # 200
    learning_rate=0.007146870451096577,
    max_depth=6,
    subsample=0.8886419356213825,
    colsample_bytree=1,
    random_state=42,
    min_child_weight = 7,
    eval_metric='rmse'
)

# Fit
model.fit(X_train, y_train, 
          eval_set=[(X_train, y_train), (X_test, y_test)],
          verbose=False)

# Predict
y_pred = model.predict(X_test)

# ==================== EVALUATION ====================
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n=== PERFORMANCE DO MODELO (Conjunto de teste) ===")
print(f"RMSE: {rmse:.2f} casos/dia")
print(f"MAE:  {mae:.2f} casos/dia")
print(f"R²:   {r2:.3f} (mais perto de 1 = melhor)")

# Feature importance (top 15)
importances = pd.DataFrame({
    'fator': feature_cols,
    'importância': model.feature_importances_
}).sort_values('importância', ascending=False)

print("\nTop 15 fatores mais importantes:")
print(importances.head(15))

# ==================== VISUALIZATIONS ====================
# Actual vs Predicted
plt.figure(figsize=(12, 6))
plt.plot(merged_df['data'].iloc[split_idx:], y_test, label='Casos Reais', alpha=0.8)
plt.plot(merged_df['data'].iloc[split_idx:], y_pred, label='Casos Previstos', alpha=0.8)
plt.title('XGBoost - Ocorrências diárias de doenças respiratórias: Real vs Previsto')
plt.xlabel('Data')
plt.ylabel('Número de casos')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
save_path = 'generated-graphs/xgboost-act-vs-pred'
plt.savefig(save_path, dpi=160, bbox_inches='tight')
# plt.show()

# Feature importance plot
plt.figure(figsize=(10, 8))
sns.barplot(x='importância', y='fator', data=importances.head(15))
plt.title('Top 15 fatores mais influentes nas previsões')
plt.xlabel('Importância')
plt.tight_layout()
save_path = 'generated-graphs/xgboost-top-feat'
plt.savefig(save_path, dpi=140, bbox_inches='tight')
# plt.show()

# ==================== CROSS-VALIDATION WITH TimeSeriesSplit ====================
print("\nFazendo validação cruzada com TimeSeriesSplit...")
tscv = TimeSeriesSplit(n_splits=5)
cv_scores = cross_val_score(model, X, y, cv=tscv, scoring='neg_root_mean_squared_error')
print(f"CV RMSE: {-cv_scores.mean():.2f} ± {cv_scores.std():.2f}")

# ==================== SAVE MODEL FOR FUTURE USE ====================
model_save_path = 'xgboost_respiratory_weather_model.json'
model.save_model(model_save_path)
print(f"\nModelo salvo como '{model_save_path}'")
print(f"Para carregar depois: model = xgb.XGBRegressor(); model.load_model('{model_save_path}')")

