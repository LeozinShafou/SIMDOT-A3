from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///PATH/denuncia.html")  # Altere PATH para sua pasta

driver.find_element(By.ID, "tipo").send_keys("Buraco na via")
driver.find_element(By.ID, "descricao").send_keys("Buraco grande em frente ao número 100.")
driver.find_element(By.ID, "endereco").send_keys("Rua Central, 100")

driver.find_element(By.ID, "enviar").click()

msg = driver.find_element(By.ID, "sucesso").text
assert "Denúncia registrada" in msg
print("Teste 2 executado: Denúncia registrada corretamente.")
driver.quit()
