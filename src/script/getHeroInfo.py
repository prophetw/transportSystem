from bs4 import BeautifulSoup
import requests
import os
import json

#  target url https://pvp.qq.com/web201605/herolist.shtml
result = requests.get('https://pvp.qq.com/web201605/herolist.shtml')
baseurl = 'https://pvp.qq.com/web201605/'

# html.parser lxml html5lib https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
soup = BeautifulSoup(result.content, 'lxml')
ul = soup.find('ul', class_="herolist")
print(ul.get('class'))
allli = ul.find_all('li')
a = allli[0].find('a')
img = a.find('img')
print(a)
# print(a.get('href'))

herodata = []
#<li><a href="herodetail/112.shtml" target="_blank"><img alt="鲁班七号" height="91" src="//game.gtimg.cn/images/yxzj/img201606/heroimg/112/112.jpg" width="91"/>鲁班七号</a></li>
#<li><a href="herodetail/111.shtml" target="_blank"><img alt="孙尚香" height="91" src="//game.gtimg.cn/images/yxzj/img201606/heroimg/111/111.jpg" width="91"/>孙尚香</a></li>
#<li><a href="herodetail/110.shtml" target="_blank"><img alt="嬴政" height="91" src="//game.gtimg.cn/images/yxzj/img201606/heroimg/110/110.jpg" width="91"/>嬴政</a></li>
#<li><a href="herodetail/109.shtml" target="_blank"><img alt="妲己" height="91" src="//game.gtimg.cn/images/yxzj/img201606/heroimg/109/109.jpg" width="91"/>妲己</a></li>

# url game.gtimg.cn/images/yxzj/img201606/heroimg/109/109.jpg
# dirName
# name 109.jpg
def downloadImg(url):
    dirName = '../assets/img'
    # game.gtimg.cn/images/yxzj/img201606/heroimg/109/109.jpg
    # 暂时的方案是 把链接存到文件名 这样就可以通过文件名 来找到网页的图片了
    # 例如
    # 存成 ooxx/page-2307#comment-3362040.jpg
    r = requests.get(url)
    if os.path.exists(dirName)==False:
        os.makedirs(dirName)
    name = getNameFrom(url)
    with open(dirName+'/'+name, "wb") as code:
        code.write(r.content)

def getNameFrom(url):
    arr = url.split('/')
    name = arr[len(arr)-1]
    return name

def getHeroIdFrom(name):
    arr = name.split('.')
    return arr[0]



headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh,en;q=0.9,ja;q=0.8,zh-CN;q=0.7",
    "cache-control": "no-cache",
    "content-length": "2141",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://image.ttwz.qq.com",
    "pragma": "no-cache",
    "referer": "https://image.ttwz.qq.com/h5/webdist/hero-detail.html?heroid=170&isNavigationBarHidden=1&isOpenBattleAssist=0&serverName=%E5%BE%AE%E4%BF%A123%E5%8C%BA&areaName=%E8%8B%B9%E6%9E%9C&roleName=%40%E5%9C%A8%E4%B8%8B%E5%A4%B4%E5%BE%88%E9%93%81&nickname=%E5%95%8A%E5%93%9F%E5%96%82&isMainRole=1&appOpenid=oFhrws0NjsdfWNNhijrnmTacOqXE&areaId=4&roleId=147160808&gameId=20001&roleJob=%E6%B0%B8%E6%81%92%E9%92%BB%E7%9F%B3II&serverId=4033&accessToken=29_lMWK120HzDySDCXAK-_LOGFFHd2e18yK370cMVf5UnN8mi1HMZukaX37OYFedDClhIMV0y3IDDwjF-XB46zeQL1e-T-NE-oP8gvOhzYn6lA&isOpenBattlePro=0&gameOpenid=owanlssmmfbLCulJiyj0EsCo87mo&uniqueRoleId=966203057&toOpenid=owanlssmmfbLCulJiyj0EsCo87mo&filterType=0&roleLevel=30&userId=491092625&appVersion=2019101809&appVersionName=3.46.202&qi=1&wi=1&z=4033&zn=%E8%8B%B9%E6%9E%9C%E5%BE%AE%E4%BF%A123%E5%8C%BA&role=%40%E5%9C%A8%E4%B8%8B%E5%A4%B4%E5%BE%88%E9%93%81&platid=0&source=smoba_zhushou&algorithm=v2&version=3.1.96i&timestamp=1579075818922&appid=wxf4b1e8a3e9aaf978&openid=oFhrws0NjsdfWNNhijrnmTacOqXE&sig=e38861f7866b665d647f7d7909e83c9b&encode=2&msdkEncodeParam=D579695278A08EA1C34BEE5F1FC69EE8E941837A1E2DFEE41DC4E2DDE93B9F1597EDD91F731B36A802F899E1FFF4C06967D8A8159D83A7C8A0EE667209CDDB0326EC816DE2E8872DF1CF6F3EDA90CD9AA68286A7635BCED544E617B56D49B29DD74BD40DCEEF0DD6B921B3B770098DF96E41F8CFA81516BBE665FD150B37D71E64F4060D54496A7C50353CE6308C1CD6E0CE54212DEFC45EEFD3F83B1DCB1178172258D861C3F4795BC0719F2DDFD972BC50175B6DDED3B77489B0FDC1541F8F025BBA395E6706FED6AF0D31B2EFF56DAFFC3AC4BF124E7B5F7F1C90620EFF6F4D598F7E6D777307ACC36E548121BE3ADF0E1959FF638DF78D2AEE66C521175785FC378A4E5FC24F916C25698A93CFDB3DD454DC32DD5535003FC7D00CF27F72525F82A8CC171CAA361D25962397F96167FADD56FDD013833A7E4380CD95D3416CD047CC1716E1891F1029261E7746279057F106DE2652B4%27%20--data-binary%20%22heroid=149&isNavigationBarHidden=1&isOpenBattleAssist=0&serverName=%25E5%25BE%25AE%25E4%25BF%25A123%25E5%258C%25BA&areaName=%25E8%258B%25B9%25E6%259E%259C&roleName=%2540%25E5%259C%25A8%25E4%25B8%258B%25E5%25A4%25B4%25E5%25BE%2588%25E9%2593%2581&nickname=%25E5%2595%258A%25E5%2593%259F%25E5%2596%2582&isMainRole=1&appOpenid=oFhrws0NjsdfWNNhijrnmTacOqXE&areaId=4&roleId=147160808&gameId=20001&roleJob=%25E6%25B0%25B8%25E6%2581%2592%25E9%2592%25BB%25E7%259F%25B3II&serverId=4033&accessToken=29_lMWK120HzDySDCXAK-_LOGFFHd2e18yK370cMVf5UnN8mi1HMZukaX37OYFedDClhIMV0y3IDDwjF-XB46zeQL1e-T-NE-oP8gvOhzYn6lA&isOpenBattlePro=0&gameOpenid=owanlssmmfbLCulJiyj0EsCo87mo&uniqueRoleId=966203057&toOpenid=owanlssmmfbLCulJiyj0EsCo87mo&filterType=0&roleLevel=30&userId=491092625&appVersion=2019101809&appVersionName=3.46.202&qi=1&wi=1&z=4033&zn=%25E8%258B%25B9%25E6%259E%259C%25E5%25BE%25AE%25E4%25BF%25A123%25E5%258C%25BA&role=%2540%25E5%259C%25A8%25E4%25B8%258B%25E5%25A4%25B4%25E5%25BE%2588%25E9%2593%2581&platid=0&source=smoba_zhushou&algorithm=v2&version=3.1.96i&timestamp=1579075818922&appid=wxf4b1e8a3e9aaf978&openid=oFhrws0NjsdfWNNhijrnmTacOqXE&sig=e38861f7866b665d647f7d7909e83c9b&encode=2&msdkEncodeParam=D579695278A08EA1C34BEE5F1FC69EE8E941837A1E2DFEE41DC4E2DDE93B9F1597EDD91F731B36A802F899E1FFF4C06967D8A8159D83A7C8A0EE667209CDDB0326EC816DE2E8872DF1CF6F3EDA90CD9AA68286A7635BCED544E617B56D49B29DD74BD40DCEEF0DD6B921B3B770098DF96E41F8CFA81516BBE665FD150B37D71E64F4060D54496A7C50353CE6308C1CD6E0CE54212DEFC45EEFD3F83B1DCB1178172258D861C3F4795BC0719F2DDFD972BC50175B6DDED3B77489B0FDC1541F8F025BBA395E6706FED6AF0D31B2EFF56DAFFC3AC4BF124E7B5F7F1C90620EFF6F4D598F7E6D777307ACC36E548121BE3ADF0E1959FF638DF78D2AEE66C521175785FC378A4E5FC24F916C25698A93CFDB3DD454DC32DD5535003FC7D00CF27F72525F82A8CC171CAA361D25962397F96167FADD56FDD013833A7E4380CD95D3416CD047CC1716E1891F1029261E7746279057F106DE2652B4&gameOpenId=owanlssmmfbLCulJiyj0EsCo87mo&heroId=149&cSystem=ios&msdkToken=4eNjTZGe&h5Get=1",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
}
formdata = {
    "heroId": "174",
    "heroid": "174",
    "isNavigationBarHidden": "1",
    "isOpenBattleAssist": "0",
    "serverName": "%25E5%25BE%25AE%25E4%25BF%25A123%25E5%258C%25BA",
    "areaName": "%25E8%258B%25B9%25E6%259E%259C",
    "roleName": "%2540%25E5%259C%25A8%25E4%25B8%258B%25E5%25A4%25B4%25E5%25BE%2588%25E9%2593%2581",
    "nickname": "%25E5%2595%258A%25E5%2593%259F%25E5%2596%2582",
    "isMainRole": "1",
    "appOpenid": "oFhrws0NjsdfWNNhijrnmTacOqXE",
    "areaId": "4",
    "roleId": "147160808",
    "gameId": "20001",
    "roleJob": "%25E6%25B0%25B8%25E6%2581%2592%25E9%2592%25BB%25E7%259F%25B3II",
    "serverId": "4033",
    "accessToken": "29_lMWK120HzDySDCXAK-_LOGFFHd2e18yK370cMVf5UnN8mi1HMZukaX37OYFedDClhIMV0y3IDDwjF-XB46zeQL1e-T-NE-oP8gvOhzYn6lA",
    "isOpenBattlePro": "0",
    "gameOpenid": "owanlssmmfbLCulJiyj0EsCo87mo",
    "uniqueRoleId": "966203057",
    "toOpenid": "owanlssmmfbLCulJiyj0EsCo87mo",
    "filterType": "0",
    "roleLevel": "30",
    "userId": "491092625",
    "appVersion": "2019101809",
    "appVersionName": "3.46.202",
    "qi": "1",
    "wi": "1",
    "z": "4033",
    "zn": "%25E8%258B%25B9%25E6%259E%259C%25E5%25BE%25AE%25E4%25BF%25A123%25E5%258C%25BA",
    "role": "%2540%25E5%259C%25A8%25E4%25B8%258B%25E5%25A4%25B4%25E5%25BE%2588%25E9%2593%2581",
    "platid": "0",
    "source": "smoba_zhushou",
    "algorithm": "v2",
    "version": "3.1.96i",
    "timestamp": "1579075818922",
    "appid": "wxf4b1e8a3e9aaf978",
    "openid": "oFhrws0NjsdfWNNhijrnmTacOqXE",
    "sig": "e38861f7866b665d647f7d7909e83c9b",
    "encode": "2",
    "msdkEncodeParam": "D579695278A08EA1C34BEE5F1FC69EE8E941837A1E2DFEE41DC4E2DDE93B9F1597EDD91F731B36A802F899E1FFF4C06967D8A8159D83A7C8A0EE667209CDDB0326EC816DE2E8872DF1CF6F3EDA90CD9AA68286A7635BCED544E617B56D49B29DD74BD40DCEEF0DD6B921B3B770098DF96E41F8CFA81516BBE665FD150B37D71E64F4060D54496A7C50353CE6308C1CD6E0CE54212DEFC45EEFD3F83B1DCB1178172258D861C3F4795BC0719F2DDFD972BC50175B6DDED3B77489B0FDC1541F8F025BBA395E6706FED6AF0D31B2EFF56DAFFC3AC4BF124E7B5F7F1C90620EFF6F4D598F7E6D777307ACC36E548121BE3ADF0E1959FF638DF78D2AEE66C521175785FC378A4E5FC24F916C25698A93CFDB3DD454DC32DD5535003FC7D00CF27F72525F82A8CC171CAA361D25962397F96167FADD56FDD013833A7E4380CD95D3416CD047CC1716E1891F1029261E7746279057F106DE2652B4",
    "gameOpenId": "owanlssmmfbLCulJiyj0EsCo87mo",
    "cSystem": "ios",
    "msdkToken": "w2J8D59q",
    "h5Get": "1",
}
def getHeroExtraInfo(heroIdStr):
    herobaseurl = "https://ssl.kohsocialapp.qq.com:10001/hero/getheroextrainfo"
    # 克制信息 post
    # Request URL: https://ssl.kohsocialapp.qq.com:10001/hero/getheroextrainfo
    # Request Method: POST
    # cURL
    # curl -H 'Host: ssl.kohsocialapp.qq.com:10001' -H 'accept: application/json, text/plain, */*'
    # -H 'content-type: application/x-www-form-urlencoded'
    # -H 'origin: https://image.ttwz.qq.com' -H 'accept-language: zh-cn'
    # -H 'user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;GameHelper;smobagamehelper,iphoneX'
    # -H 'referer: https://image.ttwz.qq.com/h5/webdist/hero-detail.html?heroid=149&isNavigationBarHidden=1&isOpenBattleAssist=0&serverName=%E5%BE%AE%E4%BF%A123%E5%8C%BA&areaName=%E8%8B%B9%E6%9E%9C&roleName=%40%E5%9C%A8%E4%B8%8B%E5%A4%B4%E5%BE%88%E9%93%81&nickname=%E5%95%8A%E5%93%9F%E5%96%82&isMainRole=1&appOpenid=oFhrws0NjsdfWNNhijrnmTacOqXE&areaId=4&roleId=147160808&gameId=20001&roleJob=%E6%B0%B8%E6%81%92%E9%92%BB%E7%9F%B3II&serverId=4033&accessToken=29_lMWK120HzDySDCXAK-_LOGFFHd2e18yK370cMVf5UnN8mi1HMZukaX37OYFedDClhIMV0y3IDDwjF-XB46zeQL1e-T-NE-oP8gvOhzYn6lA&isOpenBattlePro=0&gameOpenid=owanlssmmfbLCulJiyj0EsCo87mo&uniqueRoleId=966203057&toOpenid=owanlssmmfbLCulJiyj0EsCo87mo&filterType=0&roleLevel=30&userId=491092625&appVersion=2019101809&appVersionName=3.46.202&qi=1&wi=1&z=4033&zn=%E8%8B%B9%E6%9E%9C%E5%BE%AE%E4%BF%A123%E5%8C%BA&role=%40%E5%9C%A8%E4%B8%8B%E5%A4%B4%E5%BE%88%E9%93%81&platid=0&source=smoba_zhushou&algorithm=v2&version=3.1.96i&timestamp=1579075818922&appid=wxf4b1e8a3e9aaf978&openid=oFhrws0NjsdfWNNhijrnmTacOqXE&sig=e38861f7866b665d647f7d7909e83c9b&encode=2&msdkEncodeParam=D579695278A08EA1C34BEE5F1FC69EE8E941837A1E2DFEE41DC4E2DDE93B9F1597EDD91F731B36A802F899E1FFF4C06967D8A8159D83A7C8A0EE667209CDDB0326EC816DE2E8872DF1CF6F3EDA90CD9AA68286A7635BCED544E617B56D49B29DD74BD40DCEEF0DD6B921B3B770098DF96E41F8CFA81516BBE665FD150B37D71E64F4060D54496A7C50353CE6308C1CD6E0CE54212DEFC45EEFD3F83B1DCB1178172258D861C3F4795BC0719F2DDFD972BC50175B6DDED3B77489B0FDC1541F8F025BBA395E6706FED6AF0D31B2EFF56DAFFC3AC4BF124E7B5F7F1C90620EFF6F4D598F7E6D777307ACC36E548121BE3ADF0E1959FF638DF78D2AEE66C521175785FC378A4E5FC24F916C25698A93CFDB3DD454DC32DD5535003FC7D00CF27F72525F82A8CC171CAA361D25962397F96167FADD56FDD013833A7E4380CD95D3416CD047CC1716E1891F1029261E7746279057F106DE2652B4' --data-binary "heroid=149&isNavigationBarHidden=1&isOpenBattleAssist=0&serverName=%25E5%25BE%25AE%25E4%25BF%25A123%25E5%258C%25BA&areaName=%25E8%258B%25B9%25E6%259E%259C&roleName=%2540%25E5%259C%25A8%25E4%25B8%258B%25E5%25A4%25B4%25E5%25BE%2588%25E9%2593%2581&nickname=%25E5%2595%258A%25E5%2593%259F%25E5%2596%2582&isMainRole=1&appOpenid=oFhrws0NjsdfWNNhijrnmTacOqXE&areaId=4&roleId=147160808&gameId=20001&roleJob=%25E6%25B0%25B8%25E6%2581%2592%25E9%2592%25BB%25E7%259F%25B3II&serverId=4033&accessToken=29_lMWK120HzDySDCXAK-_LOGFFHd2e18yK370cMVf5UnN8mi1HMZukaX37OYFedDClhIMV0y3IDDwjF-XB46zeQL1e-T-NE-oP8gvOhzYn6lA&isOpenBattlePro=0&gameOpenid=owanlssmmfbLCulJiyj0EsCo87mo&uniqueRoleId=966203057&toOpenid=owanlssmmfbLCulJiyj0EsCo87mo&filterType=0&roleLevel=30&userId=491092625&appVersion=2019101809&appVersionName=3.46.202&qi=1&wi=1&z=4033&zn=%25E8%258B%25B9%25E6%259E%259C%25E5%25BE%25AE%25E4%25BF%25A123%25E5%258C%25BA&role=%2540%25E5%259C%25A8%25E4%25B8%258B%25E5%25A4%25B4%25E5%25BE%2588%25E9%2593%2581&platid=0&source=smoba_zhushou&algorithm=v2&version=3.1.96i&timestamp=1579075818922&appid=wxf4b1e8a3e9aaf978&openid=oFhrws0NjsdfWNNhijrnmTacOqXE&sig=e38861f7866b665d647f7d7909e83c9b&encode=2&msdkEncodeParam=D579695278A08EA1C34BEE5F1FC69EE8E941837A1E2DFEE41DC4E2DDE93B9F1597EDD91F731B36A802F899E1FFF4C06967D8A8159D83A7C8A0EE667209CDDB0326EC816DE2E8872DF1CF6F3EDA90CD9AA68286A7635BCED544E617B56D49B29DD74BD40DCEEF0DD6B921B3B770098DF96E41F8CFA81516BBE665FD150B37D71E64F4060D54496A7C50353CE6308C1CD6E0CE54212DEFC45EEFD3F83B1DCB1178172258D861C3F4795BC0719F2DDFD972BC50175B6DDED3B77489B0FDC1541F8F025BBA395E6706FED6AF0D31B2EFF56DAFFC3AC4BF124E7B5F7F1C90620EFF6F4D598F7E6D777307ACC36E548121BE3ADF0E1959FF638DF78D2AEE66C521175785FC378A4E5FC24F916C25698A93CFDB3DD454DC32DD5535003FC7D00CF27F72525F82A8CC171CAA361D25962397F96167FADD56FDD013833A7E4380CD95D3416CD047CC1716E1891F1029261E7746279057F106DE2652B4&gameOpenId=owanlssmmfbLCulJiyj0EsCo87mo&heroId=149&cSystem=ios&msdkToken=4eNjTZGe&h5Get=1"
    # --compressed 'https://ssl.kohsocialapp.qq.com:10001/hero/getheroextrainfo'
    # heroid=149&isNavigationBarHidden=1&isOpenBattleAssist=0&serverName=%25E5%25BE%25AE%25E4%25BF%25A123%25E5%258C%25BA&areaName=%25E8%258B%25B9%25E6%259E%259C&roleName=%2540%25E5%259C%25A8%25E4%25B8%258B%25E5%25A4%25B4%25E5%25BE%2588%25E9%2593%2581&nickname=%25E5%2595%258A%25E5%2593%259F%25E5%2596%2582&isMainRole=1&appOpenid=oFhrws0NjsdfWNNhijrnmTacOqXE&areaId=4&roleId=147160808&gameId=20001&roleJob=%25E6%25B0%25B8%25E6%2581%2592%25E9%2592%25BB%25E7%259F%25B3II&serverId=4033&accessToken=29_lMWK120HzDySDCXAK-_LOGFFHd2e18yK370cMVf5UnN8mi1HMZukaX37OYFedDClhIMV0y3IDDwjF-XB46zeQL1e-T-NE-oP8gvOhzYn6lA&isOpenBattlePro=0&gameOpenid=owanlssmmfbLCulJiyj0EsCo87mo&uniqueRoleId=966203057&toOpenid=owanlssmmfbLCulJiyj0EsCo87mo&filterType=0&roleLevel=30&userId=491092625&appVersion=2019101809&appVersionName=3.46.202&qi=1&wi=1&z=4033&zn=%25E8%258B%25B9%25E6%259E%259C%25E5%25BE%25AE%25E4%25BF%25A123%25E5%258C%25BA&role=%2540%25E5%259C%25A8%25E4%25B8%258B%25E5%25A4%25B4%25E5%25BE%2588%25E9%2593%2581&platid=0&source=smoba_zhushou&algorithm=v2&version=3.1.96i&timestamp=1579075818922&appid=wxf4b1e8a3e9aaf978&openid=oFhrws0NjsdfWNNhijrnmTacOqXE&sig=e38861f7866b665d647f7d7909e83c9b&encode=2&msdkEncodeParam=D579695278A08EA1C34BEE5F1FC69EE8E941837A1E2DFEE41DC4E2DDE93B9F1597EDD91F731B36A802F899E1FFF4C06967D8A8159D83A7C8A0EE667209CDDB0326EC816DE2E8872DF1CF6F3EDA90CD9AA68286A7635BCED544E617B56D49B29DD74BD40DCEEF0DD6B921B3B770098DF96E41F8CFA81516BBE665FD150B37D71E64F4060D54496A7C50353CE6308C1CD6E0CE54212DEFC45EEFD3F83B1DCB1178172258D861C3F4795BC0719F2DDFD972BC50175B6DDED3B77489B0FDC1541F8F025BBA395E6706FED6AF0D31B2EFF56DAFFC3AC4BF124E7B5F7F1C90620EFF6F4D598F7E6D777307ACC36E548121BE3ADF0E1959FF638DF78D2AEE66C521175785FC378A4E5FC24F916C25698A93CFDB3DD454DC32DD5535003FC7D00CF27F72525F82A8CC171CAA361D25962397F96167FADD56FDD013833A7E4380CD95D3416CD047CC1716E1891F1029261E7746279057F106DE2652B4&gameOpenId=owanlssmmfbLCulJiyj0EsCo87mo&heroId=149&cSystem=ios&msdkToken=4eNjTZGe&h5Get=1
    # url 可以直接打开
    # https://image.ttwz.qq.com/h5/webdist/hero-detail.html?heroid=170&isNavigationBarHidden=1&isOpenBattleAssist=0&serverName=%E5%BE%AE%E4%BF%A123%E5%8C%BA&areaName=%E8%8B%B9%E6%9E%9C&roleName=%40%E5%9C%A8%E4%B8%8B%E5%A4%B4%E5%BE%88%E9%93%81&nickname=%E5%95%8A%E5%93%9F%E5%96%82&isMainRole=1&appOpenid=oFhrws0NjsdfWNNhijrnmTacOqXE&areaId=4&roleId=147160808&gameId=20001&roleJob=%E6%B0%B8%E6%81%92%E9%92%BB%E7%9F%B3II&serverId=4033&accessToken=29_lMWK120HzDySDCXAK-_LOGFFHd2e18yK370cMVf5UnN8mi1HMZukaX37OYFedDClhIMV0y3IDDwjF-XB46zeQL1e-T-NE-oP8gvOhzYn6lA&isOpenBattlePro=0&gameOpenid=owanlssmmfbLCulJiyj0EsCo87mo&uniqueRoleId=966203057&toOpenid=owanlssmmfbLCulJiyj0EsCo87mo&filterType=0&roleLevel=30&userId=491092625&appVersion=2019101809&appVersionName=3.46.202&qi=1&wi=1&z=4033&zn=%E8%8B%B9%E6%9E%9C%E5%BE%AE%E4%BF%A123%E5%8C%BA&role=%40%E5%9C%A8%E4%B8%8B%E5%A4%B4%E5%BE%88%E9%93%81&platid=0&source=smoba_zhushou&algorithm=v2&version=3.1.96i&timestamp=1579075818922&appid=wxf4b1e8a3e9aaf978&openid=oFhrws0NjsdfWNNhijrnmTacOqXE&sig=e38861f7866b665d647f7d7909e83c9b&encode=2&msdkEncodeParam=D579695278A08EA1C34BEE5F1FC69EE8E941837A1E2DFEE41DC4E2DDE93B9F1597EDD91F731B36A802F899E1FFF4C06967D8A8159D83A7C8A0EE667209CDDB0326EC816DE2E8872DF1CF6F3EDA90CD9AA68286A7635BCED544E617B56D49B29DD74BD40DCEEF0DD6B921B3B770098DF96E41F8CFA81516BBE665FD150B37D71E64F4060D54496A7C50353CE6308C1CD6E0CE54212DEFC45EEFD3F83B1DCB1178172258D861C3F4795BC0719F2DDFD972BC50175B6DDED3B77489B0FDC1541F8F025BBA395E6706FED6AF0D31B2EFF56DAFFC3AC4BF124E7B5F7F1C90620EFF6F4D598F7E6D777307ACC36E548121BE3ADF0E1959FF638DF78D2AEE66C521175785FC378A4E5FC24F916C25698A93CFDB3DD454DC32DD5535003FC7D00CF27F72525F82A8CC171CAA361D25962397F96167FADD56FDD013833A7E4380CD95D3416CD047CC1716E1891F1029261E7746279057F106DE2652B4%27%20--data-binary%20%22heroid=149&isNavigationBarHidden=1&isOpenBattleAssist=0&serverName=%25E5%25BE%25AE%25E4%25BF%25A123%25E5%258C%25BA&areaName=%25E8%258B%25B9%25E6%259E%259C&roleName=%2540%25E5%259C%25A8%25E4%25B8%258B%25E5%25A4%25B4%25E5%25BE%2588%25E9%2593%2581&nickname=%25E5%2595%258A%25E5%2593%259F%25E5%2596%2582&isMainRole=1&appOpenid=oFhrws0NjsdfWNNhijrnmTacOqXE&areaId=4&roleId=147160808&gameId=20001&roleJob=%25E6%25B0%25B8%25E6%2581%2592%25E9%2592%25BB%25E7%259F%25B3II&serverId=4033&accessToken=29_lMWK120HzDySDCXAK-_LOGFFHd2e18yK370cMVf5UnN8mi1HMZukaX37OYFedDClhIMV0y3IDDwjF-XB46zeQL1e-T-NE-oP8gvOhzYn6lA&isOpenBattlePro=0&gameOpenid=owanlssmmfbLCulJiyj0EsCo87mo&uniqueRoleId=966203057&toOpenid=owanlssmmfbLCulJiyj0EsCo87mo&filterType=0&roleLevel=30&userId=491092625&appVersion=2019101809&appVersionName=3.46.202&qi=1&wi=1&z=4033&zn=%25E8%258B%25B9%25E6%259E%259C%25E5%25BE%25AE%25E4%25BF%25A123%25E5%258C%25BA&role=%2540%25E5%259C%25A8%25E4%25B8%258B%25E5%25A4%25B4%25E5%25BE%2588%25E9%2593%2581&platid=0&source=smoba_zhushou&algorithm=v2&version=3.1.96i&timestamp=1579075818922&appid=wxf4b1e8a3e9aaf978&openid=oFhrws0NjsdfWNNhijrnmTacOqXE&sig=e38861f7866b665d647f7d7909e83c9b&encode=2&msdkEncodeParam=D579695278A08EA1C34BEE5F1FC69EE8E941837A1E2DFEE41DC4E2DDE93B9F1597EDD91F731B36A802F899E1FFF4C06967D8A8159D83A7C8A0EE667209CDDB0326EC816DE2E8872DF1CF6F3EDA90CD9AA68286A7635BCED544E617B56D49B29DD74BD40DCEEF0DD6B921B3B770098DF96E41F8CFA81516BBE665FD150B37D71E64F4060D54496A7C50353CE6308C1CD6E0CE54212DEFC45EEFD3F83B1DCB1178172258D861C3F4795BC0719F2DDFD972BC50175B6DDED3B77489B0FDC1541F8F025BBA395E6706FED6AF0D31B2EFF56DAFFC3AC4BF124E7B5F7F1C90620EFF6F4D598F7E6D777307ACC36E548121BE3ADF0E1959FF638DF78D2AEE66C521175785FC378A4E5FC24F916C25698A93CFDB3DD454DC32DD5535003FC7D00CF27F72525F82A8CC171CAA361D25962397F96167FADD56FDD013833A7E4380CD95D3416CD047CC1716E1891F1029261E7746279057F106DE2652B4&gameOpenId=owanlssmmfbLCulJiyj0EsCo87mo&heroId=149&cSystem=ios&msdkToken=4eNjTZGe&h5Get=1

    formdata["heroId"] = heroIdStr
    formdata["heroid"] = heroIdStr
    result = requests.post(herobaseurl, data=formdata, headers=headers)
    out = json.loads(result.text)
    # print(out['data']['bkzInfo'])
    return out['data']

def getAllHeroAvatar():
    for li in allli:
        a = li.find('a')
        img = a.find('img')
        imgurl = img.get('src')
        herochinesename = img.get('alt')
        savename = getNameFrom(imgurl)
        heroid = getHeroIdFrom(savename)
        hero = {
            "name": herochinesename,
            "id": heroid
        }
        herodata.append(hero)
        downloadImg('http:'+imgurl)
def getAllHeroData():
    for li in allli:
        hero = getHeroData(li)
        herodata.append(hero)
    return herodata

# soupobj  <li><a href="herodetail/112.shtml" target="_blank"><img alt="鲁班七号" height="91" src="//game.gtimg.cn/images/yxzj/img201606/heroimg/112/112.jpg" width="91"/>鲁班七号</a></li>
def getHeroData(lisoupobj):
    a = lisoupobj.find('a')
    herodetailurl = a.get('href')
    herodetaildata = getHeroDetailSoup(baseurl + herodetailurl)
    herotype = getHeroDetail(herodetaildata, 'type')
    # print(herotype)

    img = a.find('img')
    imgurl = img.get('src')
    herochinesename = img.get('alt')
    savename = getNameFrom(imgurl)
    heroid = getHeroIdFrom(savename)
    heroExInfo = getHeroExtraInfo(heroid)
    # bkzInfo
    # kzInfo
    hero = {
        "name": herochinesename,
        "id": heroid,
        "type": herotype,
        "exInfo": heroExInfo
    }
    return hero

def getHeroDetail(soup, prop):
    if prop == 'type':
        typeinfo = soup.find('span', class_="herodetail-sort")
        type = typeinfo.find('i').get('class')[0]
        if type == 'herodetail-sort-6':
            type = "辅助"
        if type == 'herodetail-sort-5':
            type = "射手"
        if type == 'herodetail-sort-4':
            type = "刺客"
        if type == 'herodetail-sort-3':
            type = "坦克"
        if type == 'herodetail-sort-2':
            type = "法师"
        if type == 'herodetail-sort-1':
            type = "战士"
        return type
def getHeroDetailSoup(url):
    herodetail = requests.get(url)
    soup = BeautifulSoup(herodetail.content, 'lxml')
    return soup
def exportHeroData(data):
    jsondata = json.dumps(data)
    with open("./hero.json", "w") as herodata:
        herodata.write(jsondata)
    return


# test downloadImg('http://game.gtimg.cn/images/yxzj/img201606/heroimg/109/109.jpg')
# getAllHeroAvatar()

# 获取英雄数据
# data = getAllHeroData()
# exportHeroData(data)

# getHeroData(allli[0])



# heroExInfo = getHeroExtraInfo("506")
# print(heroExInfo)





