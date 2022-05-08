from ui_frame_pom_v2_demo.key_word.keyword_web import WebKeys
from ui_frame_pom_v2_demo.page import allPages


class Login(WebKeys):
    def login(self):
        self.locator_list(allPages.page_goodsDetail_loginUser).send_keys("shan000jing")
        self.locator_list(allPages.page_goodsDetail_loginPwd).send_keys("shanjing@.000")
        self.locator_list(allPages.page_goodsDetail_loginBtn).click()