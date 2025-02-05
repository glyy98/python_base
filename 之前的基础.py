2023.11.23
1. import  module  和 from  module  import *  区别
前者在引用模块的函数时，必须要带上模块名。例如：module.函数（）
后者则可以直接使用 例如：函数（）  后者是直接把（函数、类、变量）导入到当前命名空间中，但是后者可能会存在命名冲突的问题。
2023.11.29
- 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
- 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
2024.2.5
1. 装饰器的作用

2024.2.22
- 定位下拉框后，无法选择下拉框的值
原因：选项都是调取后台接口动态获取，所以无法精准定位
解决：观察后发现所有值的class相同，通过css_selector，获取所有属性，“li.相同的class”
使用find_elements获取的是列表，然后遍历所有值，再精准匹配，elements是所有值
for element in elements:  
    print(element.text)  
    if element.text=='白钢':
        element.click()

- 如果下拉框的值不是动态获取，可以使用js
学会编写xpath，由于选项都是li开头，所以选项为‘周期’的xpath可以写为：//li//span[text()='周期']  
单引号外面要用双引号包住
含义：
1. //: 从当前节点开始，选择与选择条件匹配的文档中的节点，无论它们的位置在哪里。
2. li: 选择所有 <li> 元素。
3. //: 再次从当前节点开始，选择与选择条件匹配的文档中的节点，无论它们的位置在哪里。在这里，它用于选择任何 <li> 元素下的任何 <span> 元素。
4. span: 选择所有 <span> 元素。
5. [text()='周期']: 这是一个谓词，用于为所选节点指定条件。它仅选择文本内容完全等于字符串 '周期' 的 <span> 元素。
因此，用通俗的语言解释，XPath //li//span[text()='周期'] 选择任何 <span> 元素，只要它是任何 <li> 元素的后代，并且文本内容等于 '周期'。

2024.2.26
pytest运行用例命名规则：
A、文件名规则：test_*.py或者 *_test.py
B、函数名规则：以test_开头的函数
C、文件夹中如果含有_init_.py文件（即使它为空的），那这个文件夹就会视为一个包，后续才能被引入
D、静默函数，-q或者-quiet，为了减少冗余信息

Pytest 的运行方式：
1、通过文件名运行，在代码中加入
If __name__== '__main__':
pytest.main(["-s", "test_mm.py"])   加-s是为了让脚本中的print语句能够直接显示到控制台中

2024.2.27
定义夹具（xxfixture）时可以使用装饰器（@pytest.fixture），测试用例如果需要使用这个夹具，夹具可以作为参数传递给测试函数
fixture参数，夹具的使用说明
参数原型：fixture（scope=“function”，params=None，autouse=False（手动调用），ids=None，name=None）
scope=默认:function，还有class、module、package、session   以上都为作用范围
name为装饰函数的名称
autouse=True  代表所有用例自动调用这个夹具
#yield的作用是分割线，在这条语句之前的是前置条件，之后的是后置条件
假设一个测试用例调用了一个夹具内的函数，先执行该函数的前置条件然后执行用例最后再执行该函数的后置条件

#夹具名称自定义，mark用法
@pytest.mark.自动以名称
假设运行：pytest -s -m login test001.py  （运行单个）
运行多个：“login  or case1 or case2”   需要加引号
只会执行test001文件下  标注为@pytest.mark.login 的函数
-s的作用还是为了测试小套件，直接运行在终端，方便测试。不建议在大型测试时使用

2024.3.5
时间选择器，如果遇到是可以直接输入的，复制xpath的时候记得尾端需要带input
打印项目组织架构：ctrl+shift+p 选project tree
当终端进入到非运行模式，输入exit（）退出

2024.3.6
下载扩展，在左侧菜单的【测试】选择case文件夹进行调试，可视化执行用例
Python Test Explorer for Visual Studio Code
2024.3.8
使用allure，官网下载安装包，将bin路径配置到环境变量中（放到path中）
在allure的bin中打开终端，PS D:\Soft\allure-2.27.0\bin> allure serve D:\python\project\report
执行命令，report放的是用例跑完后生成的json文件
- 正杠：/  
- 反杠： \

2024.3.13
from selenium.webdriver.support import expected_conditions as EC
实例：crane = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, crane_xpath)))
self.driver：浏览器驱动
 10：最长超过时间
expected_conditions类 预期条件判断的方法
1、element_to_be_clickable  判断某个元素中是否可见并且可点击
2、

2024.3.15
使用autoit工具，实现模拟用户点击上传，操作windows文件资源管理器。
1、点击上传，弹出窗口
2、定位文件名框，输入文件地址，回车
3、定位【打开】按钮，上传成功
使用 scite 脚本工具编写打开弹窗后的操作
在代码中调用此脚本，exe
弊端就是更换文档路径后需要重新使用 autov2 生成新的 exe  

2024.6.6
if name == "__main__   
假如在新增功能的脚本末尾加上这个调用登录函数，像查询功能的脚本调用了新增脚本，这时候是不会执行登录的脚本，意思就是只要在这个if name == "__main__   之后的代码都不会被非主函数的代码调用

读取文件，填写相对路径
先定义一个变量，file_path=“D:/python/PW/config/login-info.yaml”，正斜杠
引入from pathlib import Path，面相对象的路径处理方法
实例：
读取登录信息
def read_login_info():  
    file_path=Path("D:/python/PW/config/login-info.yaml")   
    with open(file_path, "r",encoding='utf-8') as file:   #读取yaml文件，将文件赋值给file变量
        login_info = yaml.safe_load(file)  
        username = login_info["username"]
        password = login_info["password"]
    return username, password

2024.6.19
在使用input函数时，输出的结果在输出窗口，导致无法输入。
解决方法：
打开VSCode设置（使用快捷键Ctrl + ,）。
搜索code runner，找到Code-runner: Run in Terminal选项，并勾选它。这将确保你的代码在终端中运行，而不是在输出窗口中运行。

