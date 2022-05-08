'''
程序主入口
'''
from ui_test_frame_excel_driver.excel_driver import excel_read

if __name__ == '__main__':
    excel_read.read('./excel_case/excel_driver.xlsx')
