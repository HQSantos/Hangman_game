import requests
import os

class GeminiClient:
    def __init__(self):
        # Obtém a chave API da variável de ambiente
        self.api_key = os.environ.get('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("A variável de ambiente GEMINI_API_KEY não está definida.")
        self.model = 'gemini-1.5-flash' 
        self.endpoint = f'https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}'

    def call(self, word):
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
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
        except KeyError:
            print("Erro ao processar a resposta da API.")
            return None

# Exemplo de uso
if __name__ == "__main__":
    client = GeminiClient()
    dica = client.call("exemplo")
    if dica:
        print(f"Dica gerada: {dica}")