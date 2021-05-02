import time
from datetime import date, timedelta
from openpyxl import Workbook
from selenium import webdriver
from bs4 import BeautifulSoup

write_wb = Workbook()
#write_ws = write_wb.create_sheet('schedule')
write_ws = write_wb.active
write_ws.append(["Company", "Date", "Time", "Product"])

datelist = []

raw_date = date.today()
for i in range(0,7):
    date_input = str(raw_date.year) + str(raw_date.strftime("%m")) + str(raw_date.strftime("%d"))
    datelist.append(date_input)
    raw_date = raw_date + timedelta(days=1)
    i = i + 1

driver = webdriver.Chrome("./chromedriver")

url = "https://www.gsshop.com/shop/tv/tvScheduleMain.gs?lseq=415680-1&gsid=ECmain-AU415680-AU415680-1#{}_LIVE"
#driver.get("https://www.gsshop.com/shop/tv/tvScheduleMain.gs?lseq=415680-1&gsid=ECmain-AU415680-AU415680-1#{}_LIVE")

for i in datelist:
    link = url.format(i)
    print(link)
    driver.get(link)
    #driver.implicitly_wait(2)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    timeslots = soup.select("article.items")
    for tslot in timeslots:
        live_time = tslot.select_one("span.times").text.strip()
        productslots = tslot.select("li.prd-item")
        for prdslot in productslots:
            product = prdslot.select_one("dt.prd-name").text.strip()
            """
            prd_names = str(product)
            prd_names = re.sub(pattern='[TV상품]', repl='', string=prd_names)
            prd_names = re.sub(pattern='[]', repl='', string=prd_names)
            product = prd_names.strip()
            """
            #prd_names = re.sub('^{30}', '', prd_names, 0).strip()
            write_ws.append(["GSHOP_LIVE", i, live_time, product])
            #print(live_time, product)

url = "https://www.gsshop.com/shop/tv/tvScheduleMain.gs?lseq=415680-1&gsid=ECmain-AU415680-AU415680-1#{}_DATA"
#driver.get("https://www.gsshop.com/shop/tv/tvScheduleMain.gs?lseq=415680-1&gsid=ECmain-AU415680-AU415680-1#{}_LIVE")

for i in datelist:
    link = url.format(i)
    print(link)
    driver.get(link)
    #driver.implicitly_wait(2)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    timeslots = soup.select("article.items")
    for tslot in timeslots:
        live_time = tslot.select_one("span.times").text.strip()
        productslots = tslot.select("li.prd-item")
        for prdslot in productslots:
            product = prdslot.select_one("dt.prd-name").text.strip()
            """
            prd_names = str(product)
            prd_names = re.sub(pattern='[TV상품]', repl='', string=prd_names)
            prd_names = re.sub(pattern='[]', repl='', string=prd_names)
            product = prd_names.strip()
            """
            #prd_names = re.sub('^{30}', '', prd_names, 0).strip()
            write_ws.append(["GSHOP_DATA", i, live_time, product])
            #print(live_time, product)

url = "http://display.cjmall.com/p/homeTab/main?hmtabMenuId=002409&broadType=live#bdDt%3A{}"
#driver.get("https://www.gsshop.com/shop/tv/tvScheduleMain.gs?lseq=415680-1&gsid=ECmain-AU415680-AU415680-1#{}_LIVE")

for i in datelist:
    link = url.format(i)
    print(link)
    driver.get(link)
    #driver.implicitly_wait(2)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    timeslots = soup.select("span.pgmDtm")
    productdiv = soup.select("ul.list_schedule_prod")
    k = 0

    for prd in productdiv:
        titleslot = prd.select("strong.tit_prod")
        for tit in titleslot:
            product = tit.select_one("span").text.strip()
            write_ws.append(["O_Shopping_live", i, timeslots[k].text.strip(), product])
        k = k + 1

url = "http://display.cjmall.com/p/homeTab/main?hmtabMenuId=002409&broadType=plus#bdDt%3A{}"
#driver.get("https://www.gsshop.com/shop/tv/tvScheduleMain.gs?lseq=415680-1&gsid=ECmain-AU415680-AU415680-1#{}_LIVE")

for i in datelist:
    link = url.format(i)
    print(link)
    driver.get(link)
    #driver.implicitly_wait(2)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    timeslots = soup.select("span.pgmDtm")
    productdiv = soup.select("ul.list_schedule_prod")
    k = 0

    for prd in productdiv:
        titleslot = prd.select("strong.tit_prod")
        for tit in titleslot:
            product = tit.select_one("span").text.strip()
            write_ws.append(["O_Shopping_plus", i, timeslots[k].text.strip(), product])
        k = k + 1

url = "https://www.hmall.com/p/bmc/brodPordPbdv.do?type=03&date={}"
#driver.get("https://www.gsshop.com/shop/tv/tvScheduleMain.gs?lseq=415680-1&gsid=ECmain-AU415680-AU415680-1#{}_LIVE")

for i in datelist:
    link = url.format(i)
    print(link)
    driver.get(link)
    #driver.implicitly_wait(2)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #timeslots = soup.select("span.pgmDtm")
    product_container = soup.select("li.ui-conts-break-wrap")
    time_save = ""

    for cont in product_container:

        try:
            timedata = cont.select_one("span.time").text.strip()
        except:
            timedata = time_save
        else:
            time_save = timedata
        finally:
            prdlist = cont.select("div.pdname")
            for prd in prdlist:
                write_ws.append(["HY_Shopping", i, timedata, prd.text.strip()])

url = "https://www.hmall.com/p/bmc/brodPordPbdv.do?type=03&date={}"
#driver.get("https://www.gsshop.com/shop/tv/tvScheduleMain.gs?lseq=415680-1&gsid=ECmain-AU415680-AU415680-1#{}_LIVE")

for i in datelist:
    link = url.format(i)
    print(link)
    driver.get(link)
    #driver.implicitly_wait(2)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #timeslots = soup.select("span.pgmDtm")
    product_container = soup.select("li.ui-conts-break-wrap")
    time_save = ""

    for cont in product_container:

        try:
            timedata = cont.select_one("span.time").text.strip()
        except:
            timedata = time_save
        else:
            time_save = timedata
        finally:
            prdlist = cont.select("div.pdname")
            for prd in prdlist:
                write_ws.append(["HY_Shopping", i, timedata, prd.text.strip()])

url = "https://www.hmall.com/p/bmc/dtvBrodFmtb.do?&date={}"
#driver.get("https://www.gsshop.com/shop/tv/tvScheduleMain.gs?lseq=415680-1&gsid=ECmain-AU415680-AU415680-1#{}_LIVE")

for i in datelist:
    link = url.format(i)
    print(link)
    driver.get(link)
    #driver.implicitly_wait(2)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #timeslots = soup.select("span.pgmDtm")
    product_container = soup.select("li.ui-conts-break-wrap")
    time_save = ""

    for cont in product_container:

        try:
            timedata = cont.select_one("span.time").text.strip()
        except:
            timedata = time_save
        else:
            time_save = timedata
        finally:
            prdlist = cont.select("div.pdname")
            for prd in prdlist:
                write_ws.append(["HY_PlusShop", i, timedata, prd.text.strip()])

write_wb.save("./Schedule.xlsx")