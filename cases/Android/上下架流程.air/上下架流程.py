# -*- encoding=utf8 -*-
import configparser
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from config import get_config
poco = AndroidUiautomationPoco(force_restart=False)
# start your script here
auto_setup(__file__)

# 获取配置信息
config = configparser.ConfigParser()
config.read("config/account.ini", encoding="utf8")
user = config.get("account_user", "username")
print("=================================================")
print("user:", user)
print("===================================================")

touch(Template(r"tpl1526984740704.png", record_pos=(0.4, -0.453), resolution=(1440, 2560)))

wait(Template(r"tpl1531478150436.png", record_pos=(0.129, 0.853), resolution=(1440, 2560)))
poco("com.addcn.android.hk591new:id/tab_i_house").click()
poco("com.addcn.android.hk591new:id/tv_i_house_user_name").click()
poco("com.addcn.android.hk591new:id/et_user_name").click()
text("94894811")
poco("com.addcn.android.hk591new:id/et_pass_word").click()
text("123456")
poco("com.addcn.android.hk591new:id/btn_user_login").click()



touch(wait(Template(r"tpl1527243380300.png", record_pos=(-0.378, -0.252), resolution=(1440, 2560))))
#wait(Template(r"tpl1527161410539.png", record_pos=(0.384, -0.176), resolution=(1440, 2560)))

#touch(wait(Template(r"tpl1527161410539.png", record_pos=(0.384, -0.176), resolution=(1440, 2560))))
poco("android.widget.LinearLayout").child("android:id/content").child("android.widget.LinearLayout").child("android.widget.LinearLayout").child("com.addcn.android.hk591new:id/viewpage").child("android.widget.LinearLayout").child("com.addcn.android.hk591new:id/list_view_layout").child("com.addcn.android.hk591new:id/listview").child("android.widget.LinearLayout").child("android.widget.LinearLayout").child("com.addcn.android.hk591new:id/ll_opt").child("android.widget.LinearLayout").child("com.addcn.android.hk591new:id/btn_opt_to_open").click()
wait(Template(r"tpl1527165210324.png", record_pos=(0.344, 0.815), resolution=(1440, 2560)),timeout=20)

touch(wait(Template(r"tpl1527165210324.png", record_pos=(0.344, 0.815), resolution=(1440, 2560))))
touch(Template(r"tpl1527161058264.png", record_pos=(-0.266, -0.74), resolution=(1440, 2560)))
keyevent("BACK")

touch(Template(r"tpl1527164964684.png", record_pos=(0.372, -0.57), resolution=(1440, 2560)))

poco(text="售盤").click()
poco("com.addcn.android.hk591new:id/btn_house_deal").click()
poco(text="下架廣告").click()

keyevent("BACK")
poco("android.widget.LinearLayout").child("android:id/content").child("android:id/tabhost").child("android.widget.LinearLayout").child("android:id/tabcontent").child("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android:id/content").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("android.widget.LinearLayout").child("android.widget.ScrollView").child("android.widget.LinearLayout").child("com.addcn.android.hk591new:id/ll_identity_agent").child("android.widget.LinearLayout").child("com.addcn.android.hk591new:id/ll_published_in").child("android.widget.FrameLayout").child("android.widget.ImageView").click()
poco(text="刊登中").click()


wait(Template(r"tpl1527165083324.png", record_pos=(-0.004, 0.17), resolution=(1440, 2560)))

exists(Template(r"tpl1527161183396.png", record_pos=(-0.026, 0.163), resolution=(1440, 2560)))

keyevent("BACK")
keyevent("BACK")
touch(Template(r"tpl1527160906660.png", record_pos=(0.323, 0.128), resolution=(1440, 2560)))