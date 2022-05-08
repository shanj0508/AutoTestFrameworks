## 0.9.1(2021-10-26)

- 框架组成：unittest+selenium 
- 设计模式：
  - 关键字驱动
  - pom
- 项目结构：
  - 工具层：key_word/
  - 页面层：page_object/
  - 配置层：conf/
  - 用例层：test_cases/
  - 测试套件层：test_suite/
  - 根目录：
    - requirements.txt：环境安装依赖
      - selenium: Web UI自动化测试库
      - ddt: Pytest扩展插件，支持unittest的数据驱动模块
      - PyYaml：实现读取yaml文件的插件
      - 安装方式：pip install -r requirements.txt
      

