from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Cargar el modelo en español
generador = pipeline("text-generation", model="distilgpt2")

# Definir esquema de entrada
class PromptInput(BaseModel):
    prompt: str

@app.post("/generar_texto")
def generar_texto(input: PromptInput):
    resultado = generador(input.prompt, max_length=100, num_return_sequences=1)
    respuesta = resultado[0]['generated_text']
    return {"respuesta": respuesta}
