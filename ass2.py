import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import adafruit_mpl3115a2
import time

# Size of display
WIDTH = 128
HEIGHT = 64

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# Initialize sensor
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

while True:
    
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)

    # Read sensor values
    pressure = sensor.pressure
    pressureSTR = 'Pressure: {0:0.3f} Pa'.format(pressure)
    temperature = sensor.temperature
    temperatureSTR = 'Temp: {0:0.1f} C'.format(temperature)

    # text position
    bbox = font.getbbox(temperatureSTR)
    (font_width, font_height) = bbox[2] - bbox[0], bbox[3] - bbox[1]
    temp_text_x = oled.width // 2 - font_width // 2
    temp_text_y = oled.height // 4 - font_height // 2

    pressure_bbox = font.getbbox(pressureSTR)
    (pressure_font_width, pressure_font_height) = pressure_bbox[2] - pressure_bbox[0], pressure_bbox>
    pressure_text_x = oled.width // 2 - pressure_font_width // 2
    pressure_text_y = 3 * (oled.height // 4) - pressure_font_height // 2

    # Draw text
    draw.text((temp_text_x, temp_text_y), temperatureSTR, font=font, fill=255)
    draw.text((pressure_text_x, pressure_text_y), pressureSTR, font=font, fill=255)

    # Display image
    oled.image(image)
    oled.show()

    time.sleep(1.0)
