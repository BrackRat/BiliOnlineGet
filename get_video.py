import requests
import json as jsonp

api = 'http://api.bilibili.com/x/web-interface/view?bvid='
class owner:
    mid = 0
    name = ''
    face = ''
    def __init__(self,mid,name,face):
        self.mid = mid
        self.name = name 
        self.face = face

class stat:
    view = -1
    danmaku = -1
    reply = -1
    favorite = -1
    coin = -1
    share = -1
    now_rank = -1
    his_rank = -1
    like = -1
    def __init__(self,view,danmaku,reply,favorite,coin,share,now_rank,his_rank,like):
        self.view = view
        self.danmaku = danmaku
        self.reply = reply
        self.favorite =favorite
        self.coin =coin
        self.share = share
        self.now_rank =now_rank
        self.his_rank =his_rank
        self.like = like

class bv:
    bvid = ''
    aid = -1
    cid = -1
    tid = -1
    tname= ''
    copyright = -1
    pic = ''
    title  =''
    pubdate = -1
    ctime = -1
    desc = ''
    state = -1
    duration = -1
    owner = owner
    stat = stat

    def __init__(self,bvid,aid,cid,tid,tname,copyright,pic,title,pubdate,ctime,desc,state,duration,owner,stat):
        self.bvid = bvid      
        self.aid = aid
        self.cid = cid
        self.tid = tid
        self.tname= tname
        self.copyright = copyright
        self.pic = pic
        self.title  =title
        self.pubdate = pubdate
        self.ctime = ctime
        self.desc = desc
        self.state = state
        self.duration = duration
        self.owner = owner
        self.stat = stat



def getJsonFromBvid(bvid):
    response = requests.get(api + bvid)
    # print(response.text)
    info = ''
    info = response.text
    return info 

def parseInfoFromJson(infoj):
    # print(infoj)
    try:
        jj = jsonp.loads(infoj)
    except Exception:
        print('[!] ErrorCannotLoadJson:{}'.format(Exception.with_traceback))
    try:
        data = jj['data']
    except Exception:
        print('[!] ErrorCannotParseJson:{}'.format(Exception.with_traceback))
    statS = data['stat']
    statC = stat(statS['view'],statS['danmaku'],statS['reply'],statS['favorite'],statS['coin'],statS['share'],statS['now_rank'],statS['his_rank'],statS['like'])
    ownerS = data['owner']
    ownerC = owner(ownerS['mid'],ownerS['name'],ownerS['face'])
    infoC = bv(data['bvid'],data['aid'],data['cid'],data['tid'],data['tname'],data['copyright'],data['pic'],data['title'],data['pubdate'],data['ctime'],data['desc'],data['state'],data['duration'],ownerC,statC)
    return infoC


def getVideoClass(bvid):
    
    json = getJsonFromBvid(bvid)
    bvClass = parseInfoFromJson(json)
    return bvClass
