from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from googlesearch import search
from function_Uteis import basicos
import pywhatkit


def buscar_conteudo_web():
    basicos.reproduzir_voz('Qual opção de navegador voçê quer selecionar?')
    navegador = str(input('Pessoal || vitual ')).strip().lower()
    if 'pessoal' not in navegador or 'vitual' not in navegador:
        while True:
            if navegador == 'pessoal' or navegador == 'vitual':
                break
            print('Selecione apenas as opções "pessoal" ou "vitual "')
            navegador = str(input('Pessoal? || vitual? ')).strip().lower()
    basicos.reproduzir_voz("Qual site voçê deseja que eu procure? ")
    site = str(input("qual site voçê que buscar o conteudo? ")).strip().lower()
    basicos.reproduzir_voz("que conteudo voçê deseja que eu busque?")
    conteudo = str(input('o que voçê quer buscar? ')).strip().lower()
    basicos.reproduzir_voz("Qual a quantidade maxima de links sugeridos? ")
    maxlinks = int(input("quantidade maxima de links: "))

    listas_links = []
    print("-=" * 30)
    print(f"{'Menu links':-^60}")
    print('=' * 60)
    for resultado in search(f'"{conteudo}" {site}', stop=maxlinks):
        listas_links.append(resultado)
    for id, link in enumerate(listas_links):
        print(f'[{id}] -> {link}')
    basicos.reproduzir_voz("qual link voçê deseja que eu abra? ")
    while True:
        reps = int(input("digite 999 para sair: "))
        if reps == 999:
            break
        if reps >= len(listas_links) or reps < 0:
            basicos.reproduzir_voz("Digite apenas numeros validos")
        else:
            if navegador == 'vitual':
                driver = webdriver.Chrome(ChromeDriverManager().install())
                driver.get(listas_links[reps])
            else:
                pywhatkit.search(listas_links[reps])
    print("-=" * 30)


def abir_paginas_web():
    print('=-' * 20)
    paginas_webs_salvas = {'facebook' : [], 'whatsapp' : [], 'github' : [], 'instagram': []}

    for key in paginas_webs_salvas.keys():
        paginas = basicos.lerArquivos(f'paginas webs/',f'pagina {key}','txt')
        lista = []
        for pagina in paginas:
            lista.append(pagina.rstrip("\n"))
        paginas_webs_salvas[f'{key}'] = lista

    basicos.reproduzir_voz('Aquir estão todas as páginas já registradas')
    basicos.reproduzir_voz('Escolha a que voçê deseja')

    print('-' * 40)
    for key in paginas_webs_salvas.keys():
        print(f'  *{key}*')
    print('-' * 40)

    while True:
        pag = str(input('Qual voçê quer abrir? [digite "exit" para sair] ')).strip().lower()
        if pag == 'exit':
            break
        elif pag in paginas_webs_salvas.keys():
            pywhatkit.search(paginas_webs_salvas[pag][0])
        else:
            print('Ainda não tem essa página cadastrada!')
    print('=-' * 20)
