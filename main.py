
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests
import csv
import pprint




f = open("temp_stock_database.csv")
reader = csv.reader(f)
l = [row for row in reader]
f.close()
ll = l[0][0]
print(l)
my_url2 = "https://stocks.finance.yahoo.co.jp/us/history/"
my_url3 = l[0][0]
my_url4 = my_url2+my_url3
print(my_url4)


print(" ")
iter = 0
fruits = ["apple", "banana", "cherry"]
for x in  l:
    my_url = "https://stocks.finance.yahoo.co.jp/us/history/"
    my_url5 = l[iter][0]
    my_url6 = my_url+my_url5
    try:
        uClient = uReq(my_url6)
        page_html = uClient.read()
        uClient.close()
         #html parser
        page_soup = soup(page_html,"html.parser")
        containers3 = page_soup.find_all("td")
        #####
        contain3 = containers3[7]
        name = "NO."+str(iter)+ " "+my_url5+" End1:" + contain3.text.strip()
        print(name)
        #####
        #####
        contain4 = containers3[14]
        name = "NO."+str(iter)+ " "+my_url5+" End2:" + contain4.text.strip()
        print(name)
        #####
        #####
        contain5 = containers3[21]
        name = "NO."+str(iter)+ " "+my_url5+" End3:" + contain5.text.strip()
        print(name)
        #####
        #####
        contain6 = containers3[28]
        name = "NO."+str(iter)+ " "+my_url5+" End4:" + contain6.text.strip()
        print(name)
        #####
        #####
        contain7 = containers3[35]
        name = "NO."+str(iter)+ " "+my_url5+" End5:" + contain7.text.strip()
        print(name)
        #####
        if( (float(contain3.text.strip())-float(contain4.text.strip())) > 0):
            print("----------------------------------------------------------------------------->row1 "+my_url6)
            if((float(contain4.text.strip())-float(contain5.text.strip())) > 0):
                print("----------------------------------------------------------------------------->row2 "+my_url6)
                if( (float(contain5.text.strip())-float(contain6.text.strip())) > 0):
                    print("----------------------------------------------------------------------------->row3 "+my_url6)
                    if( (float(contain6.text.strip())-float(contain7.text.strip())) > 0):
                        print("----------------------------------------------------------------------------->row4 "+my_url6)
                                    
        print("/////")
        iter +=1
        
    except:
        name = str(iter)+ " pass" 
        print(name)
        iter +=1
        print("/////")
        pass



print("finish")

