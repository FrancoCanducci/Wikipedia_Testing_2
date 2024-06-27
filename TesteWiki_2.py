from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Configuração do WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Execução em modo headless (sem interface gráfica)
driver = webdriver.Chrome(options=options)

# URL do artigo na Wikipedia sobre Selenium
url = 'https://pt.wikipedia.org/wiki/Selenium_(software)'

# Iniciar contagem de tempo
start_time = time.time()

# Abrir a página
driver.get(url)

try:
    print("Aguardando o campo de busca ficar clicável...")
    # Esperar até que o campo de busca esteja presente e interagível
    search_box = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='searchInput']"))
    )
    print("Campo de busca encontrado!")

    # Digitar 'História' no campo de busca e enviar ENTER
    search_box.clear()
    search_box.send_keys('História')
    search_box.send_keys(Keys.ENTER)
    print("Termo 'História' enviado.")

    # Esperar um pouco para garantir que a página carregue completamente
    time.sleep(5)

    # Medir o tempo total
    end_time = time.time()
    total_time = end_time - start_time

    # Exibir o tempo total
    print(f'Tempo total para buscar e carregar o termo "História": {total_time:.2f} segundos')

except TimeoutException:
    print("Timeout ao tentar encontrar o campo de busca.")
    # Capturar a tela para depuração
    driver.save_screenshot('screenshot.png')
finally:
    # Fechar o navegador
    driver.quit()
