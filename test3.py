# _*_ coding:utf-8 _*_
import os
import time

#读取两个文件中最新信息
with open('asset.txt') as f:
    assetsInfo = f.readlines()
    asset = float(assetsInfo[0].split()[1])
    debt = float(assetsInfo[1].split()[1])
    estate = float(assetsInfo[2].split()[1])
    updateTime = assetsInfo[3].split()[1]
with open('dayAccount.txt') as g:
    dayAccount = g.readlines()

while True:
    service = input('1.查账;2.记账\n请选择服务:')
    if(service == '1'):
        while True:
            search_mode = input('\n查账模式\n1.查询最近十笔交易记录\n2.查询与某公司交易往来\n3.查询最近资产负债状况\n请选择服务:')
            if(search_mode == '1'):
                for x in dayAccount[-11:-1]:
                    print(x)
                break
            elif(search_mode == '2'):
                companyName = input('请输入公司名:')
                for x in dayAccount:
                    if x[0] == companyName:
                        print(x)
                break
            elif(search_mode == '3'):
                print('最新资产:%s\n最新负债:%s\n最新净资产:%s\n最后更新时间:%s'%(asset,debt,estate,updateTime))
                break
            else:
                print('请输入正确的选项！')

    elif(service == '2'):
        write_mode_object = input('\n记账模式\n交易对象:')
        while True:
            income = input('收入/万:')
            if income.isdigit():
                income = float(income)
                break
            else:
                print('请输入正确的数字！')
        while True:
            expend = input('支出/万:')
            if expend.isdigit():
                expend = float(expend)
                break
            else:
                print('请输入正确的数字！')
        while True:
            receivable = input('应收账款/万:')
            if receivable.isdigit():
                receivable = float(receivable)
                break
            else:
                print('请输入正确的数字！')
        while True:
            payment = input('应出账款/万:')
            if payment.isdigit():
                payment = float(payment)
                break
            else:
                print('请输入正确的数字！')
        lst = [write_mode_object,income,expend,receivable,payment]
        updateTime = time.localtime(time.time())
        lst.append(time.strftime('%Y-%m-%d %H:%M:%S',updateTime))
        #添加纪录到dayAccount 文档
        with open('dayAccount.txt','a') as g:
            g.write('\n' + ' '.join(map(str,lst)))

        asset = asset + income - expend
        debt = debt + payment - receivable
        estate = asset -debt
        print('交易已记录\n\n当前资产状况:\n最新资产:%s\n最新负债:%s\n最新净资产%s:'%(asset,debt,estate))
        with open('asset.txt','w') as f:
            f.write('最新资产(万)： %f'%asset)
            f.write('\n' + '最新负债(万)： %f'%expend)
            f.write('\n' + '最新净资产(万)： %f'%estate)
            f.write('\n' + '更新时间: %s'% time.strftime('%Y-%m-%d %H:%M:%S',updateTime))
        break

    else:
        print('请输入正确的选项！')