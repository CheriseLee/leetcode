with open('hidewords.txt','r+') as f:
    text = f.readlines()
    print(text)

data = input('please input your info:')
for x in text:
    if x.strip() in data:
        data = data.replace( x.strip().lower(),'!!')
print(data)