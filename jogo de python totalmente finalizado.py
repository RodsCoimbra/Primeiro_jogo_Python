
import random
#importar a função que permite ao computador escolher uma opção da lista
print("Este programa é um trabalho no âmbito da disciplina de aplicações informáticas.\nEste jogo consiste num conjunto de minijogos criado por:\n ->João Ferreira nº11 12ºA\n ->Rodrigo Coimbra nº13 12ºA")
regras=0
#A variável "regras" serve apenas para o jogo da forca e é explicada lá. Aqui apenas a definimos como 0.  
jogo="a"
#Definir a variável jogo como "a". 
while jogo=="a":
    #Isto serve para enquanto jogo for igual a "a" ele executar o comando de seleção de jogos.
    jogo=int(input("\nEscolha um dos três minijogos:\n 1->pedra,papel ou tesoura.\n 2->cara ou coroa.\n 3->jogo da forca.\n 4-> Terminar.\n"))
    while jogo>4 or jogo<1:
        #Como só há 4 opções de jogo se "jogo" for um número diferente de 1, 2, 3 ou 4 ele vai dizer que a opção é inválida e vai voltar a pedir para escolher um minijogo.
        print("\nOpção inválido!")
        jogo=int(input("\nEscolha um dos três minijogos:\n ->Escreva 1 para o jogo do pedra, papel ou tesoura.\n ->Escreva 2 para o jogo do cara ou coroa.\n ->Escreva 3 para o jogo da forca.\n"))

        
    while jogo==1:
        #Para executar o pedra, papel ou tesoura se jogo é igual a 1.                             
        lista=("pedra","papel","tesoura")
        #lista com as opções do computador
        pontos_j=0
        #pontos do jogador
        pontos_c=0
        #pontos do computador
        print("Bem vindo ao jogo do pedra, papel ou tesoura. Para vencer tens de jogar:\n ->pedra se o PC escolher tesoura.\n ->tesoura se o PC escolher papel.\n ->papel se o PC escolher pedra.")
        rod=1
        #variável que vai dizer em que rodada o jogador está
        print("\n\nrodada:",rod)
        #Escrever a rodada
        esc=str(input("Escreva pedra, papel ou tesoura(escreva fim se quiser acabar)")).lower().strip()
        #esc é a escolha que o jogador faz, esta torna-se sempre uma letra minúscula indepentemente como o jogador escrever 

        while esc!="fim":
            #Enquanto a escolha do jogador for diferente de fim ele vai executar o jogo
            cpu=random.choice(lista)
            #cpu é a escolha que o computador faz
            if esc=="pedra":
                if cpu=="papel":
                    #Caso em que o jogador escolhe pedra e o computador papel
                    pontos_c+=1
                    #Adição de um ponto ao computador, porque o jogador perdeu esta rodada
                    print("Tu perdeste porque",cpu,"embrulha",esc,"!")
                    print("Pontuação: J-",pontos_j,"PC-",pontos_c,)
                    #Escrever quem venceu esta rodada e escrever as respetivas pontuações
                    rod+=1
                    #Adição de 1 à rodada.
                    print("\n\nrodada:",rod)
                    #Escrever a rodada
                    esc=str(input("Escreva pedra, papel ou tesoura(escreva fim se quiser acabar)").lower().strip())
                    #É a escolha que o jogador faz para a próxima rodada, esta torna-se sempre uma letra minúscula indepentemente como o jogador escrever
                elif cpu=="pedra":
                    #Caso em que o jogador escolhe pedra e o computador também
                    print("Tu empataste porque",esc,"anula",cpu,"!")
                    print("Pontuação: J-",pontos_j,"PC-",pontos_c,)
                    #Escrever que houve uma empate nesta rodada e escrever as respetivas pontuações
                    rod+=1
                    #Adição de 1 à rodada.
                    print("\n\nrodada:",rod)
                    #Escrever a rodada
                    esc=str(input("Escreva pedra, papel ou tesoura(escreva fim se quiser acabar)")).lower().strip()
                    #É a escolha que o jogador faz para a próxima rodada, esta torna-se sempre uma letra minúscula indepentemente como o jogador escrever
                elif cpu=="tesoura":
                    #Caso em que o jogador escolhe pedra e o computador tesoura                                                            
                    pontos_j+=1
                    #Adição de um ponto ao jogador, porque venceu esta rodada
                    print("Tu ganhaste porque",esc,"parte",cpu,"!")
                    print("Pontuação: J-",pontos_j,"PC-",pontos_c,)
                    #Escrever a quem venceu esta rodada e escrever as respetivas pontuações
                    rod+=1
                    #Adição de 1 à rodada.
                    print("\n\nrodada:",rod)
                    #Escrever a rodada
                    esc=str(input("Escreva pedra, papel ou tesoura(escreva fim se quiser acabar)")).lower().strip()
                    #É a escolha que o jogador faz para a próxima rodada, esta torna-se sempre uma letra minúscula indepentemente como o jogador escrever
            elif esc=="papel":
                #o resto das opções são iguais à primeira, diferindo apenas na escolha do jogador.
                 if cpu=="tesoura":
                    pontos_c+=1
                    print("Tu perdeste porque",cpu,"corta",esc,"!")
                    print("Pontuação: J-",pontos_j,"PC-",pontos_c,)
                    rod+=1
                    print("\n\nrodada:",rod)
                    esc=str(input("Escreva pedra, papel ou tesoura(escreva fim se quiser acabar)")).lower().strip()
                 elif cpu=="papel":
                    print("Tu empataste porque",esc,"anula",cpu,"!")
                    print("Pontuação: J-",pontos_j,"PC-",pontos_c,)
                    rod+=1
                    print("\n\nrodada:",rod)
                    esc=str(input("Escreva pedra, papel ou tesoura(escreva fim se quiser acabar)")).lower().strip()
                 elif cpu=="pedra":                                                           
                    pontos_j+=1
                    print("Tu ganhaste porque",esc,"embrulha",cpu,"!")
                    print("Pontuação: J-",pontos_j,"PC-",pontos_c,)
                    rod+=1
                    print("\n\nrodada:",rod)
                    esc=str(input("Escreva pedra, papel ou tesoura(escreva fim se quiser acabar)")).lower().strip()
            elif esc=="tesoura":
                #o resto das opções são iguais à primeira, diferindo apenas na escolha do jogador.
                 if cpu=="pedra":
                    pontos_c+=1
                    print("Tu perdeste porque",cpu,"parte",esc,"!")
                    print("Pontuação: J-",pontos_j,"PC-",pontos_c,)
                    rod+=1
                    print("\n\nrodada:",rod)
                    esc=str(input("Escreva pedra, papel ou tesoura(escreva fim se quiser acabar)")).lower().strip()
                 elif cpu=="tesoura":
                    print("Tu empataste porque",esc,"anula",cpu,"!")
                    print("Pontuação: J-",pontos_j,"PC-",pontos_c,)
                    rod+=1
                    print("\n\nrodada:",rod)
                    esc=str(input("Escreva pedra, papel ou tesoura(escreva fim se quiser acabar)")).lower().strip()
                 elif cpu=="papel":                                                           
                    pontos_j+=1
                    print("Tu ganhaste porque",esc,"corta",cpu,"!")
                    print("Pontuação: J-",pontos_j,"PC-",pontos_c,)
                    rod+=1
                    print("\n\nrodada:",rod)
                    esc=str(input("Escreva pedra, papel ou tesoura(escreva fim se quiser acabar)")).lower().strip()
            else:
                #caso em que a jogador não escreve pedra, papel ou tesoura
                print("Palavra inválida, confirme se escreveu se escreveu a palavra correta.")
                esc=str(input("\n\nEscreva pedra, papel ou tesoura(escreva fim se quiser acabar)")).lower().strip()
                #Pedir a escolha do jogador de novo, esta torna-se sempre uma letra minúscula indepentemente como o jogador escrever
        print("\nFim, a pontuação foi",pontos_j,"para o jogador foi",pontos_c,"para o computador.")
        #Caso em que o jogador escreve "fim" o programa escreve fim e a respetivas pontuações.
        jogo = "a"
        #Definir jogo de novo como "a" para voltar para o menu de seleção de minijogo

        
    while jogo==2:
        #Para executar o cara ou coroa se jogo é igual a 2.   
        lista2=("cara","coroa")
        #lista com as opções do computador
        pontos_j2=0
        #pontos do jogador
        print("Bem vindo ao jogo do cara ou coroa. Para vencer tem de te calhar o mesmo que escolheste.")
        rod2=1
        #variável que vai dizer em que rodada o jogador está
        print("\nrodada:",rod2)
        #Escrever a rodada
        esc2=str(input("Escreva cara ou coroa(escreva fim se quiser acabar)")).lower().strip()
        #esc2 é a escolha que o jogador faz, esta torna-se sempre uma letra minúscula indepentemente como o jogador escrever
        while esc2!="fim":
            #Enquanto a escolha do jogador for diferente de fim ele vai executar o jogo
            cpu2=random.choice(lista2)
            #cpu2 é a escolha que o computador faz
            if esc2=="cara":
                if cpu2=="coroa":
                    #Caso em que o jogador escolhe cara e o computador coroa
                    print("Tu perdeste porque calhou",cpu2,"!")
                    print("Pontuação: J-",pontos_j2,".")
                    #Escrever que o jogador perdeu esta rodada e escrever sua pontuação
                    rod2+=1
                    #Adição de 1 à rodada
                    print("\n\nrodada:",rod2)
                    #Escrever a rodada
                    esc2=str(input("Escreva cara ou coroa(escreva fim se quiser acabar)")).lower().strip()
                    #É a escolha que o jogador faz para a próxima rodada, esta torna-se sempre uma letra minúscula indepentemente como o jogador escrever
                else:
                    #Caso em que o jogador escolhe cara e o computador também
                    print("Tu ganhaste porque calhou",cpu2,"!")
                    #Escrever que o jogador ganhou esta rodada
                    pontos_j2+=1
                    #Adição de um ponto ao jogador, porque venceu esta rodada
                    print("Pontuação: J-",pontos_j2,".")
                    #Escrever a pontuação do jogador
                    rod2+=1
                    #Adição de 1 à rodada
                    print("\n\nrodada:",rod2)
                    #Escrever a rodada
                    esc2=str(input("Escreva cara ou coroa(escreva fim se quiser acabar)")).lower().strip()
                    #É a escolha que o jogador faz para a próxima rodada
            elif esc2=="coroa":
                #o resto das opções são iguais à primeira, diferindo apenas na escolha do jogador.
                if cpu2=="coroa":
                    print("Tu ganhaste porque calhou",cpu2,"!")
                    pontos_j2+=1
                    print("Pontuação: J-",pontos_j2,".")
                    rod2+=1
                    print("\n\nrodada:",rod2)
                    esc2=str(input("Escreva cara ou coroa(escreva fim se quiser acabar)")).lower().strip()
                else:
                    print("Tu perdeste porque calhou",cpu2,"!")
                    print("Pontuação: J-",pontos_j2,".")
                    rod2+=1
                    print("\n\nrodada:",rod2)
                    esc2=str(input("Escreva cara ou coroa(escreva fim se quiser acabar)")).lower().strip()
            else:
                #caso em que o jogador não escreve cara ou coroa
                print("Palavra inválida, confirme se escreveu tudo em letras minúsculas ou se escreveu a palavra correta.")
                esc2=str(input("\n\nEscreva cara ou coroa(escreva fim se quiser acabar)")).lower().strip()
                #Pedir a escolha do jogador de novo
        print("\nFim, a pontuação foi",pontos_j2,".")
        #Caso em que o jogador escreve "fim", o programa escreve fim e a pontuação do jogador
        jogo = "a"
        #Definir jogo de novo como "a" para voltar para o menu de seleção de minijogo

        
    while jogo==3:
        #Para executar jogo da forca se jogo é igual a 3.   
        if regras==0:
            #Esta variável serve para apresentar as regras do jogo quando ela é igual a 0
            print("\nBem vindo ao jogo da forca. O objetivo do jogo é descobrires a palavra secreta.\nAs palavras estão todas com letras minúsculas e sem acentos.\nTens sete vidas que perdes à medida que escreves letras que não estão na palavra.\nQuando selecionares o tema vão aparecer tantos pontos como o número de letras da palavra.")
            regras=1
            #Definir regras como 1 para se o jogador voltar a jogar outra partida deste minijogo não mostrar de novo as regras. 
        lista_desporto=("volei","basquetebol","futebol","badminton","atletismo","rugby","tenis","andebol","basebol","golfe")
        lista_animais=("chita","urso","leao","jaguar","camelo","cao","gato","crocodilo","avestruz","baleia","javali","kiwi")
        lista_p_e_c=("roma","argentina","italia","berlim","toquio","madrid","japao","espanha","nepal","peru","londres","inglaterra","amsterdao","holanda")
        #Listas organizadas por tema com as palavras que o computador selecionará para serem senhas
        tema=int(input("\n\nEscolha um dos seguintes temas:\n 1->desportos;\n 2->animais;\n 3->países e capitais;\n 4->Voltar para o menu de seleção.\n"))
        #Tema escolhido pelo jogador
        while tema>4 or tema<1:
            #Caso em que o jogador não escolhe nenhuma opção válida
                print("Número inválido.Escreva 1, 2 ou 3 para escolher um dos temas")
                tema=int(input("Escolha um dos seguintes temas:\n 1->desportos;\n 2->animais;\n 3->países e capitais\n"))
                #Pedir o tema ao jogador de novo
        if tema==1:
            #caso em que o tema é igual a 1, ou seja, desporto
            lista3=lista_desporto
            #define a lista do tema como lista3
        elif tema == 2:
            #caso em que o tema é igual a 2, ou seja, animais 
            lista3=lista_animais
            #define a lista do tema como lista3
        elif tema == 3:
            #caso em que o tema é igual a 3, ou seja, países e capitais
            lista3=lista_p_e_c
            #define a lista do tema como lista3
        elif tema == 4:
            #caso em que o tema é igual a 4, ou seja, o jogador quer terminar o jogo
            jogo = "a"
            #Definir jogo de novo como "a" para voltar para o menu de seleção de minijogo
            break
            #Interromper o while jogo==3
        palavra =random.choice(lista3)
        #palavra é uma senha de entre as palavras que estavam na lista3
        digitadas = ()
        #variável que serve para definir as letras já digitadas
        acertadas = ()
        #variável que serve para definir as letras já acertadas
        erros = 0
        #Definir erro como 0
        while True: 
             senha = ""
             for letra in palavra:
                 senha += letra if letra in acertadas else " _ "
                 #Se a letra escrita está na palavra então ele adiciona-a à senha e as restantes letras são substituidas por underscore
             print(senha)
             #Escrever a senha
             if senha == palavra:
                #Caso em que o jogador já descobriu a palavra
                print("Você descobriu a palavra!")
                break
                #Interromper o while true
             tentativa =(input("\nDigite uma letra:")).lower().strip()
             #Letra que o jogador escreve, esta torna-se sempre uma letra minúscula indepentemente como o jogador escrever
             if tentativa in digitadas:
                #Caso em que o jogador escreve uma letra já usada
                if tentativa in palavra and tentativa not in senha:
                    #Serve para eliminar o problema em que o jogador escreve uma palavra que não é a certa, mas que esta contém letras que estão na palavra final e depois se escrevê-se alguma das letras da senha que estavam na palavra ele assumia como palavra repetidas, fazendo o jogador não conseguir terminar o jogo
                    acertadas += tuple(tentativa)
                else:
                    print("Ja usou esta letra!")
                
             else:
                digitadas += tuple(tentativa)
                #Adição da letra usada na tentativa às digitadas
                if tentativa in palavra:
                       #Caso em que a letra escrita está na palavra
                       acertadas += tuple(tentativa)
                       #Adição da letra usada na tentativa às acertadas
                else:
                       #Caso em que o jogador escreve uma palavra que não está na palavra
                       erros += 1
                       #Adição de 1 a erros
                       print("Letra errada!")
                       #Escrever que a letra está incorreta
             if erros == 0:
                       #Caso em que o jogador ainda tem zero erros, tendo portanto todas as vidas
                       print("Tem 7 vidas")
                       #Escrever o número de vidas
             elif erros == 1:
                       #o resto das opções são iguais à primeira variando apenas o número de erros já obtidos e consequentemente as vidas restantes
                       print("Tem 6 vidas")
             elif erros == 2:
                       print("Tem 5 vidas")
             elif erros == 3:
                       print("Tem 4 vidas")
             elif erros == 4:
                       print("Tem 3 vidas")
             elif erros == 5:
                       print("Tem 2 vidas")
             elif erros == 6:
                       print("Tem 1 vidas")
             else:
                       #Caso em que o jogador já não tem mais vidas
                       print("\nGame over!")
                       print("A palavra era",palavra,"!")
                       print("Tenta outra vez!")
                       #Escrever que o jogo acabou e revelar a senha
                       break
                       #Interromper o while true 
        


                  

                    

