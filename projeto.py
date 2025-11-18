#Importação de bibilotecas
import openai
chave_API = #colocar chave de API corretamente

openai.api.key = chave_API

def enviar_mensagem(mensagem, lista_mensagens = []):
    lista_mensagens.append(
        ('role': 'user', 'content': mensagem)
    )
    
    resposta = openai.ChatCompletion.create(
        model = "gpt-4.1", #Verificar o modelo correto e ajustar
        messages = lista_mensagens
        ]
    )
    return resposta['choices'][0]['message']

while True:
    texto = input('Escreva sua mensagem').lower

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto,lista_mensagens)
        lista_mensagens.append(resposta)
        print('Chatbot:', resposta["content"])

print(enviar_mensagem("Em que ano foi criado o primeiro avião"))