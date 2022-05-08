# 接口测试框架：关键字驱动
- 框架组成：requests + excel 
- 设计模式：
  - 关键字驱动
- 项目结构：
  - 工具层：api_keyword/
  - 用例层：excel_case/
  - 数据驱动：excel_driver/
  - 根目录：
    - requirements.txt：环境安装依赖
      - requests: Python接口自动化测试库
      - openpyxl: Python读写excel文件的库
      - jsonpath:Python处理Json字符串的库
      - 安装方式：pip install -r requirements.txt
      