from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///PATH/login.html")  # Altere PATH para sua pasta

assert "SIMDOT - Login" in driver.title
print("Teste 1 executado com sucesso: Página aberta corretamente.")
driver.quit()
