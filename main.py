from comandosdb import *
from comum import *
from ETL import *

def main():

    driver = Iniciar_Browser()
    cursor = Conexao_DB()
    Criando_DB(cursor)
    Coletando_Informacoes(driver,cursor)

if __name__=='__main__':
    main()