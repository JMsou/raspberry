from machine import Timer, ADC, PWM, Pin, RTC
import tools

tools.connect()

adc = ADC(4) # built-in thermal sensor
pwm = PWM(Pin(15),freq=50)
rtc = RTC()
conversion_factor = 3.3/65535
'''
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
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    adc_res = ADC(0) #GP26
    duty = adc_res.read_u16()
    year, month, day, weekday, hour, minute ,second ,subsecond= rtc.datetime()
    datetime_str = f"{year}-{month}-{day} {hour}:{minute}:{second}"
    print(f'''
{datetime_str}
可變電阻阻值={round(duty/65535*10)}k
vol. = {reading}V
temp.= {temperature}C''')
    
def do_thing1(t):
    adc_res = ADC(0) #GP26
    duty = adc_res.read_u16()
    print(duty)
    pwm.duty_u16(duty)
    
    

Timer(period=1000, mode=Timer.PERIODIC, callback=do_thing)
Timer(period=1000, mode=Timer.PERIODIC, callback=do_thing1)


