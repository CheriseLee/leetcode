height = float(input("please input your height(m):"))
weight = float(input("please input your weight(kg):"))
BMI = weight/(height * height)
if(BMI <18.5):
    print("体重偏轻")
elif(18.5 < BMI <24):
    print("体重正常")
else:
    print("体重偏重")
                
