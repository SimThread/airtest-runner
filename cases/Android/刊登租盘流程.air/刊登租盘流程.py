# -*- encoding=utf8 -*-
__author__ = "10606"
__title__ = "test script title"
__desc__ = """
this is a test script.
必須在購買腳本后運行
"""

# start your script here
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__)
poco = AndroidUiautomationPoco(force_restart=False)
#touch(Template(r"tpl1526984740704.png", record_pos=(0.4, -0.453), resolution=(1440, 2560)))
# wait(Template(r"tpl1529844258339.png", record_pos=(-0.39, -0.386), resolution=(1440, 2560)))
poco(text="刊登租盤").click()
poco(text="住宅").click()
poco("com.addcn.android.hk591new:id/purpose_tv").click()
poco("android:id/button1").click()#選擇類型
poco("com.addcn.android.hk591new:id/address_tv").click()#選擇屋苑
poco("com.addcn.android.hk591new:id/actv_community").click()
text("天",enter=False)
poco(text="天巒").click()
poco("com.addcn.android.hk591new:id/space_tv").click()#選擇間隔
poco("android:id/button1").click()
poco("com.addcn.android.hk591new:id/use_area_et").click()#填寫實用面積
text("356",enter=False)
poco("com.addcn.android.hk591new:id/use_area_et").click()
keyevent("BACK")
poco("com.addcn.android.hk591new:id/price_et").click()#填寫租金
text("3566",enter=False)
poco(text="按        金").swipe([0.0433, -0.7392])

poco("com.addcn.android.hk591new:id/title_et").click()#填寫標題後期會在標題加入時間
text("自動腳本刊登出租",enter=False)
poco(text="房屋圖片").swipe([0.0397, -0.6437])

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






