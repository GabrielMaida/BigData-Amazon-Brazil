# Projeto de Ingestão e Armazenamento de Dados

## 📝 Objetivo
O objetivo deste projeto é criar um sistema de ingestão e armazenamento de dados que permite **ler arquivos CSV**, armazená-los de forma eficiente no **formato Parquet** e realizar operações básicas de manipulação de dados para exploração.


## 💻 Tecnologias Utilizadas
Este projeto é desenvolvido com as seguintes tecnologias e bibliotecas Python:

* **Python 3.x**
* **Pandas**: Para manipulação e análise de dados.
* **PyArrow**: Engine fundamental para o suporte ao formato Parquet no Pandas.
* **ZipFile**: Módulo padrão do Python para extração de arquivos ZIP.


## ⚙️ Requisitos
Para executar este projeto, você precisará ter o **Python 3.x** instalado em seu sistema. Além disso, as dependências do projeto estão listadas no arquivo `requirements.txt`.

### Instalação de Dependências

Você pode instalar todas as dependências necessárias executando o seguinte comando no seu terminal, preferencialmente dentro de um ambiente virtual (`venv`):

```bash
pip install -r requirements.txt
```

**Conteúdo de `requirements.txt`:**

```
numpy==2.3.1
pandas==2.3.0
pip==25.1.1
pyarrow==20.0.0
python-dateutil==2.9.0.post0
pytz==2025.2
six==1.17.0
tzdata==2025.2
```


## 🚀 Tutorial de Execução
Siga os passos abaixo para clonar o projeto e executá-lo em sua máquina:

1.  **Clone o repositório do projeto:**
    ```bash
    git clone https://github.com/GabrielMaida/BigData-Amazon-Brazil
    ```

2.  **Acesse o diretório do projeto:**
    ```bash
    cd projeto-ingestao-dados
    ```

3.  **Instale as dependências do Python (Se ainda não tiver feito)**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o script `extract.py` para extrair o arquivo ZIP:**
    Este passo é crucial para descompactar o dataset CSV (`amazon-brazil-produtos.csv`) a partir do arquivo `amazon-brazil.zip`.
    ```bash
    python extract.py
    ```

5.  **Execute o script `main.py` para iniciar o sistema de ingestão e armazenamento de dados:**
    ```bash
    python main.py
    ```

6.  **Interação:**
    Siga as instruções apresentadas no menu do terminal para realizar operações de ingestão, armazenamento e exploração dos dados.
    

## ✨ Funcionalidades
O sistema oferece as seguintes funcionalidades principais:

* **Leitura de arquivos CSV**: Carrega datasets do formato CSV para um DataFrame Pandas.
* **Armazenamento de dados em formato Parquet**: Converte e salva DataFrames para o formato colunar Parquet, otimizado para Big Data.
* **Operações básicas de manipulação de dados**: Inclui a capacidade de exibir informações do DataFrame (e.g., `.info()`, `.shape`), visualizar amostras de dados (`.head()`), e inspecionar colunas e tipos de dados.
* **Recarga dinâmica**: Permite recarregar tanto o arquivo CSV original quanto o arquivo Parquet do disco durante a execução do programa.


## 📄 Licença
Este projeto é licenciado sob a licença **MIT**. Para mais detalhes, consulte o arquivo [`LICENSE`](LICENSE) na raiz do repositório.


## 🤝 Contribuição
Contribuições são sempre bem-vindas! Se você tiver sugestões de melhoria, identificou um bug ou deseja adicionar novas funcionalidades, por favor, sinta-se à vontade para abrir uma [issue](https://github.com/seu-usuario/projeto-ingestao-dados/issues) ou enviar um [pull request](https://github.com/seu-usuario/projeto-ingestao-dados/pulls).