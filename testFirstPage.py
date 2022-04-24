from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class TestCase(unittest.TestCase):
    def setUp(self):
        self.broser = webdriver.Chrome()
        self.broser.get('test')
        self.broser.maximize_window()
        self.broser.implicitly_wait(20)

    def tearDown(self):
        self.broser.close()

    def wait(self, by, tiaojian, msg):
        # 简化强制等待语句
        WebDriverWait(self.broser, 30, 0.2).until(EC.presence_of_element_located((by, tiaojian)), message=msg)

    def move(self, by, path):
        # 简化鼠标停留语句
        demo = self.broser.find_element(by, path)
        # 将demo获取到的定位作为参数，模拟鼠标放置效果，使其展开
        ActionChains(self.broser).move_to_element(demo).perform()

    def testFirst(self):

        self.broser.find_element(By.ID, "username").send_keys('admin')
        self.broser.find_element(By.XPATH, "//input[@ng-model='formData.password']").send_keys('test')
        self.broser.find_element(By.TAG_NAME, "button").click()
        # WebDriverWait(self.broser, 30, 0.2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]')), message=' User Defined Links ')
        self.wait(By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]', ' User Defined Links ')
        # demo = self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/a/span')
        # # 将demo获取到的定位作为参数，模拟鼠标放置效果，使其展开
        # ActionChains(self.broser).move_to_element(demo).perform()
        self.move(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/a/span')
        self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/ul/li[5]/a').click()
        # WebDriverWait(self.broser, 30, 0.2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]')), message=' 快速连结 ')
        self.wait(By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]', ' 快速连结 ')
        # demo = self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/a')
        # # 将demo获取到的定位作为参数，模拟鼠标放置效果，使其展开
        # ActionChains(self.broser).move_to_element(demo).perform()
        self.move(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/a')
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/ul/li/div/div/div/ul/li[2]/a[1]').click()
        # WebDriverWait(self.broser, 30, 0.2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div[1]')), message=' 我的任务状态')
        # self.wait(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div[1]', ' 我的任务状态')
        try:
            self.assertIn(r'任务管理',
                          self.broser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/h3').text)
            print('success')
        except:
            print("失败")

    def testSecond(self):
        self.broser.find_element(By.ID, "username").send_keys('klein')
        self.broser.find_element(By.XPATH, "//input[@ng-model='formData.password']").send_keys('test')
        # 此处是根据页面的元素类型定位，tag_name是input也就是输入框，tagname最容易重复，不建议使用
        self.broser.find_element(By.TAG_NAME, "button").click()
        # 隐式等待，页面加载完成后进行下一步操作，对全局生效，设置时间为15秒，如果15秒页面未完全加载，则抛出异常
        # 定位”安全与健康“
        WebDriverWait(self.broser, 30, 0.2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]')), '快速连结')
        demo = self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[4]/a')
        # 将demo获取到的定位作为参数，模拟鼠标放置效果，使其展开
        ActionChains(self.broser).move_to_element(demo).perform()
        # find_element_by_css_selector是根据页面的css定位，此处使用的是绝对路径
        # 点击”立即检查“使其展开
        self.broser.find_element \
            (By.CSS_SELECTOR, "body > div.page-header.navbar.navbar-fixed-top.ng-scope > div > "
                              "div.page-header-menu > div > div > div > ul > li:nth-child(4) > ul > "
                              "li > div > div > div > ul > li.ng-scope.dropdown-submenu > a").click()
        # find_element_by_name()有可能重复是根据name定位元素，由于name通常不具备唯一性，所以尽量少使用
        time.sleep(0.5)
        # 点击”无计划检查“
        self.broser.find_element \
            (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[4]/ul/li/div/div/div/ul/li[2]/ul/li/a").click()
        # 此处为显示等待，在指定的元素加载出来后，执行下一步，显示等待可以有效减少等待时间，加快程序运行速度，等待内容较为灵活
        # 参数中10和0.2的意思是十秒内每0.2秒检查一次页面元素，此处的设置为等”注释”加载出来就执行下一步
        WebDriverWait(self.broser, 10, 0.2).until(EC.presence_of_element_located((By.ID, "comment")), message='注释')
        # 点击”被检查工厂“
        self.broser.find_element(By.XPATH, '//*[@id="facility_id"]/a').click()

        time.sleep(1)
        # 此处是根据class_name定位  classname有可能重复
        # self.broser.find_element_by_class_name("select2-choice ui-select-match select2-default").click()
        # self.broser.find_element_by_xpath('//*[@id="facility_id"]/div/ul').send_keys('jinshan')//*[@id="facility_id"]/div/ul
        # self.broser.find_element_by_link_text('[F037] NPJinshan').click()
        # print(self.broser.find_element_by_xpath('//*[@id="facility_id"]/div/ul').text)
        # st=self.broser.find_element_by_xpath('//*[@id="facility_id"]/div/ul')
        # Select(st).select_by_visible_text('[F037] NPJinshan')
        # ul = self.broser.find_element_by_xpath('//*[@id="primary_menu"]/ul')
        # 点击”其中一个工厂“
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/form/div/div[1]/div[2]/div/div/div[1]/div/ul/li/ul/li[1]').click()
        # ul=self.broser.find_element_by_xpath('//*[@id="ui-select-choices-4"]')
        # print(ul.text)
        # list = ul.find_elements_by_xpath('//*[@id="ui-select-choices-row-4-0"]')
        # len(list)  # 计算有多少个li
        # # 用列表标识符取最后一个li
        # list[-1].click()
        # st.find_element_by_xpath('//*[@id="ui-select-choices-row-4-3"]').click()
        # print(self.broser.find_element_by_link_text('[F037] NPJinshan').text)
        # print(self.broser.find_element_by_xpath('//*[@id="ui-select-choices-row-4-3"]').text)
        # print(self.broser.find_element_by_xpath('//*[@id="ui-select-choices-row-4-3"]/div').text)
        # print(self.broser.find_element_by_xpath('//*[@id="ui-select-choices-row-4-3"]/div/div').text)
        # self.broser.find_element_by_xpath('//*[@id="facility_id"]/div/ul').click()
        # 点击”日历“下拉框
        self.broser.find_element(By.XPATH, '//*[@id="inspection_date"]/div/div[1]').click()
        # 点击”今天“
        self.broser.find_element(By.XPATH, '//*[@id="inspection_date"]/div/div[1]/ul/li[2]/span/button[1]').click()
        # 点击保存按钮
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/form/div/div[4]/button[2]').click()
        time.sleep(0.5)
        try:
            self.assertIn(r'添加成功', self.broser.find_element(By.ID, 'notification-1').text)
            print('success')
        except:
            print("失败")

    def testThird(self):
        self.broser.find_element_by_id("username").send_keys('admin')
        self.broser.find_element_by_xpath("//input[@ng-model='formData.password']").send_keys('test')
        # 此处是根据页面的元素类型定位，tag_name是input也就是输入框，tagname最容易重复，不建议使用
        self.broser.find_element_by_tag_name("button").click()
        self.wait(By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]', ' User Defined Links ')
        self.move(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/a/span')
        self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/ul/li[5]/a').click()
        self.move(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/a')
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[2]/a[1]').click()
        try:
            self.assertIn(r'组织架构', self.broser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]').text)
            print('success')
        except:
            print("失败")

    def testFourth(self):
        self.broser.find_element_by_id("username").send_keys('admin')
        self.broser.find_element_by_xpath("//input[@ng-model='formData.password']").send_keys('test')
        # 此处是根据页面的元素类型定位，tag_name是input也就是输入框，tagname最容易重复，不建议使用
        self.broser.find_element_by_tag_name("button").click()
        # 查看是否进入到首页
        self.wait(By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]', ' User Defined Links ')
        # 修改语言
        self.move(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/a/span')
        self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/ul/li[5]/a').click()
        # 切换员工管理页面
        self.move(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/a')
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[3]/a[1]').click()
        try:
            self.assertIn(r'员工管理', self.broser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]').text)
            print('success')
        except:
            print("失败")

    def testFri(self):
        self.broser.find_element_by_id("username").send_keys('admin')
        self.broser.find_element_by_xpath("//input[@ng-model='formData.password']").send_keys('test')
        # 此处是根据页面的元素类型定位，tag_name是input也就是输入框，tagname最容易重复，不建议使用
        self.broser.find_element_by_tag_name("button").click()
        # 查看是否进入到首页
        self.wait(By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]', ' User Defined Links ')
        # 修改语言
        self.move(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/a/span')
        self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/ul/li[5]/a').click()
        # 切换Q代码页面
        self.move(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/a')
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[4]/a[1]').click()
        try:
            self.assertIn(r'Q代码', self.broser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]').text)
            print('success')
        except Exception as e:
            print(e)
            print(str(e))
            print(repr(e))
        except:
            print("失败")

    def testSix(self):
        self.broser.find_element_by_id("username").send_keys('admin')
        self.broser.find_element_by_xpath("//input[@ng-model='formData.password']").send_keys('test')
        # 此处是根据页面的元素类型定位，tag_name是input也就是输入框，tagname最容易重复，不建议使用
        self.broser.find_element_by_tag_name("button").click()
        # 查看是否进入到首页
        self.wait(By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]', ' User Defined Links ')
        # 修改语言
        self.move(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/a/span')
        self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/ul/li[5]/a').click()
        # 切换工厂页面
        self.move(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/a')
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[5]/a[1]').click()
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[5]/ul/li[1]/a').click()
        try:
            self.assertIn(r'工厂', self.broser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]').text)
            print('success')
        except Exception as e:
            print(e)
            print(str(e))
            print(repr(e))
        except:
            print("失败")

    def testSeven(self):
        self.broser.find_element_by_id("username").send_keys('admin')
        self.broser.find_element_by_xpath("//input[@ng-model='formData.password']").send_keys('test')
        # 此处是根据页面的元素类型定位，tag_name是input也就是输入框，tagname最容易重复，不建议使用
        self.broser.find_element_by_tag_name("button").click()
        # 查看是否进入到首页
        self.wait(By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]', ' User Defined Links ')
        # 修改语言
        self.move(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/a/span')
        self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/ul/li[5]/a').click()
        # 切换区域页面
        self.move(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/a')
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[5]/a[1]').click()
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[5]/ul/li[2]/a').click()
        try:
            self.assertIn(r'区域', self.broser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]').text)
            print('success')
        except Exception as e:
            print(e)
            print(str(e))
            print(repr(e))
        except:
            print("失败")

    def testEig(self):
        self.broser.find_element_by_id("username").send_keys('admin')
        self.broser.find_element_by_xpath("//input[@ng-model='formData.password']").send_keys('test')
        # 此处是根据页面的元素类型定位，tag_name是input也就是输入框，tagname最容易重复，不建议使用
        self.broser.find_element_by_tag_name("button").click()
        # 查看是否进入到首页
        self.wait(By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]', ' User Defined Links ')
        # 修改语言
        self.move(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/a/span')
        self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/ul/li[5]/a').click()
        # 切换地点页面
        self.move(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/a')
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[5]/a[1]').click()
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[5]/ul/li[3]/a').click()
        try:
            self.assertIn(r'地点', self.broser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]').text)
            print('success')
        except Exception as e:
            print(e)
            print(str(e))
            print(repr(e))
        except:
            print("失败")

    def testNig(self):
        self.broser.find_element_by_id("username").send_keys('admin')
        self.broser.find_element_by_xpath("//input[@ng-model='formData.password']").send_keys('test')
        # 此处是根据页面的元素类型定位，tag_name是input也就是输入框，tagname最容易重复，不建议使用
        self.broser.find_element_by_tag_name("button").click()
        # 查看是否进入到首页
        self.wait(By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]', ' User Defined Links ')
        # 修改语言
        self.move(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/a/span')
        self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/ul/li[5]/a').click()
        # 切换设备页面
        self.move(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/a')
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[5]/a[1]').click()
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[5]/ul/li[4]/a').click()
        try:
            self.assertIn(r'设备', self.broser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]').text)
            print('success')
        except Exception as e:
            print(e)
            print(str(e))
            print(repr(e))
        except:
            print("失败")

    def testTen(self):
        self.broser.find_element_by_id("username").send_keys('admin')
        self.broser.find_element_by_xpath("//input[@ng-model='formData.password']").send_keys('test')
        # 此处是根据页面的元素类型定位，tag_name是input也就是输入框，tagname最容易重复，不建议使用
        self.broser.find_element_by_tag_name("button").click()
        # 查看是否进入到首页
        self.wait(By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]', ' User Defined Links ')
        # 修改语言
        self.move(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/a/span')
        self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/ul/li[5]/a').click()
        # 切换设施页面
        self.move(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/a')
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[5]/a[1]').click()
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[5]/ul/li[5]/a').click()
        try:
            self.assertIn(r'设施', self.broser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]').text)
            print('success')
        except Exception as e:
            print(e)
            print(str(e))
            print(repr(e))
        except:
            print("失败")

    def testEle(self):
        self.broser.find_element_by_id("username").send_keys('admin')
        self.broser.find_element_by_xpath("//input[@ng-model='formData.password']").send_keys('test')
        # 此处是根据页面的元素类型定位，tag_name是input也就是输入框，tagname最容易重复，不建议使用
        self.broser.find_element_by_tag_name("button").click()
        # 查看是否进入到首页
        self.wait(By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]', ' User Defined Links ')
        # 修改语言
        self.move(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/a/span')
        self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/ul/li[5]/a').click()
        # 切换排口管理页面
        self.move(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/a')
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[5]/a[1]').click()
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[5]/ul/li[6]/a').click()
        try:
            self.assertIn(r'排口管理', self.broser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]').text)
            print('success')
        except Exception as e:
            print(e)
            print(str(e))
            print(repr(e))
        except:
            print("失败")

    def testTwe(self):
        self.broser.find_element_by_id("username").send_keys('admin')
        self.broser.find_element_by_xpath("//input[@ng-model='formData.password']").send_keys('test')
        # 此处是根据页面的元素类型定位，tag_name是input也就是输入框，tagname最容易重复，不建议使用
        self.broser.find_element_by_tag_name("button").click()
        # 查看是否进入到首页
        self.wait(By.XPATH, '//*[@id="user_links"]/div/div/div[1]/div[1]', ' User Defined Links ')
        # 修改语言
        self.move(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/a/span')
        self.broser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/ul/li[5]/ul/li[5]/a').click()
        # 切换区域页面
        self.move(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/a')
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[6]/a').click()
        self.broser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/ul/li/div/div/div/ul[1]/li[6]/ul/li[1]/a').click()
        try:
            self.assertIn(r'问题库', self.broser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]').text)
            print('success')
        except Exception as e:
            print(e)
            print(str(e))
            print(repr(e))
        except:
            print("失败")


if __name__ == '__main__':
    unittest.main(verbosity=2)
