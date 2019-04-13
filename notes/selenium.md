- selenium 可以模拟浏览器操作，使用requests等操作获取不到网页内容的时候可以使用它
- 主要用来解决JavaScript渲染的问题
- 需要安装 `pip3 install selenium`
- Selenium3.x调用浏览器必须有一个webdriver驱动文件`chromedriver`，下载了exe文件之后放到python的路径里面（环境变量）才能运行

使用方法可以查找selenium文档 !(https://selenium-python-zh.readthedocs.io/en/latest/)

## 使用方法

### 声明浏览器对象

```python
from selenium import webdriver

browser = webdriver.Chrome() # 可以任意更换浏览器
```

### 访问对象

```python
from selenium import webdriver

browser = webdriver.Chrome() # 这里会打开浏览器
browser.get("url")
print(browser.page_source)
print(browser.get_cookies())
print(browser.current_url)  # 可以附加的一些参数
browser.close()

browser.quit() # 控制关闭浏览器
```

### 查找元素

#### 查找单个元素

```python
browser.find_element_by_id('名称')
browser.find_element_xpath('xpath路径') # 返回的是一个selenium...的对象
```

#### 查找多个元素

```python
browser.find_elements_css_selection('') # 返回的是一个selenium...对象组成的列表
```

#### 元素交互操作

```python
from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("http://www.pniao.com") # 还是以胖鸟为例

input = browser.find_element_by_id('movieSoWord') # 搜索框的地址
input.send_keys('西游记') # send_keys 输入内容
time.sleep(1)
input.clear() # 清除内容
input.send_keys('兄弟')
button = browser.find_element_by_id('movieSoBtn') # 搜索按钮的地址
button.click() # 按下按钮，进行搜索
```

#### 前进or后退

```python
browser.back() # 后退页面
browser.forward() # 前进页面
```

#### cookies处理

```python
browser.get_cookies() # 获取网页的cookies
browser.add_cookie({cookie的字典}) # 增加cookies
browser.delete_all_cookies() # 删除所有cookies
```

#### 选项卡管理

```python
browser.execute_script('window.open') # 新建一个选项卡
browser.switch_to_window(browser.window_handles[number]) # 选择对某一个选项卡进行操作
```

- 小插曲
字典推导式：
```python
cookie = ""
cookie_dict = {i.split('=')[0]:i.split('=')[1] for i in cookie.split('; ')}
```

#### 拖拽滑块

```python
dragger = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nc_1_n1z"))) # 捕捉初始位置
action_chains = ActionChains(browser) # 动作链，这一步一定要有

for index in range(500):
  try:
    action_chains.drag_and_drop_by_offset(dragger, 500, 0).perform()#平行移动鼠标，此处直接设一个超出范围的值，这样拉到头后会报错从而结束这个动作
  except UnexpectedAlertPresentException:
    break
```

-淘宝页面加载不出来，最终没做这个项目，但是selenium知识还是用得到的

