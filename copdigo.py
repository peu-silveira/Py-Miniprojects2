# Automacao

import pyautogui # biblioteca que vai permitir com que você controle o mouse e o seu teclado para fazer as automações no seu computador utilizando o Python
import pandas as pd
import time 

# importar a base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)

# 1) Abrir o navegador 

# definir o tempo de espera entre os comandos do pyautogui
pyautogui.PAUSE = 0.5

# abrir o sistema (no caso, o chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera carregar
time.sleep(5)

# 2) Acessar o site do sistema com login e senha

pyautogui.click(x=723, y=407)
pyautogui.write("pythonalgo@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.click(x=697, y=564)

# 3) Inserir todas as informacoes do produto 

# para cada linha da tabela, vamos cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=690, y=290) # clica no primeiro campo
    pyautogui.write(str(tabela.loc[linha, "codigo"])) # pega o codigo da tabela e escreve no campo
    pyautogui.press("tab") # aperta tab para ir pro proximo campo
    # agora, repetir isso para todos os outros campos
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
    pyautogui.write(str(tabela.loc[linha, "obs"]))

    # enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000) # pra voltar ao topo do formulario
    