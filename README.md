# mobility-app-anomalies-detector

[🇧🇷 Versão em Português](#versão-em-português) | [🇺🇸 English Version](#english-version)

---

## Versão em Português

**mobility-app-anomalies-detector** é um projeto de engenharia de dados em desenvolvimento que tem como objetivo identificar comportamentos anômalos ou suspeitos em plataformas de mobilidade urbana, como Uber ou 99. O sistema simula dados realistas de corridas por aplicativo e constrói pipelines escaláveis para analisar, validar e sinalizar padrões de fraude relacionados a motoristas, passageiros, rotas e preços.

### Índice

- [Objetivos do projeto](#objetivos-do-projeto)
- [Exemplos de anomalias detectadas](#exemplos-de-anomalias-detectadas)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Estrutura prevista do projeto](#estrutura-prevista-do-projeto)
- [Status](#status)

### Objetivos do projeto

Os principais objetivos deste projeto são:

- Simular dados de corridas com padrões geográficos e comportamentais realistas
- Validar os dados estruturados utilizando Pydantic
- Detectar anomalias como:
  - Corridas muito curtas com valores altos
  - Coordenadas de GPS inconsistentes
  - Taxas excessivas de cancelamento
  - Volume incomum de corridas por usuário ou motorista
  - Corridas em horários ou regiões incomuns
- Armazenar, orquestrar e processar os dados com ferramentas escaláveis

### Exemplos de anomalias detectadas

- Corridas com distância mínima e valor elevado
- Motoristas completando número anormal de corridas por hora
- Passageiros usando cupons repetidamente ou cancelando com frequência
- Diferença entre a distância reportada e a real (GPS)
- Tempo parado excessivo durante uma corrida em andamento
- Corridas em horários ou locais atípicos

### Tecnologias utilizadas

- Python para simulação e processamento dos dados
- Pydantic para validação rigorosa dos dados gerados
- Apache Airflow para orquestração dos pipelines
- PySpark para processamento distribuído e análise de anomalias
- MongoDB para armazenar as corridas e os registros sinalizados
- Redis (opcional) para cache e monitoramento de anomalias recentes
- AWS S3 para armazenar os arquivos `.jsonl` com os dados simulados

### Estrutura prevista do projeto

- `include/scripts/`: geração de dados simulados das corridas
- `include/models/`: schemas de validação com Pydantic
- `dags/`: DAGs do Airflow para orquestração
- `include/data/`: arquivos gerados localmente antes do envio ao S3
- `tests/`: testes unitários gerados com Pytest

### Status

Este projeto está em desenvolvimento.  
As próximas etapas incluem:

- Finalizar o gerador de corridas simuladas
- Implementar regras e validações de anomalias
- Construir o pipeline de processamento com PySpark
- Integrar o fluxo com MongoDB e Airflow

As instruções de instalação e execução serão adicionadas após a finalização das etapas principais.

---

## English Version

**mobility-app-anomalies-detector** is a data engineering project currently under development that aims to detect **anomalous or suspicious behavior** in urban mobility platforms, such as Uber or 99. The system simulates realistic ride data and builds scalable pipelines to analyze, validate, and flag potential fraud patterns related to drivers, passengers, routes, and pricing.

### Table of Contents

- [Project Goals](#project-goals)
- [Examples of Detected Anomalies](#examples-of-detected-anomalies)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Status](#status-1)

### Project Goals

The main objectives of this project are:

- Simulate ride data with realistic geographic and behavioral patterns
- Validate structured data using Pydantic
- Detect anomalies such as:
  - Very short rides with high prices
  - Inconsistent GPS coordinates
  - Excessive cancellation rates
  - Unusual ride volume per user or driver
  - Rides at uncommon times or in strange regions
- Store, orchestrate, and process the data using scalable tools

### Examples of Detected Anomalies

- Rides with minimal distance and elevated price
- Drivers completing an abnormal number of rides per hour
- Passengers using discount codes repeatedly or canceling too often
- Differences between reported and actual distance (GPS)
- Excessive idle time during active rides
- Rides happening at unusual times or locations

### Technologies Used

- Python for data simulation and processing
- Pydantic for strict data validation
- Apache Airflow for pipeline orchestration
- PySpark for distributed processing and anomaly detection
- MongoDB to store rides and flagged records
- Redis (optional) for caching and anomaly tracking
- AWS S3 to store `.jsonl` ride files

### Project Structure

- `include/scripts/`: ride data generation scripts
- `include/models/`: validation schemas using Pydantic
- `dags/`: Airflow DAGs for orchestration
- `include/data/`: locally generated files before uploading to S3
- `tests/`: unit tests written with Pytest

### Status

This project is currently in development.  
Next steps include:

- Finalizing the simulated ride generator
- Implementing anomaly rules and validations
- Building the processing pipeline with PySpark
- Integrating with MongoDB and Airflow

Setup and execution instructions will be added once the core development is complete.
