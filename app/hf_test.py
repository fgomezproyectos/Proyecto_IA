from transformers import pipeline

# Crear el generador de texto
generador = pipeline("text-generation", model="datificate/gpt2-small-spanish")

# Texto inicial para probar
entrada = "Bien hecho!"

# Generar texto
resultados = generador(entrada, max_length=50, num_return_sequences=1)

# Mostrar resultado
for i, resultado in enumerate(resultados):
    print(f"Resultado {i+1}: {resultado['generated_text']}")
