from time import sleep
from random import randint

turno = 0
carga_watergun = 5
carga_barrier = 1
carga_poisonjab = 2
defesa_tentacruel = 0
hp_tentacruel = hp_pikachu = 200
cont_envenenamento = cont_escudo = cont_stun = cont_cd = stack_envenenamento = 0
dano_pikachu = 27
dano_tentacruel = 25
dano_jabpoison = 0
non_stun = True
cd_stun = escudo = False

while True:
    turno += 1
    print(f'\033[1;36m{f"TURNO {turno}":>^116}\033[m')
    sleep(1)
    if turno % 5 == 0:
        if carga_watergun < 5:
            carga_watergun += 1
        if carga_poisonjab < 2:
            carga_poisonjab += 1
    if turno % 7 == 0:
        if carga_barrier < 1:
            carga_barrier += 1

    if non_stun:
        while True:
            print('Ações: ')
            if carga_watergun > 0:
                print(f'\033[1;36m{"[digite (1)] water gun":<23}\033[m', end='')
            else:
                print(f'\033[1;31m{"[Recarga] Tackle":<23}\033[m', end='')
            if carga_barrier > 0 and escudo == False:
                print(f'\033[1;32m{"[digite (2)] Barrier":<40}\033[m', end='')
            else:
                print(f'\033[1;31m{"[Recarga] Barrier":<40}\033[m', end='')
            if carga_poisonjab > 0:
                print(f'\033[1;35m{"[digite (3)] Poison Jab"}\033[m')
            else:
                print(f'\033[1;31m{"[Recarga] Poison Jab"}\033[m')

            print(f'{f"Causa {dano_tentacruel} de dano":<23}', end='')
            print(f'{"Recebe +10 de defesa por 3 turnos":<40}', end='')
            print(f'{"Causa um danos entre 13 a 29 e envenenamento por 3 turnos"}')

            print(f'Carga: {carga_watergun:<16}', end='')
            print(f'Carga: {carga_barrier:<33}', end='')
            print(f'Carga: {carga_poisonjab}')

            escolha = str(input('Escolha a ação: '))
            if escolha == '1' and carga_watergun == 0:
                print(' ')
                print('\033[1;31mHabilidade recarregando, tente outra!\033[m')
            elif escolha == '2' and carga_barrier == 0:
                print('\033[1;31mHabilidade recarregando, tente outra!\033[m')
                print(' ')
            elif escolha == '2' and escudo:
                print('\033[1;31mHabilidade em uso, tente outra!\033[m')
                print(' ')
            elif escolha == '3' and carga_poisonjab == 0:
                print(' ')
                print('\033[1;31mHabilidade recarregando, tente outra!\033[m')
            elif escolha == '1' or escolha == '2' or escolha == '3':
                break
            elif escolha != '1' or escolha != '2' or escolha != '3':
                print(' ')
                print('\033[1;31mOpção inválida, tente outra!\033[m')

        if escolha == '1':
            hp_pikachu -= dano_tentacruel
            carga_watergun -= 1
            print('\033[1;34m-\033[m' * 117)
            print(f'tentacruel causa \033[1;31m{dano_tentacruel}\033[m de dano!')
            if hp_pikachu > 0:
                print(f'HP do pikachu: \033[1;32m{hp_pikachu}\033[m')
            else:
                print(f'HP do pikachu: \033[1;32m0\033[m')
            print('\033[1;34m-\033[m' * 117)
            sleep(1)

        elif escolha == '2':
            carga_barrier -= 1
            cont_escudo = 3
            defesa_tentacruel += 10
            print('\033[1;34m-\033[m' * 117)
            print(f'defesa do tentacruel sobe para \033[1;34m{defesa_tentacruel}!')
            print('\033[1;34m-\033[m' * 117)
            escudo = True
            sleep(1)

        if escolha == '3':
            stack_envenenamento += 1
            carga_poisonjab -= 1
            if cont_envenenamento == 0:
               cont_envenenamento = 3
            print('\033[1;34m-\033[m' * 117)
            for c in range(1):
                if hp_pikachu > 0:
                    dano_jabpoison = randint(13, 29)
                    hp_pikachu -= dano_jabpoison
                print(f'{c}° veneno causa \033[1;31m{dano_jabpoison}\033[m!')
                sleep(0.7)
            if hp_pikachu > 0:
                print(f'HP do pikachu: \033[1;32m{hp_pikachu}\033[m')
            else:
                print(f'HP do pikachu: \033[1;32m0\033[m')
            print('\033[1;34m-\033[m' * 117)

    if cont_escudo > 0:
        cont_escudo -= 1
    elif cont_escudo == 0:
        defesa_tentacruel = 0
        escudo = False

    if cont_envenenamento > 0:
        if hp_pikachu > 0:
            hp_pikachu -= 5 * stack_envenenamento
            cont_envenenamento -= 1
            print('\033[1;35m-\033[m' * 117)
            print('O pikachu recebe dano por \033[1;35menvenenamento\033[m!')
            if hp_pikachu > 0:
                print(f'HP do pikachu: \033[1;32m{hp_pikachu}\033[m')
            else:
                print(f'HP do pikachu: \033[1;32m0\033[m')
            print('\033[1;35m-\033[m' * 117)
        sleep(1)
    elif cont_envenenamento == 0:
        stack_envenenamento = 0

    if hp_pikachu <= 0:
        print('\033[1;32mParabéns, tentacruel Wins!\033[m')
        break

    if not cd_stun:
        escolhamonstro = randint(1, 2)
    else:
        escolhamonstro = randint(1, 1)

    if escolhamonstro == 1:
        dano_pikachu -= defesa_tentacruel
        hp_tentacruel -= dano_pikachu
        print('\033[1;31m-\033[m' * 117)
        print(f'O pikachu usa ataque rapido e te causa \033[1;31m{dano_pikachu}\033[m de dano!')
        if hp_tentacruel > 0:
            print(f'HP do Tentacruel: \033[1;32m{hp_tentacruel}\033[m')
        else:
            print(f'HP do Tentacruel: \033[1;32m0\033[m')
        print('\033[1;31m-\033[m' * 117)
        sleep(1)
        dano_pikachu = 27

    if escolhamonstro == 2:
        non_stun = False
        cd_stun = True
        cont_cd = 5
        print('\033[1;31m-\033[m' * 117)
        print('O pikachu usa \033[1;33;40mThunder Wave\033[m e te paralisa por 2 turnos!')
        print('\033[1;31m-\033[m' * 117)
        sleep(1)
        cont_stun = 2
    if cont_cd > 0:
        cont_cd -= 1
    elif cont_cd == 0:
        cd_stun = False

    if cont_stun == 0:
        non_stun = True
    elif cont_stun <= 2:
        cont_stun -= 1

    if hp_tentacruel <= 0:
        print('\033[1;31mPikachu wins, voce perdeu!\033[m')
        break