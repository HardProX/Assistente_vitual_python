import wikipedia
import speech_recognition as sr
from function_Uteis import basicos


def wikipédia(entrada):
    wikipedia.set_lang('pt')
    termo = entrada.split("wikipédia")
    termo_da_pesquisa = termo[1]
    basicos.escreval(f'pesquisando por {termo_da_pesquisa} no wikipédia')
    basicos.reproduzir_voz(f'pesquisando por {termo_da_pesquisa} no wikipédia')
    pesquisa = wikipedia.page(termo_da_pesquisa)
    basicos.escreval(f"Achamos a pagina {pesquisa.title} no wikipédia")
    basicos.reproduzir_voz(f"Achamos a pagina {pesquisa.title} no wikipédia")
    basicos.escreval("Agora estamos buscando o conteúdo dela")
    basicos.reproduzir_voz("Agora estamos buscando o conteúdo dela")
    print(f'Fonte: {pesquisa.url}')
    print(f'{pesquisa.content}')
    basicos.criaArquivos("Pesquisas wikipédia/", f"{pesquisa.title}{basicos.nomeAleatorio()}", "txt", pesquisa.content)
    rec = sr.Recognizer()
    with sr.Microphone() as s:
        basicos.reproduzir_voz("você deseja que eu leia?")
        try:
            voz = rec.listen(s)
            entrada = rec.recognize_google(voz, language="pt")
            entrada = entrada.lower()

            if entrada == "sim":
                basicos.reproduzir_voz(pesquisa.content)
            elif entrada == "não":
                basicos.reproduzir_voz("Modo ler desativado")
                pass
        except sr.UnknownValueError:
            basicos.reproduzir_voz("não entendir o que você disse!")
            basicos.reproduzir_voz("acho melhor digitar!")
            while True:
                reps = str(input('sim|não: ')).strip().lower()
                if reps == "sim":
                    basicos.reproduzir_voz(pesquisa.content)
                elif reps == "não" or reps == "nao":
                    basicos.reproduzir_voz("Modo ler desativado")
                    break
                else:
                    basicos.reproduzir_voz('por favor digite apenas as opção dispoinvies.')
