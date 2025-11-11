DROP TABLE IF EXISTS dnc_resp_ctr_oeste;

CREATE TABLE dnc_resp_ctr_oeste (
    "ANO_CMPT" smallint,
    "MES_CMPT" smallint,
    "NASC" int,
    "SEXO" smallint,
    "def_sexo" text,
    "UTI_MES_TO" smallint,
    "def_uti_mes_to" text,
    "MARCA_UTI" text,
    "def_marca_uti" text,
    "QT_DIARIAS" smallint,
    "VAL_TOT" real,
    "VAL_UTI" real,
    "DT_INTER" int,
    "DT_SAIDA" int,
    "DIAG_PRINC" text,
    "DIAG_SECUN" text,
    "COBRANCA" smallint,
    "def_cobranca" text,
    "DIAS_PERM" smallint,
    "def_dias_perm" text,
    "MORTE" smallint,
    "def_morte" text,
    "NACIONAL" text,
    "CAR_INT" text,
    "def_car_int" text,
    "CID_ASSO" text,
    "CID_MORTE" text,
    "COMPLEX" text,
    "def_complex" text,
    "VAL_UCI" float8,
    "MARCA_UCI" text,
    "def_marca_uci" text,
    "DIAGSEC1" text,
    "DIAGSEC2" text,
    "DIAGSEC3" text,
    "DIAGSEC4" text,
    "DIAGSEC5" text,
    "DIAGSEC6" text,
    "DIAGSEC7" text,
    "DIAGSEC8" text,
    "DIAGSEC9" text,
    "TPDISEC1" int,
    "def_tpdisec1" text,
    "TPDISEC2" int,
    "def_tpdisec2" text,
    "TPDISEC3" int,
    "def_tpdisec3" text,
    "TPDISEC4" int,
    "def_tpdisec4" text,
    "TPDISEC5" int,
    "def_tpdisec5" text,
    "TPDISEC6" int,
    "def_tpdisec6" text,
    "TPDISEC7" int,
    "def_tpdisec7" text,
    "TPDISEC8" int,
    "def_tpdisec8" text,
    "TPDISEC9" int,
    "def_tpdisec9" text,
    "res_MUNNOME" text,
    "res_MUNNOMEX" text,
    "res_LATITUDE" float8,
    "res_LONGITUDE" float8,
    "res_ALTITUDE" int,
    "res_SIGLA_UF" text,
    "res_NOME_UF" text,
    "res_REGIAO" text,
    "int_MUNNOME" text,
    "int_MUNNOMEX" text,
    "int_LATITUDE" float8,
    "int_LONGITUDE" float8,
    "int_ALTITUDE" int,
    "int_SIGLA_UF" text,
    "int_NOME_UF" text,
    "int_REGIAO" text,
    "def_reg_metr_int" text,
    "def_reg_metr_res" text,
    "def_meso_int" text,
    "def_meso_res" text,
    "def_micro_res" text,
    "def_micro_int" text,
    "def_nacionalidade" text,
    "def_leitos" text,
    "def_procedimento_realizado" text,
    "def_procedimento_solicitado" text,
    "IDADE" smallint,
    "COD_IDADE" smallint,
    "def_cod_idade" text,
    "def_idade_anos" text,
    "def_idade_meses" text,
    "def_idade_dias" text,
    "def_diag_princ_cap" text,
    "def_diag_princ_grupo" text,
    "def_diag_princ_cat" text,
    "def_diag_princ_subcat" text,
    "def_diag_secun_cap" text,
    "def_diag_secun_grupo" text,
    "def_diag_secun_cat" text,
    "def_diag_secun_subcat" text,
    "dt_inter" date,
    "dt_saida" date,
);
COMMENT ON COLUMN dnc_resp_ctr_oeste."ANO_CMPT" IS 'Ano de processamento da AIH';
COMMENT ON COLUMN dnc_resp_ctr_oeste."MES_CMPT" IS 'Mês de processamento da AIH';
COMMENT ON COLUMN dnc_resp_ctr_oeste."NASC" IS 'Data de nascimento do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."SEXO" IS 'Sexo do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_sexo" IS 'Definição do sexo do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."UTI_MES_TO" IS 'Quantidade de dias de UTI no mês';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_uti_mes_to" IS 'Definição do número de dias de UTI no mês';
COMMENT ON COLUMN dnc_resp_ctr_oeste."MARCA_UTI" IS 'Indica qual o tipo de UTI utilizada pelo paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_marca_uti" IS 'Definição do tipo de UTI utilizada pelo paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."QT_DIARIAS" IS 'Quantidade de diárias';
COMMENT ON COLUMN dnc_resp_ctr_oeste."VAL_TOT" IS 'Valor total da AIH';
COMMENT ON COLUMN dnc_resp_ctr_oeste."VAL_UTI" IS 'Valor de UTI';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DT_INTER" IS 'Data de internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DT_SAIDA" IS 'Data de saída';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DIAG_PRINC" IS 'Código do diagnóstico principal (CID10)';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DIAG_SECUN" IS 'Código do diagnóstico secundário (CID10)';
COMMENT ON COLUMN dnc_resp_ctr_oeste."COBRANCA" IS 'Motivo de saída/permanência';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_cobranca" IS 'Definição do motivo de saída/permanência';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DIAS_PERM" IS 'Dias de permanência';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_dias_perm" IS 'Definição de dias de permanência';
COMMENT ON COLUMN dnc_resp_ctr_oeste."MORTE" IS 'Indica óbito';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_morte" IS 'Definição de óbito';
COMMENT ON COLUMN dnc_resp_ctr_oeste."NACIONAL" IS 'Código da nacionalidade do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."CAR_INT" IS 'Caráter da internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_car_int" IS 'Definição do caráter da internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."CID_ASSO" IS 'CID-10 condições secundárias, comorbidades ou complicações, podem ter contribuído p/ a internação ou agravado o quadro principal';
COMMENT ON COLUMN dnc_resp_ctr_oeste."CID_MORTE" IS 'CID-10 da causa que iniciou a sequência de eventos que levou ao óbito';
COMMENT ON COLUMN dnc_resp_ctr_oeste."COMPLEX" IS 'Complexidade';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_complex" IS 'Definição de complexidade';
COMMENT ON COLUMN dnc_resp_ctr_oeste."VAL_UCI" IS 'Valor de UCI';
COMMENT ON COLUMN dnc_resp_ctr_oeste."MARCA_UCI" IS 'Tipo de UCI utilizada pelo paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_marca_uci" IS 'Definição do tipo de UCI utilizada pelo paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DIAGSEC1" IS 'Diagnóstico secundário 1';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DIAGSEC2" IS 'Diagnóstico secundário 2';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DIAGSEC3" IS 'Diagnóstico secundário 3';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DIAGSEC4" IS 'Diagnóstico secundário 4';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DIAGSEC5" IS 'Diagnóstico secundário 5';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DIAGSEC6" IS 'Diagnóstico secundário 6';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DIAGSEC7" IS 'Diagnóstico secundário 7';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DIAGSEC8" IS 'Diagnóstico secundário 8';
COMMENT ON COLUMN dnc_resp_ctr_oeste."DIAGSEC9" IS 'Diagnóstico secundário 9';
COMMENT ON COLUMN dnc_resp_ctr_oeste."TPDISEC1" IS 'Tipo de diagnóstico secundário 1';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_tpdisec1" IS 'Tipo de diagnóstico secundário 1';
COMMENT ON COLUMN dnc_resp_ctr_oeste."TPDISEC2" IS 'Tipo de diagnóstico secundário 2';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_tpdisec2" IS 'Tipo de diagnóstico secundário 2';
COMMENT ON COLUMN dnc_resp_ctr_oeste."TPDISEC3" IS 'Tipo de diagnóstico secundário 3';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_tpdisec3" IS 'Tipo de diagnóstico secundário 3';
COMMENT ON COLUMN dnc_resp_ctr_oeste."TPDISEC4" IS 'Tipo de diagnóstico secundário 4';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_tpdisec4" IS 'Tipo de diagnóstico secundário 4';
COMMENT ON COLUMN dnc_resp_ctr_oeste."TPDISEC5" IS 'Tipo de diagnóstico secundário 5';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_tpdisec5" IS 'Tipo de diagnóstico secundário 5';
COMMENT ON COLUMN dnc_resp_ctr_oeste."TPDISEC6" IS 'Tipo de diagnóstico secundário 6';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_tpdisec6" IS 'Tipo de diagnóstico secundário 6';
COMMENT ON COLUMN dnc_resp_ctr_oeste."TPDISEC7" IS 'Tipo de diagnóstico secundário 7';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_tpdisec7" IS 'Tipo de diagnóstico secundário 7';
COMMENT ON COLUMN dnc_resp_ctr_oeste."TPDISEC8" IS 'Tipo de diagnóstico secundário 8';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_tpdisec8" IS 'Tipo de diagnóstico secundário 8';
COMMENT ON COLUMN dnc_resp_ctr_oeste."TPDISEC9" IS 'Tipo de diagnóstico secundário 9';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_tpdisec9" IS 'Tipo de diagnóstico secundário 9';
COMMENT ON COLUMN dnc_resp_ctr_oeste."res_MUNNOME" IS 'Nome (acentuado, maiúsculas e minúsculas) do Município (padrão DOS, página de código 850) de residência do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."res_MUNNOMEX" IS 'Nome (sem acentos, em maiúsculas) do Município de residência do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."res_LATITUDE" IS 'Latitude da sede do Município de residência do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."res_LONGITUDE" IS 'Longitude da sede do Município de residência do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."res_ALTITUDE" IS 'Área, em quilômetros quadrados, do Município de residência do paciente, segundo a Resolução 05, de 10/12/2002, do IBGE';
COMMENT ON COLUMN dnc_resp_ctr_oeste."res_SIGLA_UF" IS 'Sigla da unidade da federação de residência do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."res_NOME_UF" IS 'Nome da unidade da federação de residência do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."res_REGIAO" IS 'Nome da Região da unidade da federação de residência do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."int_MUNNOME" IS 'Nome (acentuado, maiúsculas e minúsculas) do Município (padrão DOS, página de código 850) do estabelecimento de internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."int_MUNNOMEX" IS 'Nome (sem acentos, em maiúsculas) do Município do estabelecimento de internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."int_LATITUDE" IS 'Latitude da sede do Município do estabelecimento de internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."int_LONGITUDE" IS 'Longitude da sede do Município do estabelecimento de internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."int_ALTITUDE" IS 'Altitude, em metros, da sede do Município do estabelecimento de internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."int_SIGLA_UF" IS 'Sigla da unidade da federação do estabelecimeto de internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."int_NOME_UF" IS 'Código IBGE da Unidade da Federação do estabelecimento de internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."int_REGIAO" IS 'Nome da Região da unidade da federação do estabelecimento de internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_reg_metr_int" IS 'Região metropolitana do estabelecimento de internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_reg_metr_res" IS 'Região metropolitana de residência do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_meso_int" IS 'Mesorregião do estabelecimento de internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_meso_res" IS 'Mesorregião de residência do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_micro_res" IS 'Microrregião de residência do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_micro_int" IS 'Microrregião de internação do paciente';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_nacionalidade" IS 'Definição de nacionalidade';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_leitos" IS 'Definição de leitos';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_procedimento_realizado" IS 'Definição do procedimento realizado';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_procedimento_solicitado" IS 'Definição do procedimento solicitado';
COMMENT ON COLUMN dnc_resp_ctr_oeste."IDADE" IS 'Idade';
COMMENT ON COLUMN dnc_resp_ctr_oeste."COD_IDADE" IS 'Unidade de medida da idade';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_cod_idade" IS 'Definição da unidade de medida da idade';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_idade_anos" IS 'Idade em anos';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_idade_meses" IS 'Idade em meses';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_idade_dias" IS 'Idade em dias';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_diag_princ_cap" IS 'Definição do capítulo do diagnóstico principal';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_diag_princ_grupo" IS 'Definição do grupo do diagnóstico principal';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_diag_princ_cat" IS 'Definição da categoria do diagnóstico principal';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_diag_princ_subcat" IS 'Definição da sub categoria do diagnóstico principal';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_diag_secun_cap" IS 'Definição do capítulo do primeiro diagnóstico secundário';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_diag_secun_grupo" IS 'Definição do grupo do primeiro diagnóstico secundário';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_diag_secun_cat" IS 'Definição da categoria do primeiro diagnóstico secundário';
COMMENT ON COLUMN dnc_resp_ctr_oeste."def_diag_secun_subcat" IS 'Definição da sub categoria do primeiro diagnóstico secundário';
COMMENT ON COLUMN dnc_resp_ctr_oeste."dt_inter" IS 'Data de internação';
COMMENT ON COLUMN dnc_resp_ctr_oeste."dt_saida" IS 'Data de saída';
