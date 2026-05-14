DROP TABLE IF EXISTS etlsih_st_df;

CREATE TABLE etlsih_st_df (
    "UF_ZI" int,
    "ANO_CMPT" smallint,
    "MES_CMPT" smallint,
    "ESPEC" text,
--     "CGC_HOSP" text,
--     "N_AIH" int,
--     "def_identific" text,
--     "def_n_aih" text,
--     "IDENT" int,
--     "def_ident" text,
--     "CEP" text,
    "MUNIC_RES" int,
    "NASC" int,
    "SEXO" smallint,
    "def_sexo" text,
--     "UTI_MES_IN" int,
--     "UTI_MES_AN" int,
--     "UTI_MES_AL" int,
    "UTI_MES_TO" smallint,
    "def_uti_mes_to" text,
    "MARCA_UTI" text,
    "def_marca_uti" text,
--     "UTI_INT_IN" int,
--     "UTI_INT_AN" int,
--     "UTI_INT_AL" int,
--     "UTI_INT_TO" int,
--     "DIAR_ACOM" int,
    "QT_DIARIAS" smallint,
--     "PROC_SOLIC" text,
--     "PROC_REA" text,
--     "VAL_SH" float8,
--     "VAL_SP" float8,
--     "VAL_SADT" float8,
--     "VAL_RN" float8,
--     "VAL_ACOMP" float8,
--     "VAL_ORTP" float8,
--     "VAL_SANGUE" float8,
--     "VAL_SADTSR" float8,
--     "VAL_TRANSP" float8,
--     "VAL_OBSANG" float8,
--     "VAL_PED1AC" float8,
    "VAL_TOT" real,
    "VAL_UTI" real,
--     "US_TOT" float8,
    "DT_INTER" int,
    "DT_SAIDA" int,
    "DIAG_PRINC" text,
    "DIAG_SECUN" text,
    "COBRANCA" smallint,
    "def_cobranca" text,
--     "NATUREZA" int,
--     "def_regime" text,
--     "NAT_JUR" text,
--     "def_nat_jur" text,
--     "GESTAO" int,
--     "def_gestao" text,
--     "RUBRICA" int,
--     "IND_VDRL" int,
--     "def_ind_vdrl" text,
    "MUNIC_MOV" int,
    "DIAS_PERM" smallint,
    "def_dias_perm" text,
    "MORTE" smallint,
    "def_morte" text,
    "NACIONAL" text,
--     "NUM_PROC" text,
    "CAR_INT" text,
    "def_car_int" text,
--     "TOT_PT_SP" int,
--     "CPF_AUT" text,
--     "HOMONIMO" int,
--     "def_homonimo" text,
--     "NUM_FILHOS" int,
--     "def_num_filhos" text,
--     "INSTRU" int,
--     "def_instru" text,
--     "CID_NOTIF" text,
--     "CONTRACEP1" text,
--     "def_contracep1" text,
--     "CONTRACEP2" text,
--     "def_contracep2" text,
--     "GESTRISCO" int,
--     "def_gestrisco" text,
--     "INSC_PN" text,
--     "SEQ_AIH5" int,
--     "def_seq_aih5" text,
--     "CBOR" text,
--     "CNAER" int,
--     "VINCPREV" int,
--     "def_vincprev" text,
--     "GESTOR_COD" text,
--     "GESTOR_TP" int,
--     "GESTOR_CPF" text,
--     "GESTOR_DT" text,
--     "CNES" int,
--     "CNPJ_MANT" text,
--     "INFEHOSP" text,
--     "def_infehosp" text,
    "CID_ASSO" text,
    "CID_MORTE" text,
    "COMPLEX" text,
    "def_complex" text,
--     "FINANC" text,
--     "def_financ" text,
--     "FAEC_TP" text,
--     "def_faec_tp" text,
--     "REGCT" text,
--     "def_regct" text,
--     "RACA_COR" text,
--     "def_raca_cor" text,
--     "ETNIA" text,
--     "SEQUENCIA" int,
--     "REMESSA" text,
--     "AUD_JUST" text,
--     "SIS_JUST" text,
--     "VAL_SH_FED" float8,
--     "VAL_SP_FED" float8,
--     "VAL_SH_GES" float8,
--     "VAL_SP_GES" float8,
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
    "res_MUNCOD" int,
    "res_MUNNOME" text,
    "res_MUNNOMEX" text,
--     "res_AMAZONIA" text,
--     "res_FRONTEIRA" text,
--     "res_CAPITAL" text,
--     "res_MSAUDCOD" int,
--     "res_RSAUDCOD" int,
--     "res_CSAUDCOD" int,
    "res_LATITUDE" float8,
    "res_LONGITUDE" float8,
    "res_ALTITUDE" int,
--     "res_AREA" float8,
--     "res_codigo_adotado" int,
    "res_SIGLA_UF" text,
    "res_CODIGO_UF" int,
    "res_NOME_UF" text,
    "res_REGIAO" text,
    "int_MUNCOD" int,
    "int_MUNNOME" text,
    "int_MUNNOMEX" text,
--     "int_AMAZONIA" text,
--     "int_FRONTEIRA" text,
--     "int_CAPITAL" text,
--     "int_MSAUDCOD" int,
--     "int_RSAUDCOD" int,
--     "int_CSAUDCOD" int,
    "int_LATITUDE" float8,
    "int_LONGITUDE" float8,
    "int_ALTITUDE" int,
--     "int_AREA" float8,
--     "int_codigo_adotado" int,
    "int_SIGLA_UF" text,
    "int_CODIGO_UF" int,
    "int_NOME_UF" text,
    "int_REGIAO" text,
    "res_coordenadas" text,
    "int_coordenadas" text,
    "def_reg_metr_int" text,
    "def_reg_metr_res" text,
--     "def_cir_int" text,
--     "def_cir_res" text,
--     "def_aglr_int" text,
--     "def_aglr_res" text,
    "def_meso_int" text,
    "def_meso_res" text,
    "def_micro_res" text,
    "def_micro_int" text,
--     "def_rsaud_int" text,
--     "def_rsaud_res" text,
--     "def_csaud_int" text,
--     "def_csaud_res" text,
--     "def_esferajur" text,
--     "def_etnia" text,
    "def_nacionalidade" text,
--     "def_cbo" text,
--     "def_cnae" text,
    "def_leitos" text,
    "def_procedimento_realizado" text,
    "def_procedimento_solicitado" text,
    "IDADE" smallint,
    "COD_IDADE" smallint,
    "def_cod_idade" text,
    "def_idade_anos" text,
    "def_idade_meses" text,
    "def_idade_dias" text,
--     "def_idade_bas" text,
--     "def_idade_pub" text,
--     "def_idade_18" text,
    "def_diag_princ_cap" text,
    "def_diag_princ_grupo" text,
    "def_diag_princ_cat" text,
    "def_diag_princ_subcat" text,
    "def_diag_secun_cap" text,
    "def_diag_secun_grupo" text,
    "def_diag_secun_cat" text,
    "def_diag_secun_subcat" text,
    "dt_inter" date,
--     "ano_internacao" int,
--     "mes_internacao" int,
--     "dia_semana_internacao" text,
    "dt_saida" date,
--     "ano_saida" int,
--     "mes_saida" int,
--     "dia_semana_saida" text,
--     "codidade" int
);

COMMENT ON COLUMN etlsih_st_df."UF_ZI" IS 'Município gestor';
COMMENT ON COLUMN etlsih_st_df."ANO_CMPT" IS 'Ano de processamento da AIH';
COMMENT ON COLUMN etlsih_st_df."MES_CMPT" IS 'Mês de processamento da AIH';
COMMENT ON COLUMN etlsih_st_df."ESPEC" IS 'Especialidade do leito';
-- COMMENT ON COLUMN etlsih_st_df."CGC_HOSP" IS 'CNPJ do estabelecimento';
-- COMMENT ON COLUMN etlsih_st_df."N_AIH" IS 'Número da AIH';
-- COMMENT ON COLUMN etlsih_st_df."def_identific" IS 'Definição da identificação da AIH';
-- COMMENT ON COLUMN etlsih_st_df."def_n_aih" IS 'Definição do número da AIH';
-- COMMENT ON COLUMN etlsih_st_df."IDENT" IS 'Identificação do tipo da AIH';
-- COMMENT ON COLUMN etlsih_st_df."def_ident" IS 'Definição da identificação do tipo da AIH';
-- COMMENT ON COLUMN etlsih_st_df."CEP" IS 'CEP do paciente';
COMMENT ON COLUMN etlsih_st_df."MUNIC_RES" IS 'Município de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."NASC" IS 'Data de nascimento do paciente';
COMMENT ON COLUMN etlsih_st_df."SEXO" IS 'Sexo do paciente';
COMMENT ON COLUMN etlsih_st_df."def_sexo" IS 'Definição do sexo do paciente';
-- COMMENT ON COLUMN etlsih_st_df."UTI_MES_IN" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."UTI_MES_AN" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."UTI_MES_AL" IS 'Sem descrição';
COMMENT ON COLUMN etlsih_st_df."UTI_MES_TO" IS 'Quantidade de dias de UTI no mês';
COMMENT ON COLUMN etlsih_st_df."def_uti_mes_to" IS 'Definição do número de dias de UTI no mês';
COMMENT ON COLUMN etlsih_st_df."MARCA_UTI" IS 'Indica qual o tipo de UTI utilizada pelo paciente';
COMMENT ON COLUMN etlsih_st_df."def_marca_uti" IS 'Definição do tipo de UTI utilizada pelo paciente';
-- COMMENT ON COLUMN etlsih_st_df."UTI_INT_IN" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."UTI_INT_AN" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."UTI_INT_AL" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."UTI_INT_TO" IS 'Quantidade de diárias em unidade intermediária';
-- COMMENT ON COLUMN etlsih_st_df."DIAR_ACOM" IS 'Quantidade de diárias de acompanhante';
COMMENT ON COLUMN etlsih_st_df."QT_DIARIAS" IS 'Quantidade de diárias';
-- COMMENT ON COLUMN etlsih_st_df."PROC_SOLIC" IS 'Procedimento solicitado';
-- COMMENT ON COLUMN etlsih_st_df."PROC_REA" IS 'Procedimento realizado';
-- COMMENT ON COLUMN etlsih_st_df."VAL_SH" IS 'Valor de serviços hospitalares';
-- COMMENT ON COLUMN etlsih_st_df."VAL_SP" IS 'Valor de serviços profissionais';
-- COMMENT ON COLUMN etlsih_st_df."VAL_SADT" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."VAL_RN" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."VAL_ACOMP" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."VAL_ORTP" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."VAL_SANGUE" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."VAL_SADTSR" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."VAL_TRANSP" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."VAL_OBSANG" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."VAL_PED1AC" IS 'Sem descrição';
COMMENT ON COLUMN etlsih_st_df."VAL_TOT" IS 'Valor total da AIH';
COMMENT ON COLUMN etlsih_st_df."VAL_UTI" IS 'Valor de UTI';
-- COMMENT ON COLUMN etlsih_st_df."US_TOT" IS 'Valor total, em dólar';
COMMENT ON COLUMN etlsih_st_df."DT_INTER" IS 'Data de internação';
COMMENT ON COLUMN etlsih_st_df."DT_SAIDA" IS 'Data de saída';
COMMENT ON COLUMN etlsih_st_df."DIAG_PRINC" IS 'Código do diagnóstico principal (CID10)';
COMMENT ON COLUMN etlsih_st_df."DIAG_SECUN" IS 'Código do diagnóstico secundário (CID10)';
COMMENT ON COLUMN etlsih_st_df."COBRANCA" IS 'Motivo de saída/permanência';
COMMENT ON COLUMN etlsih_st_df."def_cobranca" IS 'Definição do motivo de saída/permanência';
-- COMMENT ON COLUMN etlsih_st_df."NATUREZA" IS 'Natureza jurídica do hospital';
-- COMMENT ON COLUMN etlsih_st_df."def_regime" IS 'Definição da natureza (regime)';
-- COMMENT ON COLUMN etlsih_st_df."NAT_JUR" IS 'Natureza jurídica do estabelecimento, conforme a Comissão Nacional de Classificação (CONCLA)';
-- COMMENT ON COLUMN etlsih_st_df."def_nat_jur" IS 'Definição da natureza jurídica';
-- COMMENT ON COLUMN etlsih_st_df."GESTAO" IS 'Indica o tipo de gestão do hospital';
-- COMMENT ON COLUMN etlsih_st_df."def_gestao" IS 'Definição do tipo de gestão do hospital';
-- COMMENT ON COLUMN etlsih_st_df."RUBRICA" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."IND_VDRL" IS 'Indica exame VDRL';
-- COMMENT ON COLUMN etlsih_st_df."def_ind_vdrl" IS 'Definição de exame VDRL';
COMMENT ON COLUMN etlsih_st_df."MUNIC_MOV" IS 'Município do estabelecimento';
COMMENT ON COLUMN etlsih_st_df."DIAS_PERM" IS 'Dias de permanência';
COMMENT ON COLUMN etlsih_st_df."def_dias_perm" IS 'Definição de dias de permanência';
COMMENT ON COLUMN etlsih_st_df."MORTE" IS 'Indica óbito';
COMMENT ON COLUMN etlsih_st_df."def_morte" IS 'Definição de óbito';
COMMENT ON COLUMN etlsih_st_df."NACIONAL" IS 'Código da nacionalidade do paciente';
-- COMMENT ON COLUMN etlsih_st_df."NUM_PROC" IS 'Sem descrição';
COMMENT ON COLUMN etlsih_st_df."CAR_INT" IS 'Caráter da internação';
COMMENT ON COLUMN etlsih_st_df."def_car_int" IS 'Definição do caráter da internação';
-- COMMENT ON COLUMN etlsih_st_df."TOT_PT_SP" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."CPF_AUT" IS 'Sem descrição';
-- COMMENT ON COLUMN etlsih_st_df."HOMONIMO" IS 'Indicador se o paciente da AIH é homônimo do paciente de outra AIH';
-- COMMENT ON COLUMN etlsih_st_df."def_homonimo" IS 'Definição do indicador de homônimo';
-- COMMENT ON COLUMN etlsih_st_df."NUM_FILHOS" IS 'Número de filhos do paciente';
-- COMMENT ON COLUMN etlsih_st_df."def_num_filhos" IS 'Definição do número de filhos do paciente';
-- COMMENT ON COLUMN etlsih_st_df."INSTRU" IS 'Grau de instrução do paciente (sempre vem 0, remover)';
-- COMMENT ON COLUMN etlsih_st_df."def_instru" IS 'Definição do grau de instrução do paciente (sempre vem 'não se aplica', remover)';
-- COMMENT ON COLUMN etlsih_st_df."CID_NOTIF" IS 'CID de notificação';
-- COMMENT ON COLUMN etlsih_st_df."CONTRACEP1" IS 'Tipo de contraceptivo utilizado';
-- COMMENT ON COLUMN etlsih_st_df."def_contracep1" IS 'Definição do tipo de contraceptivo utilizado';
-- COMMENT ON COLUMN etlsih_st_df."CONTRACEP2" IS 'Segundo tipo de contraceptivo utilizado';
-- COMMENT ON COLUMN etlsih_st_df."def_contracep2" IS 'Definição do segundo tipo de contraceptivo utilizado';
-- COMMENT ON COLUMN etlsih_st_df."GESTRISCO" IS 'Indicador se é gestante de risco';
-- COMMENT ON COLUMN etlsih_st_df."def_gestrisco" IS 'Definição da gestão de risco';
-- COMMENT ON COLUMN etlsih_st_df."INSC_PN" IS 'Número de inscrição da gestante no programa de assistência pré-natal';
-- COMMENT ON COLUMN etlsih_st_df."SEQ_AIH5" IS 'Sequencial de longa permanência';
-- COMMENT ON COLUMN etlsih_st_df."def_seq_aih5" IS 'Definição do sequencial de longa permanência';
-- COMMENT ON COLUMN etlsih_st_df."CBOR" IS 'Ocupação do paciente, segundo a Classificação Brasileira de Ocupações (CBO)';
-- COMMENT ON COLUMN etlsih_st_df."CNAER" IS 'Código de acidente de trabalho';
-- COMMENT ON COLUMN etlsih_st_df."VINCPREV" IS 'Vínculo com a previdência';
-- COMMENT ON COLUMN etlsih_st_df."def_vincprev" IS 'Definição do vínculo da previdência';
-- COMMENT ON COLUMN etlsih_st_df."GESTOR_COD" IS 'Motivo de autorização da AIH pelo gestor';
-- COMMENT ON COLUMN etlsih_st_df."GESTOR_TP" IS 'Tipo de gestor';
-- COMMENT ON COLUMN etlsih_st_df."GESTOR_CPF" IS 'Número do CPF do gestor';
-- COMMENT ON COLUMN etlsih_st_df."GESTOR_DT" IS 'Data da autorização dada pelo gestor';
-- COMMENT ON COLUMN etlsih_st_df."CNES" IS 'Código CNES do hospital';
-- COMMENT ON COLUMN etlsih_st_df."CNPJ_MANT" IS 'CNPJ da mantenedora';
-- COMMENT ON COLUMN etlsih_st_df."INFEHOSP" IS 'Status de infecção hospitalar';
-- COMMENT ON COLUMN etlsih_st_df."def_infehosp" IS 'Definição de infecção hospitalar';
COMMENT ON COLUMN etlsih_st_df."CID_ASSO" IS 'CID-10 condições secundárias, comorbidades ou complicações, podem ter contribuído p/ a internação ou agravado o quadro principal';
COMMENT ON COLUMN etlsih_st_df."CID_MORTE" IS 'CID-10 da causa que iniciou a sequência de eventos que levou ao óbito';
COMMENT ON COLUMN etlsih_st_df."COMPLEX" IS 'Complexidade';
COMMENT ON COLUMN etlsih_st_df."def_complex" IS 'Definição de complexidade';
-- COMMENT ON COLUMN etlsih_st_df."FINANC" IS 'Tipo de financiamento';
-- COMMENT ON COLUMN etlsih_st_df."def_financ" IS 'Definição do tipo de financiamento';
-- COMMENT ON COLUMN etlsih_st_df."FAEC_TP" IS 'Subtipo de financiamento FAEC';
-- COMMENT ON COLUMN etlsih_st_df."def_faec_tp" IS 'Definição do subtipo de financiamento FAEC';
-- COMMENT ON COLUMN etlsih_st_df."REGCT" IS 'Regra contratual';
-- COMMENT ON COLUMN etlsih_st_df."def_regct" IS 'Definição da regra contratual';
-- COMMENT ON COLUMN etlsih_st_df."RACA_COR" IS 'Raça/cor do paciente';
-- COMMENT ON COLUMN etlsih_st_df."def_raca_cor" IS 'Definição de raça/cor do paciente';
-- COMMENT ON COLUMN etlsih_st_df."ETNIA" IS 'Etnia do paciente, se raça cor for indígena';
-- COMMENT ON COLUMN etlsih_st_df."SEQUENCIA" IS 'Sequencial da AIH na remessa';
-- COMMENT ON COLUMN etlsih_st_df."REMESSA" IS 'Número da remessa';
-- COMMENT ON COLUMN etlsih_st_df."AUD_JUST" IS 'Justificativa do auditor para aceitação da AIH sem o número do Cartão Nacional de Saúde';
-- COMMENT ON COLUMN etlsih_st_df."SIS_JUST" IS 'Justificativa do estabelecimento para aceitação da AIH sem o número do Cartão Nacional de Saúde';
-- COMMENT ON COLUMN etlsih_st_df."VAL_SH_FED" IS 'Valor do complemento federal de serviços hospitalares. Está incluído no valor total da AIH';
-- COMMENT ON COLUMN etlsih_st_df."VAL_SP_FED" IS 'Valor do complemento federal de serviços profissionais. Está incluído no valor total da AIH';
-- COMMENT ON COLUMN etlsih_st_df."VAL_SH_GES" IS 'Valor do complemento do gestor (estadual ou municipal) de serviços hospitalares. Está incluído no valor total da AIH';
-- COMMENT ON COLUMN etlsih_st_df."VAL_SP_GES" IS 'Valor do complemento do gestor (estadual ou municipal) de serviços profissionais. Está incluído no valor total da AIH';
COMMENT ON COLUMN etlsih_st_df."VAL_UCI" IS 'Valor de UCI';
COMMENT ON COLUMN etlsih_st_df."MARCA_UCI" IS 'Tipo de UCI utilizada pelo paciente';
COMMENT ON COLUMN etlsih_st_df."def_marca_uci" IS 'Definição do tipo de UCI utilizada pelo paciente';
COMMENT ON COLUMN etlsih_st_df."DIAGSEC1" IS 'Diagnóstico secundário 1';
COMMENT ON COLUMN etlsih_st_df."DIAGSEC2" IS 'Diagnóstico secundário 2';
COMMENT ON COLUMN etlsih_st_df."DIAGSEC3" IS 'Diagnóstico secundário 3';
COMMENT ON COLUMN etlsih_st_df."DIAGSEC4" IS 'Diagnóstico secundário 4';
COMMENT ON COLUMN etlsih_st_df."DIAGSEC5" IS 'Diagnóstico secundário 5';
COMMENT ON COLUMN etlsih_st_df."DIAGSEC6" IS 'Diagnóstico secundário 6';
COMMENT ON COLUMN etlsih_st_df."DIAGSEC7" IS 'Diagnóstico secundário 7';
COMMENT ON COLUMN etlsih_st_df."DIAGSEC8" IS 'Diagnóstico secundário 8';
COMMENT ON COLUMN etlsih_st_df."DIAGSEC9" IS 'Diagnóstico secundário 9';
COMMENT ON COLUMN etlsih_st_df."TPDISEC1" IS 'Tipo de diagnóstico secundário 1';
COMMENT ON COLUMN etlsih_st_df."def_tpdisec1" IS 'Tipo de diagnóstico secundário 1';
COMMENT ON COLUMN etlsih_st_df."TPDISEC2" IS 'Tipo de diagnóstico secundário 2';
COMMENT ON COLUMN etlsih_st_df."def_tpdisec2" IS 'Tipo de diagnóstico secundário 2';
COMMENT ON COLUMN etlsih_st_df."TPDISEC3" IS 'Tipo de diagnóstico secundário 3';
COMMENT ON COLUMN etlsih_st_df."def_tpdisec3" IS 'Tipo de diagnóstico secundário 3';
COMMENT ON COLUMN etlsih_st_df."TPDISEC4" IS 'Tipo de diagnóstico secundário 4';
COMMENT ON COLUMN etlsih_st_df."def_tpdisec4" IS 'Tipo de diagnóstico secundário 4';
COMMENT ON COLUMN etlsih_st_df."TPDISEC5" IS 'Tipo de diagnóstico secundário 5';
COMMENT ON COLUMN etlsih_st_df."def_tpdisec5" IS 'Tipo de diagnóstico secundário 5';
COMMENT ON COLUMN etlsih_st_df."TPDISEC6" IS 'Tipo de diagnóstico secundário 6';
COMMENT ON COLUMN etlsih_st_df."def_tpdisec6" IS 'Tipo de diagnóstico secundário 6';
COMMENT ON COLUMN etlsih_st_df."TPDISEC7" IS 'Tipo de diagnóstico secundário 7';
COMMENT ON COLUMN etlsih_st_df."def_tpdisec7" IS 'Tipo de diagnóstico secundário 7';
COMMENT ON COLUMN etlsih_st_df."TPDISEC8" IS 'Tipo de diagnóstico secundário 8';
COMMENT ON COLUMN etlsih_st_df."def_tpdisec8" IS 'Tipo de diagnóstico secundário 8';
COMMENT ON COLUMN etlsih_st_df."TPDISEC9" IS 'Tipo de diagnóstico secundário 9';
COMMENT ON COLUMN etlsih_st_df."def_tpdisec9" IS 'Tipo de diagnóstico secundário 9';
COMMENT ON COLUMN etlsih_st_df."res_MUNCOD" IS 'Código do município de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."res_MUNNOME" IS 'Nome (acentuado, maiúsculas e minúsculas) do Município (padrão DOS, página de código 850) de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."res_MUNNOMEX" IS 'Nome (sem acentos, em maiúsculas) do Município de residência do paciente';
-- COMMENT ON COLUMN etlsih_st_df."res_AMAZONIA" IS 'Indica (S ou N) se o município de residência do paciente faz parte da Amazônia Legal (conforme IBGE)';
-- COMMENT ON COLUMN etlsih_st_df."res_FRONTEIRA" IS 'Indica (S ou N) se o município de residência do paciente faz parte da faixa de fronteira (conforme IBGE)';
-- COMMENT ON COLUMN etlsih_st_df."res_CAPITAL" IS 'Indica (S ou N) se o município de residência do paciente é capital da UF';
-- COMMENT ON COLUMN etlsih_st_df."res_MSAUDCOD" IS 'Código da Regional de Saúde a que o Município de residência do paciente pertence';
-- COMMENT ON COLUMN etlsih_st_df."res_RSAUDCOD" IS 'Código da Microrregional de Saúde a que o Município de residência do paciente pertence';
-- COMMENT ON COLUMN etlsih_st_df."res_CSAUDCOD" IS 'Código da Microrregional de Saúde a que o Município de residência pertence';
COMMENT ON COLUMN etlsih_st_df."res_LATITUDE" IS 'Latitude da sede do Município de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."res_LONGITUDE" IS 'Longitude da sede do Município de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."res_ALTITUDE" IS 'Área, em quilômetros quadrados, do Município de residência do paciente, segundo a Resolução 05, de 10/12/2002, do IBGE';
-- COMMENT ON COLUMN etlsih_st_df."res_AREA" IS 'Armazena o código atribuído ao município de residência do paciente, tratando os casos em que múltiplos códigos tenham sido utilizados para um mesmo município ao longo do tempo';
-- COMMENT ON COLUMN etlsih_st_df."res_codigo_adotado" IS 'Armazena o código atribuído ao município de residência do paciente, tratando os casos em que múltiplos códigos tenham sido utilizados para um mesmo município ao longo do tempo';
COMMENT ON COLUMN etlsih_st_df."res_SIGLA_UF" IS 'Sigla da unidade da federação de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."res_CODIGO_UF" IS 'Código da UF de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."res_NOME_UF" IS 'Nome da unidade da federação de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."res_REGIAO" IS 'Nome da Região da unidade da federação de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."int_MUNCOD" IS 'Código do município do estabelecimento de internação';
COMMENT ON COLUMN etlsih_st_df."int_MUNNOME" IS 'Nome (acentuado, maiúsculas e minúsculas) do Município (padrão DOS, página de código 850) do estabelecimento de internação';
COMMENT ON COLUMN etlsih_st_df."int_MUNNOMEX" IS 'Nome (sem acentos, em maiúsculas) do Município do estabelecimento de internação';
-- COMMENT ON COLUMN etlsih_st_df."int_AMAZONIA" IS 'Indica (S ou N) se o município do estabelecimento de internação faz parte da Amazônia Legal (conforme IBGE)';
-- COMMENT ON COLUMN etlsih_st_df."int_FRONTEIRA" IS 'Indica (S ou N) se o município do estabelecimento de internação faz parte da faixa de fronteira (conforme IBGE)';
-- COMMENT ON COLUMN etlsih_st_df."int_CAPITAL" IS 'Indica (S ou N) se o município do estabelecimento de internação é capital da UF';
-- COMMENT ON COLUMN etlsih_st_df."int_MSAUDCOD" IS 'Código da Regional de Saúde a que o Município do estabelecimento de internação';
-- COMMENT ON COLUMN etlsih_st_df."int_RSAUDCOD" IS 'Código da Microrregional de Saúde a que o Município do estabelecimento de internação';
-- COMMENT ON COLUMN etlsih_st_df."int_CSAUDCOD" IS 'Código da Microrregional de Saúde a que o Município de internação pertence';
COMMENT ON COLUMN etlsih_st_df."int_LATITUDE" IS 'Latitude da sede do Município do estabelecimento de internação';
COMMENT ON COLUMN etlsih_st_df."int_LONGITUDE" IS 'Longitude da sede do Município do estabelecimento de internação';
COMMENT ON COLUMN etlsih_st_df."int_ALTITUDE" IS 'Altitude, em metros, da sede do Município do estabelecimento de internação';
-- COMMENT ON COLUMN etlsih_st_df."int_AREA" IS 'Área, em quilômetros quadrados, do Município do estabelecimento de internação, segundo a Resolução 05, de 10/12/2002, do IBGE';
-- COMMENT ON COLUMN etlsih_st_df."int_codigo_adotado" IS 'Armazena o código atribuído ao município do estabelecimento de internação, tratando os casos em que múltiplos códigos tenham sido utilizados para um mesmo município ao longo do tempo';
COMMENT ON COLUMN etlsih_st_df."int_SIGLA_UF" IS 'Sigla da unidade da federação do estabelecimeto de internação';
COMMENT ON COLUMN etlsih_st_df."int_CODIGO_UF" IS 'Código da UF do estabelecimento de internação';
COMMENT ON COLUMN etlsih_st_df."int_NOME_UF" IS 'Código IBGE da Unidade da Federação do estabelecimento de internação';
COMMENT ON COLUMN etlsih_st_df."int_REGIAO" IS 'Nome da Região da unidade da federação do estabelecimento de internação';
COMMENT ON COLUMN etlsih_st_df."res_coordenadas" IS 'Coordenadas do município de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."int_coordenadas" IS 'Coordenadas do município do estabelecimento de internação';
COMMENT ON COLUMN etlsih_st_df."def_reg_metr_int" IS 'Região metropolitana do estabelecimento de internação';
COMMENT ON COLUMN etlsih_st_df."def_reg_metr_res" IS 'Região metropolitana de residência do paciente';
-- COMMENT ON COLUMN etlsih_st_df."def_cir_int" IS 'Comissão Intergestora Regional do estabelecimento de internação';
-- COMMENT ON COLUMN etlsih_st_df."def_cir_res" IS 'Comissão Intergestora Regional da residência do paciente';
-- COMMENT ON COLUMN etlsih_st_df."def_aglr_int" IS 'AGL do estabelecimento de internação';
-- COMMENT ON COLUMN etlsih_st_df."def_aglr_res" IS 'AGL de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."def_meso_int" IS 'Mesorregião do estabelecimento de internação';
COMMENT ON COLUMN etlsih_st_df."def_meso_res" IS 'Mesorregião de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."def_micro_res" IS 'Microrregião de residência do paciente';
COMMENT ON COLUMN etlsih_st_df."def_micro_int" IS 'Microrregião de internação do paciente';
-- COMMENT ON COLUMN etlsih_st_df."def_rsaud_int" IS 'Região de saúde do estabelecimento de internação';
-- COMMENT ON COLUMN etlsih_st_df."def_rsaud_res" IS 'Região de saúde de residência do paciente';
-- COMMENT ON COLUMN etlsih_st_df."def_csaud_int" IS 'CSAUDE do estabelecimento de internação';
-- COMMENT ON COLUMN etlsih_st_df."def_csaud_res" IS 'CSAUDE de residência do paciente';
-- COMMENT ON COLUMN etlsih_st_df."def_esferajur" IS 'Definição de esfera jurídica';
-- COMMENT ON COLUMN etlsih_st_df."def_etnia" IS 'Definição de etnia';
COMMENT ON COLUMN etlsih_st_df."def_nacionalidade" IS 'Definição de nacionalidade';
-- COMMENT ON COLUMN etlsih_st_df."def_cbo" IS 'Definição da Classificação Brasileira de Ocupações (CBO)';
-- COMMENT ON COLUMN etlsih_st_df."def_cnae" IS 'Definição do Classificação Nacional de Atividades Econômicas';
COMMENT ON COLUMN etlsih_st_df."def_leitos" IS 'Definição de leitos';
COMMENT ON COLUMN etlsih_st_df."def_procedimento_realizado" IS 'Definição do procedimento realizado';
COMMENT ON COLUMN etlsih_st_df."def_procedimento_solicitado" IS 'Definição do procedimento solicitado';
COMMENT ON COLUMN etlsih_st_df."IDADE" IS 'Idade';
COMMENT ON COLUMN etlsih_st_df."COD_IDADE" IS 'Unidade de medida da idade';
COMMENT ON COLUMN etlsih_st_df."def_cod_idade" IS 'Definição da unidade de medida da idade';
COMMENT ON COLUMN etlsih_st_df."def_idade_anos" IS 'Idade em anos';
COMMENT ON COLUMN etlsih_st_df."def_idade_meses" IS 'Idade em meses';
COMMENT ON COLUMN etlsih_st_df."def_idade_dias" IS 'Idade em dias';
-- COMMENT ON COLUMN etlsih_st_df."def_idade_bas" IS 'Definição de faixa etária 1';
-- COMMENT ON COLUMN etlsih_st_df."def_idade_pub" IS 'Definição de faixa etária 2';
-- COMMENT ON COLUMN etlsih_st_df."def_idade_18" IS 'Definição de faixa etária 3';
COMMENT ON COLUMN etlsih_st_df."def_diag_princ_cap" IS 'Definição do capítulo do diagnóstico principal';
COMMENT ON COLUMN etlsih_st_df."def_diag_princ_grupo" IS 'Definição do grupo do diagnóstico principal';
COMMENT ON COLUMN etlsih_st_df."def_diag_princ_cat" IS 'Definição da categoria do diagnóstico principal';
COMMENT ON COLUMN etlsih_st_df."def_diag_princ_subcat" IS 'Definição da sub categoria do diagnóstico principal';
COMMENT ON COLUMN etlsih_st_df."def_diag_secun_cap" IS 'Definição do capítulo do primeiro diagnóstico secundário';
COMMENT ON COLUMN etlsih_st_df."def_diag_secun_grupo" IS 'Definição do grupo do primeiro diagnóstico secundário';
COMMENT ON COLUMN etlsih_st_df."def_diag_secun_cat" IS 'Definição da categoria do primeiro diagnóstico secundário';
COMMENT ON COLUMN etlsih_st_df."def_diag_secun_subcat" IS 'Definição da sub categoria do primeiro diagnóstico secundário';
COMMENT ON COLUMN etlsih_st_df."dt_inter" IS 'Data de internação';
-- COMMENT ON COLUMN etlsih_st_df."ano_internacao" IS 'Ano de internação';
-- COMMENT ON COLUMN etlsih_st_df."mes_internacao" IS 'Mês de internação';
-- COMMENT ON COLUMN etlsih_st_df."dia_semana_internacao" IS 'Dia da semana de internação';
COMMENT ON COLUMN etlsih_st_df."dt_saida" IS 'Data de saída';
-- COMMENT ON COLUMN etlsih_st_df."ano_saida" IS 'Ano de saída';
-- COMMENT ON COLUMN etlsih_st_df."mes_saida" IS 'Mês de saída';
-- COMMENT ON COLUMN etlsih_st_df."dia_semana_saida" IS 'Dia da semana da saída';
-- COMMENT ON COLUMN etlsih_st_df."codidade" IS 'Código da idade (nada a ver com o valor)';
