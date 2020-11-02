from selenium import webdriver
import sys


# funcao que converte uma lista em string
def convert(s):
    str1 = ""
    return str1.join(s)


# assimila os argumentos para uma variavel search_string
search_string = sys.argv[1:]

# converte os argumentos de lista para string
search_string = convert(search_string)

# transforma a string em url de busca
search_string = search_string.replace(' ', '+')

# atribui o webdriver, que no caso eh do chrome
browser = webdriver.Chrome('chromedriver')

for i in range(1):
    matched_elements = browser.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))
