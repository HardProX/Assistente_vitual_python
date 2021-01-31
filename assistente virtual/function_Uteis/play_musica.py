from function_Uteis import basicos
from random import randint
import pygame


def reproduzir_musica():
    estilo_musicas = {'rock': [],"pop" : [], "relaxar" : [], "rap" : [], "sads" : []}

    for key in estilo_musicas.keys():
        songs = basicos.lerArquivos(f'../../../musicas/{key}/',f'{key} songs','txt')
        lista = []
        for song in songs:
            lista.append(song.rstrip("\n"))
        estilo_musicas[f'{key}'] = lista

    print('-=' * 30)
    print(f'\033[1;36m{"menu estilos musicais".center(60)}\033[m')
    print('-=' * 30)

    print('-' * 30)
    for key in estilo_musicas.keys():
        print(f'   * {key}')
    print('-' * 30)

    basicos.reproduzir_voz('Aquir estão todas as playlist já criadas')
    basicos.reproduzir_voz('selecione a playlist que voçê deseja')
    nomePlay = str(input('\033[1;37mQual playlist voçê que selecionar? \033[m')).strip().lower()

    if nomePlay in estilo_musicas.keys():
        basicos.reproduzir_voz(f'voçê escolheu a playlist {nomePlay}')
        lista_musicas = []
        for key, musica in estilo_musicas.items():
            if key == nomePlay:
                for i, valor in enumerate(musica):
                    lista_musicas.append(valor)
                    print(f'{i} -> \033[1;37m{valor}\033[m')
        basicos.reproduzir_voz('Escolha entre o modo aleatório ou o modo manual')
        reps = str(input('\033[1;37mmodo aleátorio | modo manual: \033[m')).strip().lower()

        if 'aleátorio' in reps:
            pygame.mixer.init()
            repitido = []
            total_musicas = 0
            while True:
                aleatorio = randint(0, (len(lista_musicas) - 1))
                if total_musicas == len(lista_musicas):
                    break
                if aleatorio not in repitido:
                    musica = lista_musicas[aleatorio]
                    pygame.mixer.music.load(f"../../../musicas/{nomePlay}/{musica}")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    repitido.append(aleatorio)
                    total_musicas += 1
        else:
            pygame.mixer.init()
            lista_musicas_selecionadas = []
            max = int(input('\033[1;37mQuantas musicas voçê quer selecionar? \033[m'))
            for c in range(0, max):
                music = int(input(f'\033[1;37mqual musica deseja colocar na posição {c}° ? \033[m'))
                lista_musicas_selecionadas.append(music)
            for c in range(0, max):
                musica = lista_musicas[lista_musicas_selecionadas[c]]
                pygame.mixer.music.load(f"../../../musicas/{nomePlay}/{musica}")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
    else:
        basicos.reproduzir_voz('Essa playlist não existe, ou pelo menos não ainda')
    print('\033[7mPLAYLIST ENCERRADA!\033[m')
    print('-=' * 30)
