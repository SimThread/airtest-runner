# -*- encoding=utf8 -*-
from airtest.core.api import *
ST.PROJECT_ROOT = "C:\\Users\\10714\\Desktop\\reference\\airtest-runner\\cases\\Android"
using("common.air")

from common import login, logout
import configparser
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(force_restart=False)
auto_setup(__file__)
#touch(Template(r"tpl1526984740704.png", record_pos=(0.4, -0.453), resolution=(1440, 2560)))
# wait(Template(r"tpl1529844258339.png", record_pos=(-0.39, -0.386), resolution=(1440, 2560)))

# 填寫表單
def fillForm():
    poco(text="刊登售盤").click()
    poco(text="住宅").click()
    poco("com.addcn.android.hk591new:id/purpose_tv").click()

    # 選擇類型
    poco("android:id/button1").click()

    # 選擇屋苑
    poco("com.addcn.android.hk591new:id/address_tv").click()
    poco("com.addcn.android.hk591new:id/actv_community").click()
    text("天")
    poco(text="天鑽").click()

    # 選擇間隔
    poco("com.addcn.android.hk591new:id/space_tv").click()
    poco("android:id/button1").click()

    # 填寫實用面積
    poco("com.addcn.android.hk591new:id/use_area_et").click()
    text("356")

    poco("com.addcn.android.hk591new:id/use_area_et").click()
    keyevent("BACK")

    # 填寫售金
    poco("com.addcn.android.hk591new:id/price_et").click()
    text("3566")

    # 填寫標題 - 後期會在標題加入時間
    poco("com.addcn.android.hk591new:id/price_title_tv").swipe([0.0108, -0.5666])
    poco("com.addcn.android.hk591new:id/title_et").focus([0.5, 0.5])
    text("回归测试-自動腳本刊登出售")  
    
    poco("com.addcn.android.hk591new:id/linkrole_tv").swipe([0.0506, -0.2724])


    # 上傳照片功能
    # poco(text="房屋圖片").swipe([0.0469, -0.3696])
    
    # 提交表单
    poco("com.addcn.android.hk591new:id/btn_submit").click()  
    
def assert_success():
    assert_exists(Template(r"tpl1546841770726.png", record_pos=(-0.003, -0.739), resolution=(1080, 1920)), "刊登售盘成功")


# 开始退出
def startExit():
    poco(text="售盤長期付費方案").wait(30)
    keyevent("BACK")
    keyevent("BACK")


login()

fillForm()

assert_success()

startExit()

logout()

