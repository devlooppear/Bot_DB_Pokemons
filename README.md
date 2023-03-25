# Introdução

- Este código utiliza a biblioteca Selenium do Python para obter informações sobre os Pokémons do site PokemonDB e armazená-las em um banco de dados Postgres. A biblioteca Selenium permite automatizar a navegação em um navegador, enquanto o banco de dados é usado para armazenar as informações dos Pokémons coletadas pelo código.

## Pré-requisitos

- Para executar este código, é necessário ter o Python 3 instalado e as bibliotecas a seguir:

- selenium
- webdriver_manager
- psycopg2
- Além disso, é necessário ter o navegador Microsoft Edge instalado em seu sistema operacional.

## Como usar

Para utilizar este código, siga as etapas abaixo:

- Instale as bibliotecas necessárias usando pip:

- pip install selenium
- pip install webdriver_manager
- pip install psycopg2

- É necessário ter o Microsoft Edge instalado, ou então, adaptar para outro navegador, o que é possível na função abaixo, presente no arquivo `comum.py`.

```python
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def Iniciar_Browser():

    servico = EdgeService(executable_path=EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=servico)
    driver.get("https://pokemondb.net/pokedex/all")

    return driver
```

- Caso queira atualizar para o Google Chrome, por exemplo, copie e cole a função abaixo no lugar da supracitada:

```python
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def Iniciar_Browser():
    servico = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)
    driver.get("https://pokemondb.net/pokedex/all")
    return driver
```

- Note que também é necessário atualizar as bibliotecas

## Funcionamento

- O código abre o navegador Microsoft Edge e acessa a página do PokemonDB contendo informações sobre todos os Pokémons. Em seguida, ele rola a página para baixo até o final para carregar todas as informações. Em seguida, ele extrai as informações de cada linha da tabela e armazena em uma lista de dicionários chamada "pokemon_data".

- Cada dicionário contém as informações do nome, tipo, descrição, pontos de vida, região e URL da imagem de cada Pokémon. A descrição é gerada aleatoriamente a partir de uma lista de frases.

- O código então insere as informações de cada Pokémon na tabela "pokemons" do banco de dados Postgres. O código verifica se um Pokémon já existe na lista "pokemon_data" e, se existir, adiciona um número ao final do nome para torná-lo único.

- O código termina a execução quando todas as informações, tratadas que foram extraídas e armazenadas no banco de dados.

## Conclusão

Esse código é uma automação, utilizando como Sistema Gerenciador de Banco de Dados (SGBD) o Postgres armazenando as informações obtidas em um banco de dados. Este código pode ser facilmente adaptado para extrair informações de outros sites e armazená-las em outros bancos de dados.