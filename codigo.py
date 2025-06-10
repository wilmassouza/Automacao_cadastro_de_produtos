## Automatização cadastro de produtos

# Importação das bibliotecas
import pyautogui
import time


pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
# Abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# digitar o site 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# ESPERA 3 SEGUNDOS
time.sleep(3)

# Passo 2: Fazer login
# preencher e-mail
pyautogui.click(x=669, y=469)
pyautogui.write("wilmasilv@hotmail.com")

# preencher a senha
pyautogui.press("tab")
pyautogui.write("senhasecreta")
 
# botão logar
pyautogui.press("tab")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=606, y=322)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.press("enter") #cadastra o produto (botão enviar)
    pyautogui.scroll(5000) #dar scroll de tudo para cima
    #repetir o processo até o fim


    
