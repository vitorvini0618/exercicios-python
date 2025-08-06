def somar (n1, n2):  
    soma = n1 + n2
    return soma

resultado_soma = somar(1232328, 2128)
resultado_de_outra_soma = somar(12, 2)
#print(f'tivemos o resultado da primeira soma, {resultado_soma}, e tambem o da segunda soma {resultado_de_outra_soma}')

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def somar_lista(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

def calcular_media(*numeros):
    qtd = len(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    media = soma / qtd
    return media

#resultado_da_media = calcular_media(3, 5, 6)
#media_redonda = round(resultado_da_media, 2)
#print(f'a media é {media_redonda}')

def informacoes_pessoais(**informacoes):
    for chave, valor in informacoes.items():
        print(f"{chave} : {valor}")

#informacoes_pessoais(nome='Vitor', idade=18 , sexo='masculino' , altura=1.8)

def saudacao(nome):
    print(f'Prazer {nome}')


def contador_menos(numero):
    while True:
        print(numero)
        numero -= 1
        if numero < 0:
            break

def contador_menos2(numero):
    for i in range(numero, 0, -1):
        print(i)

def maior_numero(lista_de_numeros):
    maior_numero = lista_de_numeros[0]
    for numero in lista_de_numeros:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

lista = [12, 23, 2, 3, 9]
maior_numero_da_lista = maior_numero(lista)

def maior_numero2(lista_de_numeros):
    maior_numero2 = max(lista_de_numeros)
    return maior_numero2

#lista = [12, 232, 2, 3000, 900]
#maior_numero_da_lista = maior_numero2(lista)
#print(maior_numero_da_lista)