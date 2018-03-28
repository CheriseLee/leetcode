class Olympic:
    countryName = ''
    glodMedalNo = 0
    sliverMedalNo = 0
    bronzeMedalNo = 0
    count = 0
    def medalNo(self, glod, sliver, bronze):
        self.glodMedalNo += glod
        self.sliverMedalNo += sliver
        self.bronzeMedalNo += bronze
        self.count = self.glodMedalNo + self.sliverMedalNo + self.bronzeMedalNo

#按金牌数排行
def sortbygold(total):
    byGold = sorted(total, key = lambda x:x[1], reverse = True)
    print("======Sorted by Glod Number======")
    for x in byGold:
        z = ' '.join(map(str,x))
        print(z)


#按奖牌总数排行
def sortbyTotalNo(total):
    byTotalNo = sorted(total, key = lambda x:x[4], reverse = True)
    print("======Sorted by Total Number======")
    for x in byTotalNo:
        z = ' '.join(map(str, x))
        print(z)

China = Olympic()
China.countryName = 'China'
China.medalNo(5, 4, 6)
chinainfo = [China.countryName, China.glodMedalNo, China.sliverMedalNo, China.bronzeMedalNo, China.count]

Japan = Olympic()
Japan.countryName = 'Japan'
Japan.medalNo(1, 3, 7)
japaninfo = [Japan.countryName, Japan.glodMedalNo, Japan.sliverMedalNo, Japan.bronzeMedalNo, Japan.count]

USA = Olympic()
USA.countryName = 'USA'
USA.medalNo(2, 10, 7)
usainfo = [USA.countryName, USA.glodMedalNo, USA.sliverMedalNo, USA.bronzeMedalNo, USA.count]

total = [chinainfo, japaninfo, usainfo]

sortbygold(total)
sortbyTotalNo(total)


