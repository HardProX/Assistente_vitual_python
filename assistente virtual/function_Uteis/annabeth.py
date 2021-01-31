import speech_recognition as sr
import os
from function_Uteis import basicos
from function_Uteis import wikipedia
from function_Uteis import pesquisa_web
from function_Uteis import play_musica


def convesar_annabeth(micro=True):
    basicos.reproduzir_voz("olá, meu nome é Annabeth!")
    basicos.reproduzir_voz("Estarei lhe ajudando quando você precisar")
    rec = sr.Recognizer()

    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        print('-' * 40)
        print('[1] => "\033[35mannabeth iniciar\033[m" ')
        print('[2] => "\033[35mconfiguração do microforne\033[m" ')
        print('[3] => "\033[35mencerrar programa\033[m" ')
        print('[4] -> "\033[35mmostrar menu novamente\033[m" ')
        print('-' * 40)
        basicos.reproduzir_voz("este é o menu das opções disponíveis!")
        basicos.reproduzir_voz('fale a opção desejada!')
        while True:
            try:
                voz = rec.listen(s)
                inicialização = rec.recognize_google(voz, language="pt")
                inicialização.lower()
            except sr.UnknownValueError:
                basicos.escreval('\033[1;31mnão entedir o que foi dito\033[m')
            else:
                basicos.escreval(f'\033[1;30mvoçê disse: {inicialização}\033[m')
                if inicialização == 'encerrar programa':
                    basicos.reproduzir_voz("encerrando o programa!, foi um prazer atendê-lo!")
                    break
                elif inicialização == "mostrar menu novamente":
                    print('-' * 40)
                    print('[1] => "\033[35mannabeth iniciar\033[m" ')
                    print('[2] => "\033[35mconfiguração do microforne\033[m" ')
                    print('[3] => "\033[35mencerrar programa\033[m" ')
                    print('[4] -> "\033[35mmostrar menu novamente\033[m" ')
                    print('-' * 40)
                elif inicialização == "configuração do microfone":
                    basicos.reproduzir_voz("Qual opção o senhor deseja?")
                    print("-=" * 15)
                    print(f"\033[33m{'[1]-> MICROFORNE ATIVADO'}\033[m")
                    print(f"\033[31m{'[2]-> MICROFORNE DESATIVADO'}\033[m")
                    print("-=" * 15)
                    try:
                        while True:
                            voz = rec.listen(s)
                            reps = rec.recognize_google(voz, language="pt")
                            reps = reps.lower()

                            if reps == "primeira opção" or reps == "numero 1" or reps == 'microforne ativado':
                                micro = True
                                print(f"\033[33m{'MICROFORNE ATIVADO':-^30}\033[m")
                                basicos.reproduzir_voz("MICROFORNE ATIVADO")
                                break
                            elif reps == "segunda opção" or reps == "numero 2" or reps == 'microforne desativado':
                                micro = False
                                print(f"\033[31m{'MICROFORNE DESATIVADO':-^30}\033[m")
                                basicos.reproduzir_voz("MICROFORNE DESATIVADO")
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
                                    print(f"\033[33m{'MICROFORNE ATIVADO':-^30}\033[m")
                                    basicos.reproduzir_voz("Primeira opção ativada")
                                    break
                                elif reps == 2:
                                    micro = False
                                    print(f"\033[31m{'MICROFORNE DESATIVADO':-^30}\033[m")
                                    basicos.reproduzir_voz("Segunda opção ativada")
                                    break
                                else:
                                    basicos.reproduzir_voz('por favor digite apenas Números disponiveis.')
                            except ValueError:
                                basicos.reproduzir_voz('por favor Digite somente Números.')
                elif inicialização == "Annabeth iniciar":
                    basicos.reproduzir_voz("iniciando")
                    basicos.reproduzir_voz("eu estou pronta para ser usada")
                    print('-' * 40)
                    print('[1] => "\033[35mqual o horário atual?\033[m" ')
                    print(f'[2] => "\033[35mwikipédia {"pesquisa"}\033[m" ')
                    print(f'[3] => "\033[35mabrir página web\033[m" ')
                    print(f'[4] => "\033[35mprocurar conteúdo na web\033[m" ')
                    print(f'[5] => "\033[35mabrir playlist de músicas\033[m" ')
                    print('[6] -> "\033[35mmostrar menu novamente\033[m" ')
                    print('[7] -> "\033[35mlimpe a tela\033[m" ')
                    print('[8] -> "\033[35msair deste modo\033[m" ')
                    print('-' * 40)
                    while True:
                        try:
                            if micro:
                                voz = rec.listen(s)
                                entrada = rec.recognize_google(voz, language="pt")
                                entrada = entrada.lower()
                                basicos.escreval(f'\033[1;32mvoçê disse: {entrada}\033[m')
                                basicos.reproduzir_voz(f"voçê disse {entrada}")
                            elif not micro:
                                entrada = str(input('Digite alguma coisa: ')).strip().lower()
                                basicos.reproduzir_voz(f"voçê disse {entrada}")

                            if "horas" in entrada or "hora" in entrada or "data" in entrada or "horário" in entrada:
                                horaHorario = basicos.horario("hora") + "-" + basicos.horario("data")
                                basicos.reproduzir_voz(horaHorario)
                                basicos.escreval(horaHorario)
                            elif "wikipédia" in entrada and len(entrada) >= 2:
                                wikipedia.wikipédia(entrada)
                            elif "abrir" in entrada and "página" in entrada:
                                pesquisa_web.abir_paginas_web()
                            elif entrada == "procurar conteúdo na web":
                                pesquisa_web.buscar_conteudo_web()
                            elif "abrir" in entrada and "músicas" in entrada:
                                play_musica.reproduzir_musica()
                            elif entrada == "sair deste modo":
                                basicos.reproduzir_voz('saindo...')
                                break
                            elif entrada == "limpe a tela":
                                os.system('cls') or None
                            elif entrada == "mostrar menu novamente":
                                print('-' * 40)
                                print('[1] => "\033[35mqual o horário atual?\033[m" ')
                                print(f'[2] => "\033[35mwikipédia {"pesquisa"}\033[m" ')
                                print(f'[3] => "\033[35mabrir página web\033[m" ')
                                print(f'[4] => "\033[35mprocurar conteúdo na web\033[m" ')
                                print(f'[5] => "\033[35mabrir playlist de músicas\033[m" ')
                                print('[6] -> "\033[35mmostrar menu novamente\033[m" ')
                                print('[7] -> "\033[35mlimpe a tela\033[m" ')
                                print('[8] -> "\033[35msair deste modo\033[m" ')
                                print('-' * 40)
                            else:
                                print('\033[1;33mAinda não possuo esse comando!\033[m')
                                basicos.reproduzir_voz("Ainda não possuo esse comando!")
                        except sr.UnknownValueError:
                            basicos.escreval(f"\033[1;31mAnnabeth-> Eu não entendi\033[m")
                            basicos.reproduzir_voz("Eu não entendi o que foi dito")
