import speech_recognition as sr
import pyttsx3
from random import randint
from time import sleep
from datetime import datetime
import wikipedia
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from googlesearch import search


#configuração de voz
engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty("voice", voice.id)


def Menu():
    print("-/" * 30)
    print(f"{'MENU':-^60}")
    print("-/" * 30)
    reproduzir_voz("bem vindo! o meu nome é Annabeth!")
    reproduzir_voz("Qual opção o senhor deseja, antes de iniciar o programa? ")
    print("-=" * 15)
    print(f"{'[1]-> MICROFORNE ATIVADO'}")
    print(f"{'[2]-> MICROFORNE DESATIVADO'}")
    print("-=" * 15)
    rec = sr.Recognizer()
    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        try:
            while True:
                voz = rec.listen(s)
                reps = rec.recognize_google(voz, language="pt")
                reps = reps.lower()

                if reps == "primeira opção" or reps == "numero 1":
                    micro = True
                    print(f"{'MICROFORNE ATIVADO':-^30}")
                    reproduzir_voz("Primeira opção ativada")
                    break
                elif reps == "segunda opção" or reps == "numero 2":
                    micro = False
                    print(f"{'MICROFORNE DESATIVADO':-^30}")
                    reproduzir_voz("Segunda opção ativada")
                    break
                else:
                    reproduzir_voz("fale novamente")
        except sr.UnknownValueError:
            reproduzir_voz("não entendir o que você disse!")
            reproduzir_voz("Digite a opção que você deseja: ")
            while True:
                try:
                    reps = int(input('Digite a opção desejada: '))
                    if reps == 1:
                        micro = True
                        print(f"{'MICROFORNE ATIVADO':-^30}")
                        reproduzir_voz("Primeira opção ativada")
                        break
                    elif reps == 2:
                        micro = False
                        print(f"{'MICROFORNE DESATIVADO':-^30}")
                        reproduzir_voz("Segunda opção ativada")
                        break
                    else:
                        reproduzir_voz('por favor digite apenas Números disponiveis.')
                except ValueError:
                    escreval(Exception)
                    reproduzir_voz('por favor Digite somente Números.')
    if micro:
        convesar_annabeth(micro)
    else:
        convesar_annabeth(micro)


def escreval(frase):
    print('~' * (len(frase) + 4))
    print(f' {frase}')
    print('~' * (len(frase) + 4))


def nomeAleatorio():
    ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']
    cont = 0
    nome = ""
    while cont <= 5:
        nome += "" + ABC[randint(0,25)]
        cont+=1
    return nome


def criaArquivos(caminho,nome,extençao, conteudo):
    arquivo = open(f"{caminho}{nome}.{extençao}", "w", encoding="utf-8")
    arquivo.write(conteudo)


def lerArquivos(caminho,nome,extençao):
    arquivo = open(f"{caminho}{nome}.{extençao}", "r")
    conteudo = arquivo.readlines()
    return conteudo


def reproduzir_voz(frase):
    engine.say(frase)
    engine.runAndWait()


def horario(data):
    if data == "hora":
        now = datetime.now()
        hora_de_agora = (f'{now.hour} e {now.minute}')
        return hora_de_agora
    elif data == "data":
        now = datetime.now()
        data_de_hoje = (f'{now.day} do {now.month} de {now.year}')
        return data_de_hoje


def wikipédia(entrada):
    wikipedia.set_lang('pt')
    termo = entrada.split("wikipédia")
    termo_da_pesquisa = termo[1]
    escreval(f'pesquisando por {termo_da_pesquisa} no wikipédia')
    reproduzir_voz(f'pesquisando por {termo_da_pesquisa} no wikipédia')
    pesquisa = wikipedia.page(termo_da_pesquisa)
    escreval(f"Achamos a pagina {pesquisa.title} no wikipédia")
    reproduzir_voz(f"Achamos a pagina {pesquisa.title} no wikipédia")
    escreval("Agora estamos buscando o conteúdo dela")
    reproduzir_voz("Agora estamos buscando o conteúdo dela")
    print(f'Fonte: {pesquisa.url}')
    print(f'{pesquisa.content}')
    criaArquivos("Pesquisas wikipédia/", f"{pesquisa.title}{nomeAleatorio()}", "txt", pesquisa.content)
    rec = sr.Recognizer()
    with sr.Microphone() as s:
        reproduzir_voz("você deseja que eu leia?")
        try:
            voz = rec.listen(s)
            entrada = rec.recognize_google(voz, language="pt")
            entrada = entrada.lower()

            if entrada == "sim":
                reproduzir_voz(pesquisa.content)
            elif entrada == "não":
                reproduzir_voz("Modo ler desativado")
                pass
        except sr.UnknownValueError:
            reproduzir_voz("não entendir o que você disse!")
            reproduzir_voz("acho melhor digitar!")
            while True:
                reps = str(input('sim|não: ')).strip().lower()
                if reps == "sim":
                    reproduzir_voz(pesquisa.content)
                elif reps == "não" or reps == "nao":
                    reproduzir_voz("Modo ler desativado")
                    break
                else:
                    reproduzir_voz('por favor digite apenas as opção dispoinvies.')


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


def buscar_conteudo_web():
    reproduzir_voz("Qual site voçê deseja que eu procure? ")
    site = str(input("qual site voçê que buscar o conteudo? ")).strip().lower()
    reproduzir_voz("que conteudo voçê deseja que eu busque?")
    conteudo = str(input('o que voçê quer buscar? ')).strip().lower()
    reproduzir_voz("Qual a quantidade maxima de links sugeridos? ")
    maxlinks = int(input("quantidade maxima de links: "))

    listas_links = []
    print("-=" * 30)
    print(f"{'Menu links':-^60}")
    print('=' * 60)
    for resultado in search(f'"{conteudo}" {site}', stop=maxlinks):
        listas_links.append(resultado)
    for id, link in enumerate(listas_links):
        print(f'[{id}] -> {link}')
    reproduzir_voz("qual link voçê deseja que eu abra? ")
    while True:
        reps = int(input("digite 999 para sair: "))
        if reps == 999:
            break
        if reps > len(listas_links):
            reproduzir_voz("Digite apenas numeros validos")
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(listas_links[reps])
    print("-=" * 30)


def convesar_annabeth(micro):
    rec = sr.Recognizer()

    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        reproduzir_voz("eu estou pronta para ser usada")
        while True:
            try:
                if micro:
                    voz = rec.listen(s)
                    entrada = rec.recognize_google(voz, language="pt")
                    entrada = entrada.lower()
                    escreval(f'voçê disse: {entrada}')
                    reproduzir_voz(f"voçê disse {entrada}")
                elif not micro:
                    entrada = str(input('Digite alguma coisa: ')).strip().lower()
                    reproduzir_voz(f"voçê disse {entrada}")

                if "horas" in entrada or "hora" in entrada:
                    reproduzir_voz(horario("hora"))
                    escreval(horario("hora"))
                elif "data" in entrada:
                    reproduzir_voz(horario("data"))
                    escreval(horario("data"))
                elif "wikipédia" in entrada:
                    wikipédia(entrada)
                elif "abrir" in entrada and "página" in entrada:
                    p = entrada.split()
                    pagina = p[-1]
                    reproduzir_voz(f"abrindo a pagina {pagina}!")
                    abir_paginas_web(pagina)
                elif entrada == "buscar conteúdo na web":
                    buscar_conteudo_web()
                elif "modo" in entrada and "espera" in entrada:
                    lista = entrada.split()
                    reproduzir_voz(f"modo espera definido para {lista[-2]} segundos")
                    sleep(int(lista[-2]))
                elif "modo" in entrada and "saída" in entrada:
                    reproduzir_voz("Fechando o programa!, foi um prazer atendê-lo!")
                    break
                else:
                    print('Ainda não tenho uma resposta para a sua frase!')
                    reproduzir_voz("Ainda não tenho uma resposta para a sua frase!")
            except sr.UnknownValueError:
                escreval(f"Annabeth-> Eu não entendi o que foi dito")
                reproduzir_voz("Eu não entendi o que foi dito")
