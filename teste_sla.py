import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

linhas=[7, 11, 13, 15]
for i in range (4):
    GPIO.setup(linhas[i], GPIO.OUT)
    
colunas=[29, 18, 31, 22]
for j in range (4):
    GPIO.setup(colunas[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def leitura(LINHAS,CARACTERES):
    GPIO.output(LINHAS,GPIO.HIGH)
    if (GPIO.input(colunas[0])==1):
        print(CARACTERES[0])
    if (GPIO.input(colunas[1])==1):
        print(CARACTERES[1])
    if (GPIO.input(colunas[2])==1):
        print(CARACTERES[2])
    if (GPIO.input(colunas [3])==1):
        print(CARACTERES[3])
    GPIO.output(LINHAS,GPIO.LOW)
try:
    while True:
        leitura(linhas[0],["1","2","3","A"])
        leitura(linhas[1],["4","5","6","B"])
        leitura(linhas[2],["7","8","9","C"])
        leitura(linhas[3],["*","0","#","D"])
        sleep(0.1)#Sensibilidad 
except KeyboardInterrupt:
    print("\n fim")