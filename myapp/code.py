from bs4 import BeautifulSoup
import requests
     #flipkart.............................
def inpu(search_text):         
        newText=search_text.replace(' ', '%20')
        url="https://www.flipkart.com/search?q="+newText
        return url
def scrap(url):
      var=' '
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
    data = newSoup.findAll('div',attrs={'class':'_2_AcLJ'})
    for div in data:
        lnk=div['style']
        lnk=lnk.split('(')[1][:-1]
        break  
    return lnk,newSoup


#getting name of product
    
def  title(var,newsoup):
    for tex in newsoup.find_all(class_='_35KyD6'):
        fin=tex.text
        return fin 
#getting the base price
def price(var,newsoup):
    for price in newsoup.find_all(class_='_3auQ3N _1POkHg'):
        return price.text
def price2(var,newsoup):
    for pric in newsoup.find_all(class_='_1vC4OE _3qQ9m1'):
        return pric.text        





        #amazon......................
def inpu1(srh_txt):
    newText=srh_txt.replace(' ', '+')
    ur="https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="+newText
    return ur 

def scrap1(ur):
        var1=' '
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}
        r = requests.get(ur, headers=headers)
        soup = BeautifulSoup(r.content, "lxml") 
        counter=0
        data = soup.findAll('div',attrs={'class':'a-row a-spacing-none'})
        for div in data:
            links = div.findAll('a')
            for a in links:
                if "https://" in a['href'] and "spons" not in a['href']:
                   counter+=1
                   if(counter==1):
                        var1=a['href'] 
        return var1
def image1(var1):
    img=' '
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}
    newr = requests.get(var1, headers=headers)
    newsoup = BeautifulSoup(newr.content, "lxml")
    data = newsoup.findAll('div',attrs={'class':'imgTagWrapper'})
    for div in data:
        links = div.findAll('img')
        for a in links:
            img = a['data-old-hires']
        if "https://" not in img :
            for div in data:
                links = div.findAll('img')
                for a in links:
                    lnk=a['data-a-dynamic-image']
                    img=lnk.split(':[')[0][2:-1]  
            
    return img
def title1(var1):
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}
    newr = requests.get(var1, headers=headers)
    newsoup = BeautifulSoup(newr.content, "lxml")
    
    fin=' '
    for tex in newsoup.find_all('h1',class_='a-size-large'):
        fin=tex.text
        fin=fin.strip()
        break
    return fin
def price3(var1):
    #base price
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}
    newr = requests.get(var1, headers=headers)
    newsoup = BeautifulSoup(newr.content, "lxml")
    
    pr=' '
    for price in newsoup.find_all(class_='a-text-strike'):
        pr=price.text
    return pr
def price4(var1):
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}
    newr = requests.get(var1, headers=headers)
    newsoup = BeautifulSoup(newr.content, "lxml")
    
    #amazon price
    fin1=' '
    for pric in newsoup.find_all(id='priceblock_ourprice',class_='a-size-medium a-color-price'):
       fin1 = pric.text       
    return fin1    