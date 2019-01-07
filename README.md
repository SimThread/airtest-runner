# airtest-runner

## 功能

1. 脚本批量执行
2. 每个脚本执行日志分开存放
3. 每个脚本单独生成一个html报告并在父文件夹生成一个聚合报告

## 使用
- 用例必须以“case”结尾才能识别
- 以端类型作为用例命名开头。例如：安卓的登录用例为：android_login, 苹果的登录用例为：ios_login, WebPC端的登录用例为：webpc_login，触屏端的登录用例为：webmobile_login
- 

```python
def runCase(self, vars):
    # 业务逻辑代码
    pass
```

## 常用命令
执行所有测试用例
```shell
# 语法
python runner.py 用例集目录

# 示例
python runner.py cases
```

生成报告
```shell
# 语法
python report.py 日志文件夹名称

# 示例：
python report.py log_20190101_010101
```

## 目录结构

```shell
root
├─report.py                # 生成报告
├─runner.py                # 执行脚本
├─summary_template.html    # 报告模板
├─cases                    # 用例集
│      ├──交易失败          #图片存放目录
│      ├──交易成功
│      ├──交易失败.py       #测试用例
│      └──交易成功.py
└─登录用例集
        ├──登录失败.py
        └──登录成功.py
```
