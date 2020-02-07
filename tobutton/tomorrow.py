import sys
import requests
import string
import pandas as pd
from bs4 import BeautifulSoup
url = 'https://www.prokerala.com/astrology/horoscope/?sign=aries&day=tomorrow'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
horodate1=[]
horotitle1=[]
hr=[]
dis=[]
table=soup.find_all("h1")
for x in table:
    #print( x.text.strip())
    g=[]
    g=x.text.split()
    #print(g)
    t0 = g[1]
    t1 = g[5]
    t2 = g[6]
    t3 = g[7]
    horodate1.append(t1+','+t2+t3)
    horotitle1.append(t0)
   
table1=soup.find_all("p")
for y in table1:
    #print( y.text.strip())
    hr.append(y.text.strip())
#print(hr)
aa=hr[1]
ab=hr[2]
ac=hr[3]
ad=hr[5]

dis.append(aa+ab+ac+ad)

url = 'https://www.prokerala.com/astrology/horoscope/?sign=taurus&day=tomorrow'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
hr1=[]
table=soup.find_all("h1")
for x in table:
    #print( x.text.strip())
    g=[]
    g=x.text.split()
    #print(g)
    t0 = g[1]
    t1 = g[5]
    t2 = g[6]
    t3 = g[7]
    horodate1.append(t1+','+t2+t3)
    horotitle1.append(t0)
  
table1=soup.find_all("p")
for y in table1:
    #print( y.text.strip())
    hr1.append(y.text.strip())
#print(hr)
aa1=hr1[1]
ab1=hr1[2]
ac1=hr1[3]
ad1=hr1[5]

dis.append(aa1+ab1+ac1+ad1)

url = 'https://www.prokerala.com/astrology/horoscope/?sign=gemini&day=tomorrow'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
hr2=[]
table=soup.find_all("h1")
for x in table:
    #print( x.text.strip())
    g=[]
    g=x.text.split()
    #print(g)
    t0 = g[1]
    t1 = g[5]
    t2 = g[6]
    t3 = g[7]
    horodate1.append(t1+','+t2+t3)
    horotitle1.append(t0)
   
table1=soup.find_all("p")
for y in table1:
    #print( y.text.strip())
    hr2.append(y.text.strip())
#print(hr)
aa2=hr2[1]
ab2=hr2[2]
ac2=hr2[3]
ad2=hr2[5]

dis.append(aa2+ab2+ac2+ad2)

url = 'https://www.prokerala.com/astrology/horoscope/?sign=cancer&day=tomorrow'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
hr3=[]
table=soup.find_all("h1")
for x in table:
    #print( x.text.strip())
    g=[]
    g=x.text.split()
    #print(g)
    t0 = g[1]
    t1 = g[5]
    t2 = g[6]
    t3 = g[7]
    horodate1.append(t1+','+t2+t3)
    horotitle1.append(t0)
    
table1=soup.find_all("p")
for y in table1:
    #print( y.text.strip())
    hr3.append(y.text.strip())
#print(hr)
aa3=hr3[1]
ab3=hr3[2]
ac3=hr3[3]
ad3=hr3[5]
dis.append(aa3+ab3+ac3+ad3)


url = 'https://www.prokerala.com/astrology/horoscope/?sign=leo&day=tomorrow'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
hr4=[]
table=soup.find_all("h1")
for x in table:
    #print( x.text.strip())
    g=[]
    g=x.text.split()
    #print(g)
    t0 = g[1]
    t1 = g[5]
    t2 = g[6]
    t3 = g[7]
    horodate1.append(t1+','+t2+t3)
    horotitle1.append(t0)
 
table1=soup.find_all("p")
for y in table1:
    #print( y.text.strip())
    hr4.append(y.text.strip())
#print(hr)
aa4=hr4[1]
ab4=hr4[2]
ac4=hr4[3]
ad4=hr4[5]
dis.append(aa4+ab4+ac4+ad4)



url = 'https://www.prokerala.com/astrology/horoscope/?sign=virgo&day=tomorrow'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
hr5=[]
table=soup.find_all("h1")
for x in table:
    #print( x.text.strip())
    g=[]
    g=x.text.split()
    #print(g)
    t0 = g[1]
    t1 = g[5]
    t2 = g[6]
    t3 = g[7]
    horodate1.append(t1+','+t2+t3)
    horotitle1.append(t0)
    
table1=soup.find_all("p")
for y in table1:
    #print( y.text.strip())
    hr5.append(y.text.strip())
#print(hr)
aa5=hr5[1]
ab5=hr5[2]
ac5=hr5[3]
ad5=hr5[5]
dis.append(aa5+ab5+ac5+ad5)



url = 'https://www.prokerala.com/astrology/horoscope/?sign=libra&day=tomorrow'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
hr6=[]
table=soup.find_all("h1")
for x in table:
    #print( x.text.strip())
    g=[]
    g=x.text.split()
    #print(g)
    t0 = g[1]
    t1 = g[5]
    t2 = g[6]
    t3 = g[7]
    horodate1.append(t1+','+t2+t3)
    horotitle1.append(t0)
   
table1=soup.find_all("p")
for y in table1:
    #print( y.text.strip())
    hr6.append(y.text.strip())
#print(hr)
aa6=hr6[1]
ab6=hr6[2]
ac6=hr6[3]
ad6=hr6[5]
dis.append(aa6+ab6+ac6+ad6)



url = 'https://www.prokerala.com/astrology/horoscope/?sign=scorpio&day=tomorrow'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
hr7=[]
table=soup.find_all("h1")
for x in table:
    #print( x.text.strip())
    g=[]
    g=x.text.split()
    #print(g)
    t0 = g[1]
    t1 = g[5]
    t2 = g[6]
    t3 = g[7]
    horodate1.append(t1+','+t2+t3)
    horotitle1.append(t0)
  
table1=soup.find_all("p")
for y in table1:
    #print( y.text.strip())
    hr7.append(y.text.strip())
#print(hr)
aa7=hr7[1]
ab7=hr7[2]
ac7=hr7[3]
ad7=hr7[5]
dis.append(aa7+ab7+ac7+ad7)




url = 'https://www.prokerala.com/astrology/horoscope/?sign=sagittarius&day=tomorrow'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
hr8=[]
table=soup.find_all("h1")
for x in table:
    #print( x.text.strip())
    g=[]
    g=x.text.split()
    #print(g)
    t0 = g[1]
    t1 = g[5]
    t2 = g[6]
    t3 = g[7]
    horodate1.append(t1+','+t2+t3)
    horotitle1.append(t0)
table1=soup.find_all("p")
for y in table1:
    #print( y.text.strip())
    hr8.append(y.text.strip())
#print(hr)
aa8=hr8[1]
ab8=hr8[2]
ac8=hr8[3]
ad8=hr8[5]
dis.append(aa8+ab8+ac8+ad8)

url = 'https://www.prokerala.com/astrology/horoscope/?sign=capricorn&day=tomorrow'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
hr9=[]
table=soup.find_all("h1")
for x in table:
    #print( x.text.strip())
    g=[]
    g=x.text.split()
    #print(g)
    t0 = g[1]
    t1 = g[5]
    t2 = g[6]
    t3 = g[7]
    horodate1.append(t1+','+t2+t3)
    horotitle1.append(t0)

table1=soup.find_all("p")
for y in table1:
    #print( y.text.strip())
    hr9.append(y.text.strip())
#print(hr)
aa9=hr9[1]
ab9=hr9[2]
ac9=hr9[3]
ad9=hr9[5]
dis.append(aa9+ab9+ac9+ad9)



url = 'https://www.prokerala.com/astrology/horoscope/?sign=aquarius&day=tomorrow'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
hr10=[]
table=soup.find_all("h1")
for x in table:
    #print( x.text.strip())
    g=[]
    g=x.text.split()
    #print(g)
    t0 = g[1]
    t1 = g[5]
    t2 = g[6]
    t3 = g[7]
    horodate1.append(t1+','+t2+t3)
    horotitle1.append(t0)
   
table1=soup.find_all("p")
for y in table1:
    #print( y.text.strip())
    hr10.append(y.text.strip())
#print(hr)
aa10=hr10[1]
ab10=hr10[2]
ac10=hr10[3]
ad10=hr10[5]
dis.append(aa10+ab10+ac10+ad10)


url = 'https://www.prokerala.com/astrology/horoscope/?sign=pisces&day=tomorrow'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
hr11=[]
table=soup.find_all("h1")
for x in table:
    #print( x.text.strip())
    g=[]
    g=x.text.split()
    #print(g)
    t0 = g[1]
    t1 = g[5]
    t2 = g[6]
    t3 = g[7]
    horodate1.append(t1+','+t2+t3)
    print(horodate1)
    horotitle1.append(t0)
    print(horotitle1)
table1=soup.find_all("p")
for y in table1:
    #print( y.text.strip())
    hr11.append(y.text.strip())
#print(hr)
aa11=hr11[1]
ab11=hr11[2]
ac11=hr11[3]
ad11=hr11[5]
dis.append(aa11+ab11+ac11+ad11)
print(dis)


df = pd.DataFrame({'horotitle1':horotitle1,'horodate1':horodate1 ,'dis': dis})
print(df)
df.to_csv(input('please insert csv file name with extension : '),index = False)



    
    
   

    






   


