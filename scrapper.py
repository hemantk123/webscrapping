import requests

from bs4 import BeautifulSoup

import smtplib

url = 'https://www.amazon.in/Samsung-250GB-Internal-Solid-MZ-76E250BW/dp/B079DTMNWC/ref=sr_1_7?keywords=ssd&qid=1562418155&s=gateway&sr=8-7'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    
def check():    
    page = requests.get(url, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = price[1:7]
    converted_price = float(converted_price.replace(",", ""))
    
    if(converted_price < 4000.0):
        mail()

    print(title.strip())
    print(converted_price)

def mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('hemantkumar12380@gmail.com','hrcetowteelegdqm')

    subject = 'Utha le jldi'

    body =   'Idhar maar ungli nalle \n https://www.amazon.in/Samsung-250GB-Internal-Solid-MZ-76E250BW/dp/B079DTMNWC/ref=sr_1_7?keywords=ssd&qid=1562418155&s=gateway&sr=8-7'

    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'hemantkumar12380@gmail.com',
        'hiteshdabas2204@gmail.com',
        msg
    )
    print('Email sent')

    server.quit()


check()