#!coding:utf-8    相信这句大家都懂的，不解释

#导入需要的python模块httplib，用来模拟提交http请求，详细的用法可见python帮助手册

import httplib

#导入需要的python模块urllib，用来对数据进行编码
import urllib
#定义请求头

reqheaders={'Content-type':'application/x-www-form-urlencoded',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Host':'www.renren.com',
'Origin':'http://zhichang.renren.com',
'Referer':'http://zhichang.renren.com',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',}

#定义post的参数

reqdata={'email':'xxxx@xxx.com',
'password':'xxxx',
'autoLogin':'on',
'origURL':'http://zhichang.renren.com/?login_state=rr',
'domain':'renren.com'
}

#对请求参数进行编码

data=urllib.urlencode(reqdata)

#利用httplib库模拟接口请求

#先连接到人人

conn=httplib.HTTPConnection('renren.com')

#提交登录的post请求
conn.request('POST', '/PLogin.do', data, reqheaders)

#获取服务器的返回
res=conn.getresponse()

#打印服务器返回的状态
print(res.status)

#以dictionary形式答应服务器返回的 response header

print(res.msg)
#打印服务器返回请求头中设置的cookie
print(res.getheader('Set-Cookie'))

#以下为运行程序后的结果

302 登录成功后重定向了
Server: nginx/1.2.0
Date: Sat, 15 Feb 2014 04:47:09 GMT
Content-Length: 80
Connection: keep-alive
Cache-Control: no-cache
Pragma: no-cache
Expires: Thu, 01 Jan 1970 00:00:00 GMT
Location: http://zhichang.renren.com/?login_state=rr    重定向的URL
Set-Cookie: anonymid=hroelq3l-czxmdy; domain=.renren.com; path=/; expires=Thu, 14-Feb-2019 04:47:09 GMT
Set-Cookie: _de=97FB170A42B4342D1C47A157AD77AAFC1383380866D39FF5; domain=.renren.com; path=/; expires=Tue, 10-Feb-2015 04:47:09 GMT
Set-Cookie: p=31991a0a194c34e606ef1263317b06372; domain=renren.com; path=/; expires=Mon, 17-Mar-2014 04:47:09 GMT
Set-Cookie: ap=229996362; domain=renren.com; path=/; expires=Mon, 17-Mar-2014 04:47:09 GMT
Set-Cookie: first_login_flag=1; domain=renren.com; path=/
Set-Cookie: t=c5424876f4a3363b98b6f92e677f04bc2; domain=.renren.com; path=/
Set-Cookie: t=a0196d1d663ad5a060ee47466123042d; domain=renren.com; path=/xtalk/
Set-Cookie: societyguester=c5424876f4a3363b98b6f92e677f04bc2; domain=.renren.com; path=/
Set-Cookie: id=229996362; domain=.renren.com; path=/  （这个是返回的人人ID）
Set-Cookie: xnsid=cc216a6b; domain=.renren.com; path=/  （有这个就登录成功了）
Set-Cookie: loginfrom=syshome; domain=.renren.com; path=/

#以下就是cookie了，以后发请求，就可以带上这个cookie

anonymid=hroelq3l-czxmdy; domain=.renren.com; path=/; expires=Thu, 14-Feb-2019 04:47:09 GMT, _de=97FB170A42B4342D1C47A157AD77AAFC1383380866D39FF5; domain=.renren.com; path=/; expires=Tue, 10-Feb-2015 04:47:09 GMT, p=31991a0a194c34e606ef1263317b06372; domain=renren.com; path=/; expires=Mon, 17-Mar-2014 04:47:09 GMT, ap=229996362; domain=renren.com; path=/; expires=Mon, 17-Mar-2014 04:47:09 GMT, first_login_flag=1; domain=renren.com; path=/, t=c5424876f4a3363b98b6f92e677f04bc2; domain=.renren.com; path=/, t=a0196d1d663ad5a060ee47466123042d; domain=renren.com; path=/xtalk/, societyguester=c5424876f4a3363b98b6f92e677f04bc2; domain=.renren.com; path=/, id=229996362; domain=.renren.com; path=/, xnsid=cc216a6b; domain=.renren.com; path=/, loginfrom=syshome; domain=.renren.com; path=/
