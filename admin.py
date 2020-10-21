import lib.util as util

temas = []
historico = ['Home', 'Administração']
titulo = "administração do sistema"
def listar_palavras(tema, origem='listagem'): 
  palavras = util.carregar_palavras(tema)
  util.clear()
  
  util.cabecalho(titulo, historico)

  if len(palavras) == 0:
    print('NÃO HÁ PALAVRAS CADASTRADAS NESTE TEMA')
  else:
    for count in range(len(palavras)):
        print('%d - %s'%(count+1, palavras[count]))

  
  print()
  print()
  print('----Opções----')
  print('1 - Adicionar Palavra')
  if not len(palavras) == 0:
    print('2 - Editar Palavra')
    print('3 - Apagar Palavra')
  print('4 - Voltar')

  

  opcao = input('Opção: ')

  while len(palavras) == 0 and opcao == '2' or len(palavras) == 0 and opcao == '3':
    print('NÃO HÁ NENHUMA PALAVRA!')
    opcao = input('Opção: ')
  
  while not (opcao != '1' or opcao != '2' or opcao != '3' or opcao != '4'):
    print('OPÇÃO INVÁLIDA!')
    opcao = int(input('Opção: '))
  
  if opcao == '1':
    nova_palavra  = input('Nova palavra: ')
    palavras.append(nova_palavra)
    arquivo_tema = util.carregar_arquivo('./arquivos/'+tema+'.txt', 'a')
    arquivo_tema.write(nova_palavra+'\n')
    arquivo_tema.close()
    listar_palavras(tema)
  
  if opcao == '2':
    palavra_selecionada = input('Digite o número da palavra a ser editada: ')
    while not util.eh_inteiro(palavra_selecionada):
      print('INSIRA UM NUḾERO!')
      palavra_selecionada = input('Digite o número da palavra a ser editada: ')
    while not (int(palavra_selecionada) in range(1, len(palavras) + 1)):
      print('OPÇÃO INVÁLIDA!')
      palavra_selecionada = int(input('Digite o número da palavra a ser editada: '))
      while not util.eh_inteiro(palavra_selecionada):
        print('INSIRA UM NUḾERO!')
        palavra_selecionada = input('Digite o número da palavra a ser editada: ')
    palavras[int(palavra_selecionada) - 1] = input('Nova palavra: ')
    arquivo_tema = util.carregar_arquivo('./arquivos/'+tema+'.txt', 'w')
    for palavra in palavras:
      arquivo_tema.write(palavra+'\n')
    arquivo_tema.close()
    listar_palavras(tema)
  if opcao == '3':
    palavra_selecionada = input('Digite o número da palavra a ser apagada: ')
    while not util.eh_inteiro(palavra_selecionada):
      print('INSIRA UM NÚMERO!')
      palavra_selecionada = input('Digite o número da palavra a ser apagada: ')
    while not (int(palavra_selecionada) in range(1, len(palavras) + 1)):
      print('OPÇÃO INVÁLIDA!')
      palavra_selecionada = input('Digite o número da palavra a ser apagada: ')
      while not util.eh_inteiro(palavra_selecionada):
        print('INSIRA UM NÚMERO!')
        palavra_selecionada = input('Palavra a ser apagada: ')
    del palavras[int(palavra_selecionada) - 1]
    for palavra in palavras:
      arquivo_tema.write(palavra+'\n')
    
    arquivo_tema = util.carregar_arquivo('./arquivos/'+tema+'.txt', 'w')
    arquivo_tema.close()
    listar_palavras(tema)
  
  if opcao == '4':
    historico.pop()
    if origem == 'listagem':
      listar_temas()
    else:
      historico.pop()
      options()

  
def testar_tema(tema):
  temas = util.carregar_temas()
  for i in temas:
    if tema.upper() == i.upper():
      return True
  return False

def opcao_listar_palavras(temas, origem='listagem'):
  tema = int(input('Número do tema: '))
  while not (tema in range(1, len(temas) + 1)):
    print('OPÇÃO INVÁLIDA')
    tema = int(input('Número do tema: '))
  historico.append(temas[tema-1])
  listar_palavras(temas[tema-1], origem=origem)


def opcao_editar_nome_tema(temas):
  tema_editar = input('Numero do tema a ser editado: ')
  while not util.eh_inteiro(tema_editar):
    print('Insira um numero válido!')
    tema_editar = input('Numero do tema a ser editado: ')
  
  while not (int(tema_editar) in range(1, len(temas)+1)):
    print('Insira um numero válido!')
    tema_editar = input('Numero do tema a ser editado: ')
  
  novo_nome = input('Novo nome do tema: ')
  nome_antigo = temas[int(tema_editar) - 1]
  temas[int(tema_editar) - 1] = novo_nome
  arquivo_temas = util.carregar_arquivo('./arquivos/temas.txt', 'w')
  for tema in temas:
    arquivo_temas.write(tema+'\n')
  arquivo_temas.close()
  arquivo_tema_new_name = util.carregar_arquivo('./arquivos/'+novo_nome+'.txt', 'w')
  palavras_arquivo_old = util.carregar_palavras(nome_antigo)
  for palavra in palavras_arquivo_old:
    arquivo_tema_new_name.write(palavra+'\n')
  arquivo_tema_new_name.close()
  util.apagar_arquivo('./arquivos/'+nome_antigo+'.txt')
  
def opcao_apagar_tema(temas):
  numero_tema = input('Insira o numero do tema a ser apagado: ')
  while not util.eh_inteiro(numero_tema):
    print('INSIRA UM NUMERO!')
    numero_tema = input('Insira o numero do tema a ser apagado: ')
  
  while not (int(numero_tema) in range(1, len(temas) + 1)):
    print('INSIRA UMA OPÇÃO VÁLIDA!')
    numero_tema = input('Insira o numero do tema a ser apagado: ')
    while not util.eh_inteiro(numero_tema):
      print('INSIRA UM NUMERO!')
      numero_tema = input('Insira o numero do tema a ser apagado: ')
  
  tema_a_apagar = temas[int(numero_tema) - 1]
  del temas[int(numero_tema) - 1]
  arquivo_temas = util.carregar_arquivo('./arquivos/temas.txt', 'w')
  for tema in temas:
    arquivo_temas.write(tema+'\n')
  
  arquivo_temas.close()
        
  util.apagar_arquivo('./arquivos/'+tema_a_apagar+'.txt')

def listar_temas():
  util.clear()
  temas = util.carregar_temas()
  util.cabecalho(titulo, historico)
  if len(temas) == 0:
    print('NENHUM TEMA CADASTRADO!')
  else:
    for tema in range(len(temas)):
      print('%d - %s'%(tema+1, temas[tema]))
  
  print()
  print()
  print('----Opções----')
  if not len(temas) == 0:
    print('1 - Ver palavras de um tema')
    print('2 - Editar nome do tema')
    
    print('4 - Apagar tema')
  print('3 - Criar tema')
  print('5 - Voltar')
  opcao = input('Opção: ')
  while len(temas) == 0 and opcao == '1' or len(temas) == 0 and opcao == '2' or len(temas) == 0 and opcao == '4':
    print('NÃO HÁ NENHUM TEMA!')
    opcao = input('Opção: ')
  while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
    print('OPÇÃO INVÁLIDA')
    opcao = input('Opção: ')
  
  while len(temas) == 0 and opcao == '1' or len(temas) == 0 and opcao == '2' or len(temas) == 0 and opcao == '4':
    print('NÃO HÁ NENHUM TEMA!')
    opcao = input('Opção: ')

  if opcao == '1':
    opcao_listar_palavras(temas)
  
  if opcao == '2':
    opcao_editar_nome_tema(temas)
    listar_temas()
  
  if opcao == '3':
    nome = input('Nome do novo tema: ')
    teste = testar_tema(nome)
    while teste:
      print('Este tema já existe!')
      nome = input('Nome do novo tema: ')
      teste = testar_tema(nome)
    
    arquivo_tema = util.carregar_arquivo('./arquivos/temas.txt', 'a')
    arquivo_tema.write(nome+'\n')
    arquivo_tema.close()
    arquivo_tema = util.carregar_arquivo('./arquivos/'+nome+'.txt', 'w')
    arquivo_tema.close()
    historico.append(nome)
    temas.append(nome)
    listar_palavras(nome)

  if opcao == '4':
    opcao_apagar_tema(temas)
    listar_temas()
  
  if opcao == '5':
        historico.pop()
        options()
  

def resultado_pesquisa_tema(resultados):
  util.clear()
  util.cabecalho('Pesquisa de temas', historico)
  
  if len(resultados) == 0:
    print('NÃO HÁ RESULTADOS!')
  else:
    for i in range(len(resultados)):
      print('%d - %s'%(i+1, resultados[i]))
    
  
  print()
  print()
  print('----Opções----')
  if not len(resultados) == 0:
    print('1 - Ver palavras de um tema')
    print('2 - Editar nome do tema')
    print('3 - Apagar tema')
  print('4 - Voltar')
  opcao = input('Opção: ')
  if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
    print('INSIRA UMA OPÇÃO VÁLIDA!')
    opcao = input('Opção: ')
  while len(resultados) == 0 and opcao == '1' or len(resultados) == 0 and opcao == '2' or len(resultados) == 0 and opcao == '3':
    print('NÃO HÁ NENHUM TEMA!')
    opcao = input('Opção: ')
  if opcao == '1':
    opcao_listar_palavras(resultados, origem='pesquisa')
  
  if opcao == '2':
    opcao_editar_nome_tema(resultados)
    resultado_pesquisa_tema(resultados)
  
  if opcao == '3':
    opcao_apagar_tema(resultados)
    resultado_pesquisa_tema(resultados)
  
  if opcao == '4':
    historico.pop()
    options()

def opcao_editar_palavra(palavra ,tema, retorno):
  palavras = util.carregar_palavras(tema)
  posicao = palavras.index(palavra)
  palavras[posicao] = input('Insira a nova palavra: ')
  arq_tema = util.carregar_arquivo('./arquivos/'+tema+'.txt', 'w')
  for palavra in palavras:
    arq_tema.write(palavra+'\n')
  
  arq_tema.close()
  pesquisar_palavra(retorno)


      
def pesquisar_palavra(pesquisa):
  util.clear()
  temas = util.carregar_temas()
  resultados = []
  for tema in temas:
    palavras = util.carregar_palavras(tema)
    for palavra in palavras:
      if pesquisa.upper() in palavra.upper():
        resultados.append('%s - %s'%(palavra, tema))
  
  util.cabecalho('Resultados da Pesquisa', historico)

  if len(resultados) == 0:
    print('NÃO HÁ RESULTADOS!')
  else:
    for palavra in range(len(resultados)):
      print('%d - %s'%(palavra+1, resultados[palavra]))
  
  print()
  print()
  if not len(resultados) == 0:
    print('1 - Editar Palavra')
    print('2 - Apagar Palavra')
  print('3 - Voltar')

  opcao = input('Opção: ')
  while not util.eh_inteiro(opcao):
    print('INSIRA UM NÚMERO!')
    opcao = input('Opção: ')

  while len(resultados) == 0 and opcao == '1' or len(resultados) == 0 and opcao == '2':
    print('NÃO HÁ NENHUMA PALAVRA!')
    opcao = input('Opção: ')
    while not util.eh_inteiro(opcao):
      print('INSIRA UM NÚMERO!')
      opcao = input('Opção: ')

  
  while opcao != '1' and opcao != '2' and opcao != '3':
    print('INSIRA UMA OPÇÃO VÁLIDA!')
    opcao = input('Opção: ')
    while not util.eh_inteiro(opcao):
      print('INSIRA UM NÚMERO!')
      opcao = input('Opção: ')

  if opcao == '1':
    numero_palavra = input('Digite o numero da palavra para editar: ')
    while not util.eh_inteiro(numero_palavra):
      print('INSIRA UM NUMERO!')
      numero_palavra = input('Digite o numero da palavra para editar: ')
    
    while not (int(numero_palavra) in range(1, len(resultados)+1)):
      print('NÚMERO INVÁLIDO!')
      numero_palavra = input('Digite o numero da palavra para editar: ')
      while not util.eh_inteiro(numero_palavra):
        print('INSIRA UM NUMERO!')
        numero_palavra = input('Digite o numero da palavra para editar: ')
    palavra = resultados[int(numero_palavra)-1].split(' - ')
    opcao_editar_palavra(palavra[0], palavra[1], pesquisa)
    



def options():
  util.clear()
  util.cabecalho(titulo, historico)
  print('----Opções----')
  print('1 - Listar temas')
  print('2 - Pesquisar Temas')
  print('3 - Pesquisar Palavra')
  print('4 - Voltar')

  opcao = input('Opção: ')
  while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
      print('OPÇÃO INVÁLIDA')
      opcao = input('Opção: ')

  if opcao == '1':
    historico.append('Temas')
    listar_temas()
  
  if opcao == '2':
    temas = util.carregar_temas()
    pesquisa = input('Nome do tema a pesquisar: ')
    resultados = []
    

    for palavra in temas:
      if palavra.upper().find(pesquisa.upper()) >= 0:
            resultados.append(palavra)
    
    historico.append('Resultados da Pesquisa')
    resultado_pesquisa_tema(resultados)

  if opcao == '3':
    pesquisa = input('Palavra para pesquisar:')
    historico.append('Pesquisar Palavra')
    pesquisar_palavra(pesquisa)
    
  
  if opcao == '4':
    historico.pop()
    import main
    main.main()