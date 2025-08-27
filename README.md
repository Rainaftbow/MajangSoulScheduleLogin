## 使用方法
1. Fork本仓库
2. 点击Settings->Secrets and variables->Actions->New repository secret，依次配置`EMAIL`、`PASSWD`
    - EMAIL 是雀魂的邮箱账号，如有多个账户用空格分隔，例如`example@gmail.com example@qq.com`
    - PASSWD 是雀魂的密码，如有多个账户用空格分隔，与邮箱依次对应，例如`grc28r7g3 pdtaw3fwag`
3. 先在Actions页面将GitHub Action启用，再选择对应的workflow，将scheduled workflow启用
4. Enjoy it!