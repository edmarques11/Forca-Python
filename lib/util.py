import os 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho(titulo, historico):
  print("------ %s ------"%(titulo.upper()))
  for i in range(len(historico)-1):
    print('%s > '%(historico[i]), end=' ')
  print('%s'%(historico[len(historico)-1]))
  print()

def carregar_arquivo(nome, modo):
  return open(nome, modo)

def carregar_temas():
  arquivo_temas = carregar_arquivo('./arquivos/temas.txt', 'r')
  temas = []
  for tema in arquivo_temas:
    temas.append(tema.strip())
  
  arquivo_temas.close()
  return temas

def carregar_palavras(tema):
  arquivo_tema = carregar_arquivo('./arquivos/'+tema+'.txt', 'r')
  palavras = []
  for palavra in arquivo_tema:
    palavras.append(palavra.strip())

  arquivo_tema.close()
  return palavras

def apagar_arquivo(caminho):
  if os.path.exists(caminho):
    os.remove(caminho)

def eh_inteiro(string):
  try:
    int(string)
    return True
  except:
    return False


def cadastrar_ranking(resultado):                   
  arquivo = carregar_arquivo("./arquivos/ranking.txt",'r')
  linhas = []
  for linha in arquivo:
    linhas.append(linha.strip())
  
  arquivo.close()
  alterou = False
  for linha in range(len(linhas)):
    separador = resultado.split(' - ')
    if separador[0] in linhas[linha]:
      if int(separador[1]) > int(linhas[linha].split(' - ')[1]):
        linhas[linha] = "%s - %s"%(linhas[linha].split(' - ')[0], separador[1])
        alterou = True
        break
  
  if not alterou:
    linhas.append(resultado)
  
  arquivo = carregar_arquivo('./arquivos/ranking.txt', 'w')
  for linha in linhas:
    arquivo.write(linha.upper()+'\n')
  arquivo.close()
  

def carregar_ranking():
  arq_ranking = carregar_arquivo('./arquivos/ranking.txt', 'r')
  resultado = []
  maior = 0
  linhas = []
  for linha in arq_ranking:
    linhas.append(linha.strip())
  
  index = 0
  while len(linhas) > 0:
    for linha in linhas:
      separador = linha.split(' - ')
      if int(separador[1]) > maior:
        maior = int(separador[1])
        resultado.insert(index, linha)
    linhas.remove(resultado[index])
    index = index + 1
    maior = 0
  return resultado
