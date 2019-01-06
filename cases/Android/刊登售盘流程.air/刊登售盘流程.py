# -*- encoding=utf8 -*-
from airtest.core.api import *
import configparser
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)
auto_setup(__file__)
#touch(Template(r"tpl1526984740704.png", record_pos=(0.4, -0.453), resolution=(1440, 2560)))
# wait(Template(r"tpl1529844258339.png", record_pos=(-0.39, -0.386), resolution=(1440, 2560)))

# 从配置文件读取账号密码
config = configparser.ConfigParser()
config.read("config/account.ini", encoding="utf8")
username = config.get("account_user", "username")
password = config.get("account_user", "password")

poco = AndroidUiautomationPoco(force_restart=False)

# 启动591APP应用
start_app('com.addcn.android.hk591new')

# 等待进入APP界面
wait(Template(r"tpl1535510550041.png", record_pos=(0.377, 0.819), resolution=(1440, 2560)))

# 點擊我的
poco("com.addcn.android.hk591new:id/tab_i_house").click()

# 點擊進入登錄頁面，填写账号和密码
poco("com.addcn.android.hk591new:id/tv_i_house_user_name").click()
poco("com.addcn.android.hk591new:id/et_user_name").click()
text(username)
poco("com.addcn.android.hk591new:id/et_pass_word").click()
text(password)
poco("com.addcn.android.hk591new:id/btn_user_login").click()
exists(Template(r"tpl1522745145959.png", record_pos=(-0.235, -0.767), resolution=(1440, 2560)))

# 刊登售盘
poco(text="刊登售盤").click()
poco(text="住宅").click()
poco("com.addcn.android.hk591new:id/purpose_tv").click()
poco("android:id/button1").click()#選擇類型
poco("com.addcn.android.hk591new:id/address_tv").click()#選擇屋苑
poco("com.addcn.android.hk591new:id/actv_community").click()
text("天",enter=False)
poco(text="天鑽").click()
poco("com.addcn.android.hk591new:id/space_tv").click()#選擇間隔
poco("android:id/button1").click()
poco("com.addcn.android.hk591new:id/use_area_et").click()#填寫實用面積
text("356",enter=False)
poco("com.addcn.android.hk591new:id/use_area_et").click()
keyevent("BACK")
poco("com.addcn.android.hk591new:id/price_et").click()#填寫售金
text("3566",enter=False)
poco("com.addcn.android.hk591new:id/price_title_tv").swipe([0.0108, -0.5666])
poco("com.addcn.android.hk591new:id/title_et").click()#填寫標題後期會在標題加入時間
text("自動腳本刊登出售",enter=False)
poco(text="房屋圖片").swipe([0.0469, -0.3696])

#後期加上上傳照片功能


#提交刊登
poco("com.addcn.android.hk591new:id/btn_submit").click()
wait(Template(r"tpl1529846309291.png", record_pos=(0.355, 0.815), resolution=(1440, 2560)))

touch(Template(r"tpl1529846309291.png", record_pos=(0.355, 0.815), resolution=(1440, 2560)))
poco("com.addcn.android.hk591new:id/iv_clear").click()
wait(Template(r"tpl1529844258339.png", record_pos=(-0.39, -0.386), resolution=(1440, 2560)))
poco("com.addcn.android.hk591new:id/tv_i_house_contact").swipe([0.0325, -0.6336])
keyevent("BACK")
poco("android:id/button1").click()

