from function_Uteis import basicos
from random import randint
import pygame


def reproduzir_musica():
    estilo_musicas = {'rock': [],"pop" : [], "relaxar" : [], "rap" : [], "sads" : []}
    songs_rock = basicos.lerArquivos('musicas/rock/','rock songs','txt')
    songs_pop = basicos.lerArquivos('musicas/pop/','pop songs','txt')
    songs_relaxar = basicos.lerArquivos('musicas/relaxar/', 'relaxar songs', 'txt')
    songs_rap = basicos.lerArquivos('musicas/rap/', 'rap songs', 'txt')
    songs_sads = basicos.lerArquivos('musicas/sads/', 'sads songs', 'txt')
    lista = []
    for song in songs_rock:
        lista.append(song.rstrip("\n"))
    estilo_musicas['rock'] = lista
    lista = []
    for song in songs_pop:
        lista.append(song.rstrip("\n"))
    estilo_musicas['pop'] = lista
    lista = []
    for song in songs_relaxar:
        lista.append(song.rstrip("\n"))
    estilo_musicas['relaxar'] = lista
    lista = []
    for song in songs_rap:
        lista.append(song.rstrip("\n"))
    estilo_musicas['rap'] = lista
    lista = []
    for song in songs_sads:
        lista.append(song.rstrip("\n"))
    estilo_musicas['sads'] = lista

    print('-=' * 30)
    print(f'{"menu estilos musicais".center(60)}')
    print('-=' * 30)

    print('-' * 30)
    for key in estilo_musicas.keys():
        print(f'   * {key}')
    print('-' * 30)

    basicos.reproduzir_voz('Aquir estão todas as playlist criadas')
    basicos.reproduzir_voz('selecione a playlist que voçê deseja')
    reps = str(input('Qual playlist voçê que selecionar? ')).strip().lower()

    if reps == 'rock':
        basicos.reproduzir_voz(f'voçê escolheu a playlist {reps}')
        lista_musicas = []
        for key, musica in estilo_musicas.items():
            if key == 'rock':
                for i, valor in enumerate(musica):
                    lista_musicas.append(valor)
                    print(f'{i} -> {valor}')
        basicos.reproduzir_voz('Escolha entre o modo aleatório ou o modo manual')
        reps = str(input('modo aleatorio | modo manual: ')).strip().lower()

        if 'aleatorio' in reps:
            pygame.mixer.init()
            repitido = 999
            total_musicas = 0
            while True:
                aleatorio = randint(0, (len(lista_musicas) - 1))
                if total_musicas == len(lista_musicas):
                    break
                if aleatorio != repitido:
                    musica = lista_musicas[aleatorio]
                    pygame.mixer.music.load(f"../musicas/rock/{musica}")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    repitido = aleatorio
                    total_musicas += 1
        else:
            pygame.mixer.init()
            lista_musicas_selecionadas = []
            max = int(input('Quantas musicas voçê quer selecionar? '))
            for c in range(0, max):
                music = int(input(f'qual musica deseja colocar na posição {c}° ? '))
                lista_musicas_selecionadas.append(music)
            for c in range(0, max):
                musica = lista_musicas[lista_musicas_selecionadas[c]]
                pygame.mixer.music.load(f"../musicas/rock/{musica}")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
    elif reps == 'pop':
        basicos.reproduzir_voz(f'voçê escolheu a playlist {reps}')
        lista_musicas = []
        for key, musica in estilo_musicas.items():
            if key == 'pop':
                for i, valor in enumerate(musica):
                    lista_musicas.append(valor)
                    print(f'{i} -> {valor}')
        basicos.reproduzir_voz('Escolha entre o modo aleatório ou o modo manual')
        reps = str(input('modo aleatorio | modo manual: ')).strip().lower()

        if 'aleatorio' in reps:
            pygame.mixer.init()
            repitido = 999
            total_musicas = 0
            while True:
                aleatorio = randint(0, (len(lista_musicas) - 1))
                if total_musicas == len(lista_musicas):
                    break
                if aleatorio != repitido:
                    musica = lista_musicas[aleatorio]
                    pygame.mixer.music.load(f"../musicas/pop/{musica}")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    repitido = aleatorio
                    total_musicas += 1
        else:
            pygame.mixer.init()
            lista_musicas_selecionadas = []
            max = int(input('Quantas musicas voçê quer selecionar? '))
            for c in range(0, max):
                music = int(input(f'qual musica deseja colocar na posição {c}° ? '))
                lista_musicas_selecionadas.append(music)
            for c in range(0, max):
                musica = lista_musicas[lista_musicas_selecionadas[c]]
                pygame.mixer.music.load(f"../musicas/pop/{musica}")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
    elif reps == 'relaxar':
        basicos.reproduzir_voz(f'voçê escolheu a playlist {reps}')
        lista_musicas = []
        for key, musica in estilo_musicas.items():
            if key == 'relaxar':
                for i, valor in enumerate(musica):
                    lista_musicas.append(valor)
                    print(f'{i} -> {valor}')
        basicos.reproduzir_voz('Escolha entre o modo aleatório ou o modo manual')
        reps = str(input('modo aleatorio | modo manual: ')).strip().lower()

        if 'aleatorio' in reps:
            pygame.mixer.init()
            repitido = 999
            total_musicas = 0
            while True:
                aleatorio = randint(0, (len(lista_musicas) - 1))
                if total_musicas == len(lista_musicas):
                    break
                if aleatorio != repitido:
                    musica = lista_musicas[aleatorio]
                    pygame.mixer.music.load(f"../musicas/relaxar/{musica}")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    repitido = aleatorio
                    total_musicas += 1
        else:
            pygame.mixer.init()
            lista_musicas_selecionadas = []
            max = int(input('Quantas musicas voçê quer selecionar? '))
            for c in range(0, max):
                music = int(input(f'qual musica deseja colocar na posição {c}° ? '))
                lista_musicas_selecionadas.append(music)
            for c in range(0, max):
                musica = lista_musicas[lista_musicas_selecionadas[c]]
                pygame.mixer.music.load(f"../musicas/relaxar/{musica}")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
    elif reps == 'rap':
        basicos.reproduzir_voz(f'voçê escolheu a playlist {reps}')
        lista_musicas = []
        for key, musica in estilo_musicas.items():
            if key == 'rap':
                for i, valor in enumerate(musica):
                    lista_musicas.append(valor)
                    print(f'{i} -> {valor}')
        basicos.reproduzir_voz('Escolha entre o modo aleatório ou o modo manual')
        reps = str(input('modo aleatorio | modo manual: ')).strip().lower()

        if 'aleatorio' in reps:
            pygame.mixer.init()
            repitido = 999
            total_musicas = 0
            while True:
                aleatorio = randint(0, (len(lista_musicas) - 1))
                if total_musicas == len(lista_musicas):
                    break
                if aleatorio != repitido:
                    musica = lista_musicas[aleatorio]
                    pygame.mixer.music.load(f"../musicas/rap/{musica}")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    repitido = aleatorio
                    total_musicas += 1
        else:
            pygame.mixer.init()
            lista_musicas_selecionadas = []
            max = int(input('Quantas musicas voçê quer selecionar? '))
            for c in range(0, max):
                music = int(input(f'qual musica deseja colocar na posição {c}° ? '))
                lista_musicas_selecionadas.append(music)
            for c in range(0, max):
                musica = lista_musicas[lista_musicas_selecionadas[c]]
                pygame.mixer.music.load(f"../musicas/rap/{musica}")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
    elif reps == 'sads':
        basicos.reproduzir_voz(f'voçê escolheu a playlist {reps}')
        lista_musicas = []
        for key, musica in estilo_musicas.items():
            if key == 'pop':
                for i, valor in enumerate(musica):
                    lista_musicas.append(valor)
                    print(f'{i} -> {valor}')
        basicos.reproduzir_voz('Escolha entre o modo aleatório ou o modo manual')
        reps = str(input('modo aleatorio | modo manual: ')).strip().lower()

        if 'aleatorio' in reps:
            pygame.mixer.init()
            repitido = 999
            total_musicas = 0
            while True:
                aleatorio = randint(0, (len(lista_musicas) - 1))
                if total_musicas == len(lista_musicas):
                    break
                if aleatorio != repitido:
                    musica = lista_musicas[aleatorio]
                    pygame.mixer.music.load(f"../musicas/sads/{musica}")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    repitido = aleatorio
                    total_musicas += 1
        else:
            pygame.mixer.init()
            lista_musicas_selecionadas = []
            max = int(input('Quantas musicas voçê quer selecionar? '))
            for c in range(0, max):
                music = int(input(f'qual musica deseja colocar na posição {c}° ? '))
                lista_musicas_selecionadas.append(music)
            for c in range(0, max):
                musica = lista_musicas[lista_musicas_selecionadas[c]]
                pygame.mixer.music.load(f"../musicas/sads/{musica}")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
    else:
        basicos.reproduzir_voz('Essa playlist não existe, ou pelo menos não ainda')
    print('-=' * 30)