# Geração e Salvamento de Partições de Treino e Teste

Este repositório contém scripts utilizados para gerar e salvar partições de treino e teste, baseadas na [base de dados de discurso de ódio em português](https://github.com/paulafortuna/Portuguese-Hate-Speech-Dataset), disponibilizada por Paula Fortuna.

O script responsável por realizar este procedimento, localizado em [`Scripts/SalvaParticoes.py`](https://github.com/Carlosbera7/SalvarParticoes/blob/main/Scripts/SalvaParticoes.py), foi desenvolvido com base na seção de experimentos do trabalho de Fortuna et al. (2019). Ele segue os parâmetros descritos pela autora, incluindo o pré-processamento da coluna `text` e o uso da coluna `Hate.speech` como variável alvo.

As partições geradas são salvas no diretório [`Data/`](https://github.com/Carlosbera7/SalvarParticoes/tree/main/Data). Este repositório contém as partições já geradas e utilizadas nos experimentos, disponíveis em [`Data/Particoes Utilizadas`](https://github.com/Carlosbera7/SalvarParticoes/tree/main/Data/Particoes%20Utilizadas). O objetivo é garantir consistência nos dados utilizados em experimentos futuros. O código pode ser testado diretamente em [`Execução`](https://obscure-xylophone-wrr9q4j5v525g6.github.dev/)

## Detalhes das Partições

- **Partição de Treino:**  
  Contém 5.101 instâncias, sendo:  
  - 1.092 classificadas como discurso de ódio  
  - 4.009 classificadas como não discurso de ódio  

- **Partição de Teste:**  
  Contém 567 instâncias, sendo:  
  - 136 classificadas como discurso de ódio  
  - 431 classificadas como não discurso de ódio  

### Distribuição das Classes
A figura a seguir ilustra a distribuição das classes nas partições:  
![Distribuição das Partições](https://github.com/user-attachments/assets/b3efd3eb-8b77-42c8-8c40-7b90d9fef00b)

## Observação
Os experimentos futuros utilizarão exclusivamente estas partições salvas para garantir a reprodutibilidade e comparabilidade dos resultados.  
