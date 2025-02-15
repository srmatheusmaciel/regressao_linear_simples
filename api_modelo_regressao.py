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