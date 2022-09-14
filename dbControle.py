import sqlite3

con = sqlite3.connect("./dados.db")
cur = con.cursor()

# criar tabela de nomes e senhas
def criarTabelaDados():
  cur.execute('''
    CREATE TABLE IF NOT EXISTS dados (
      matricula INTEGER PRIMARY KEY, 
      nome TEXT, 
      senha TEXT
    )'''
)

# criar tabela de entradas e saidas 
def criaTabelaES():
  cur.execute('''
  CREATE TABLE IF NOT EXISTS entrada_saida (
    horario DATETIME, 
    nome TEXT,
    acao TEXT
  )'''
  )

# inserir dados na tabela de dados
# data = [
#  (20200099305, "Thullyo", '1235'),
#  (20210054405, "Breno Rocha Fonseca", '124578'),
#  (20210029206, "Newton Leonardo Leite Filho" , '218100'),
# ]
def inserirDados(data):
  cur.executemany("INSERT INTO dados VALUES(?, ?, ?)", data)
  con.commit()

# alterar dados na tabela de dados
# matricula = 0
# senha = ''


def atualizarDados(matricula, senha):
  dados = [senha, matricula]
  cur.execute("UPDATE dados SET senha = ? WHERE matricula = ?", dados)
  con.commit()

# encontrar alguem na tabela de dados
def encontrarPessoa(matricula, senha):
  dados = [matricula, senha]
  cur.execute('''
    SELECT matricula, nome, senha
    FROM dados 
    WHERE matricula = ? AND senha = ?
    ''', 
    dados)
  
  encontrado = cur.fetchone()

  return encontrado

# criar entrada na tabela de acao
def inserirEntradaSaida(data):
  cur.executemany("INSERT INTO entrada_saida VALUES (?, ?, ?)", data)
  con.commit()

# pegar tabela de entrada e saida
def pegarTabela():
  cur.execute("SELECT * FROM entrada_saida")
  tabela = cur.fetchall()

  return tabela

def ultimo_valor():
  cur.execute("SELECT * FROM entrada_saida ORDER BY horario DESC")
  valor = cur.fetchone()

  return valor
## Chamar as funções aqui embaixo caso seja necessario alguma delas
# sequencia -> criar, inserir dados