import pandas as pd
from sklearn.model_selection import train_test_split
import os
import re
import nltk
import matplotlib.pyplot as plt

nltk.download('stopwords')
from nltk.corpus import stopwords

def clean_text(text):
    """
    Limpa o texto removendo pontuação, convertendo para minúsculas
    e removendo stopwords.
    """
    text = re.sub(r'[^\w\s]', '', str(text).lower())  # Remove pontuação e converte para minúsculas
    stop_words = set(stopwords.words('portuguese'))
    words = [word for word in text.split() if word not in stop_words]  # Remove stopwords
    return ' '.join(words)

def preprocess_and_save_partitions(input_filepath, output_dir='partitions', test_size=0.1, random_state=42):
    """
    Lê os dados, cria partições de treino e teste, e salva em arquivos CSV.
    """
    # Carrega os dados
    data = pd.read_csv(input_filepath)
    
    # Processa o texto
    data['cleaned_text'] = data['text'].apply(clean_text)
    
    # Divide os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        data['cleaned_text'], 
        data['Hate.speech'], 
        test_size=test_size, 
        random_state=random_state, 
        stratify=data['Hate.speech']
    )
    
    # Cria o diretório de saída, se não existir
    os.makedirs(output_dir, exist_ok=True)
    
    # Salva as partições em arquivos CSV
    pd.DataFrame({'text': X_train, 'label': y_train}).to_csv(os.path.join(output_dir, 'train.csv'), index=False)
    pd.DataFrame({'text': X_test, 'label': y_test}).to_csv(os.path.join(output_dir, 'test.csv'), index=False)
    print(f"Partições salvas em '{output_dir}'.")
    
def plot_partitions_distribution(partition_dir):
    """
    Carrega as partições de treino e teste e plota a distribuição de classes.
    """
    # Verifica se o diretório existe
    if not os.path.exists(partition_dir):
        print(f"Diretório '{partition_dir}' não encontrado.")
        return
    
    # Carrega os dados de treino e teste
    train_filepath = os.path.join(partition_dir, 'train.csv')
    test_filepath = os.path.join(partition_dir, 'test.csv')
    
    if not os.path.exists(train_filepath) or not os.path.exists(test_filepath):
        print("Os arquivos de partições não foram encontrados.")
        return
    
    train_data = pd.read_csv(train_filepath)
    test_data = pd.read_csv(test_filepath)
    
    # Calcula a distribuição de classes
    train_distribution = train_data['label'].value_counts()
    test_distribution = test_data['label'].value_counts()
    
    # Cria os gráficos
    fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
    
    # Gráfico de treino
    axes[0].bar(train_distribution.index.astype(str), train_distribution.values, color='blue', alpha=0.7)
    axes[0].set_title("Distribuição de Classes - Treino")
    axes[0].set_xlabel("Classes")
    axes[0].set_ylabel("Quantidade")
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)
    
    # Gráfico de teste
    axes[1].bar(test_distribution.index.astype(str), test_distribution.values, color='orange', alpha=0.7)
    axes[1].set_title("Distribuição de Classes - Teste")
    axes[1].set_xlabel("Classes")
    axes[1].grid(axis='y', linestyle='--', alpha=0.7)
    
    # Ajusta o layout
    plt.tight_layout()
    plt.show()    

if __name__ == "__main__":
    # Caminho do arquivo de entrada
    input_filepath = '2019-05-28_portuguese_hate_speech_hierarchical_classification.csv'
    
    # Diretório de saída para salvar as partições
    output_dir = 'partitions'
    
    # Chama a função para criar e salvar as partições
    preprocess_and_save_partitions(input_filepath, output_dir)
    plot_partitions_distribution(output_dir)
