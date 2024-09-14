# import tools #自訂的module檔案就是.py，這次module檔名叫tools
import widget

while True:
    height = 0
    weight = 0
    cm, kg = widget.input_data() #呼叫子程式

    print(f'身高={cm}，體重={kg}')
    BMI = widget.calculate_bmi(weight=kg,height=cm)
    # 引數名稱呼叫 parameter = argument；優點可以不依照順序
    print(f'你的BMI值是{BMI}')
    print(widget.get_status(BMI))

    play_again = input('還要繼續算BMI嗎？(y,n)')
    if play_again == 'n':
        break

print("BMI計算結束")
