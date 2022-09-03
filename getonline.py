import requests
import json
import datetime
import time

import get_video

# 自定义配置项
checkingList = ['BV1aW4y1q7si','BV1DG4y1i7Lu'] # 被检测的视频列表,请填写bvid,默认(目前只能)获取视频的首个分p
EACH_VIDEO_GAPTIME = 3 # (秒) 建议最小次3秒
EACH_ROUND_GAPTIME = 60 # (秒) 建议最小每轮回60秒
UPGRADE_VIDEO_DETAIL = 1 # 0 关闭视频细节更新(包括浏览数 点赞数 投币数等); 1 开启关闭视频细节更新 

# 下方为程序自用配置项,无需改动
STATUS_INIT = -1
checkingListVideo =[]

def printTime():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log(10,now_time)

def log(status,text):
    stText = ''
    if(status == 0): # 正常日志
        stText = '[-]'
    if(status == 1): # 通知
        stText = '[●]'
    if(status == -1): # 警告
        stText = '[!]'
    if(status == 2): # 间隔
        stText = '[/]'
        print('{} {}'.format(stText,text*80))
        return
    if(status == 10): # 时间
        stText = '[~]'
    
    print('{} {}'.format(stText,text))

def getOnline(v:get_video.bv):
    api = "https://api.bilibili.com/x/player/online/total?aid={}&cid={}&bvid={}".format(v.aid,v.cid,v.bvid)
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
        "Referer":"https://www.bilibili.com/video/{}".format(v.bvid),
        "Origin":"https://www.bilibili.com"
    }
    
    response = requests.get(api,headers=headers)
    data = json.loads(response.text)
    online = int(data['data']['total'])
    return online

def init():
    global checkingList,checkingListVideo,EACH_VIDEO_GAPTIME,STATUS_INIT

    for video in checkingList:
        v = get_video.getVideoClass(video)
        checkingListVideo.append(v)
        log(1,'Appended Video:{}'.format(v.title))
        time.sleep(EACH_VIDEO_GAPTIME)
    
    STATUS_INIT = 1
        
    

def main():
    init()
    global checkingListVideo,EACH_VIDEO_GAPTIME,EACH_ROUND_GAPTIME,UPGRADE_VIDEO_DETAIL,STATUS_INIT

    while 1:
        printTime()
        if(UPGRADE_VIDEO_DETAIL == 0):
            for video in checkingListVideo:
                
                online = getOnline(video)
                log(0,"bvid:{} Title:{}... Online:{}".format(video.bvid,video.title[:16],online))
                time.sleep(EACH_VIDEO_GAPTIME)

        if(UPGRADE_VIDEO_DETAIL == 1):
            if(STATUS_INIT == 0): 
                cacheList= [] # 视频细节更新方法为删除原表并重新制作新表，再获取在线人数
                for video in checkingListVideo: 
                    cacheList.append(video.bvid)

                checkingListVideo.clear()
                log(1,'Checking List cleared')
                for bv in cacheList:
                    v = get_video.getVideoClass(bv)
                    checkingListVideo.append(v)
                    log(1,'Upgrade Video:{}'.format(v.title))
                    time.sleep(EACH_VIDEO_GAPTIME)

                for video in checkingListVideo:
                    
                    online = getOnline(video)
                    log(0,"bvid:{} Title:{}... Online:{} View:{}".format(video.bvid,video.title[:16],online,video.stat.view))
                    time.sleep(EACH_VIDEO_GAPTIME)
            else: # 若是初始化模式，不需要再次更新
                for video in checkingListVideo:
                    online = getOnline(video)
                    log(0,"bvid:{} Title:{}... Online:{} View:{}".format(video.bvid,video.title[:16],online,video.stat.view))
                    time.sleep(EACH_VIDEO_GAPTIME)
                    
        log(2,'-')
        STATUS_INIT = 0
        time.sleep(EACH_ROUND_GAPTIME)

main()
