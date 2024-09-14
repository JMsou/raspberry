def input_data()->tuple[int,int]:
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

def get_status(bmi:float)->str:
    if bmi<18.5:
        return '您的體重過輕'
    elif bmi<24:
        return '您的體重正常'
    elif bmi<27:
        return '您的體重過重'
    elif bmi<30:
        return '您現在輕度肥胖'
    elif bmi<35:
        return '您現在中度肥胖'
    else:
        return '您現在重度肥胖'
    
def calculate_bmi(height:int, weight:int)->float:
    BMI = weight/((height/100)**2)
    return BMI  #子程式的BMI只是區域變數，只有子程式內在用而已