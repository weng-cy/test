height = input('請輸入身高:')
weight = input('請輸入體重:')
height = float(height)
weight = float(weight)
height = height / 100 # 換成公尺
bmi = weight / height / height
if bmi < 18.5:
	print('體重過輕', bmi)
elif bmi >= 18.5 and bmi < 24:
	print('正常範圍', bmi) 
elif bmi >=24 and bmi < 30:
	print('輕度肥胖', bmi)
elif bmi >= 30 and bmi < 35:
	print('中度肥胖', bmi)
elif bmi >= 35:
	print('重度肥胖', bmi)
