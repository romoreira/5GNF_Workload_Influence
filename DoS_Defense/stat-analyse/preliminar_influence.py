import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('../registration_times_with_stress.csv')
print("DF: ", df.head())

# Teste One-Way ANOVA para ver se a NF influencia o tempo de registro
model_nf = smf.ols('Q("Tempo gasto (ms)") ~ C(nf)', data=df).fit()
anova_nf = sm.stats.anova_lm(model_nf, typ=2)

print(anova_nf)
