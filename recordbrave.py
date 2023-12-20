from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import DesiredCapabilities
import time, datetime
import pyshark

# demo flag
demo = False

def getPage(url, httpversion, log):
    print(url)
    # httpversion = 0 -- No HTTP 2 nor HTTP 3
    # httpversion = 1 -- No HTTP 2
    # httpversion = 2 -- No HTTP 3

    # Demo flag
    demo = False
    logmessage = ""

    driver_path = "C:/Webdrivers/chromedriver/chromedriver.exe"
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    # lighthouse_path = "C:/Webdrivers/extensions/extension_100_0_0_3.crx"

    option = webdriver.ChromeOptions()
    option.binary_location = brave_path

    if demo == True:
        option.add_experimental_option("detach", True)

    # wait for all resources to download
    option.page_load_strategy = "normal"
    # HTTP Version Desired
    if httpversion == 1:
        logmessage += "HTTP 1; "
        option.add_argument("-disable-http2")
        option.add_argument("-disable-quic")
    if httpversion == 2:
        logmessage += "HTTP 1 and 3; "
        option.add_argument("-disable-http2")
    if httpversion == 3:
        logmessage += "HTTP 1 and 2; "
        option.add_argument("-disable-quic")
    if httpversion == 4:
        logmessage += "HTTP 1, 2, and 3; "
    # option.add_extension(lighthouse_path)
    # option.add_argument("--incognito") OPTIONAL
    # option.add_argument("--headless") OPTIONAL

    # Create new Instance of Chrome Brave

    service = Service(executable_path=driver_path)
    browser = webdriver.Chrome(service=service, options=option)

    browser.get("brave://about")

    initial_time = time.time()
    browser.get(url)
    ending_time = time.time()

    rtt = ending_time-initial_time
    
    logmessage += str(url) + "; "
    logmessage += str(rtt)

    logmessage += "\n"
    f = open(log, "a")
    f.write(logmessage)
    f.close()

    if demo != True:
        browser.quit()


if demo == True:
    log = "demo-" + str(datetime.date.today()) + ".txt"
    urlfile = "demo-urllist.txt"
    f = open(log, "a")
    f.write("url" + ": " + "rtt\n")
    f.close()
else:
    log = str(datetime.date.today()) + ".txt"
    urlfile = "urllist-50.txt"
    f = open(log, "a")
    f.write("protocol; url" + "; " + "rtt - Optimum Internet - Home Internet - Wifi - " +str(datetime.datetime.now()) +"\n")
    f.close()
urllist = open(urlfile, "r")
temp = urllist.read().splitlines()
urllist.close()
for i in range(10):
    print(i)
    for line in temp:
        try:
            getPage(line, 1, log)
            getPage(line, 2, log)
            getPage(line, 3, log)
            getPage(line, 4, log)
        except:
            continue