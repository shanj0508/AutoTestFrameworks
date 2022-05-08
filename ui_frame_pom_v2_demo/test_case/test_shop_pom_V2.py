from time import sleep
import pytest
from ui_frame_pom_v2_demo.key_word.keyword_web import WebKeys
from ui_frame_pom_v2_demo.logic.shopping_tb import GoodsSale
from ui_frame_pom_v2_demo.page import allPages

# 购物相关业务
class TestShop():

    # 购物
    # @pytest.mark.slow
    def test_case01(self,browser):
        action = GoodsSale(browser)
        action.shopping()

    # 删除全部购物车商品
    @pytest.mark.slow
    def test_case02(self,browser):
        # 先调用已封装购物逻辑进行购物
        action = GoodsSale(browser)
        action.shopping()
        # 删除购物车商品(关闭窗口)
        wk = WebKeys(browser)
        sleep(3)
        # 全选商品
        wk.locator_list(allPages.page_cartDetail_selectAll).click()
        sleep(3)
        # 点击删除按钮
        wk.locator_list(allPages.page_cartDetail_delBtn).click()
        # 点击确认按钮
        sleep(3)
        wk.locator_list(allPages.page_cartDetail_confirmBtn).click()


    # 修改购物车商品SKU
    # @pytest.mark.slow
    def test_case03(self, browser):
        # 先调用已封装购物逻辑进行购物
        action = GoodsSale(browser)
        action.shopping()
        wk = WebKeys(browser)
        sleep(3)
        # 调试专用，运行去掉
        # wk.change_window(1)
        # 鼠标悬停
        wk.mouse_hold(allPages.page_cartDetail_colorClum)
        # 点击修改sku
        wk.locator_list(allPages.page_cartDetail_modifyBtn).click()
        # 选择颜色分类
        wk.locator_list(allPages.page_cartDetail_colors).click()
        # 点击确认
        wk.locator_list(allPages.page_cartDetail_colorsConfirmBtn).click()

    # 移入收藏夹
    # @pytest.mark.slow
    def test_case04(self, browser):
        action = GoodsSale(browser)
        action.shopping()

        wk = WebKeys(browser)
        # 点击移入收藏夹
        wk.locator_list(allPages.page_cartDetail_favorites).click()

    def test_case05(self):
        assert 1 == 1

    def test_case06(self):
        assert 1 == 1

# if __name__ == '__main__':
#     pytest.main(['-s','test_shop_pom.py'])