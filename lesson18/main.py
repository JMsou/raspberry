#! usr/bin/micropython

'''
LED -> GPIO15
可變電阻 -> GPIO26
光敏電阻 -> GPIO28
Thermal sensor -> adc最後1pin,共5pin
'''

from machine import Timer, ADC, PWM, Pin, RTC
import binascii
from umqtt.simple import MQTTClient
import tools,config

'''
解釋內建溫度感測器測出的電壓如何轉換成現實溫度
while True:  
    reading = adc.read_u16() * conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    temperature = 27 - (reading - 0.706)/0.001721
    print(f'{reading}V')
    print(f'{temperature}C')
    time.sleep(1)
'''
def do_thing(t):
    '''
    :param t:Timer的實體
    負責可變電阻、內建溫度、光線及RTC，目前每1秒執行一次
    '''
    adc_res = ADC(0) #GP26
    duty = adc_res.read_u16()
    light_level = round(duty/65535*10)
    mqtt.publish('SA-52/LED_LEVEL', f'{light_level}')
    blynk_mqtt.publish('ds/led_level', f'{light_level}')
    
    reading = adc.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706)/0.001721,2)
    mqtt.publish('SA-52/TEMPERATURE', f'{temperature}')
    
    adc_value = adc_light.read_u16()
    light_state = 0 if adc_value < 1000 else 1
    mqtt.publish('SA-52/LIGHT_STATE', f'{light_state}')
    
    year, month, day, weekday, hour, minute ,second ,subsecond= rtc.datetime()
    datetime_str = f"{year}-{month}-{day} {hour}:{minute}:{second}"
    print(f'''
{datetime_str}
可變電阻阻值={light_level}k
光線={adc_value} -> {light_state}
vol. = {reading}V
temp.= {temperature}°C''')
    
def do_thing1(t):
    '''
    這是顯示可變電阻轉變出的16bits值
    '''
    adc_res = ADC(0) #GP26
    duty = adc_res.read_u16()
    print(duty)
    pwm.duty_u16(duty)
    

def main():
    global blynk_mqtt
    print(config.BLYNK_MQTT_BROKER)
    print(config.BLYNK_TEMPLATE_ID)
    print(config.BLYNK_AUTH_TOKEN)
    blynk_mqtt = MQTTClient(config.BLYNK_TEMPLATE_ID, config.BLYNK_MQTT_BROKER,user='device',password=config.BLYNK_AUTH_TOKEN,keepalive=60)
    blynk_mqtt.connect
    
    
if __name__ == "__main__":
    adc = ADC(4) # built-in thermal sensor
    adc_light = ADC(Pin(28))
    pwm = PWM(Pin(15),freq=50)
    rtc = RTC()
    conversion_factor = 3.3/65535
    
    #連進區域Wifi
    try:
        tools.connect()
    except RuntimeError as e:
        print(e)
    except Exception:
        print('莫名失敗')
    else:
        #MQTT
        SERVER = "192.168.0.252"
        CLIENT_ID = binascii.hexlify(machine.unique_id())
        mqtt = MQTTClient(CLIENT_ID, SERVER,user='pi',password='raspberry')
        mqtt.connect()
        Timer(period=5000, mode=Timer.PERIODIC, callback=do_thing)
        Timer(period=5000, mode=Timer.PERIODIC, callback=do_thing1)
    blynk_mqtt = None        
    
    
    #執行主程式
    main()
    






