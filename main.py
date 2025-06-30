import pandas as pd

CSV_FILE_NAME = 'amazon-brazil-produtos.csv'
PARQUET_FILE_NAME = 'amazon-brazil-produtos.parquet'

# --- Funções de Ingestão e Armazenamento ---
def ler_csv(file_path):
    """Lê um arquivo CSV e retorna um DataFrame."""
    try:
        print(f"Tentando ler o arquivo CSV: {file_path}")
        df = pd.read_csv(file_path)
        print('DataFrame lido com sucesso do CSV!')
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo CSV '{file_path}' não foi encontrado. Certifique-se de ter executado 'extract.py'.")
        return None
    except Exception as e:
        print(f"Erro ao ler o CSV: {e}")
        return None

def salvar_para_parquet(df, file_path):
    """Salva um DataFrame no formato Parquet."""
    try:
        print(f"\nTentando salvar o DataFrame como Parquet: {file_path}")
        df.to_parquet(file_path, index=False) # index=False para não salvar o índice do DataFrame
        print('DataFrame salvo com sucesso como Parquet!')
        return True
    except Exception as e:
        print(f"Erro ao salvar o DataFrame como Parquet: {e}")
        return False

def ler_do_parquet(file_path):
    """Lê um arquivo Parquet e retorna um DataFrame."""
    try:
        print(f"\nTentando ler o arquivo Parquet: {file_path}")
        df = pd.read_parquet(file_path)
        print('DataFrame lido com sucesso do Parquet!')
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo Parquet '{file_path}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o Parquet: {e}")
        return None

# --- Execução Inicial ---
df_original = ler_csv(CSV_FILE_NAME)

# Se o CSV não puder ser lido, o programa não pode continuar
if df_original is None:
    exit("Erro fatal: Não foi possível carregar o CSV. Encerrando programa.")

# Tenta salvar o DataFrame inicial como Parquet
if salvar_para_parquet(df_original, PARQUET_FILE_NAME):
    # Se salvou com sucesso, tenta ler o Parquet para uso subsequente
    df_parquet = ler_do_parquet(PARQUET_FILE_NAME)
else:
    # Se não conseguiu salvar, tenta ler o Parquet existente (caso haja)
    # ou define como None se não existir ou houver erro na leitura
    df_parquet = ler_do_parquet(PARQUET_FILE_NAME)
    if df_parquet is None:
        print("Aviso: Não foi possível salvar ou carregar o arquivo Parquet inicialmente.")

# --- Funções de Interface do Usuário ---
def printar_menu():
    """Imprime as opções do menu."""
    print('''
---
Escolha uma opção:
- 1) Informações do DataFrame (CSV original em memória)
- 2) Formato do DataFrame (Parquet em memória)
- 3) Amostra de dados (CSV original em memória)
- 4) Reler arquivo CSV original
- 5) Salvar e Recarregar arquivo Parquet (resync com CSV em memória)
- 6) Mostrar colunas (CSV original em memória)
- 7) Mostrar tipos de dados (CSV original em memória)
- 8) Recarregar APENAS arquivo Parquet (do disco)
- 9) Encerrar execução do programa
    ''')

# --- Loop Principal do Programa ---

printar_menu()

while True:
    choice = input("Escolha uma opção: ")

    if choice == '1':
        print("\n--- Informações do DataFrame (CSV original em memória) ---")
        if df_original is not None:
            df_original.info()
        else:
            print("DataFrame original (CSV) não carregado.")

    elif choice == '2':
        print("\n--- Formato do DataFrame (Parquet em memória) ---")
        if df_parquet is not None:
            print(df_parquet.shape) # Correção: .shape é atributo, não método
        else:
            print("DataFrame Parquet não carregado.")

    elif choice == '3':
        print("\n--- Amostra de dados (CSV original em memória) ---")
        if df_original is not None:
            print(df_original.head())
        else:
            print("DataFrame original (CSV) não carregado.")

    elif choice == '4':
        print("\n--- Reler arquivo CSV original ---")
        temp_df = ler_csv(CSV_FILE_NAME)
        if temp_df is not None:
            df_original = temp_df
            print("\nArquivo CSV relido com sucesso!")
        else:
            print("\nFalha ao reler o arquivo CSV.")

    elif choice == '5':
        print("\n--- Salvar e Recarregar arquivo Parquet (resync com CSV em memória) ---")
        if df_original is not None:
            if salvar_para_parquet(df_original, PARQUET_FILE_NAME):
                df_parquet = ler_do_parquet(PARQUET_FILE_NAME)
                if df_parquet is not None:
                    print("\nArquivo Parquet salvo e recarregado com sucesso!")
                else:
                    print("\nFalha ao recarregar o arquivo Parquet após salvar.")
            else:
                print("\nFalha ao salvar o arquivo Parquet.")
        else:
            print("DataFrame original (CSV) não carregado para salvar no Parquet.")
    
    elif choice == '6':
        print("\n--- Mostrar colunas originais (CSV original em memória) ---")
        if df_original is not None:
            print(df_original.columns.tolist())
        else:
            print("DataFrame original (CSV) não carregado.")

    elif choice == '7':
        print("\n--- Mostrar tipos de dados (CSV original em memória) ---")
        if df_original is not None:
            print(df_original.dtypes)
        else:
            print("DataFrame original (CSV) não carregado.")
            
    elif choice == '8':
        print("\n--- Recarregar APENAS arquivo Parquet (do disco) ---")
        temp_df_parquet = ler_do_parquet(PARQUET_FILE_NAME)
        if temp_df_parquet is not None:
            df_parquet = temp_df_parquet
            print("\nArquivo Parquet recarregado com sucesso!")
        else:
            print("\nFalha ao recarregar o arquivo Parquet.")

    elif choice == '9':
        print("\n--- Encerrando execução do programa ---")
        break

    else:
        print("\n--- Opção inválida. Tente novamente ---")