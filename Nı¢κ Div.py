import pyautogui
import pyperclip
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import json

def ler_dados():
    with open('dados.json', 'r', encoding='utf8') as f:
        return json.load(f)

def date_function_w(dados):
    with open('save_system.json', 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))

def date_function_r():
    with open('save_system.json', 'r') as b:
        return json.load(b)

dados = ler_dados()
email = dados[0]
password = dados[1]

date_system = date_function_r()

save_system_on = str(input(f'''\033[33mRestaurar progresso? (y) para sim (n) para não 
\033[33mServidor {date_system["servidor"]},
Limitador {date_system["limitador"]},
Contador {date_system["contador"]},
Delay {date_system["delay"]}
\033[32mDigite Aqui: '''))

if save_system_on.lower() == 'y':
    servidor = date_system["servidor"]
    vezes = date_system["limitador"]
    cont = date_system["contador"]
    delay = date_system["delay"]
elif save_system_on.lower() == 'n':
    servidor = input('Digite o nome do servidor em que você deseja divulgar!: ')
    vezes = int(input('Digite a quantidade de pessoas que deseja divulgar!: '))
    cont = int(input('Digite a quantidade de pessoas que deseja evitar da staff!: '))
    delay = int(input('Digite o delay de mensagens em segundos!: '))
else:
    print('\033[31mVocê digitou algo errado!')

navegador = webdriver.Chrome()
navegador.get('https://discord.com/login')
elem = navegador.find_element_by_name('email')
elem.clear()
elem.send_keys(email)
elem = navegador.find_element_by_name('password')
elem.clear()
elem.send_keys(password + Keys.ENTER)
navegador.implicitly_wait(10)
elem = navegador.find_element_by_class_name('searchBarComponent-32dTOx')
elem.click()
navegador.implicitly_wait(10)
elem = navegador.find_element_by_xpath('//*[@id="app-mount"]/div[4]/div[2]/div/div/div/input')
elem.clear()
elem.send_keys(servidor)
elem.send_keys(Keys.ENTER)

for i in range(0,vezes):
    navegador.implicitly_wait(10)
    navegador.find_element_by_xpath('//div//h2[@class= "membersGroup-v9BXpm container-2ax-kl"]').click()
    for a in range(0, cont):
        pyautogui.press('down')
    sleep(2)
    pyautogui.press('enter')
    navegador.implicitly_wait(10)
    elem = navegador.find_element_by_tag_name('input')
    elem.click()
    pyperclip.copy('👽**Estamos distribuindo 🌀Nitro Free e 💎5600 Diamantes no Free Fire💎 para todo mundo!!**👽')
    pyautogui.hotkey('ctrl', 'v')
    elem.send_keys(Keys.ENTER)
    # pyperclip.copy('@')
    sleep(3)
    # pyautogui.hotkey('ctrl', 'v')
    # pyautogui.press('enter')
    pyperclip.copy('👉  🏆 https://discord.gg/kXygSsWdX2 🏆  👈')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    # pyperclip.copy('https://media1.tenor.com/images/89acee0d42460e342339fd0ebd912676/tenor.gif?itemid=18776841')
    # pyautogui.hotkey('ctrl', 'v')
    # pyautogui.press('enter')
    # pyperclip.copy('@')
    # pyautogui.hotkey('ctrl', 'v')
    # pyautogui.press('enter')
    # pyperclip.copy('**👉Não perca essa oportunidade unica e venha logo garantir o seu!**')
    # pyautogui.hotkey('ctrl', 'v')
    # pyautogui.press('enter')
    # pyperclip.copy('🏆 https://discord.gg/Y4zbTAZd74 🏆')
    # pyautogui.hotkey('ctrl', 'v')
    # pyautogui.press('enter')
    navegador.back()
    sleep(delay)
    cont += 1
    save_system = {
        'servidor': servidor,
        'limitador': vezes,
        'contador': cont,
        'delay': delay
    }
    date_function_w(save_system)