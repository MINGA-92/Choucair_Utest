
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

#Variables Globales
global driver
global Url
global Name
global LastName
global Email
global DateBirth
global Mobile
global ModeloMobile
global OperatingSystem
global Password
global ConfirmPassword
Url= "https://utest.com/"
Name= "Sujeto"
LastName= "De Prueba"
Email= "SujetoDePrueba@Utest.com"
DateBirth= "15/04/1912"
Mobile= "Xiaomi"
ModeloMobile= "Redmi Note 8"
OperatingSystem= "Android 9"
Password= "Contraseña2*"
ConfirmPassword= "Contraseña2*"

def Registro():
	try:
		try:
			#BtnJoinToday
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/unauthenticated-container/div/div/unauthenticated-header/div/div[3]/ul[2]/li[2]/a')))
			driver.find_element(By.XPATH, '//html/body/ui-view/unauthenticated-container/div/div/unauthenticated-header/div/div[3]/ul[2]/li[2]/a').click()
			time.sleep(4)
		except:
			try:
				#Selector con JSpath
				driver.execute_script("document.querySelector('body > ui-view > unauthenticated-container > div > div > unauthenticated-header > div > div.unauthenticated-nav-bar__links.navbar-right.hidden-sm.hidden-xs > ul:nth-child(2) > li:nth-child(2) > a').click()")
				print("Ingreso Con JSpath...")
			except:
				driver.get("https://utest.com/signup/personal")
			time.sleep(4)
		driver.maximize_window()

		#Name
		try:
			#Selector con ID
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'firstName')))
			driver.find_element(By.ID,'firstName').send_keys(Name)
			time.sleep(2)	
		except:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="firstName"]')))
				driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys(Name)
			except:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[1]/input')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[1]/input').send_keys(Name)
			time.sleep(2)

		#LastName
		try:
			#Selector con ID
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'lastName')))
			driver.find_element(By.ID,'lastName').send_keys(LastName)
			time.sleep(2)	
		except:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="lastName"]')))
				driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys(LastName)
			except:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[2]/input')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[2]/input').send_keys(LastName)
			time.sleep(2)
				

		#Email
		try:
			#Selector con ID
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'email')))
			driver.find_element(By.ID,'email').send_keys(Email)
			time.sleep(2)	
		except:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="email"]')))
				driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(Email)
			except:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[3]/input')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[3]/input').send_keys(Email)
			time.sleep(2)

		#Languages
		try:
			#Selector con ID
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'languages')))
			driver.find_element(By.ID,'languages').send_keys("Spanish")

			pyautogui.press('enter')
			time.sleep(2)
		except:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="languages"]/div[1]/input')))
				driver.find_element(By.XPATH, '//*[@id="languages"]/div[1]/input').send_keys("Spanish")
			except:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[5]/div[2]/div[1]/input')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[5]/div[2]/div[1]/input').send_keys("Spanish")
			time.sleep(2)
			pyautogui.press('enter')
			time.sleep(1)
		
		#Control Fecha
		print("Fecha: ", DateBirth)
		ArrayDateBirth= []
		ArrayDateBirth= DateBirth.split("/")
		Day= ArrayDateBirth[0]
		NumeroMes= ArrayDateBirth[1]
		Year= ArrayDateBirth[2]
		
		try:
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="birthMonth"]')))
			Select= driver.find_element_by_xpath('//*[@id="birthMonth"]')
			Select.click()
		except:
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[4]/div[2]/div/div[1]/select')))
			Select= driver.find_element_by_xpath('//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[4]/div[2]/div/div[1]/select').click()
		time.sleep(2)
		
		if NumeroMes == "01":
			Option= driver.find_element_by_xpath('//*[@id="birthMonth"]/option[2]')
			Option.click()
		elif NumeroMes == "02":
			Option= driver.find_element_by_xpath('//*[@id="birthMonth"]/option[3]')
			Option.click()
		elif NumeroMes == "03":
			Option= driver.find_element_by_xpath('//*[@id="birthMonth"]/option[4]')
			Option.click()
		elif NumeroMes == "04":
			Option= driver.find_element_by_xpath('//*[@id="birthMonth"]/option[5]')
			Option.click()
		elif NumeroMes == "05":
			Option= driver.find_element_by_xpath('//*[@id="birthMonth"]/option[6]')
			Option.click()
		elif NumeroMes == "06":
			Option= driver.find_element_by_xpath('//*[@id="birthMonth"]/option[7]')
			Option.click()
		elif NumeroMes == "07":
			Option= driver.find_element_by_xpath('//*[@id="birthMonth"]/option[8]')
			Option.click()
		elif NumeroMes == "08":
			Option= driver.find_element_by_xpath('//*[@id="birthMonth"]/option[9]')
			Option.click()
		elif NumeroMes == "09":
			Option= driver.find_element_by_xpath('//*[@id="birthMonth"]/option[10]')
			Option.click()
		elif NumeroMes == "10":
			Option= driver.find_element_by_xpath('//*[@id="birthMonth"]/option[11]')
			Option.click()
		elif NumeroMes == "11":
			Option= driver.find_element_by_xpath('//*[@id="birthMonth"]/option[12]')
			Option.click()
		elif NumeroMes == "12":
			Option= driver.find_element_by_xpath('//*[@id="birthMonth"]/option[13]')
			Option.click()	

		#Day
		try:
			#Selector con ID
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'birthDay')))
			driver.find_element(By.ID,'birthDay').send_keys(Day)
			time.sleep(2)	
		except:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="birthDay"]')))
				driver.find_element(By.XPATH, '//*[@id="birthDay"]').send_keys(Day)
			except:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[4]/div[2]/div/div[2]/select')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[4]/div[2]/div/div[2]/select').send_keys(Day)
			time.sleep(2)

		#Year
		try:
			#Selector con ID
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'birthYear')))
			driver.find_element(By.ID,'birthYear').send_keys(Year)
			time.sleep(2)	
		except:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="birthYear"]')))
				driver.find_element(By.XPATH, '//*[@id="birthYear"]').send_keys(Year)
			except:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[4]/div[2]/div/div[3]/select')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[4]/div[2]/div/div[3]/select').send_keys(Year)
			time.sleep(2)

		
		#BtnNext
		try:
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[2]/a')))
			driver.find_element(By.XPATH, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[2]/a').click()
			time.sleep(5)
		except:
			try:
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[2]/a')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[2]/a').click()
			except:
				driver.execute_script("document.querySelector('#regs_container > div > div:nth-child(2) > div > div.ui-view > div > form > div.form-group.col-xs-12.text-right > a').click()")
				print("Avanzo Con JSpath...")
			time.sleep(5)


		#BtnNext_2
		try:
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[2]/div/a')))
			driver.find_element(By.XPATH, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[2]/div/a').click()
			time.sleep(5)
		except:
			try:
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[2]/div/a')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[2]/div/a').click()
			except:
				driver.execute_script("document.querySelector('#regs_container > div > div:nth-child(2) > div > div.ui-view > div > form > div:nth-child(2) > div > a').click()")
				print("Avanzo Con JSpath...")
			time.sleep(5)


		#Mobile
		try:
			#Selector con Xpath
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mobile-device"]/div[1]/div[2]/div/div[1]/span')))
			driver.find_element(By.XPATH, '//*[@id="mobile-device"]/div[1]/div[2]/div/div[1]/span').click()
			time.sleep(2)
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mobile-device"]/div[1]/div[2]/div/input[1]')))
			driver.find_element(By.XPATH, '//*[@id="mobile-device"]/div[1]/div[2]/div/input[1]').send_keys(Mobile)
		except:
			#Selector con FullXpath 
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/div[1]/span')))
			driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/div[1]/span').click()
			time.sleep(2)
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/input[1]')))
			driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/input[1]').send_keys(Mobile)
		pyautogui.press('enter')
		time.sleep(2)

		#ModeloMobile
		try:
			#Selector con Xpath
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mobile-device"]/div[2]/div[2]/div/div[1]/span')))
			driver.find_element(By.XPATH, '//*[@id="mobile-device"]/div[2]/div[2]/div/div[1]/span').click()
			time.sleep(2)
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mobile-device"]/div[2]/div[2]/div/input[1]')))
			driver.find_element(By.XPATH, '//*[@id="mobile-device"]/div[2]/div[2]/div/input[1]').send_keys(ModeloMobile)
		except:
			#Selector con FullXpath
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/div[1]/span/span[2]')))
			driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/div[1]/span/span[2]').click()
			time.sleep(2)
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/input[1]')))
			driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/input[1]').send_keys(ModeloMobile)
		pyautogui.press('enter')
		time.sleep(2)

		#OperatingSystem
		try:
			#Selector con Xpath
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mobile-device"]/div[3]/div[2]/div/div[1]/span')))
			driver.find_element(By.XPATH, '//*[@id="mobile-device"]/div[3]/div[2]/div/div[1]/span').click()
			time.sleep(2)
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mobile-device"]/div[3]/div[2]/div/input[1]')))
			driver.find_element(By.XPATH, '//*[@id="mobile-device"]/div[3]/div[2]/div/input[1]').send_keys(OperatingSystem)
		except:
			#Selector con FullXpath
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[1]/span')))
			driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[1]/span').click()
			time.sleep(2)
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[3]/div[2]/div/input[1]')))
			driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[3]/div[2]/div/input[1]').send_keys(OperatingSystem)
		pyautogui.press('enter')
		time.sleep(2)

		#BtnNext_3
		try:
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="regs_container"]/div/div[2]/div/div[2]/div/div[2]/div/a')))
			driver.find_element(By.XPATH, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/div[2]/div/a').click()
			time.sleep(5)
		except:
			try:
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[2]/div/a')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[2]/div/a').click()
			except:
				driver.execute_script("document.querySelector('#regs_container > div > div:nth-child(2) > div > div.ui-view > div > div:nth-child(2) > div > a').click()")
				print("Avanzo Con JSpath...")
			time.sleep(5)


		#Password
		try:
			#Selector con ID
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'password')))
			driver.find_element(By.ID,'password').send_keys(Password)
			time.sleep(2)	
		except:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="password"]')))
				driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Password)
			except:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[3]/div[1]/input')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[3]/div[1]/input').send_keys(Password)
			time.sleep(2)

		#ConfirmPassword
		try:
			#Selector con ID
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'confirmPassword')))
			driver.find_element(By.ID,'confirmPassword').send_keys(ConfirmPassword)
			time.sleep(2)
		except:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="confirmPassword"]')))
				driver.find_element(By.XPATH, '//*[@id="confirmPassword"]').send_keys(ConfirmPassword)
			except:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[3]/div[2]/input')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[3]/div[2]/input').send_keys(ConfirmPassword)
			time.sleep(2)


		#Check Aceptar
		try:
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[4]/label/span')))
			driver.find_element(By.XPATH, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[4]/label/span').click()
			time.sleep(2)
		except:
			try:
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[4]/label/span')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[4]/label/span').click()
			except:
				driver.execute_script('document.querySelector("#regs_container > div > div:nth-child(2) > div > div.ui-view > div > form > div:nth-child(4) > label > span").click()')
				print("Acepto Con JSpath...")
			time.sleep(2)

		#Check Aceptar2
		try:
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[5]/label/span[1]')))
			driver.find_element(By.XPATH, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[5]/label/span[1]').click()
			time.sleep(2)
		except:
			try:
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[5]/label/span[1]')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[5]/label/span[1]').click()
			except:
				driver.execute_script('document.querySelector("#regs_container > div > div:nth-child(2) > div > div.ui-view > div > form > div:nth-child(5) > label > span.checkmark.signup-consent__checkbox.error").click()')
				print("Acepto Con JSpath...")
			time.sleep(2)

		#Check Aceptar3
		try:
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[6]/label/span[1]')))
			driver.find_element(By.XPATH, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[6]/label/span[1]').click()
			time.sleep(2)
		except:
			try:
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[6]/label/span[1]')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[6]/label/span[1]').click()
			except:
				driver.execute_script('document.querySelector("#regs_container > div > div:nth-child(2) > div > div.ui-view > div > form > div:nth-child(6) > label > span.checkmark.signup-consent__checkbox.error").click()')
				print("Acepto Con JSpath...")
			time.sleep(2)


		#BtnEnviar
		try:
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="laddaBtn"]')))
			driver.find_element(By.XPATH, '//*[@id="laddaBtn"]').click()
			time.sleep(5)
		except:
			try:
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div/div/a')))
				driver.find_element(By.XPATH, '//html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div/div/a').click()
			except:
				driver.execute_script('document.querySelector("#laddaBtn").click()')
				print("Se Guardo Con JSpath...")
			time.sleep(5)

		print("¡Proceso Finalizado Con Exito!    /    (〃￣︶￣)人(￣︶￣〃) ")
	except Exception as e:
		print("☠ eRrOr:", e)
		raise e


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
			ComprobarDriver = False
			time.sleep(2)
			try:
				#Capturar De Pantalla.
				Pantallazo= pyautogui.screenshot()
				Pantallazo.save("Imagen/Capturas/eRrOr_InstalandoChrome.png")
				time.sleep(2)
			except:
				print("eRrOr=>  !No Se Guardo La Imagen!    🤔")
				pass

		print("ComprobarDriver: "+ ComprobarDriver)
		if ComprobarDriver == "OK":
			time.sleep(2)
			Registro()
		else:
			time.sleep(2)
			ChromeDriverInicial()

ChromeDriverInicial()
