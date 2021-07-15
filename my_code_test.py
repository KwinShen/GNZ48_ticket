# 导入所有所需包
import time  # 获取当前时间，实现定时抢票
import webbrowser
from bs4 import BeautifulSoup  # 从HTML中提取数据
from selenium import webdriver  # 驱动浏览器
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()  # 打开Chrome浏览器
# 【将链接替换为对应剧场门票链接】
browser.get('https://shop.48.cn/tickets/item/4131')  # 跳转页面

# 【手动登陆账号】

html_k = browser.execute_script('return document.documentElement.outerHTML')  # 获取当前页面的HTML
bs_k = BeautifulSoup(html_k, 'html.parser')

click_time = 0


def select_seat(browser): #需要手动更改此函数内的座位类型
    # First check if the seat is available
    elements = browser.find_elements_by_xpath("//*[@class='ticketsbuy seattypebg3 ']")

    if len(elements) > 0:  # 此类型有票的情况
        determine1 = browser.find_element_by_xpath('//em[@id="seattype3"]')  # 勾选座位类型
        browser.execute_script('arguments[0].click();', determine1)
        return True
    else:
        # time.sleep(1)
        # browser.refresh()
        return False


def buy(browser):  # 检查是否到切票时间（可切票）
    elements = browser.find_elements_by_xpath('//a[@class="blue_nb_2 ma_r10"]')
    if len(elements) > 0:
        return True
    else:
        return False

# seattype2：VIP座票；seattype3：普通座票；seattype4：普通站票
# 【根据所需座位类型，配置】（也可手动勾选调整）
# determine = browser.find_element_by_xpath('//em[@id="seattype4"]')  # 勾选座位类型
# browser.execute_script('arguments[0].click();', determine)


while True:  # 无限循环
    if click_time > 0:  # 直到点击一次购票
        break
    seat = select_seat(browser)
    if_time = buy(browser)
    # try:
    if time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) >= '2021-07-16 05:57:00':  # 设置抢票时间

        if seat and if_time:
            determine = browser.find_element_by_xpath('//a[@class="blue_nb_2 ma_r10"]')  # 点击购买
            browser.execute_script('arguments[0].click();', determine)
            click_time += 1  # 退出程序
        else:  # 没选到位置类型 / 未到切票时间 --> 刷新网页
            time.sleep(1)
            browser.refresh()
'''
    except NoSuchElementException as e:  # 门票售罄/还未到时切票 也不终止程序 继续刷新
        print("No more tickets, the program continues to refresh the page")
        time.sleep(1)
        browser.refresh()
'''

