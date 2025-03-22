import pandas as pd
import statsmodels.formula.api as smf

# Carregar o arquivo CSV
df = pd.read_csv('../registration_times_with_stress.csv')

# Definir "any" como a categoria de referência (baseline)
df['stress_test'] = pd.Categorical(df['stress_test'], categories=['any', 'CPU_50_Duration_20', 'MEMORY_512_Duration_20', 'CPU_50_MEMORY_512_Duration_20'], ordered=True)

# Ajustar o modelo de efeitos mistos: CPU, Memória e CPU+Memória como fixos, NF como aleatório
model_mixed = smf.mixedlm('Q("Tempo gasto (ms)") ~ C(stress_test)', data=df, groups=df["nf"]).fit()

# Exibir o resumo do modelo
print(model_mixed.summary())
