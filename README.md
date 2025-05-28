#  mobility-app-anomalies-detector

**mobility-app-anomalies-detector** é um projeto de engenharia de dados em desenvolvimento que tem como objetivo identificar **comportamentos anômalos ou suspeitos** em plataformas de mobilidade urbana, como Uber ou 99. O sistema simula dados realistas de corridas por aplicativo e constrói pipelines escaláveis para analisar, validar e sinalizar padrões de fraude relacionados a motoristas, passageiros, rotas e preços.


## Objetivos do projeto

Os principais objetivos deste projeto são:

- Simular dados de corridas com padrões geográficos e comportamentais realistas
- Validar os dados estruturados utilizando **Pydantic**
- Detectar anomalias como:
  - Corridas muito curtas com valores altos
  - Coordenadas de GPS inconsistentes
  - Taxas excessivas de cancelamento
  - Volume incomum de corridas por usuário ou motorista
  - Corridas em horários ou regiões incomuns
- Armazenar, orquestrar e processar os dados com ferramentas escaláveis


## Exemplos de anomalias detectadas

- Corridas com distância mínima e valor elevado
- Motoristas completando número anormal de corridas por hora
- Passageiros usando cupons repetidamente ou cancelando com frequência
- Diferença entre a distância reportada e a real (GPS)
- Tempo parado excessivo durante uma corrida em andamento
- Corridas em horários ou locais atípicos


## 🧰 Tecnologias utilizadas

- **Python** para simulação e processamento dos dados
- **Pydantic** para validação rigorosa dos dados gerados
- **Apache Airflow** para orquestração dos pipelines
- **PySpark** para processamento distribuído e análise de anomalias
- **MongoDB** para armazenar as corridas e os registros sinalizados
- **Redis** (opcional) para cache e monitoramento de anomalias recentes
- **AWS S3** para armazenar os arquivos `.jsonl` com os dados simulados


## 📁 Estrutura prevista do projeto (em progresso)

- `include/scripts/`: geração de dados simulados das corridas
- `include/models/`: schemas de validação com Pydantic
- `dags/`: DAGs do Airflow para orquestração
- `include/data/`: arquivos gerados localmente antes do envio ao S3


## 🚧 Status

Este projeto está em desenvolvimento.  
As próximas etapas incluem:

- Finalizar o gerador de corridas simuladas
- Implementar regras e validações de anomalias
- Construir o pipeline de processamento com PySpark
- Integrar o fluxo com MongoDB e Airflow


*As instruções de instalação e execução serão adicionadas após a finalização das etapas principais.*

