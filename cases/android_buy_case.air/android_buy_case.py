# -*- encoding=utf8 -*-
from airtest.core.api import *
using("common.air")
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common import clear_591app, login, logout
auto_setup(__file__)
poco = AndroidUiautomationPoco(force_restart=False)

#出租購買
def buy_rent():
    touch(Template(r"tpl1527236483360.png", threshold=0.6, target_pos=5, rgb=False, record_pos=(0.122, -0.572), resolution=(1440, 2560)))
    wait(Template(r"tpl1529842335509.png", record_pos=(-0.289, -0.366), resolution=(1440, 2560)))
    touch(Template(r"tpl1529842460391.png", record_pos=(-0.351, 0.592), resolution=(1440, 2560)))

    touch(Template(r"tpl1527238689400.png", threshold=0.5, target_pos=5, rgb=False, record_pos=(0.409, 0.836), resolution=(1440, 2560)))
    
    wait(Template(r"tpl1527238885362.png", record_pos=(-0.401, -0.46), resolution=(1440, 2560)))
    assert_exists(Template(r"tpl1546845349917.png", record_pos=(-0.395, -0.414), resolution=(1080, 1920)), "出租購買成功")

#出售購買
def buy_sale():
    touch(Template(r"tpl1527236483360.png", threshold=0.6, target_pos=5, rgb=False, record_pos=(0.122, -0.572), resolution=(1440, 2560)))
    wait(Template(r"tpl1529842335509.png", threshold=0.6, target_pos=5, rgb=False, record_pos=(-0.289, -0.366), resolution=(1440, 2560)))
    touch(Template(r"tpl1529842777515.png", record_pos=(0.249, -0.601), resolution=(1440, 2560)))
    wait(Template(r"tpl1529843129257.png", threshold=0.5, target_pos=5, rgb=False, record_pos=(-0.322, 0.24), resolution=(1440, 2560)))

    touch(Template(r"tpl1529843046297.png", threshold=0.6, target_pos=5, rgb=False, record_pos=(-0.376, 0.499), resolution=(1440, 2560)))

    touch(Template(r"tpl1527238689400.png", threshold=0.6, target_pos=5, rgb=False, record_pos=(0.409, 0.836), resolution=(1440, 2560)))
    exists(Template(r"tpl1527238885362.png", threshold=0.6, target_pos=5, rgb=False, record_pos=(-0.401, -0.46), resolution=(1440, 2560)))
    assert_exists(Template(r"tpl1546845349917.png", record_pos=(-0.395, -0.414), resolution=(1080, 1920)), "出售購買成功")

login()
buy_rent()
buy_sale()
logout()


