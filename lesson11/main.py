#! usr/bin/micropython

'''
LED -> GPIO15
可變電阻 -> GPIO26
光敏電阻 -> GPIO28
Thermal sensor -> adc最後1pin,共5pin
'''

from machine import Timer, ADC, PWM, Pin, RTC
import tools
from umqtt.simple import MQTTClient
import binascii

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
    負責RTC、可變電阻、光線及內建溫度，目前每1秒執行一次
    '''
    
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    adc_res = ADC(0) #GP26
    duty = adc_res.read_u16()
    light_level = round(duty/65535*10)
    year, month, day, weekday, hour, minute ,second ,subsecond= rtc.datetime()
    adc_value = adc_light.read_u16()
    datetime_str = f"{year}-{month}-{day} {hour}:{minute}:{second}"
    print(f'''
{datetime_str}
可變電阻阻值={light_level}k
光線={adc_value}
vol. = {reading}V
temp.= {temperature}C''')
    mqtt.publish('SA-52/LED_LEVEL', f'{light_level}')
    
def do_thing1(t):
    '''
    這是顯示可變電阻轉變出的16bits值
    '''
    adc_res = ADC(0) #GP26
    duty = adc_res.read_u16()
    print(duty)
    pwm.duty_u16(duty)
    

def main():
    try:
        tools.connect()
    except RuntimeError as e:
        print(e)
    except Exception:
        print('莫名失敗')
    else:    
        Timer(period=1000, mode=Timer.PERIODIC, callback=do_thing)
        Timer(period=1000, mode=Timer.PERIODIC, callback=do_thing1)
    
if __name__ == "__main__":
    adc = ADC(4) # built-in thermal sensor
    adc_light = ADC(Pin(28))
    pwm = PWM(Pin(15),freq=50)
    rtc = RTC()
    conversion_factor = 3.3/65535
    
    #MQTT
    SERVER = "192.168.0.252"
    CLIENT_ID = binascii.hexlify(machine.unique_id())
    mqtt = MQTTClient(CLIENT_ID, SERVER,user='pi',password='raspberry')
    mqtt.connect()
    
    #執行主程式
    main()
    




