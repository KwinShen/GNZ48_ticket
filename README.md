# GNZ48-Ticket
基于Selenium、Python，在Chrome浏览器实现代码切票，
尚未测试

## 流程
1. 手动更改代码中的开始刷新网页时间（预留登录时间）、位置类型
2. 点击运行，网页弹出后手动登录，输入账号密码
3. 直至成功购买前脚本会自动刷新&选座位

## 运行前配置
* **Selenium环境**：
  * *教程搜索关键词：selenium chromedriver*
  * 下载Chrome浏览器对应版本的[chromedriver](http://chromedriver.storage.googleapis.com/index.html)
  * pip install selenium
* **Python环境**：
  * *教程搜索关键词：anaconda jupyter notebook安装*
  * 安装[Anaconda](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)

2021/05/11

5/18补充说明：可能需要注意网页读秒，以防时间到了8点网页购买链接仍不可点击，导致代码报错
