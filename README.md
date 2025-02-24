# Análise de Desempenho Acadêmico

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-green.svg)

## 📚 Sobre o Projeto

Este projeto implementa um modelo de Regressão Linear Simples para analisar a relação entre horas de estudo e pontuação em testes. A hipótese central é que existe uma correlação positiva entre o tempo dedicado ao estudo e o desempenho acadêmico dos estudantes.

O modelo foi treinado utilizando dados reais de horas de estudo e pontuações em testes, possibilitando prever o desempenho de alunos com base em seu tempo de estudo.

## 🔍 Características

- **Análise Exploratória de Dados (EDA)** detalhada do conjunto de dados
- **Modelo de Regressão Linear Simples** para previsão de pontuações
- **Análise de métricas** de desempenho do modelo
- **Análise de resíduos** para validação estatística
- **API RESTful** para integração do modelo em aplicações

## 🛠️ Tecnologias Utilizadas

### Bibliotecas Principais
- `scikit-learn`: Implementação do modelo de regressão linear
- `pandas`: Manipulação e análise de dados
- `matplotlib` e `seaborn`: Visualização de dados
- `statsmodels`: Análise estatística detalhada
- `FastAPI`: Desenvolvimento da API
- `uvicorn`: Servidor ASGI para a API
- `pydantic`: Validação de dados
- `joblib`: Serialização do modelo
- `pingouin`: Análises estatísticas adicionais

### Ambiente de Desenvolvimento
- `pipenv`: Gerenciamento de dependências e ambiente virtual
- `jupyter notebook`: Desenvolvimento e análise interativa

## 📋 Estrutura do Projeto

```
regressao_linear_simples/
│
├── datasets/
│   └── pontuacao_test.csv      # Dataset de horas de estudo e pontuações
│
├── models/
│   └── modelo_regressao.pkl    # Modelo serializado
│
├── api_modelo_regressao.py     # Implementação da API FastAPI
|
├── modelo_pontuacao.ipynb  # Notebook com EDA e treinamento do modelo
│
├── README.md                   # Este arquivo
├── Pipfile                     # Definição de dependências
└── Pipfile.lock                # Versões fixas das dependências
```

## 📊 Resultados

O modelo de regressão linear demonstrou que existe uma forte correlação positiva entre as horas de estudo e a pontuação nos testes, confirmando a hipótese inicial. As principais métricas alcançadas foram:

- **R²**: 0.9828400452912442 (coeficiente de determinação)
- **RMSE**: 27.69471608884342 (erro médio quadrático)
- **MAE**: 22.957470277134615 (erro médio absoluto)

A análise de resíduos confirmou a adequação do modelo linear para os dados.

## 🚀 Como Executar

### Requisitos

- Python 3.11+
- pipenv

### Instalação

```bash
# Clone o repositório
git clone https://github.com/srmatheusmaciel/regressao_linear_simples.git
cd regressao_linear_simples

# Instale as dependências
pipenv install scikit-learn scipy pandas matplotlib statsmodel fastapi uvicorn pydantic pingouin seaborn ipykernel
```

### Treinamento do Modelo

```bash
# Ative o ambiente virtual
pipenv shell

# Execute o notebook para análise e treinamento
jupyter notebook
```

### Executando a API

```bash
# Inicie o servidor da API
uvicorn api:app --reload

# A API estará disponível em http://localhost:8000
# A documentação Swagger estará em http://localhost:8000/docs
```


### Código da API

```python
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

# Criar uma instancia do FastAPI
app = FastAPI()

# Criar uma classe que terá os dados do request body para a API
class request_body(BaseModel):
  horas_estudo: float

# Carregar o modelo
modelo_pontuacao = joblib.load('./models/modelo_regressao.pkl')

# Criar uma rota para a API
@app.post('/predict')
def predict(data : request_body):
  
  # Preparar os dados para predição
  input_feature = [[data.horas_estudo]]
  
  # Fazer a predição
  y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)
  return {
    'pontuacao_teste' : y_pred.tolist()
    }
```

## 📈 Próximos Passos

- Implementar mais variáveis explicativas (regressão múltipla)
- Desenvolver uma interface web para consultas ao modelo
- Explorar modelos não-lineares para comparação
- Implementar sistema de feedback para melhorar o modelo com novos dados

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 👨‍💻 Autor

Matheus Maciel - [GitHub](https://github.com/srmatheusmaciel) - [LinkedIn](https://linkedin.com/in/srmatheusmaciel)
