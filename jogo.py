#Código do samuel: https://repl.it/@crisdebug/Trabalho-Forca

from random import choice
import lib.util as util




def inicio():
  util.clear()
  Temas_existentes = util.carregar_temas()
  util.cabecalho('Bem-vindo ao jogo da forca', [''])

  print('Escolha o nível de jogo:')
  print('1 - Fácil')
  print('2 - Médio')
  print('3 - Difícil')
  
  escolha_de_dificuldade = input('Opção: ')
  numero_de_chances = 0
  perda_de_pontos = 0

  while escolha_de_dificuldade != '1' and escolha_de_dificuldade != '2' and escolha_de_dificuldade != '3':
          print('Opção inválida')
          escolha_de_dificuldade = int(input())
  util.clear()



  if escolha_de_dificuldade == '1':
        numero_de_chances = 8
        perda_de_pontos = 750
  elif escolha_de_dificuldade == '2':
        numero_de_chances = 5
        perda_de_pontos = 1200
  elif escolha_de_dificuldade == '3':
        numero_de_chances = 3
        perda_de_pontos = 2000
  util.cabecalho('Bem-vindo ao jogo da forca', [''])
  print('Escolha um tema: ')
  print()
  for tema in range(len(Temas_existentes)):
    print('%d - %s'%(tema+1, Temas_existentes[tema]))

  numero_tema = input('Numero do tema: ')
  while not util.eh_inteiro(numero_tema):
    print('INSIRA UM NÚMERO!')
    numero_tema = input('Numero do tema: ')
  
  while not (int(numero_tema) in range(1, len(Temas_existentes)+1)):
    print('INSIRA UM NÚMERO VALIDO!')
    numero_tema = input('Numero do tema: ')
  while not util.eh_inteiro(numero_tema):
    print('INSIRA UM NÚMERO!')
    numero_tema = input('Numero do tema: ')
  
  
  nome_tema = Temas_existentes[int(numero_tema) - 1]
  palavras = util.carregar_palavras(nome_tema)
  palavra_secreta = choice(palavras)
  jogo(palavra_secreta, numero_de_chances, perda_de_pontos)
  

def exibir_ranking():
  util.clear()
  ranking = util.carregar_ranking()
  util.cabecalho('Ranking', [''])
  for linha in ranking:
    print('%s'%(linha))
  
  print()
  print('1 - Jogar Novamente')
  opcao = input('Opção: ')
  while opcao != '1':
    print('OPCÃO INVÁLIDA!')
    opcao = input('Opção: ')
  if opcao == '1':
    inicio()

def jogo(palavra_secreta, numero_de_chances, perda_de_pontos):
  util.clear()
  pontuacao = 6000
  
  mascara = []
  for i in range(len(palavra_secreta)):
    mascara.append('-')
  
  

  acertou = False
  enforcou = False
  erros = 0
  tentativas_restantes = numero_de_chances
  while(not acertou and not enforcou):
    util.clear()
    util.cabecalho('jogo da forca', [''])
    print("Você tem %d tentetivas restantes!"%tentativas_restantes)
    print("Sua pontuação é %d"%pontuacao)
    for char in range(len(mascara)):
      print('%s'%(mascara[char]), end='')
    print()
    chute = input('Digite uma letra: ')
    while len(chute) > 1:
      print('INSIRA SOMENTE UMA LETRA!')
      chute = input('Digite uma letra: ')
    print()
    acertou = chute.upper() in palavra_secreta.upper()
    if acertou:
      for letra in range(len(palavra_secreta)):
        if (chute.upper() == palavra_secreta[letra].upper()):
          mascara[letra] = palavra_secreta[letra].upper()
      acertou = False
    else:
      print(" ".join(mascara))
      print('Letra não existente na palavra! :-(')
      erros += 1
      tentativas_restantes -= 1
      pontuacao -= perda_de_pontos
    acertou = '-' not in mascara
    enforcou = erros == numero_de_chances 
  
  
  if (acertou):
    util.clear()
    util.cabecalho('jogo da forca', [''])
    print("Sua pontuação é %d"%pontuacao)
    for char in range(len(mascara)):
      print('%s'%(mascara[char]), end='')
    print()
    print('Você ganhouuuuuuuuu!!!')
    jogador = input("Qual o seu nome? ")
    resultado = jogador +  ' - ' + str(pontuacao)
    util.cadastrar_ranking(resultado)
  elif (not acertou):
    print()
    print()
    print("|-----   ")
    print("|    |   ")
    print("|    O   ")
    print("|   /|\          Enforcado!!!")
    print("|    |   ")
    print("|   / \  ")
    print("==========")
    print()
    print('A palavra era: %s'%(palavra_secreta))

  print('1 - Exibir Ranking   2 - Jogar Novamente   3 - Sair')
  opcao = input('Opção: ')
  while opcao != '1' and opcao != '2' and opcao != '3':
    print('OPÇAO INVALIDA!')
    opcao = input('Opção: ')

  if opcao == '1':
    exibir_ranking()

  if opcao == '2':
    inicio()

  if opcao == '3':
    util.clear()
    print('Até mais!')

      




