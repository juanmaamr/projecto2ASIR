# Realizado por: Juan Manuel Medina Ruiz
# Basado en las librerias Adafruit CircuitPython & SSD1306 Libraries
import time
import board
import busio
import digitalio

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

# Definimos el pin reset de nuestra pantalla
oled_reset = digitalio.DigitalInOut(board.D4)

# Parametros de configuración de pantalla
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Usamos I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Limpiamos la pantalla.
oled.fill(0)
oled.show()

# Creamos una imagen en blanco.
# La creamos en modo 1 con un 1-bit de color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Dibuja un fondo en blanco
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

font = ImageFont.truetype('/bin/OLED_Stats/PixelOperator.ttf', 16)


while True:

    # Dibuja un cuadrado negro para limpiar la imagen
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Variables que vamos a usar para mostrar por pantalla
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "df -h | awk '$NF==\"/media/descargas\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True )

    # Esto es lo que se  va a mostrar por pantalla
    draw.text((0, 0),"Bienvenido :)", font=font, fill=255)
    draw.text((0, 16),"Usa la siguiente IP", font=font, fill=255)
    draw.text((0, 33), "IP: " + str(IP,'utf-8'), font=font, fill=255)
    draw.text((0, 48), str(Disk,'utf-8'), font=font, fill=255)
        
    # Muestra la imagen
    oled.image(image)
    oled.show()
    time.sleep(.5)

