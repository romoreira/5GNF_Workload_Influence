import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('../registration_times_with_stress.csv')

# Ajustar o modelo de efeitos mistos: CPU e Memória como fixos, NF como aleatório
model_mixed = smf.mixedlm('Q("Tempo gasto (ms)") ~ C(stress_test)', 
                          data=df, 
                          groups=df["nf"]).fit()

# Exibir o resumo do modelo
print(model_mixed.summary())
