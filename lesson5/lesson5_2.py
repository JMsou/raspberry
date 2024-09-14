def input_data():
    while True:
        try:
            height = int(input('請輸入身高(公分)：'))
            if height > 300 or height < 0:
                raise Exception('身高請輸入300公分以內')
            break
        except ValueError:
            print('輸入格式錯誤')
            continue
        except Exception as e:
            print(e)
            continue
        
    while True:    
        try:
            weight = int(input('請輸入體重(公斤)：'))
            if weight < 0:
                raise Exception('請輸入正確體重')
            break
        except ValueError:
            print('輸入格式錯誤')
            continue
        except Exception as e:
            print(e)
            continue
    return (height,weight)

while True:
    height = 0
    weight = 0
    height, weight = input_data() #呼叫子程式

    BMI = weight/((height/100)**2)
    print(f'你的BMI值是{BMI}')
    if BMI<18.5:
        print('您的體重過輕')
    elif BMI<24:
        print('您的體重正常')
    elif BMI<27:
        print('您的體重過重')
    elif BMI<30:
        print('您現在輕度肥胖')
    elif BMI<35:
        print('您現在中度肥胖')
    else:
        print('您現在重度肥胖')

    play_again = input('還要繼續算BMI嗎？(y,n)')
    if play_again == 'n':
        break

print("BMI計算結束")
