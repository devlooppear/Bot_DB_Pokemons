from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
import psycopg2

def Iniciar_Browser():

    servico = EdgeService(executable_path=EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=servico)
    driver.get("https://pokemondb.net/pokedex/all")
    return driver

def Conexao_DB():

    conn = psycopg2.connect(
        database="pokemon",
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor