"""
Dicionarios

OBS: em algumas liinguagens de programação, são conhecidos como mapas

dicionarios sao coleções chave/valor

- são representados por '{}'

EX:

# Forma 1 (mais comum)
- paises = {'br': 'Brazil, 'ger': 'Germany', 'usa': 'United States of America'}

# Forma 2

- paises = dict(br = 'Brazil', ger = 'Germany', usa = 'United States of America')

#Acessando elementos:

Forma 1 - acessando pela chave

- print(paises['br'])

Forma 2 - acessando via GET (recomendada)

print(paises.get('br'))

#OBS: Caso o get não encontre o valor informado, ele retorna um valor None, e não um erro

- Podemos usar qualquer tipo de dados como chaves de dicionarios

#Adicionar elementos em dicionarios: 

receita = {'jan': 100, 'fev': 200, 'mar': 300}

- Forma 1 (mais comum)

receita['abr'] = 400

- Forma 2 

novo_dado = {'mai': 500}
receita.update(novo_dado)

#Atualizando dados em dicionarios

- É só usar o .update()

#OBS: em dicionarios, não se pode ter chaves repetidas!!!!

#Remover dados de dicionarios:

- Forma 1: Usando o metodo .pop()
é obrigatorio informar a chave
Ao removermos um objeto, o valor removido é retornado caso seja impresso na tela

- Forma 2: usando a palavra especial 'del'
ex: del receita['jan']

#Metodos para dicionarios:

- Limpar o dicionario (zerar dados):
    clear()

- Copiando um dicionario para outro:
#Forma 1: usando o metodo copy(), deep copy

#Forma 2: Shallow copy

- Criando dicionarios com fromkeys()

outro = {}.fromkeys('chave', 'valor')

#Iterando sobre dicionarios:

for chave in receita:
    print(chave) #imprime as chaves

for chave in receita:
    print(receita[chave]) #imprime os valores

"""
