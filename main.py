import admin
import jogo
import lib.util as util
def main():
  util.clear() 
  util.cabecalho('Bem-vindo ao jogo da forca', [''])
  print('1 - Administração do jogo')
  print('2 - Jogar')
  print('3 - Sair')
  opcao = input('Opção: ')
  while opcao != '1' and opcao != '2' and opcao != '3':
    print('OPÇÃO INVÁLIDA')
    opcao = input('Opção: ')
        
  if opcao == '1':
    admin.options()
  
  if opcao == '2':
    jogo.inicio()
  
  if opcao == '3':
    util.clear()
    print('Até mais!')


main()


