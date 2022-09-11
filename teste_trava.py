import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import socket
import os
import time
import sqlite3

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)

# Pinos LCD x Raspberry (GPIO)
lcd_rs        = 18
lcd_en        = 23
lcd_d4        = 12
lcd_d5        = 16
lcd_d6        = 20
lcd_d7        = 21
lcd_backlight = 4

# Define numero de colunas e linhas do LCD
lcd_colunas = 16
lcd_linhas  = 2

# Inicializa o LCD nos pinos configurados acima
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                           lcd_d6, lcd_d7, lcd_colunas, lcd_linhas,
                           lcd_backlight)


# Imprime texto na primeira linha
lcd.message('Digite sua senha: \n')


#TECLADO
#linhas=[7, 11, 13, 15]
linhas=[4, 17, 27, 22]
for i in range (4):
    GPIO.setup(linhas[i], GPIO.OUT)
    
#colunas=[29, 18, 31, 22]
colunas=[5, 24, 6, 25]
for j in range (4):
    GPIO.setup(colunas[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def leitura(LINHAS,CARACTERES):
    GPIO.output(LINHAS,GPIO.HIGH)
    if (GPIO.input(colunas[0])==1):
        lcd.message(CARACTERES[0])
    if (GPIO.input(colunas[1])==1):
        lcd.message(CARACTERES[1])
    if (GPIO.input(colunas[2])==1):
        lcd.message(CARACTERES[2])
    if (GPIO.input(colunas [3])==1):
        lcd.message(CARACTERES[3])
    GPIO.output(LINHAS,GPIO.LOW)
try:
    while True:
        leitura(linhas[0],["1","2","3","A"])
        leitura(linhas[1],["4","5","6","B"])
        leitura(linhas[2],["7","8","9","C"])
        leitura(linhas[3],["*","0","#","D"])
        time.sleep(0.3)#Sensibilidad 
except KeyboardInterrupt:
    print("\n fim")



