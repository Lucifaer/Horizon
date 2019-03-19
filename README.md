# Horizon
自己慢慢完善的一个爬虫小框架

# Usage

对于next page这样的模型，只需要配置一个json文件即可完成信息抓取。

由于这个只是服务于每日推送的消息抓取，所以现在还没有配置全站抓取。

json文件的格式参考config目录下的文件，抓取的消息实例如下：

```
{
    'date': '• 1\xa0day ago',
    'link': 'https://sec.todaypulses/pulsesfc25e677-2e17-44b4-983a-76ec84acb6c0/',
    'tag': 'Pentest',
    'title': 'Fileless UAC Bypass in Windows Store Binary - Active Cyber'
}
```