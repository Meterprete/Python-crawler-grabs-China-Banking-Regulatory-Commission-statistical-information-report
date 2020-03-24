# Python-crawler-grabs-China-Banking-Regulatory-Commission-statistical-information-report
**本文仅用于学习参考：**

 **项目下载链接：**
 - [**下载方式一：腾讯微云【密码：54250p】**](https://share.weiyun.com/5IG5Hte)
 - [**下载方式二：github**](https://github.com/Meterprete/Python-crawler-grabs-China-Banking-Regulatory-Commission-statistical-information-report.git)

[**初始url，即如下所示页面**](http://www.cbirc.gov.cn/cn/view/pages/ItemList.html?itemPId=953&itemId=954&itemUrl=ItemListRightList.html&itemName=%E7%BB%9F%E8%AE%A1%E4%BF%A1%E6%81%AF#1)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200214193116736.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDQ0OTUxOA==,size_16,color_FFFFFF,t_70)
**目的：抓取网页中所有的文档标题以及doc，pdf下载链接，以及发布时间，发布日期等信息。**

**分析流程：**
【1】初始页面抓包得返回信息得json请求地址
【2】对数据进行提取过滤
【3】信息整合，构造下一页url，继续重复前三个步骤

**本项目简单实现，就不多说了，可以拿去练手。**

主要逻辑代码如下图所示：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200214194013328.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDQ0OTUxOA==,size_16,color_FFFFFF,t_70)
piplines：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200214194117350.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDQ0OTUxOA==,size_16,color_FFFFFF,t_70)
**运行截图：**![在这里插入图片描述](https://img-blog.csdnimg.cn/20200214194551197.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDQ0OTUxOA==,size_16,color_FFFFFF,t_70)
**可以看到，速度还是不错的，大约13秒，抓取了55页信息，总计976条数据，并且看到信息也挺纯净的。**
