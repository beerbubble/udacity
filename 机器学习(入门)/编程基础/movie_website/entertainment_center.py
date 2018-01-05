import media
import fresh_tomatoes

# young = media.Movie("芳华",
#                         "影片讲述了在充满理想和激情的部队文工团，一群正值芳华的年轻人在爱情萌发时经历了残酷战争的洗礼。",
#                         "http://img5.mtime.cn/mg/2017/12/09/120450.70160076_270X405X4.jpg",
#                         "http://video.mtime.com/67658/?mid=236404")

# print(young.storyline)

# young.show_trailer()

fanghua = media.Movie("芳华","影片讲述了在充满理想和激情的部队文工团，一群正值芳华的年轻人在爱情萌发时经历了残酷战争的洗礼。","2017","http://img5.mtime.cn/mg/2017/12/09/120450.70160076_270X405X4.jpg","http://v.youku.com/v_show/id_XMzAyMTgxNzA3Mg==.html")

panjinlian = media.Movie("我不是潘金莲","剧情讲述了李雪莲的前夫骂李雪莲是“潘金莲”。为了还自己一个清白，李雪莲开始状告他。","2016","http://img5.mtime.cn/mg/2016/09/05/145801.14583220_270X405X4.jpg","http://v.youku.com/v_show/id_XMjQ3ODU0NzIwMA==.html")

laopao = media.Movie("老炮儿","曾经风光四九城的老炮六爷，难以适应社会巨变，蛰伏于胡同深处，过着溜鸟、管闲事、发牢骚的无聊日子。","2015","http://img31.mtime.cn/mg/2015/12/09/094723.69065942_270X405X4.jpg","http://v.youku.com/v_show/id_XMTQ3NjIyNjQzNg==.html")

zidan = media.Movie("让子弹飞","八匹纯血高头白马四蹄翻飞，车轮与铁轨撞击隆隆作响，两节火车正以“马拉火车”的梦幻奇景奔腾在南部中国的崇山峻岭之间。","2010","http://img21.mtime.cn/mt/2010/11/23/102316.52177023_270X405X4.jpg","http://v.youku.com/v_show/id_XMTk0MDc0ODY0.html")

tangshan = media.Movie("唐山大地震","1969年，卡车司机方大强在祈祷中迎来了自己的龙凤胎儿女：方登、方达。妻子李元妮差点因为难产送命，好在母子平安，一家人欢喜地离开医院，从此过上普通却幸福的生活。","2010","http://img31.mtime.cn/mg/2016/09/05/193108.90431363_270X405X4.jpg","http://v.youku.com/v_show/id_XMTY1MzM3ODA4.html")

feicheng2 = media.Movie("非诚勿扰2","《非诚勿扰2》的故事顺延着上一部的脉络进行：从北海道回来后，笑笑对方先生死心，但是对秦奋还没有产生爱情，于是两人决定住在一起试婚。","2010","http://img21.mtime.cn/mt/2012/02/09/170559.45915385_270X405X4.jpg","http://v.youku.com/v_show/id_XMjIxMTg2ODY4.html")




movies = [fanghua ,panjinlian,laopao ,zidan,tangshan,feicheng2]
fresh_tomatoes.open_movies_page(movies)