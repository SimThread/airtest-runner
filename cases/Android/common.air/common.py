# -*- encoding=utf8 -*-
from airtest.core.api import *
import configparser
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__)
poco = AndroidUiautomationPoco(force_restart=False)

def login():
    # 从配置文件读取账号密码
    config = configparser.ConfigParser()
    config.read("config/account.ini", encoding="utf8")
    username = config.get("account_user", "username")
    password = config.get("account_user", "password")

    # poco = AndroidUiautomationPoco(force_restart=False)

    # 启动591APP应用
    start_app('com.addcn.android.hk591new')

    # 等待进入APP界面
    wait(Template(r"tpl1535510550041.png", record_pos=(0.377, 0.819), resolution=(1440, 2560)))

    # 點擊我的
    poco("com.addcn.android.hk591new:id/tab_i_house").click()

    if poco("com.addcn.android.hk591new:id/iv_picture").wait(5).exists():
        poco("com.addcn.android.hk591new:id/iv_clear").click()

    # 點擊進入登錄頁面，填写账号和密码
    poco("com.addcn.android.hk591new:id/tv_i_house_user_name").click()
    poco("com.addcn.android.hk591new:id/et_user_name").click()
    text(username)
    poco("com.addcn.android.hk591new:id/et_pass_word").click()
    text(password)
    poco("com.addcn.android.hk591new:id/btn_user_login").click()

    if poco("com.addcn.android.hk591new:id/iv_picture").wait(5).exists():
        poco("com.addcn.android.hk591new:id/iv_clear").click()
    exists(Template(r"tpl1522745145959.png", record_pos=(-0.235, -0.767), resolution=(1440, 2560)))

def logout():
    # 登出
    poco("com.addcn.android.hk591new:id/tv_i_house_contact").swipe([-0.0221, -0.5148])

    poco("com.addcn.android.hk591new:id/btn_i_house_logout").click()
    poco("android:id/button1").click()
    #關閉app
    keyevent("BACK")
    poco("android:id/button1").click()

    # 停止并清空App
    stop_app('com.addcn.android.hk591new')
    clear_app('com.addcn.android.hk591new')
