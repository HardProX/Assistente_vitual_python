from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from googlesearch import search
from function_Uteis import basicos


def buscar_conteudo_web():
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
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(listas_links[reps])
    print("-=" * 30)


def abir_paginas_web(pagina):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    if pagina == "whatsapp":
        driver.get('https://web.whatsapp.com/')
    elif pagina == "google":
        driver.get('https://www.google.com/')
    elif pagina == "facebook":
        driver.get('https://www.facebook.com/')
    elif pagina == 'github':
        driver.get('https://github.com/')
    elif pagina == "youtube":
        driver.get('https://www.youtube.com/')

