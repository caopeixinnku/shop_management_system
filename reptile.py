from selenium import webdriver
import time
import random
import time
from pymysql import *  # 连接MySQL数据库
import pymysql

def parse_data(nums):
    mysql_obj = connect(host='127.0.0.1', user='TestUser', password='caopeixin628', database='dbsclab2020', port=3306,
                        charset='utf8')
    # 创建游标
    cur_obj = mysql_obj.cursor()
    # TODO 就是不要用%或者+操作符来拼接SQL语句，应该使用占位符
    divs = driver.find_elements_by_xpath('//div[@class="grid g-clearfix"]/div/div')  # 所有的div标签

    for div in divs:
        name = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text  # 商品名字
        original_price = div.find_element_by_xpath('.//strong').text  # 商品价格
        current_price = original_price
        picture = None
        introduction = None
        is_sale = 1
        is_new = 1
        addtime = '2022-10-26 14:15:44'
        views_count = 50
        subcat_id = nums
        supercat_id = 14
        cur_obj.execute(
            'insert into goods(id, name, original_price, current_price, picture, introduction, is_sale, is_new, addtime, views_count) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
            (nums, name, original_price, current_price, picture, introduction, is_sale, is_new, addtime, views_count))
        mysql_obj.commit()
        # print(nums, name, original_price, current_price, picture, introduction, is_sale, is_new, addtime, views_count)

        deal = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text  # 付款人数
        name = div.find_element_by_xpath('.//div[@class="shop"]/a/span[2]').text  # 店铺名称
        location = div.find_element_by_xpath('.//div[@class="location"]').text  # 店铺地点
        detail_url = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').get_attribute('href')  # 详情页地址
        nums += 1
        if nums>90:
            break
        # print(test, price, deal, name, location, detail_url)
    cur_obj.close()
    mysql_obj.close()


if __name__ == '__main__':



    word = input('请输入要搜索的关键字：')
    # TODO 1、创建浏览器
    driver = webdriver.Chrome()
    # TODO 2、修改了浏览器的内部属性，跳过了登录的滑动验证
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                           {"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""})
    # TODO 3、执行浏览器操作
    driver.get('https://www.taobao.com/')
    driver.implicitly_wait(10)  # 智能化等待方法
    driver.maximize_window()  # 最大化

    driver.find_element_by_xpath('//*[@id="q"]').send_keys(word)
    time.sleep(random.randint(1, 3))
    driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    time.sleep(random.randint(1, 3))

    """用户账号及密码登录"""
    driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('tb879630404')  # TODO 输入用户名
    time.sleep(random.randint(1, 3))
    driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('caopeixin628')  # TODO 输入密码
    time.sleep(random.randint(1, 3))
    driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
    time.sleep(random.randint(1, 3))
    for page in range(0, 1):
        print(f'-----------------正在爬取第{page + 1}页-----------------')
        # TODO 调用商品解析的函数
        parse_data(81)
        driver.find_element_by_xpath('//li[@class="item next"]/a[@class="J_Ajax num icon-tag"]').click()
        time.sleep(random.randint(2, 3))
