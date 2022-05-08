from ui_frame_pom_v2_demo.key_word.keyword_web import WebKeys
from ui_frame_pom_v2_demo.page import  allPages
from time import sleep
from ui_frame_pom_v2_demo.logic.login_tb import Login

class GoodsSale(Login):
    def shopping(self):
        self.open("https://www.taobao.com")
        self.locator_list(allPages.page_index_search).send_keys("膳魔师")
        self.locator_list(allPages.page_index_searchBtn).click()
        self.locator_list(allPages.page_searchResults_good).click()
        self.change_window(1)
        self.locator_list(allPages.page_goodsDetail_color).click()
        self.locator_list(allPages.page_goodsDetail_num).clear()
        self.locator_list(allPages.page_goodsDetail_num).send_keys("3")
        self.locator_list(allPages.page_goodsDetail_cartBtn).click()

        '''
            没有登录框，找不到元素，也能继续运行
            方法1:
                try:
                 elem = driver.find_element_by_name('...')
                except:
                 pass
            方法2：
                elems = driver.find_elements_by_name('...')
                if len(elems)>0:
                   elem = elems[0]
        '''
        # try:
        #     el = self.locator_list(allPages.page_goodsDetail_loginFrame)
        #     self.change_frame(el)
        #     self.login()
        #     self.change_defaultFrame()
        #     sleep(3)
        # except:
        #     pass

        elems = self.locator_list_group(allPages.page_goodsDetail_loginFrame)
        print("----:",elems)
        if len(elems)>0:
            el = elems[0]
            self.change_frame(el)
            self.login()
            self.change_defaultFrame()
            sleep(3)


        #
        # self.login()
        # sleep(3)
        # #去购物结算按钮
        # self.locator_list(allPages.page_goodsDetail_payBtn).click()


