# pip install pyautogui

import pyautogui
import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.hotkey -> atalho de teclado (ctrl, C)


# Passo 1: Abrir o sistema da empresa
# abrir o google chrome
# apertar a tecla win
pyautogui.press("win")

# digitar o texto chrome
pyautogui.write("chrome")
# apertar enter
pyautogui.press("enter")

#    Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# pedir pro computador esperar 3 segundos
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=266, y=489)
pyautogui.write("gabrielpascoal@gmail.com")

pyautogui.press("tab") # passa para o campo da senha
pyautogui.write("pascoal")

pyautogui.press("tab") # passa para o botão "logar"
pyautogui.press("enter")

# Passo 3: Importar a base de dados dos produtos
# pip install pandas openpyxl
import pandas as pd

tabela = pd.read_csv(r"C:\Users\gabri\Desktop\PYTHON POWERUP\Gabarito\produtos.csv")

print(tabela)

time.sleep(2) # precaução
# Passo 4: Cadastrar 1 produto

for linha in tabela.index:
    pyautogui.click(x=211, y=356) # clica no 1° campo

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs) # opcional
    pyautogui.press("tab")

    pyautogui.press("enter") # apertar o botao de enviar

    # numero positivo = scroll para cima
    # numero negativo = scroll para baixo
    pyautogui.scroll(10000)

# Passo 5: Repetir o passo 4 até acabar os produtos

# nan = valor vazio  em uma base de dados
# Not a Number
