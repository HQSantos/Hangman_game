import requests
import os

class GeminiClient:
    def __init__(self):
        try:
            self.api_key = os.environ.get('GEMINI_API_KEY')
        except Exception:
            print("Erro ao obter a chave da API Gemini. Certifique-se de que a variável de ambiente 'GEMINI_API_KEY' está definida.")
            self.api_key = None
        self.model = 'gemini-1.5-flash' 
        self.endpoint = f'https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}'


    def call(self, word):
        if not self.api_key or not self.endpoint:
            return "Sem dica"
        # Prompt para gerar uma dica no jogo da forca
        prompt = (
            "Você é uma inteligência artificial em um jogo da forca.\n"
            "Dado um termo-alvo, sua tarefa é gerar uma única palavra como dica em português, que esteja relacionada com o termo,\n"
            "ajudando alguém a adivinhar o termo original. A dica deve ser uma dentre essas palavras da lista: Palavras Comuns, Animais, Alimentos, Profissões, \n" 
            "Esportes,Países,Cores,Partes do Corpo,Natureza,Tecnologia,Música,Cinema,Literatura,Ciências,História,Geografia,Arte,Emoções,Tempo,Números (em palavras), Objetos do Cotidiano.\n"
            f"Termo-alvo: {word}\n"
            "Dica:"
        )
        
        # Estrutura da requisição para a API Gemini
        data = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }
        
        # Faz a chamada à API
        try:
            response = requests.post(self.endpoint, json=data)
            response.raise_for_status()  # Levanta erro se a requisição falhar
            result = response.json()
            # Extrai a dica da resposta
            hint = result['candidates'][0]['content']['parts'][0]['text']
            return hint.strip()
        except Exception:
            print("Erro ao chamar a API Gemini, cota atingiu o limite máximo")
            return "Sem dica"

# Exemplo de uso
if __name__ == "__main__":
    client = GeminiClient()
    dica = client.call("exemplo")
    if dica:
        print(f"Dica gerada: {dica}")