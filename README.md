# BiliOnlineGet 2.0
获取哔哩哔哩B站某个BV的绝大部分参数。

目前不带数据存储功能，暂请自行实现。

# 支持获取的信息：

## bv类

| 参数 | 介绍 | 补充 |
| ------ | ------ |  ------ |
|bvid |BV号| |
|aid |AV号| |
|cid |C号|用于区分 分P 弹幕  在线人数 等数据|
|tid  |分类id| |
|tname |分类名| |
|copyright |版权状态| |
|pic |封面| |
|title |标题| |
|pubdate| 发布时间| |
|ctime |通过时间| |
|desc |描述| |
|state |状态| |
|duration |视频长度| |
|owner| owner类|(见下) |
|stat |stat类|(见下) |

### owner类

| 参数 | 介绍 | 
| ------ | ------ | 
|mid| UP主uid|
|name |UP主昵称|
|face| UP主头像|


### stat类
| 参数 | 介绍 | 
| ------ | ------ | 
|view |播放数|
|danmaku| 弹幕数|
|reply |回复数|
|favorite |收藏数|
|coin |投币数|
|share| 分享数|
|now_rank |现在排行榜名次|
|his_rank| 历史排行榜名词|
|like |点赞数|
