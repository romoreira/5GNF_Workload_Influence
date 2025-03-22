import os
import requests

from datetime import datetime
import time
import json
import pandas as pd

def get_5g_nf_charts(nf_name):
    # Suponha que você tenha o JSON carregado como um dicionário Python.
    with open('charts.json') as f:
        json_data = json.load(f)

    # Filtra os gráficos relacionados ao 'amf' e pega somente a parte após '/api/v1/data?chart='.
    amf_charts = []
    amf_charts = [
        chart_data["data_url"].split("/api/v1/data?chart=")[1]
        for chart_name, chart_data in json_data["charts"].items()
        if "app.amf" in chart_data["data_url"]
    ]

    # Concatena as strings em uma única string separada por vírgulas.
    #amf_charts_string = ", ".join(amf_charts)

    return amf_charts


def merge_metrics_single_csv():
    directory = 'basic_workload/data'
    # Lista todos os arquivos CSV no diretório
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    files.sort()  # Opcional, para garantir ordem
    
    if not files:
        print("Nenhum arquivo CSV encontrado.")
        return
    
    merged_df = None
    
    for i, file in enumerate(files):
        file_path = os.path.join(directory, file)
        df = pd.read_csv(file_path)
        
        if i == 0:
            merged_df = df  # Mantém todas as colunas do primeiro arquivo
        else:
            df = df.drop(columns=['time'], errors='ignore')  # Remove a coluna 'time' dos demais arquivos
            merged_df = pd.concat([merged_df, df], axis=1)
    
    merged_df.to_csv('basic_workload/no-ddos_amf_experiment_metrics.csv', index=False)

#create a dictionary with IPv6 of a vm and the name 'Node' of the vm
dict_vm = {
    '127.0.0.1': 'Node1',
}

dict_port_node = {
    '19999': 'Node1',
}

def time_convert(data_hora_str):
    # Definir a data e hora no formato especificado

    data_hora = datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M:%S")

    # Converter para o formato de Unix epoch
    unix_epoch = int(time.mktime(data_hora.timetuple()))

    return unix_epoch

# Defina a base da URL
entity = ''
base_url = f"http://{entity}/api/v1/data?chart="

data_begin = "2025-03-21 16:21:44"  # Data de início da coleta
data_end = "2025-03-21 16:22:54"  # Data de fim da coleta

data_begin = time_convert(data_begin)
print("Timetamp do Begin: " + str(data_begin))  
data_end = time_convert(data_end)
print("Timetamp do End: " + str(data_end))

# Parâmetros adicionais que serão adicionados ao final da URL
params_suffix = f"&options=unaligned&group=average&after={data_begin}&before={data_end}&format=csv"

entities = ["127.0.0.1:19999"]  # Lista de entidades

charts = ["net.enp3s0"]
'''
charts = ["net.enp3s0",
          "net_speed.enp3s0",
          "net_duplex.enp3s0",
          "net_operstate.enp3s0",
          "net_carrier.enp3s0",
          "net_mtu.enp3s0",
          "net_packets.enp3s0",
          "net_errors.enp3s0",
          "net_drops.enp3s0",
          "net_fifo.enp3s0",
          "net_events.enp3s0",
          "system.cpu",
          "system.load",
          "system.active_processes",
          "system.cpu_some_pressure",
          "system.cpu_some_pressure_stall_time",
          "system.memory_some_pressure",
          "system.memory_some_pressure_stall_time",
          "mem.pgfaults",
          "mem.thp_faults",
          "system.ram",
          "mem.committed"]'
'''

nf_list = get_5g_nf_charts('amf')

#concatenate 5g_nf_len list to the existint one, named charts. How contatenate lists?
charts = charts + nf_list



# Faça a requisição para cada entidade e gráfico
for entity in entities:
    for chart in charts:
        # Substitua '{entity}' pelo nome da entidade
        chart_url = chart.format(entity=entity)
        # Construa a URL completa
        base_url = f"http://{entity}/api/v1/data?chart="
        url = base_url + chart_url + params_suffix

        print("URL: " + str(url))


        # Envie a requisição GET
        response = requests.get(url)

        # Verifique o status da resposta
        if response.status_code == 200:
            # Processar a resposta (por exemplo, salvar o conteúdo em um arquivo)
            #filename = f"data/{entity.split(":")[1]}_{chart_url.replace('/', '_').replace('.', '_')}.csv"  # Nome do arquivo dentro do diretório 'results'
            filename = f"basic_workload/data/{dict_port_node[entity.split(':')[1]]}_{chart_url.replace('/', '_').replace('.', '_')}.csv"  # Nome do arquivo dentro do diretório 'results'

            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Dados para {entity} e gráfico {chart_url} salvos em {filename}")
        else:
            print(f"Falha na requisição para {entity} e gráfico {chart_url}: {response.status_code}")

merge_metrics_single_csv()