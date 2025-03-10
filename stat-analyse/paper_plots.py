import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.graphics.factorplots import interaction_plot
from statsmodels.formula.api import ols

# Carregar o arquivo CSV
df = pd.read_csv('../registration_times_with_stress_renamed_stress_wihtout_none.csv')

# Renomear a coluna para um formato mais simples
df.rename(columns={'Tempo gasto (ms)': 'Tempo_gasto_ms'}, inplace=True)

# Converter a coluna Timestamp para datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Criar diretório para salvar os gráficos, se não existir
plots_dir = "plots_dir"
os.makedirs(plots_dir, exist_ok=True)

model = ols('Tempo_gasto_ms ~ stress_test * nf', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)




# Gráfico de Interação
nf_levels = df['nf'].unique()
markers = ['o', 's', 'D', '^', 'v', '<', '>', 'p', '*', 'h', '+']
colors = sns.color_palette("hsv", len(nf_levels))

# Garantir que o número de marcadores e cores não ultrapasse o número de níveis
markers = markers[:len(nf_levels)]
colors = colors[:len(nf_levels)]

plt.figure(figsize=(40, 20))  # Aumenta a largura do gráfico
interaction_plot(df['stress_test'], df['nf'], df['Tempo_gasto_ms'], markers=markers, colors=colors)

plt.xlabel('Stress Test', fontsize=16)
plt.ylabel('Registration Time (ms)', fontsize=16)
plt.xticks(fontsize=14, rotation=0)
plt.yticks(fontsize=14)

# Posiciona a legenda fora do gráfico
plt.legend(title=None, fontsize=14, loc='upper left', bbox_to_anchor=(1, 1))

plt.savefig(os.path.join(plots_dir, 'interaction_plot.png'), bbox_inches='tight')
plt.close()





# Resíduos vs Ajustados
plt.figure(figsize=(14, 7))
plt.scatter(model.fittedvalues, model.resid)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs Fitted')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.savefig(os.path.join(plots_dir, 'residuals_vs_fitted.png'))
plt.close()

# Q-Q Plot
plt.figure(figsize=(14, 7))
sm.qqplot(model.resid, line='s')
plt.title('Q-Q Plot')
plt.savefig(os.path.join(plots_dir, 'qq_plot.png'))
plt.close()


plt.figure(figsize=(14, 7))
sm.graphics.influence_plot(model, criterion="cooks")
plt.title('Influence Plot (Cook\'s Distance)')
plt.savefig(os.path.join(plots_dir, 'influence_plot.png'))
plt.close()


plt.figure(figsize=(14, 7))
plt.hist(model.resid, bins=30, edgecolor='black')
plt.title('Histogram of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.savefig(os.path.join(plots_dir, 'histogram_residuals.png'))



plt.figure(figsize=(14, 7))
plt.scatter(df['Tempo_gasto_ms'], model.fittedvalues)
plt.plot([df['Tempo_gasto_ms'].min(), df['Tempo_gasto_ms'].max()], [df['Tempo_gasto_ms'].min(), df['Tempo_gasto_ms'].max()], 'r--')
plt.title('Observed vs. Predicted Values')
plt.xlabel('Observed Values')
plt.ylabel('Predicted Values')
plt.savefig(os.path.join(plots_dir, 'observed_vs_predicted.png'))
plt.close()



plt.figure(figsize=(14, 7))
sns.kdeplot(model.resid, shade=True)
plt.title('Density Plot of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Density')
plt.savefig(os.path.join(plots_dir, 'density_plot_residuals.png'))

