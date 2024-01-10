# não faz parte da nossa automação, ele é um código independente só para que você consiga pegar a posição do mouse 

import pyautogui
import time

time.sleep(5)
print(pyautogui.position()) # pegar posicao do mouse para saber oinde clicar 
pyautogui.scroll(-200) # testar quanto de scroll