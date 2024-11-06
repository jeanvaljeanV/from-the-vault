from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura o navegador com o ChromeDriver automaticamente usando o WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL da página de livros mais vendidos na Estante Virtual
url = "https://www.estantevirtual.com.br/busca?q=mais+vendidos"
driver.get(url)

# Espera o conteúdo carregar
time.sleep(5)

# Captura o conteúdo HTML após o carregamento do JavaScript
books = driver.find_elements(By.CLASS_NAME, "livro-title")  # Ajuste a classe conforme necessário

print("Livros Mais Vendidos na Estante Virtual:")
for book in books:
    title = book.text
    print("- " + title)

input("Pressione Enter para fechar o navegador...")

# Fecha o navegador
driver.quit()


