"""
#Conjuntos

- conjuntos em qualquer linguagem, estamos fazendo referencia a teoria dos conjuntos da matematica
- No python, os conjuntos sao chamados de sets

#OBS:
-> sets não possuem valores duplicados
-> sets não possuem valores ordenados
-> sets não tem indexamento
-> sets são referenciados com '{}'
-> se houver um valor duplicado, ele é ignorado
-> pode ter todos os tipos de dados 

#Definição:
- Forma 1 (mais comum)

s = {1, 2, 3, 4, 5}

- Forma 2

s = set({1, 2, 3, 4, 5})

#iteração:

for n in s:
    print(n)

#Adicionando elementos no conjunto:

conj = {1, 2, 3}
conj.add(4)
print(conj) # {1, 2, 3, 4}

#Remover elementos:

conj.remove(2)
print(conj) # {1, 3, 4}

- para remover, tambem pode ser usada a função .discard()

#Copiando conjuntos

- Deep Copy:

conjunto = {1, 2, 3, 4}
novo = conjunto.copy()

-Shallow Copy:

novo = conjunto

#Zerar conjunto:

conjunto.clear()

#Metodos matematicos nos conjuntos:

- Gerar um conjunto com valores unicos

Usando a função union(), ou o pipe '|'
EX: 
    alunos_python = {'Jorge', 'Ana', 'Guilherme', 'Jaqueline', 'Marcos'}
    alunos_java = {'Renato', 'Lucas', 'Ana', 'Jaqueline', 'Beth'}

    unicos = estudantes_python.union(estudantes_java) #Retorna os estudantes unicos
    ou
    unicos = estudantes_python | estudantes_java

- Gerar um conjunto com valores que estão em ambos quesitos

Usando a função intersection(), ou o "&"
EX:
    ambos = estudantes_python.intersection(estudantes_java) #Retorna somente os estudantes que estão nos dois cursos
    ou
    ambos = estudantes_python & estudantes_java

- Gerar um conjunto com valores exclusivos em cada quesito

Usando a função difference()
EX:
    so_python = estudantes_python.difference(estudantes_java) #Retorna somente os estudantes de python

"""

