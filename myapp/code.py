from bs4 import BeautifulSoup
import requests
     #flipkart.............................
def inpu(search_text):         
        newText=search_text.replace(' ', '%20')
        url="https://www.flipkart.com/search?q="+newText
        return url
def scrap(url):
      req=requests.get(url)
      soupe = BeautifulSoup(req.text,'html.parser')  
      #finding the link of first item
      for link in soupe.find_all(attrs={'class': '_3O0U0u'}):
            for ab in link.find_all('a', href=True):
                var= ab['href'] 
                break
            break 
      var= 'https://www.flipkart.com'+ var      
      return var
def image(var):
    newReq=requests.get(var)
    newSoup=BeautifulSoup(newReq.text,'html.parser')
    i=[]
    count=0
    for n in newSoup.find_all('img'):
        i.append(n['src'])
        for t in i:
            if 'https' in t.split(':'):
                count+=1
                if(count==2):
                    return t


#getting name of product
    
def  title(var):
    ndreq=requests.get(var)
    soop=BeautifulSoup(ndreq.text,'html.parser')
    for tex in soop.find_all(class_='_35KyD6'):
        fin=tex.text
        return fin 
#getting the base price
def price(var):
    rdreq=requests.get(var)
    suop=BeautifulSoup(rdreq.text,'html.parser')
    for price in suop.find_all(class_='_3auQ3N _1POkHg'):
        return price.text
def price2(var):
    dreq=requests.get(var)
    suo=BeautifulSoup(dreq.text,'html.parser')
    for pric in suo.find_all(class_='_1vC4OE _3qQ9m1'):
        return pric.text        





        #amazon......................
def inpu1(srh_txt):
    newText=srh_txt.replace(' ', '+')
    ur="https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="+newText
    return ur 
def scrap1(ur):
        var1=' '
        req=requests.get(ur)
        soup = BeautifulSoup(req.text,'html.parser')
        
        for link in soup.find_all(attrs={'class': 'a-row a-spacing-none'}):
            for a in link.find_all('a', href=True):
                var1= a['href']      
            break
        if(var1==' '):
            l=[]
            var1=' '
            for link in soup.find_all(class_='a-row a-spacing-mini'):
                for a in link.find_all('a', href=True):
                    l.append(a['href'])
                    for i in l:
                        if 'https' in i.split(':'):
                            var1=i
                            break   
        return var1
def image1(var1):
    img=' '
    newReq=requests.get(var1)
    newSoup=BeautifulSoup(newReq.text,'html.parser')
    for ne in newSoup.find_all(class_='imgTagWrapper'):
       for link in ne.find_all('img',src=True):
             img=link['src']
    return img
def title1(var1):
    fin=' '
    ndreq=requests.get(var1)
    soop=BeautifulSoup(ndreq.text,'html.parser')
    for tex in soop.find_all('h1',class_='a-size-large'):
        fin=tex.text
        fin=fin.strip()            
    return fin
def price3(var1):
    #base price
    pr=' '
    rdreq=requests.get(var1)
    suop=BeautifulSoup(rdreq.text,'html.parser')
    for price in suop.find_all(class_='a-text-strike'):
        pr=price.text
    return pr
def price4(var1):
    #amazon price
    fin1=' '
    dreq=requests.get(var1)
    suo=BeautifulSoup(dreq.text,'html.parser')
    for pric in suo.find_all(id='priceblock_ourprice',class_='a-size-medium a-color-price'):
       fin1 = pric.text       
    return fin1    