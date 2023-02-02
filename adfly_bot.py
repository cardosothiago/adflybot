from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


while True:
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get_cookies()
    try:
        print('Abrindo página...')
        driver.get("http://lyksoomu.com/z2UO")
        sleep(7)
    except:
        print('Erro ao abrir página!')
    try:
        print('Clicando no botão...')
        driver.find_element(By.XPATH, "//*[@id=\"skip_bu2tton\"]").click()
        sleep(20)
        print('Sucesso! Loop executado!')
    except:
        print('Erro ao clicar no botão!')