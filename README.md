# 雀魂每日自动登录
使用selenium实现雀魂每日自动登录

## 单账号自动登录
使用cron设置为在每天5:00和23:00（北京时）自动登录一次

## 使用方法
1. Fork本仓库
2. 点击Settings->Secrets and variables->Actions->New repository secret，依次配置`EMAIL`、`PASSWD`
    - EMAIL 是雀魂的邮箱账号
    - PASSWD 是雀魂的密码
3. 先在Actions页面将GitHub Action启用，再选择对应的workflow，将scheduled workflow启用
4. 玩得开心
