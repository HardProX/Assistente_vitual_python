from time import sleep
import speech_recognition as sr
from function_Uteis import basicos
from function_Uteis import wikipedia
from function_Uteis import pesquisa_web


def Menu():
    print("-/" * 30)
    print(f"{'Annabeth - Menu':-^60}")
    print("-/" * 30)
    basicos.reproduzir_voz("bem vindo! o meu nome é Annabeth!")
    basicos.reproduzir_voz("Qual opção o senhor deseja, antes de iniciar o programa? ")
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
                    basicos.reproduzir_voz("Primeira opção ativada")
                    break
                elif reps == "segunda opção" or reps == "numero 2":
                    micro = False
                    print(f"{'MICROFORNE DESATIVADO':-^30}")
                    basicos.reproduzir_voz("Segunda opção ativada")
                    break
                else:
                    basicos.reproduzir_voz("fale novamente")
        except sr.UnknownValueError:
            basicos.reproduzir_voz("não entendir o que você disse!")
            basicos.reproduzir_voz("Digite a opção que você deseja: ")
            while True:
                try:
                    reps = int(input('Digite a opção desejada: '))
                    if reps == 1:
                        micro = True
                        print(f"{'MICROFORNE ATIVADO':-^30}")
                        basicos.reproduzir_voz("Primeira opção ativada")
                        break
                    elif reps == 2:
                        micro = False
                        print(f"{'MICROFORNE DESATIVADO':-^30}")
                        basicos.reproduzir_voz("Segunda opção ativada")
                        break
                    else:
                        basicos.reproduzir_voz('por favor digite apenas Números disponiveis.')
                except ValueError:
                    basicos.reproduzir_voz('por favor Digite somente Números.')
    if micro:
        convesar_annabeth(micro)
    else:
        convesar_annabeth(micro)


def convesar_annabeth(micro):
    rec = sr.Recognizer()

    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        basicos.reproduzir_voz("antes de tudo ative a inicialização")
        while True:
            try:
                voz = rec.listen(s)
                inicialização = rec.recognize_google(voz, language="pt")
                inicialização.lower()
            except sr.UnknownValueError:
                 basicos.escreval('não entedir o que foi dito')
            else:
                basicos.escreval(f'voçê disse: {inicialização}')
                if inicialização == 'Fechar programa':
                    basicos.reproduzir_voz("Fechando o programa!, foi um prazer atendê-lo!")
                    break
                if inicialização == "Annabeth iniciar":
                    basicos.reproduzir_voz("iniciando")
                    basicos.reproduzir_voz("eu estou pronta para ser usada")
                    while True:
                        try:
                            if micro:
                                voz = rec.listen(s)
                                entrada = rec.recognize_google(voz, language="pt")
                                entrada = entrada.lower()
                                basicos.escreval(f'voçê disse: {entrada}')
                                basicos.reproduzir_voz(f"voçê disse {entrada}")
                            elif not micro:
                                entrada = str(input('Digite alguma coisa: ')).strip().lower()
                                basicos.reproduzir_voz(f"voçê disse {entrada}")

                            if "horas" in entrada or "hora" in entrada:
                                basicos.reproduzir_voz(basicos.horario("hora"))
                                basicos.escreval(basicos.horario("hora"))
                            elif "data" in entrada:
                                basicos.reproduzir_voz(basicos.horario("data"))
                                basicos.escreval(basicos.horario("data"))
                            elif "wikipédia" in entrada and len(entrada) >= 2:
                                wikipedia.wikipédia(entrada)
                            elif "abrir" in entrada and "página" in entrada:
                                p = entrada.split()
                                pagina = p[-1]
                                basicos.reproduzir_voz(f"abrindo a pagina {pagina}!")
                                pesquisa_web.abir_paginas_web(pagina)
                            elif entrada == "buscar conteúdo na web":
                                pesquisa_web.buscar_conteudo_web()
                            elif "modo" in entrada and "saída" in entrada:
                                basicos.reproduzir_voz('saindo do modo conversa!')
                                break
                            else:
                                print('Ainda não tenho uma resposta para a sua frase!')
                                basicos.reproduzir_voz("Ainda não tenho uma resposta para a sua frase!")
                        except sr.UnknownValueError:
                            basicos.escreval(f"Annabeth-> Eu não entendi o que foi dito")
                            basicos.reproduzir_voz("Eu não entendi o que foi dito")
