import json
import sys

import requests

URL_ALL = 'https://restcountries.eu/rest/v2/all'
URL_NAME = 'https://restcountries.eu/rest/v2/name'


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print(f'Erro ao fazer requisição em: {url}')
    except Exception as error:
        print(f'{error} - Erro ao fazer requisição em: {url}')


def parsing(texto_resposta):
    try:
        return json.loads(texto_resposta)
    except:
        print('Erro ao fazer parsing')


def contagem_de_paises():
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)


def listar_paises(lista_de_paises):
    for n, pais in enumerate(lista_de_paises):
        print(n, pais['name'])


def mostrar_populacao(nome_do_pais):
    resposta = requisicao(f'{URL_NAME}/{nome_do_pais}')
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            primeiro_pais = lista_de_paises[0]
            print(f'{primeiro_pais["name"]}: {primeiro_pais["population"]}')
        else:
            print('País não encontrado!')


def mostrar_populacao_mundo():
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            populacao_total = 0
            for pais in lista_de_paises:
                populacao_total += int(pais['population'])
            print(f'Atualmente possuí {populacao_total} pessoas no mundo!')


def mostrar_moedas(nome_do_pais):
    resposta = requisicao(f'{URL_NAME}/{nome_do_pais}')
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            primeiro_pais = lista_de_paises[0]
            print(f'{primeiro_pais["name"]}: ', end='')
            for moedas in primeiro_pais["currencies"]:
                if moedas == primeiro_pais['currencies'][-1]:
                    print(f'{moedas["name"]} - {moedas["code"]}')
                else:
                    print(f'{moedas["name"]} - {moedas["code"]}', end=', ')
        else:
            print('País não encontrado!')


def ler_nome_pais():
    try:
        nome_pais = sys.argv[2]
        return nome_pais
    except:
        print('É preciso passar o nome do país')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('### Bem vindo ao sistema de países ###')
        print('Uso: python paises.py <ação> <nome do país>')
        print('Ações disponíveis: contagem, moeda, populacao, populacao_mundo')
    else:
        argumento1 = sys.argv[1]

        if argumento1 == 'contagem':
            print(f'Existem {contagem_de_paises()} países no mundo!')
        elif argumento1 == 'moeda':
            pais = ler_nome_pais()
            if pais:
                mostrar_moedas(ler_nome_pais())
        elif argumento1 == 'populacao':
            pais = ler_nome_pais()
            if pais:
                mostrar_populacao(ler_nome_pais())
        elif argumento1 == 'populacao_mundo':
            mostrar_populacao_mundo()
        else:
            print('Argumento inválido')


