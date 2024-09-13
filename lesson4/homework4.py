try:
    height = int(input('請輸入身高(公分)：'))
    weight = int(input('請輸入體重(公斤)：'))
    if height > 300 or height < 0:
        raise Exception('身高請輸入300公分以內')
    if weight < 0:
        raise Exception('請輸入正確體重')
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
    
except ValueError:
    print('請輸入純數字')
except Exception as e:
    print(e)
print('END')