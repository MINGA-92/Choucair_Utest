
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from datetime import  datetime as Date
from selenium import webdriver
from selenium import webdriver

import pyautogui
import time
import sys
import os

global driver
global Url
Url= "https://utest.com/"

def Registro():
	#BtnIngresar
	try:
		WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/unauthenticated-container/div/div/unauthenticated-header/div/div[3]/ul[2]/li[2]/a')))
		driver.find_element(By.XPATH, '//html/body/ui-view/unauthenticated-container/div/div/unauthenticated-header/div/div[3]/ul[2]/li[2]/a').click()
		time.sleep(4)
	except:
		driver.execute_script("document.querySelector('body > ui-view > unauthenticated-container > div > div > unauthenticated-header > div > div.unauthenticated-nav-bar__links.navbar-right.hidden-sm.hidden-xs > ul:nth-child(2) > li:nth-child(2) > a').click()")
		print("Ingreso Con JS...")
		time.sleep(4)



def ChromeDriverInicial():

	global driver
	os.system("TASKKILL /F /IM geckodriver.exe")
	os.system("TASKKILL /F /IM chromedriver.exe")
	RutaEjecutablePrograma = os.path.dirname(sys.argv[0]) + "\\"
	ComprobarDriver= " "
	
	try:
		RutaChromeDriver= RutaEjecutablePrograma + 'chromedriver.exe'
		ChromeOption= webdriver.ChromeOptions()
		driver = webdriver.Chrome(executable_path=RutaChromeDriver, options=ChromeOption)
		driver.set_window_rect(x=392, y=11, width=1128, height=911)
		driver.get(Url)
		time.sleep(2)
		print("Ingresando A= " +(driver.current_url)+ " ...")
		#driver.maximize_window()
		ComprobarDriver= "OK"
	except Exception as e:
		#raise e
		print("☠ Error / En El Driver De Chrome  😪")
		ComprobarDriver= "False"

	print("ComprobarDriver: "+ ComprobarDriver)
	if ComprobarDriver == "OK":
		time.sleep(2)
		Registro()
	else: 	
		try:
			print("Instalando Chrome...")
			time.sleep(2)
			driver = webdriver.Chrome(ChromeDriverManager().install())
			driver.set_window_rect(x=392, y=11, width=1128, height=911)
			driver.get(Url)
			print("Ingresando A= " +(driver.current_url)+ " ...")
			ComprobarDriver= "OK"
			time.sleep(2)
			
		except Exception as e:
			print("☠ eRrOr Instalando Chrome... ☠" + str(e))
			ComprobarDriver = "False"
			time.sleep(2)
			try:
				#Capturar De Pantalla.
				Pantallazo= pyautogui.screenshot()
				Pantallazo.save("Imagen/Capturas/eRrOr_InstalandoChrome.png")
				time.sleep(2)
			except:
				print("eRrOr=>  !No Se Guardo La Imagen!    🤔")
				pass

ChromeDriverInicial()
