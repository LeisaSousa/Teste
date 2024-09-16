import subprocess

# Executar comandos Git
subprocess.run(["git", "init"], check=True)
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
subprocess.run(["git", "remote", "add", "origin", "https://github.com/LeisaSousa/Teste.git"], check=True)
subprocess.run(["git", "push", "-u", "origin", "master"], check=True)

import sqlite3

conexao = sqlite3.connect ('banco')
cursor = conexao.cursor ()

#cursor.execute ('CREATE TABLE alunos(id INT, nome VARCHAR(30), idade INT, curso VARCHAR(50))')

# Inserindo dados na tabela
#cursor.execute ('INSERT INTO alunos (id, nome, idade, curso) VALUES (1,"Maria",25,"Engenharia de Dados")')
#cursor.execute ('INSERT INTO alunos (id, nome, idade, curso) VALUES (2,"Joao",28,"Engenharia de Dados")')
#cursor.execute ('INSERT INTO alunos (id, nome, idade, curso) VALUES (3,"Pedro",29,"Engenharia da computacao")')
#cursor.execute ('INSERT INTO alunos (id, nome, idade, curso) VALUES (4,"Vicente",21,"Engenharia de Producao")')
#cursor.execute ('INSERT INTO alunos (id, nome, idade, curso) VALUES (5,"Joana",238,"Administracao")')

# Consultas Básicas
# Selecionar todos os registros da tabela "alunos"
#dados = cursor.execute ('SELECT * FROM alunos')
#for alunos in dados:
#   print (alunos)

# Selecionar o nome e a idade dos alunos com mais de 20 anos.
#dados = cursor.execute ('SELECT nome, idade FROM alunos WHERE idade>20')
#for alunos in dados:
#    print (alunos)

# Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
#dados = cursor.execute ('SELECT * FROM alunos WHERE curso = "engenharia" ORDER BY nome ASC')
#for alunos in dados:
#    print (alunos)

# Contar o número total de alunos na tabela
#dados = cursor.execute ('SELECT COUNT(*) FROM alunos')
#for alunos in dados:
#   print (alunos)

#Atualização e Remoção
#Atualize a idade de um aluno específico na tabela.
# Definir o ID do aluno e a nova idade
#id_do_aluno = 5
#idade_antiga = 238
#nova_idade = 38
# Atualizar a idade 
#dados = cursor.execute('UPDATE alunos SET idade = 38 WHERE idade = 238 AND id = 5')
#for alunos in dados:
#print (alunos)

#Remova um aluno pelo seu ID.
#dados=cursor.execute('DELETE from alunos WHERE id = 5')

#Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela

#cursor.execute ('CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT(30), idade INTEGER, saldo INTEGER)')
# Inserindo dados na tabela
#cursor.execute ('INSERT INTO clientes (nome, idade, saldo) VALUES ("Julia",80,10000)')
#cursor.execute ('INSERT INTO clientes (nome, idade, saldo) VALUES ("Vitor",50,100)')
#cursor.execute ('INSERT INTO clientes (nome, idade, saldo) VALUES ("Lay",22,900)')
#cursor.execute ('INSERT INTO clientes (nome, idade, saldo) VALUES ("Vitoria",31,1050)')


#Selecione o nome e a idade dos clientes com idade superior a 30 anos.

#Selecionar todos os registros da tabela "clientes"
#base = cursor.execute ('SELECT * FROM clientes')
#for clientes in base:
#   print (clientes)

#base = cursor.execute ('SELECT nome, idade FROM clientes WHERE idade>30')
#for clientes in base:
#    print (clientes)

# Calcule o saldo médio dos clientes.
#base = cursor.execute('SELECT AVG(saldo) FROM clientes')
#for clientes in base:
#   print (clientes)


# Encontre o cliente com o saldo máximo.
#base = cursor.execute('SELECT MAX(saldo) FROM clientes')
#max_saldo = cursor.fetchone()[0]
# Cliente com o saldo máximo
#if max_saldo is not None:
#    cursor.execute('SELECT * FROM clientes WHERE saldo = ?', (max_saldo,))
#    cliente_saldo_maximo = cursor.fetchall()
# Exibir os clientes com o saldo máximo
#    for cliente in cliente_saldo_maximo:
#       print(cliente)

# Conte quantos clientes têm saldo acima de 1000.
#base=cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
#for clientes in base:
#   print (clientes)

# Atualize o saldo de um cliente específico.
#base = cursor.execute('UPDATE clientes SET saldo = 1000 WHERE saldo = 100 AND id = 2')

# Remova um cliente pelo seu ID.
#base=cursor.execute('DELETE from clientes WHERE id = 3')

#Crie uma segunda tabela chamada "compras" com os campos: id(chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 
# Insira algumas compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
#cursor.execute ('CREATE TABLE compras(id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_ID INTEGER, produto TEXT, valor INTEGER,FOREIGN KEY (cliente_id) REFERENCES clientes (id))')

# Inserindo dados na tabela
#cursor.execute ('INSERT INTO compras (cliente_id, produto, valor) VALUES (1,"pão",9.99)')
#cursor.execute ('INSERT INTO compras (cliente_id, produto, valor) VALUES (2,"ovo",19.99)')
#cursor.execute ('INSERT INTO compras (cliente_id, produto, valor) VALUES (4,"leite",5.99)')
#cursor.execute ('INSERT INTO compras (cliente_id, produto, valor) VALUES (4,"carne",49.99)')
#cursor.execute ('INSERT INTO compras (cliente_id, produto, valor) VALUES (4,"refrigerante",12.99)')
#cursor.execute ('INSERT INTO compras (cliente_id, produto, valor) VALUES (4,"macarrao",8.99)')

#conexao.commit ()
#conexao.close
