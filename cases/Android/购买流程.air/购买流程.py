# -*- encoding=utf8 -*-
__author__ = "10606"
__title__ = "test script title"
__desc__ = """
this is a test script.
"""
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__)
poco = AndroidUiautomationPoco(force_restart=False)
# start your script here.
#出租購買
start_app('com.addcn.android.hk591new')

wait(Template(r"tpl1531478150436.png", record_pos=(0.129, 0.853), resolution=(1440, 2560)))
poco("com.addcn.android.hk591new:id/tab_i_house").click()

poco("com.addcn.android.hk591new:id/tv_i_house_user_name").click()
poco("com.addcn.android.hk591new:id/et_user_name").click()
text("94894811")
poco("com.addcn.android.hk591new:id/et_pass_word").click()
text("123456")
poco("com.addcn.android.hk591new:id/btn_user_login").click()


touch(Template(r"tpl1527236483360.png", record_pos=(0.122, -0.572), resolution=(1440, 2560)))
wait(Template(r"tpl1529842335509.png", record_pos=(-0.289, -0.366), resolution=(1440, 2560)))
touch(Template(r"tpl1529842460391.png", record_pos=(-0.351, 0.592), resolution=(1440, 2560)))
touch(Template(r"tpl1527238689400.png", record_pos=(0.409, 0.836), resolution=(1440, 2560)))
wait(Template(r"tpl1527238885362.png", record_pos=(-0.401, -0.46), resolution=(1440, 2560)))

#出售購買
touch(Template(r"tpl1527236483360.png", record_pos=(0.122, -0.572), resolution=(1440, 2560)))
wait(Template(r"tpl1529842335509.png", record_pos=(-0.289, -0.366), resolution=(1440, 2560)))
touch(Template(r"tpl1529842777515.png", record_pos=(0.249, -0.601), resolution=(1440, 2560)))
wait(Template(r"tpl1529843129257.png", record_pos=(-0.322, 0.24), resolution=(1440, 2560)))

touch(Template(r"tpl1529843046297.png", record_pos=(-0.376, 0.499), resolution=(1440, 2560)))

touch(Template(r"tpl1527238689400.png", record_pos=(0.409, 0.836), resolution=(1440, 2560)))
exists(Template(r"tpl1527238885362.png", record_pos=(-0.401, -0.46), resolution=(1440, 2560)))


keyevent("BACK")

touch(Template(r"tpl1527160906660.png", record_pos=(0.323, 0.128), resolution=(1440, 2560)))



