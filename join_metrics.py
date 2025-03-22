import pandas as pd

# Carregar os arquivos CSV
registration_times = pd.read_csv('registration_times.csv')
stress_events = pd.read_csv('stress_events.csv')

# Converter Timestamps para datetime
registration_times['Timestamp'] = pd.to_datetime(registration_times['Timestamp'])
stress_events['begin_timestamp'] = pd.to_datetime(stress_events['begin_timestamp'], unit='s')
stress_events['end_timestamp'] = pd.to_datetime(stress_events['end_timestamp'], unit='s')

# Função para verificar se o timestamp está no intervalo de stress
def get_stress_tests(timestamp, stress_events):
    matching_tests = stress_events[(stress_events['begin_timestamp'] <= timestamp) &
                                   (stress_events['end_timestamp'] >= timestamp)]
    return matching_tests

# Criação de uma lista para armazenar os resultados
results = []

# Loop para adicionar linhas à lista de resultados
for index, row in registration_times.iterrows():
    stress_tests = get_stress_tests(row['Timestamp'], stress_events)
    if not stress_tests.empty:
        for _, stress_row in stress_tests.iterrows():
            new_row = {
                'Timestamp': row['Timestamp'],
                'Tempo gasto (ms)': row['Tempo gasto (ms)'],
                'nf': stress_row['nf'],
                'stress_test': stress_row['stress_test']
            }
            results.append(new_row)

# Converter a lista de resultados para um DataFrame
result_df = pd.DataFrame(results)

# Salvar o resultado em um novo arquivo CSV
result_df.to_csv('registration_times_with_stress.csv', index=False)

