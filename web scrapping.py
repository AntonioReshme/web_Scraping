# This code scrap the product from amazon website

from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.amazon.in/Beats-Wireless-Bluetooth-Cancelling-Headphones/dp/B0CBW7SVSC/ref=sr_1_17?crid=3AXZYIFDPQMZZ&dib=eyJ2IjoiMSJ9.hM-J2emRQ6T-dO11HZt-2n-YHXEO7kk42phku_x2bpUl5vCBDwrU11182jCumnvUpi4AYjgq-2t2n7xTWEVYVOpBk6cZvE8lNUhItcepaGmpTvdSlucIE7V-vSTTR6-3v4IcOKxRsKKbcUpfVZb_g6CzeYQfzozttSkybCRcpd-IDJaSbwx6E7Szt-ohyLEPerAIOGcyIgx_xNNGVcxdI101TjWVOXRtrlqu2TJA27AluLGa7JZlLdlfKJJo8dwH-6hR0G7UOuyCXYIg-tqUizBIVhp0lfvVGrBMcSZ1tiYmz2Xs5KJIa3UeCyCQqVbtT_5WfafVttMLXV36USQLoUVbNMSeq-8ub3dchEqkTUo.gOlw8UNe6jUoEtbC1tfXrwOYfHO4ShUCppSj34zo_Y0&dib_tag=se&keywords=apple+headphones+pro+max&nsdOptOutParam=true&qid=1741431068&refinements=p_n_format_browse-bin%3A30678584031&rnid=30678575031&s=electronics&sprefix=apple+headphones+pro+max%2Caps%2C271&sr=1-17"
headers={"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"}

response = requests.get(url,headers=headers)
if response.status_code==200:
    print(response.status_code)
    html_content = response.text
else:
    print("Fetching errors",response.status_code)
soup = BeautifulSoup(html_content,"lxml")
#print(soup.prettify())
product_title = soup.find("span",id="productTitle").text.strip()
print(product_title)
product_price = soup.find("span",class_="a-price-whole").text.strip()
print(product_price)
product_rating = soup.find("span",id="acrPopover").text.strip()
print(product_rating)
product_bp = soup.find("ul",class_="a-unordered-list a-vertical a-spacing-mini").text.strip()
print(product_bp)
product_description = soup.find("div",id="prodDetails").text.strip()
print(product_description)
product_reviews = soup.find("span",class_="global-reviews-all").text.strip()
print(product_reviews)

# saving the data

with open("amazon_airpod.csv",mode="w",newline='')as file:
    writer = csv.writer(file)
    writer.writerow(["product_title","product_price","product_rating","product_bp","product_description","product_reviews"])

    writer.writerow(["Beats Studio Pro- Wireless Bluetooth Noise Cancelling Headphones - Spatial Audio, USB-C, Up to 40H Battery Life, 10 min Fast Charge for 4H Battery Life, Apple & Android Compatible - Sandstone",37805,"3.5  3.5 out of 5 stars","Beats' custom acoustic platform delivers rich, immersive sound whether you’re listening to music or taking calls. Lossless audio via USB-C plus three distinct built-in sound profiles to enhance your listening experience. Hear what you want with two distinct listening modes: fully-adaptive Active Noise Cancelling (ANC) and Transparency mode. Enhanced compatibility with one-touch pairing and a robust set of native Apple and Android features. Personlized spatial audio with dynamic head tracking place you at the center of an immersive 360-degree listening experience    Longer Listening with up to 40 hours total battery life. A 10-minute Fast Fuel charge provides up to 4 hours of additional playback    Loud and Clear voice-targeting mics precisely filter background noise for crisp, clear call performance","Manufacturer   Beats, Apple Inc, One Apple PPark Way, Cupertino, CA 95014, USA. or Apple India Private Limited No.24, 19th floor, Concorde Tower C, UB City, Vittal Mallya Road, Bangalore - 560 001     Packer   APPLE INC, ONE APPLE PARK WAY , CUPERTINO , CA 95014 , USA     Importer   APPLE INDIA PRIVATE LIMITED,NO.24,19TH FLOOR,CONCORDE TOWER C , UB CITY , VITTAL MALLYA ROAD, BANGALORE-560000     Item Weight   260 g     Item Dimensions LxWxH   17.8 x 7.8 x 18.1 Centimeters     Net Quantity   1 Count     Included Components   Beats Studio Pro headphones, Quick Start Guide and Warranty Card, USB-C to USB-C cable for charging and audio, 3.5mm analog audio cable, Protective Case     Generic Name   Bluetooth Headphones","Ghazaal1.0 out of 5 stars"])
print("Data Saved")
