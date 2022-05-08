# UI测试框架：关键字驱动
- 框架组成：python + selenium + excel
- 设计模式：
    - 关键字驱动
- 项目结构：

      - 工具层：ui_keyword/
      - 用例层：excel_case/
      - 数据驱动：excel_driver/
      - 配置层： conf/
        -  浏览器配置
        -  日志配置
  - 根目录：
    - requirements.txt：环境安装依赖
      - selenium: Python webui自动化测试库
      - openpyxl: Python读写excel文件的库
      - jsonpath:Python处理浏览器配置库
      - 安装方式：pip install -r requirements.txt
      