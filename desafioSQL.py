import sqlite3

conexao = sqlite3.connect('banco') #Conecta com o banco de dados criado (arquivo que criamos no dbeaver)
cursor = conexao.cursor()

### Questão 1

cursor.execute('CREATE TABLE alunos( id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

### Questão 2


cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Maria Leal",23,"Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Luiza Silva",30,"Letras")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Marcos Antonio",25,"Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Camila Cruz",28,"Ciências da computação")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "José Ricardo",19,"Letras")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (6, "Otávio Luis",23,"Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (7, "Gustavo Souza",21,"Letras")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (8, "Gabriele Cristine",22,"Engenharia")')


### Questão 3

# letra a)

alunosMat= cursor.execute('SELECT * FROM alunos')

for i in alunosMat:
    print(i)



# letra b)

alunosSel = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for j in alunosSel:
    print(j)

# letra c)


alunoseng = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC')
for eng in alunoseng:
    print(eng)


# letra d)


alunostot= cursor.execute('SELECT COUNT(id) FROM alunos')

alunostot= cursor.fetchone()

print(alunostot[0]) #Número total de alunos


### Questão 4

# letra a)

cursor.execute('UPDATE alunos SET idade = 18 WHERE id = 4')

#letra b)
cursor.execute('DELETE FROM alunos WHERE id = 7')


### Questão 5


cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Maria Leal",25,"10000.50")')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Luan Almeida",28,"80000.90")')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "João Silva",35,"100.50")')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Carlos Roberto",50,"25444.92")')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Rita Santos",55,"187.50")')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (6, "Luiza Carla",28,"899.98")')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (7, "Francisco José",40,"1250000.57")')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (8, "Carolina Ribeiro",42,"810000.00")')


### Questão 6

#letra a)

clientes_sup30 = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
for i in clientes_sup30:
    print(i)


# letra b)

saldo_medio= cursor.execute('SELECT AVG(saldo) FROM clientes')
saldo_medio = cursor.fetchone()
print("R$ " + str(round(saldo_medio[0],2)))


#letra c)

saldo_max= cursor.execute('SELECT nome, MAX(saldo) FROM clientes')
saldo_max = cursor.fetchone()
print(saldo_max) #Saldo máximo


#letra d)

saldo_ac1000= cursor.execute('SELECT COUNT(id) FROM clientes WHERE saldo > 1000')
saldo_ac1000 = cursor.fetchone()
print(saldo_ac1000[0])


### Questão 7

#letra a
cursor.execute('UPDATE clientes SET saldo = 1230.57 WHERE id = 3')

# letra b 
cursor.execute('DELETE FROM clientes WHERE id = 8')


### Questão 8

#Criação da tabela de compras

cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor MONEY, FOREIGN KEY(cliente_id) REFERENCES clientes(id))')

#Alimentando a tabela 

cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 2,"Perfume","250.50")')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 2,"Delineador preto","25.99")')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, 5,"Shampoo","40.99")')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (4, 3,"Sabonete Líquido","50.50")')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (5, 1,"Perfume","170.80")')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (6, 1,"Creme de pele","80.50")')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (7, 4,"Batom","24")')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (8, 1,"Creme anti frizz","40.50")')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (9, 7,"Perfume","185.50")')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (10, 6,"Condicionador","15.50")')

#Mostrando compras

dados = cursor.execute('SELECT  nome, produto, valor FROM compras INNER JOIN clientes ON compras.cliente_id = clientes.id ORDER BY clientes.nome ASC')
for usuario in dados:
    print(usuario)




conexao.commit() #As informações serão enviados no banco 
conexao.close #Precisa fechar para não dar conflito no gerenciamento do pc