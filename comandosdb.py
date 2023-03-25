def Criando_DB(cursor):
    
    sql = ('DROP TABLE IF EXISTS pokemons2;')
    cursor.execute(sql)
    sql = ('''CREATE TABLE IF NOT EXISTS pokemons2(
    id SERIAL,
    nome VARCHAR(50) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    hp FLOAT NOT NULL,
    regiao VARCHAR(50) NOT NULL,
    image VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
    );''')
    cursor.execute(sql)