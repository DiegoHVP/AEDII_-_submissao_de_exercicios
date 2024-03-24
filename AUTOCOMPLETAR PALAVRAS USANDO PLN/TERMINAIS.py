import re

def remover_palavras_terminais(nome_arquivo):
    palavras_terminais = {'e', 'o', 'a,','um','uma','s', 'es', 'os', 'as', 'do', 'da', 'dos', 'das', 'de', 'em', 'na', 'no', 'nas', 'nos'}

    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()

    texto = texto.lower()
    # substituir todos os caracteres que não são letras, dígitos ou espaços em branco por uma string vazia
    texto = re.sub(r'[^\w\s]', '', texto)
    palavras = texto.split() # Dividir o texto em palavras

    
    palavras_sem_terminais = set() # Criar um conjunto sem repetição

    for palavra in palavras:
    	  # SE CONTEM APENAS DIGITOS \d
    	  # DO INICIO ^ AO FIM $
          # A NEGACAO DISSO ADICiONA
        if palavra not in palavras_terminais and not re.match(r'^\d+$', palavra):
            palavras_sem_terminais.add(palavra)

    # junta cseparando com espacos
    texto_sem_terminais = ' '.join(palavras_sem_terminais)

    # salva o arquivo
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto_sem_terminais)

