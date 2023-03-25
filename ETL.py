from time import sleep
from selenium.webdriver.common.by import By
from random import randint

def Coletando_Informacoes(driver,cursor):

    tipo_traducao = {
    'GRASS': 'Grama',
    'POISON': 'Veneno',
    'WATER': 'Água',
    'FIGHTING': 'Lutador',
    'PSYCHIC': 'Psíquico',
    'ROCK': 'Pedra',
    'FIRE': 'Fogo',
    'STEEL': 'Aço',
    'FAIRY': 'Fada',
    'GROUND': 'Terra',
    'ELECTRIC': 'Elétrico',
    'ICE': 'Gelo',
    'FLYING': 'Voador',
    'BUG': 'Folha',
    'DARK': 'Sombrio',
    'GHOST': 'Fantasma',
    'DRAGON': 'Dragão',
    'NORMAL': 'Normal',
    }

    descricao = [
    ' muito amigável e divertido',
    ' rápido e agitado',
    ' bem selvagem, mas que pode virar um grande amigo',
    ' de grande poder',
    ' bem ágil e amável'
    ]

    regioes = [
    'Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova', 'Kalos',
    'Sevii', 'Islands', 'Orre', 'Almia', 'Ilhas Laranja'
    ]

    sleep(2)

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        if driver.execute_script("return window.pageYOffset + window.innerHeight") >= driver.execute_script("return document.body.scrollHeight"):
            break

    table = driver.find_element(By.XPATH, "//table[@id='pokedex']")

    linhas = table.find_elements(By.XPATH, ".//tbody/tr")

    pokemon_data = []

    contador = 0

    contador_nome = 0

    while contador <= 5:
        for linha in linhas:
            imagem = ''
            contador += 1
            if contador < 10:
                imagem = f"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/00{contador}.png"
            elif contador >= 10 and contador <= 99:
                imagem = f"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/0{contador}.png"
            elif contador > 99 and contador <= 999:
                imagem = f"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{contador}.png"
            elif contador > 999:
                imagem = f"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{contador}.png"
            hp = linha.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{contador}]/td[5]').text
            nome = linha.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{contador}]/td[2]/a').text       
            novo_nome = '' 

            if any(d['nome'] == nome for d in pokemon_data):
                while any(d['nome'] == nome for d in pokemon_data):
                    contador_nome += 1
                    novo_nome = linha.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{contador+contador_nome}]/td[2]/a').text
                    if "'" in novo_nome or "'" in nome:
                        nome = nome.replace("'","")
                        novo_nome = novo_nome.replace("'","")
                    nome = novo_nome
                contador_nome = 0

            if "'" in nome:
                nome = nome.replace("'","")

            tipo  = linha.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{contador}]/td[3]/a[1]').text
            if tipo in tipo_traducao:
                tipo = tipo_traducao[tipo]

            description = f'Esse é um pokemon{descricao[randint(0,len(descricao)-1)]}'
            
            hp = float(hp)

            regiao = regioes[randint(0,len(regioes)-1)]
            pokemon_data.append({
            'nome': nome,
            'tipo': tipo,
            'description': description,
            'hp': hp,
            'region': regiao,
            'image_url': imagem
            })
            sql = f'''INSERT INTO pokemons2 (nome, tipo, descricao, hp, regiao, image)
            VALUES ( '{nome}', '{tipo}', '{description}', {hp}, '{regiao}', '{imagem}');'''
            cursor.execute(sql)
    else:
        driver.quit()
    return nome,tipo,description,hp,regiao,imagem