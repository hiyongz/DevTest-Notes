import os
import allure
import time
import pytest

# 添加报错截图到allure报告里
driver = None
screenshot_path=''
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # pic_info = adb_screen_shot()
        with allure.step('添加失败截图...'):
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            allure.attach(driver.get_screenshot_as_png(),now+"失败截图", allure.attachment_type.PNG)
            print("这是截图函数里面的"+screenshot_path)
            driver.get_screenshot_as_file(screenshot_path+'/'+now+".png")

# def adb_screen_shot():
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_base64()
# driver.get_screenshot_as_file("122.jpg")
# os.popen("adb screen -p testfailue.jpg")
@pytest.fixture(scope='module', autouse=True)
def createscreenshot():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    global screenshot_path
    screenshot_path = (r'\Users\bytedance\Documents\Windows文件\ui\UItest\demo_uitest2\screenshot/' + now)
    isExists = os.path.exists(screenshot_path)
    if not isExists:
        os.mkdir(screenshot_path)
    else:
        pass
    # print("create已经运行")
    return screenshot_path







