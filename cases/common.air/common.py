# -*- encoding=utf8 -*-
from airtest.core.api import *
import configparser
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__)
poco = AndroidUiautomationPoco(force_restart=False)

def global_setting():
    ST.FIND_TIMEOUT = 20

def clear_591app():
    stop_app('com.addcn.android.hk591new')
    clear_app('com.addcn.android.hk591new')
    
def switch_env():
    start_app('com.addcn.android.hk591new')
    wait(Template(r"tpl1535510550041.png", record_pos=(0.377, 0.819), resolution=(1440, 2560)))
    poco("com.addcn.android.hk591new:id/tab_more").click()

    if poco("com.addcn.android.hk591new:id/head_title_tv").wait(5).get_text() == "更多":
        poco("com.addcn.android.hk591new:id/head_title_tv").long_click(duration=5)
    actual_val = poco("com.addcn.android.hk591new:id/head_title_tv").get_text()
    assert_equal(actual_val, "更多 - debug模式", "切換到debug環境成功.")
    poco("com.addcn.android.hk591new:id/tab_home").click()
    stop_app('com.addcn.android.hk591new')

    
def login():
    clear_591app()
    switch_env()
    # 从配置文件读取账号密码
    config = configparser.ConfigParser()
    config_path = os.path.abspath(os.path.join(os.path.realpath(__file__), "../../../config.ini"))
    config.read(config_path, encoding="utf8")
    username = config.get("account_user", "username")
    password = config.get("account_user", "password")

    # poco = AndroidUiautomationPoco(force_restart=False)

    # 启动591APP应用
    start_app('com.addcn.android.hk591new')

    # 等待进入APP界面
    wait(Template(r"tpl1535510550041.png", record_pos=(0.377, 0.819), resolution=(1440, 2560)))

    # 點擊我的
    poco("com.addcn.android.hk591new:id/tab_i_house").click()

    if poco("com.addcn.android.hk591new:id/iv_picture").wait(10).exists():
        poco("com.addcn.android.hk591new:id/iv_clear").click()

    # 點擊進入登錄頁面，填写账号和密码
    poco("com.addcn.android.hk591new:id/tv_i_house_user_name").click()
    poco("com.addcn.android.hk591new:id/et_user_name").click()
    text(username)
    poco("com.addcn.android.hk591new:id/et_pass_word").click()
    text(password)
    poco("com.addcn.android.hk591new:id/btn_user_login").click()

    if poco("com.addcn.android.hk591new:id/iv_picture").wait(10).exists():
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

# clear_591app()
# switch_env()






