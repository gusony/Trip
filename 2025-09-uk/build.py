#!/usr/bin/env python3
"""英國行程 2025 · 從一份資料產生 html/ 下的總覽頁、14 個單日頁與路線地圖頁。

改行程只要改下面的 DAYS，然後 `python3 build.py` 重跑。
"""
import os, pathlib

OUT = pathlib.Path(__file__).parent / "html"

# ── 旅程基本資料 ──────────────────────────────────────────────
TRIP = dict(
    name="英國 · United Kingdom",
    logo="🇬🇧 UK",
    sub="2025/9/27（六）桃園出發 → 10/10（五）返台 · 2 人同行",
    title="14 天 13 夜<br>英格蘭 · 湖區 · 蘇格蘭高地",
    accent="#B91C1C",
    grad="linear-gradient(135deg,#7f1d1d 0%,#b91c1c 45%,#1E3A8A 100%)",
    stats=[("14", "天"), ("8", "座城鎮"), ("4", "段長途火車"), ("5", "天高地自駕")],
)

# 每日：(日期鍵, 星期, 主題色 accent, hero 漸層, emoji, 標題, 副標, 標籤, 行程, 補充卡片)
# 行程項目：(時間, 是否重點, 標題, 內文, 註腳)   內文/註腳可用 HTML，空字串即略過
DAYS = [
 dict(d="9/27", dow="六", a="#B91C1C", g="#7f1d1d,#b91c1c", emoji="✈️",
   title="飛往倫敦", sub="桃園 → 杜拜 → 蓋威克，落地已是傍晚",
   tags=["✈️ TPE→DXB→LGW", "🚆 railcard 七折", "🏨 Tottenham Hale"],
   items=[
     ("00:30", 1, "✈️ TPE → DXB", "桃園出發，飛杜拜轉機。", "⏱ 8 小時 45 分 · 05:15 抵達 DXB"),
     ("08:00", 1, "✈️ DXB → LGW", "杜拜轉機飛倫敦蓋威克機場。", "⏱ 7 小時 35 分 · 12:35 落地"),
     ("12:35", 0, "🛂 等出關", "入境查驗、領行李。", ""),
     ("14:35", 1, "🚆 LGW → Tottenham Hale",
      "落地後<b>現場再買</b>到倫敦的車票，套用 railcard 大約打七折，紙本票留著。<br>路線：LGW → Victoria → Tottenham Hale。", "⏱ 約 1 小時 · 15:35 抵達"),
     ("傍晚", 0, "🚶 Seven Sisters 附近晃晃", "放好行李，在住處一帶走走、熟悉環境。", ""),
     ("晚上", 0, "🛒 LIDL 補給", "超市買水跟早餐。", ""),
   ],
   stay="Tottenham Hale / Seven Sisters 一帶"),

 dict(d="9/28", dow="日", a="#B91C1C", g="#7f1d1d,#b91c1c", emoji="🌉",
   title="泰晤士河南岸<br>一路走到金融城", sub="波羅市場早午餐 → 沿河步行 → 空中花園看夜景",
   tags=["🥐 波羅市場", "🚶 南岸步行", "🍽️ Sky Garden"],
   items=[
     ("10:00", 1, "🥐 波羅市場 Borough Market 早午餐", "倫敦最老的食材市集，攤位邊走邊吃。", "⏱ 約 1 小時"),
     ("11:00", 1, "🚶 南岸 → 金融城 步行路線",
      "沿泰晤士河南岸往東，過塔橋再繞回金融城。沿途經過：<br>"
      "· <b>南華克座堂</b> Southwark Cathedral<br>"
      "· <b>金鹿號</b> The Golden Hinde（德雷克環球艦的複製船）<br>"
      "· <b>碎片塔</b> The Shard<br>"
      "· <b>帝國戰爭博物館 貝爾法斯特號艦</b> HMS Belfast<br>"
      "· <b>倫敦塔橋</b> Tower Bridge<br>"
      "· <b>倫敦塔</b> Tower of London<br>"
      "· <b>倫敦大火紀念碑</b> The Monument<br>"
      "· <b>Leadenhall Market</b>（哈利波特斜角巷取景地）",
      "這些多半是路過、外觀拍照，沒有一個個進去"),
     ("15:00", 0, "☕ 下午茶歇腳", "Blank Street 喝的、Bread Ahead 甜甜圈。", ""),
     ("16:00", 0, "🛍️ 順路逛街", "TK Maxx 外套、烏鴉帽 T。", ""),
     ("17:00", 1, "🍽️ 空中花園 Sky Garden · Darwin Brasserie 晚餐",
      "大樓頂層的免費觀景溫室，餐廳訂位可提早進場。從 35 樓看整個倫敦天際線。", "⏱ 17:00–19:30"),
   ],
   stay="Tottenham Hale / Seven Sisters 一帶"),

 dict(d="9/29", dow="一", a="#B91C1C", g="#7f1d1d,#b91c1c", emoji="💂",
   title="白金漢宮 · 西敏寺<br>晚上看音樂劇", sub="衛兵交接 → 西敏寺 → 西區劇院《班傑明的奇幻旅程》",
   tags=["💂 衛兵交接", "⛪ 西敏寺", "🎭 Benjamin Button"],
   items=[
     ("09:30", 1, "🏰 白金漢宮", "順看國王美術館 The King's Gallery、惠靈頓拱門 Wellington Arch。", "⏱ 約 1 小時"),
     ("10:30", 1, "💂 衛兵交接 Changing of the Guard", "白金漢宮門口，要卡位。", "⏱ 約 1 小時"),
     ("12:00", 0, "🍟 午餐 Laughing Halibut", "西敏區的老派炸魚薯條店。", ""),
     ("14:00", 1, "⛪ 西敏寺 Westminster Abbey", "英國歷代君王加冕與長眠之地。開放至 15:30。", "⏱ 14:00–15:30"),
     ("15:30", 1, "🚶 西敏 → 南岸 步行路線",
      "· <b>Jewel Tower</b><br>· <b>大笨鐘</b> Big Ben<br>· <b>唐寧街</b> Downing Street<br>"
      "· 過橋看 <b>倫敦水族館</b>、<b>倫敦眼</b><br>· <b>The Graffiti Tunnel</b> 塗鴉隧道", "沿途外觀、拍照"),
     ("16:30", 0, "🥩 Flat Iron Tottenham Court Road", "單一菜色的平價牛排館。", ""),
     ("19:00", 1, "🎭 Ambassadors Theatre",
      "《<b>The Curious Case of Benjamin Button</b>》班傑明的奇幻旅程 音樂劇。", "⏱ 19:00–21:30"),
   ],
   stay="Tottenham Hale / Seven Sisters 一帶"),

 dict(d="9/30", dow="二", a="#0369A1", g="#075985,#0284c7", emoji="🛶",
   title="劍橋一日", sub="從倫敦直達劍橋，康河撐篙，逛完再回倫敦",
   tags=["🚆 直達車", "🛶 康河撐篙", "🧴 Neal's Yard"],
   items=[
     ("上午", 1, "🚆 Tottenham Hale → Cambridge", "有直達車，不用轉乘。", "⏱ 約 1 小時 11 分"),
     ("中午", 1, "🛶 康河撐篙 Let's Go Punting",
      "劍橋的招牌體驗，撐篙船穿過各學院後花園與嘆息橋。", ""),
     ("下午", 0, "🚶 劍橋市區逛逛",
      "各學院、市集廣場一帶隨意走。順手逛了 <b>Neal's Yard</b>（保養品）、<b>Lush</b>、"
      "<b>Once Upon a Time</b>（童裝外套）、巧克力店。", ""),
     ("傍晚", 1, "🚆 Cambridge → Tottenham Hale", "原車返回倫敦。", "⏱ 約 1 小時 11 分"),
   ],
   stay="Tottenham Hale / Seven Sisters 一帶"),

 dict(d="10/1", dow="三", a="#B91C1C", g="#7f1d1d,#b91c1c", emoji="🏛️",
   title="大英博物館<br>＋ 西區藝文帶", sub="早餐報名字 Tim → 大英博物館 → 柯芬園一路走到特拉法加",
   tags=["🏛️ 大英博物館", "🎭 柯芬園", "🧸 Jelly Cat"],
   items=[
     ("09:00", 0, "☕ Victoria House Coffee & Food 早餐", "點餐報的名字是 <b>Tim</b>。", "⏱ 09:00–10:30"),
     ("10:40", 1, "🏛️ 大英博物館 The British Museum",
      "有另外買一份導覽 app 邊走邊聽。羅塞塔石碑、帕德嫩神廟雕帶、埃及木乃伊廳。", "⏱ 約 3 小時 20 分"),
     ("14:00", 1, "🎭 柯芬園 Covent Garden", "市集、街頭藝人，旁邊就是倫敦皇家歌劇院。", ""),
     ("15:00", 1, "🚶 河岸街 → 特拉法加廣場 步行路線",
      "· <b>考陶爾德美術館</b> The Courtauld<br>· <b>薩默塞特府</b> Somerset House<br>"
      "· <b>國家美術館</b> National Gallery<br>· <b>國家肖像館</b> National Portrait Gallery（免費）<br>"
      "· <b>特拉法加廣場</b> Trafalgar Square", ""),
     ("20:00", 1, "🧸 Selfridges · Jellycat", "百貨裡的 Jellycat 專櫃，這天買最兇。", ""),
     ("晚上", 0, "🛒 Lidl", "回程補給。", ""),
   ],
   stay="Tottenham Hale / Seven Sisters 一帶"),

 dict(d="10/2", dow="四", a="#15803D", g="#14532d,#16a34a", emoji="🚆",
   title="離開倫敦<br>北上湖區門口 Kendal", sub="上午貝克街與攝政公園 → 下午搭車 2 小時 39 分往北",
   tags=["🕵️ 貝克街 221B", "🌳 攝政公園", "🚆 Euston→Oxenholme"],
   items=[
     ("09:30", 0, "🚶 Seven Sisters 出門", "", ""),
     ("10:00", 1, "🕵️ 福爾摩斯紀念館", "貝克街 221B。門票 £20/人，有點小貴。", ""),
     ("11:00", 0, "🗿 杜莎夫人蠟像館", "就在貝克街旁邊。", ""),
     ("12:00", 0, "🍽️ 午餐", "Laville Restaurant、Carlotta 一帶。", ""),
     ("13:00", 1, "🌳 攝政公園 Regent's Park", "野餐、散步，園區北邊就是倫敦動物園。",
      "外帶口袋名單：The SeaShell of Lisson Grove、Paris's Cafe、Regent's Bar & Kitchen"),
     ("14:30", 1, "🚆 Euston → Oxenholme", "從倫敦尤斯頓站北上，車次很多。", "⏱ 2 小時 39 分 · 17:46 抵達"),
     ("18:30", 1, "🏨 The Lakeland Kendal Hotel", "旁邊 ALDI 很大間，可以採買。", ""),
   ],
   stay="The Lakeland Kendal Hotel（Kendal）"),

 dict(d="10/3", dow="五", a="#047857", g="#064e3b,#0d9488", emoji="🚗",
   title="湖區自駕日<br>一路開到 Glasgow", sub="早上租車，溫德米爾 → 安布賽德 → 格拉斯米爾 → 凱西克 → 蘇格蘭",
   tags=["🚗 Enterprise 取車", "⛵ 溫德米爾遊湖", "🍪 薑餅店", "🏙️ Glasgow"],
   items=[
     ("08:00", 1, "🚗 Enterprise 租車", "在 Kendal 火車站附近取車。", "⏱ 約 30 分"),
     ("08:30", 0, "🚗 Kendal → Windermere", "停 Bowness Coach Park。", "⏱ 30 分"),
     ("09:00", 0, "🚶 Bowness 湖邊漫步／早餐", "", ""),
     ("09:30", 1, "⛵ Windermere Lake Cruises 遊湖小船", "英格蘭最大的湖，搭船從水面上看湖區。", ""),
     ("10:00", 1, "🐰 The World of Beatrix Potter", "彼得兔作者的主題展館，現場買票即可。", "⏱ 1 小時"),
     ("11:00", 0, "🚗 Windermere → Ambleside", "停 Rydal Road Car Park。", "⏱ 16 分"),
     ("11:30", 0, "🍽️ Ambleside 午餐", "Apple Pie Cafe & Bakery。", "⏱ 1 小時"),
     ("12:30", 0, "🚗 Ambleside → Grasmere", "", "⏱ 15 分"),
     ("12:45", 1, "🍪 The Grasmere Gingerbread Shop", "1854 年開到現在的薑餅小店，買了薑餅跟 fudge。", "⏱ 15 分"),
     ("13:00", 0, "🚗 Grasmere → Keswick", "山路，慢慢開。", "⏱ 45 分"),
     ("14:15", 0, "☕ Keswick 休息", "湖區北端的小鎮。", "⏱ 45 分"),
     ("15:00", 1, "🚗 Keswick → Glasgow", "跨過英格蘭 / 蘇格蘭邊界。中途停 Tebay Services（全英最有名的休息站）。", "⏱ 2 小時 30 分"),
     ("18:00", 0, "🍜 晚餐 Four Seasons Vietnamese Restaurant", "", ""),
     ("晚上", 1, "🅿️🏨 Ibis Styles Glasgow Centre George Square",
      "車停 NCP Glasgow The Glasshouse（合作停車場，走路三分鐘）。", ""),
   ],
   stay="Ibis Styles Glasgow Centre George Square"),

 dict(d="10/4", dow="六", a="#6D28D9", g="#4c1d95,#7c3aed", emoji="🐮",
   title="Glasgow 市區<br>傍晚北上高地", sub="喬治廣場走到格拉斯哥大學，看完高地牛就開車進高地",
   tags=["🎓 格拉斯哥大學", "🐮 高地牛", "⚡ 風暴改宿"],
   alert=("w", "🌩️ 這天住宿臨時換了",
     "原本訂的是 <b>Ewich House</b>（Crianlarich 一帶）。當天接到通知，<b>風暴造成斷電</b>，"
     "臨時改訂 <b>Innisfree, Fort William</b>。兩間都是非常好的住宿。"),
   items=[
     ("上午", 0, "🧳 先把行李放上車", "或寄放飯店。退房記得拿折抵券。", ""),
     ("09:30", 1, "🚶 格拉斯哥市區步行路線",
      "· <b>喬治廣場</b> George Square<br>· <b>格拉斯哥大教堂</b> Glasgow Cathedral<br>"
      "· <b>市政廳</b> Glasgow City Chambers<br>· <b>威靈頓公爵騎馬雕像</b>（頭上永遠戴著交通錐的那座）", ""),
     ("11:00", 0, "🎨 Glasgow Gallery of Modern Art", "就在威靈頓公爵雕像後面。", ""),
     ("12:00", 1, "🎓 格拉斯哥大學 Main Building", "哥德復興式主樓與迴廊，常被說像霍格華茲。", ""),
     ("13:30", 1, "🐮 Highland Cattle Park", "看高地牛，看完再走。", ""),
     ("14:00", 0, "🍫 採買", "Glasgow Chocolate、明信片與郵票。Glasgow 是這趟採買最多的一站。", ""),
     ("15:00", 1, "🚗 離開 Glasgow 北上", "", "⏱ 約 1 小時"),
     ("16:00", 1, "🍽️ 晚餐 Cù Mara Bistro & Takeaway", "沒訂位，賭現場。", "⏱ 約 1.5 小時"),
     ("19:00", 1, "🏨 Innisfree, Fort William", "原訂 Ewich House，因風暴斷電當天改訂。", ""),
   ],
   stay="Innisfree, Fort William（原訂 Ewich House）"),

 dict(d="10/5", dow="日", a="#7C3AED", g="#3b0764,#6d28d9", emoji="🚂",
   title="高地縱貫<br>霍格華茲高架橋 → Skye 島", sub="行程表上寫著「不允許有一點拖延」的一天",
   tags=["🏞️ 蘭諾赫沼澤", "🚂 Glenfinnan", "🥃 Talisker"],
   items=[
     ("08:15", 1, "🚗 出發北上", "沿途停 <b>Rannoch Moor</b> 與 <b>Loch Leven</b> 觀景點。<br>"
      "蘭諾赫沼澤觀景點位於蘇格蘭高地西部，是一片廣闊荒涼的高原，以崎嶇地形、"
      "點綴其中的湖泊與石南花景觀聞名。<br>"
      "勒芬湖觀景點可俯瞰勒芬湖，湖中島上的勒芬城堡曾囚禁過蘇格蘭女王瑪麗一世。", "⏱ 約 1 小時 15 分"),
     ("09:30", 0, "🚻 Fort William", "太晚出門的話，這段就只上廁所。", "⏱ 20 分"),
     ("10:20", 1, "🚂 Glenfinnan Viaduct View Cafe",
      "哈利波特霍格華茲特快列車經過的那座彎曲高架橋。想看火車經過必須<b>提早到</b>，班次不多。", "⏱ 30 分 · 可上廁所、買咖啡"),
     ("10:50", 0, "🚗 一路開往 Skye 島", "中間有一小時 buffer，但不能太拖，沿路可找地方上廁所。", "⏱ 約 3 小時"),
     ("13:50", 0, "🍽️ Three Chimneys at Talisker", "提早到就進去吃午餐，這個時間人應該不多。", ""),
     ("14:50", 1, "🥃 Talisker Distillery 酒廠導覽", "Skye 島唯一的威士忌酒廠，海風泥煤味。需提早至少 15 分鐘抵達。", "⏱ 1 小時"),
     ("16:00", 0, "🚗 開往 Portree", "", "⏱ 40 分"),
     ("16:40", 1, "🏨 Bracken Hide Hotel", "Portree 郊外的小屋型旅館。附近超市 Co-op Food（Woodlands Road）。", ""),
   ],
   stay="Bracken Hide Hotel（Portree, Isle of Skye）"),

 dict(d="10/6", dow="一", a="#0E7490", g="#164e63,#0891b2", emoji="🧚",
   title="Skye 島環島", sub="城堡、精靈谷、奎靈、恐龍足跡、Kilt Rock，一天跑完北半圈",
   tags=["🏰 Dunvegan", "🥾 Quiraing", "🦕 恐龍足跡", "🏞️ Kilt Rock"],
   items=[
     ("09:00", 0, "🥖 Isle of Skye Baking Company", "開門就去買麵包，早餐加午餐一起解決。", ""),
     ("10:00", 1, "🏰 Dunvegan Castle & Gardens",
      "麥克勞德家族（Clan MacLeod）的祖傳居所，也是蘇格蘭連續居住時間最長的城堡。"
      "城堡內收藏豐富的家族文物，周圍花園也值得一遊。", "⏱ 2 小時 · 記得先上廁所"),
     ("12:45", 1, "🧚 The Fairy Glen", "小山丘與環狀石陣構成的奇特地景。快走大概半小時，也可以 pass。",
      "⏱ 30 分 · 附近有店可以先上廁所"),
     ("13:15", 0, "🍽️ 午餐", "Old School Restaurant（可訂位）或 The Anchorage Cafe。", "⏱ 25 分車程"),
     ("13:40", 1, "🥾 Quiraing", "壯觀的火山地質景觀，崎嶇山峰、懸崖與隱蔽山谷。"
      "走一圈約 <b>6.8 公里</b>，很多地方有泥濘；前一天下雨就不走。", "⏱ 2 小時"),
     ("15:55", 1, "🦕 An Corran Beach", "恐龍足跡，<b>退潮才看得到</b>。純看海的話 15 分鐘就夠。", "⏱ 15 分"),
     ("16:20", 1, "🏞️ Kilt Rock", "玄武岩柱構成的巨大海崖，外觀像蘇格蘭裙的褶皺。"
      "旁邊的米爾特瀑布 Mealt Falls 從懸崖直接落入大海。", "⏱ 20 分 · 旁有停車場"),
     ("17:00", 0, "🗿 Old Man of Storr Car Park", "停車場旁有廁所跟禮品店（真的爬上去要兩小時，這次只停）。", "⏱ 10 分"),
     ("17:10", 1, "🚗 → The Lochalsh Hotel", "離開 Skye 島，過橋住在本島這側。飯店旁有 Co-op Food。", "⏱ 約 1 小時 10 分"),
   ],
   stay="The Lochalsh Hotel（Kyle of Lochalsh）"),

 dict(d="10/7", dow="二", a="#1E3A8A", g="#172554,#1d4ed8", emoji="🏰",
   title="高地南下<br>愛丁堡還車", sub="艾琳多南城堡 → 尼斯湖 → 凱恩戈姆 → 鄧凱爾德 → 愛丁堡",
   tags=["🏰 Eilean Donan", "🐉 尼斯湖", "🚗 還車日"],
   items=[
     ("09:00", 0, "🚗 從 The Lochalsh Hotel 出發", "", ""),
     ("09:15", 1, "🏰 Eilean Donan Castle",
      "蘇格蘭最具標誌性的城堡之一，坐落在三個湖泊交匯處的小島上，許多電影電視的取景地。"
      "這天時間緊，主要是外觀拍照、禮品店跟咖啡廳。", "⏱ 30 分"),
     ("09:45", 0, "🚗 往尼斯湖", "", "⏱ 約 1 小時 10 分"),
     ("10:55", 1, "🐉 Loch Ness viewpoint",
      "位於 Fort Augustus 一帶的尼斯湖觀景點。尼斯湖是蘇格蘭最大的淡水湖之一，"
      "以傳說中的水怪聞名。可停留拍照、休息吃東西。", "⏱ 15 分"),
     ("11:10", 0, "🚗 往 Aviemore", "", "⏱ 約 1 小時 15 分"),
     ("12:25", 1, "🍽️ Aviemore 午餐",
      "凱恩戈姆山國家公園（Cairngorms National Park）中心的熱門度假小鎮，"
      "戶外活動愛好者的天堂——滑雪、徒步、騎行、水上運動。", "⏱ 1 小時"),
     ("13:25", 0, "🚗 往 Dunkeld", "", "⏱ 約 1 小時 20 分"),
     ("14:45", 1, "⛪ Dunkeld Cathedral",
      "位於伯斯郡鄧凱爾德鎮，歷史悠久的大教堂。部分建築已成廢墟，"
      "但仍是重要的歷史與建築遺址，坐落在風景如畫的泰河（River Tay）畔。", "⏱ 30 分"),
     ("15:15", 1, "🚗 返回愛丁堡 · 還車", "五天自駕在這裡結束。", "⏱ 約 1 小時 45 分"),
     ("晚上", 0, "🛒 Tesco", "飯店附近補給。", ""),
   ],
   stay="Premier Inn Edinburgh"),

 dict(d="10/8", dow="三", a="#1E40AF", g="#1e3a8a,#3730a3", emoji="🏰",
   title="愛丁堡一日", sub="城堡、巧克力、大象咖啡館、Oink 刈包，舊城區慢慢走",
   tags=["🏰 愛丁堡城堡", "☕ The Elephant House", "🥪 Oink", "🥃 威士忌"],
   items=[
     ("上午", 1, "🏰 愛丁堡城堡 Edinburgh Castle", "坐在死火山岩頂上的城堡，舊城區的制高點。", ""),
     ("中午", 1, "🥪 Oink Victoria Street", "現切烤全豬做的豬肉刈包，Victoria Street 這間排最兇（有其他分店）。", ""),
     ("下午", 1, "☕ The Elephant House", "J.K. 羅琳寫哈利波特的那間咖啡廳。", ""),
     ("下午", 0, "🍫 The Chocolatarium", "可以看製程、試吃的巧克力店。", ""),
     ("下午", 0, "⚡ Harry Potter Shop", "順路的周邊店。", ""),
     ("下午", 0, "🛍️ 舊城區採買", "Whisky Shop（買酒、巧克力）、Aelder Elixir（接骨木利口酒）、Islander 皮夾。", ""),
     ("傍晚", 0, "🍕 PIZZA MIA 雞翅 · Caffè Nero", "中間歇腳。", ""),
     ("晚上", 1, "🍽️ Amber Restaurant / Divino Enoteca",
      "Amber 是蘇格蘭威士忌體驗中心的餐廳，Divino Enoteca 是舊城區的義式酒館。", ""),
   ],
   stay="Premier Inn Edinburgh"),

 dict(d="10/9", dow="四", a="#9F1239", g="#4c0519,#be123c", emoji="🫖",
   title="愛丁堡 → York<br>當天再回倫敦", sub="中途在約克下車逛一下午，晚上長途車回倫敦",
   tags=["🚆 三段火車", "🧳 寄行李", "🫖 Bettys"],
   items=[
     ("09:30", 1, "🚆 愛丁堡 → York", "東海岸幹線，沿海一段風景很好。", "⏱ 2 小時 30 分 · 約 12:00 抵達"),
     ("12:00", 0, "🧳 York 車站寄行李", "行李寄放後輕裝逛城。", ""),
     ("12:30", 1, "🚶 York 舊城區逛逛",
      "約克大教堂 York Minster、肉舖街 The Shambles（斜角巷的原型之一）、古城牆一帶。", ""),
     ("15:00", 1, "🫖 Bettys York Cafe 下午茶", "約克最有名的茶室。", ""),
     ("16:30", 0, "🛍️ 採買", "氂牛毛隔熱手套、明信片與郵票、WHSmith 飲料、小布丁。", ""),
     ("19:00", 1, "🧳 取行李", "寄物處最晚 20:00。", ""),
     ("19:13", 1, "🚆 York → London", "最後一段長途，回倫敦。", "⏱ 21:06 抵達"),
   ],
   stay="倫敦（Tottenham Hale / Seven Sisters 一帶）"),

 dict(d="10/10", dow="五", a="#B91C1C", g="#7f1d1d,#b91c1c", emoji="🛫",
   title="倫敦最後一天<br>傍晚飛回台灣", sub="趁早開的時段進聖保羅大教堂，下午慢慢晃到搭機",
   tags=["⛪ 聖保羅大教堂", "☕ Monmouth", "✈️ Gatwick Express"],
   items=[
     ("08:00", 0, "🚶 Seven Sisters 出發", "", ""),
     ("08:30", 1, "⛪ 聖保羅大教堂 St Paul's Cathedral",
      "雷恩設計的巨大穹頂。開放時段 08:30–10:00，趁早進去人少。", "⏱ 08:30–10:00"),
     ("10:00", 0, "🛍️ Victoria Place 逛街", "維多利亞車站上方的商場。", "⏱ 10:00–12:00"),
     ("12:00", 1, "🍽️ 午餐 Paternoster Chop House", "聖保羅大教堂旁的英式烤肉館。", "⏱ 12:00–14:00"),
     ("14:00", 0, "☕ 附近公園散步／下午茶", "Monmouth Coffee，最後買了草莓、Walkers 巧克力當伴手禮。", "⏱ 14:00–17:00"),
     ("19:00", 1, "🚆 Victoria → Gatwick Express", "提早買有優惠。", "⏱ 約 40 分"),
     ("19:45", 1, "✈️ 抵達 LGW 機場", "辦登機、過安檢。", ""),
     ("隔日", 1, "🛬 21:30 抵達桃園機場", "台灣時間 10/11 晚上到家。", ""),
   ],
   stay="—"),
]

# ── 地圖點位（路線依序）────────────────────────────────────────
PINS = [
 ("倫敦 London", 51.5074, -0.1278, "Day 1–5、13–14 的基地"),
 ("劍橋 Cambridge", 52.2053, 0.1218, "Day 4 · 康河撐篙"),
 ("Kendal", 54.3280, -2.7460, "Day 6 住宿 · 湖區門口"),
 ("溫德米爾 Windermere", 54.3650, -2.9190, "Day 7 · 遊湖小船、彼得兔"),
 ("安布賽德 Ambleside", 54.4290, -2.9620, "Day 7 · 午餐"),
 ("格拉斯米爾 Grasmere", 54.4590, -3.0240, "Day 7 · 薑餅店"),
 ("凱西克 Keswick", 54.6013, -3.1347, "Day 7 · 湖區北端"),
 ("格拉斯哥 Glasgow", 55.8642, -4.2518, "Day 7 住宿、Day 8 市區"),
 ("威廉堡 Fort William", 56.8198, -5.1052, "Day 8 住宿（風暴改訂）"),
 ("Glenfinnan 高架橋", 56.8747, -5.4331, "Day 9 · 霍格華茲特快列車"),
 ("Talisker 酒廠", 57.3020, -6.3563, "Day 9 · Skye 島威士忌"),
 ("波特里 Portree", 57.4125, -6.1953, "Day 9 住宿 · Skye 島首府"),
 ("Dunvegan Castle", 57.4494, -6.5906, "Day 10 · 麥克勞德家族城堡"),
 ("The Fairy Glen", 57.5850, -6.3300, "Day 10 · 精靈谷"),
 ("Quiraing", 57.6440, -6.2770, "Day 10 · 火山地景健行"),
 ("Kilt Rock", 57.6083, -6.1753, "Day 10 · 海崖與瀑布"),
 ("Old Man of Storr", 57.5070, -6.1810, "Day 10 · 只停停車場"),
 ("Kyle of Lochalsh", 57.2810, -5.7160, "Day 10 住宿"),
 ("Eilean Donan Castle", 57.2740, -5.5162, "Day 11 · 三湖交匯的城堡"),
 ("尼斯湖 Loch Ness", 57.1440, -4.6800, "Day 11 · Fort Augustus 觀景點"),
 ("Aviemore", 57.1900, -3.8290, "Day 11 · 凱恩戈姆山午餐"),
 ("Dunkeld Cathedral", 56.5650, -3.5880, "Day 11 · 泰河畔大教堂"),
 ("愛丁堡 Edinburgh", 55.9533, -3.1883, "Day 11–12 · 還車、城堡"),
 ("約克 York", 53.9600, -1.0873, "Day 13 · 大教堂、肉舖街"),
]

# ── 樣板 ──────────────────────────────────────────────────────
FONT = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">')

BASE_CSS = """*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Inter',-apple-system,'PingFang TC',sans-serif;background:#F0F4F8;color:#0F172A;font-size:16px;line-height:1.6}
a{text-decoration:none;color:inherit}
.nav{background:#fff;border-bottom:1px solid #E2E8F0;position:sticky;top:0;z-index:100;padding:0 20px}
.nav-inner{max-width:960px;margin:0 auto;display:flex;align-items:center;height:52px;gap:6px;overflow-x:auto;scrollbar-width:none}
.nav-inner::-webkit-scrollbar{display:none}
.nav-logo{font-size:15px;font-weight:700;flex-shrink:0;margin-right:4px}
.nav-dot{color:#CBD5E1;flex-shrink:0;padding:0 2px}
.nav-pill{flex-shrink:0;padding:5px 12px;border-radius:99px;font-size:13px;font-weight:500;color:#64748B;transition:all 150ms}
.nav-pill:hover{background:#F1F5F9}
.nav-pill.active{background:var(--a);color:#fff}
.hero{color:#fff;padding:36px 20px 30px}
.hero-inner{max-width:960px;margin:0 auto}
.hero-title{font-size:28px;font-weight:700;line-height:1.25;margin-bottom:6px}
.hero-sub{font-size:14px;color:rgba(255,255,255,.75);margin-bottom:16px}
.hero-tags{display:flex;gap:8px;flex-wrap:wrap}
.htag{background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.22);border-radius:99px;font-size:13px;font-weight:500;padding:4px 12px}
.content{max-width:960px;margin:0 auto;padding:20px 20px 60px}
.sec-label{font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#94A3B8;margin:24px 0 12px 2px}
"""

DAY_CSS = """:root{--a:__A__;--al:__AL__;--am:__AM__}
.day-badge{display:inline-block;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.25);border-radius:99px;font-size:12px;font-weight:600;letter-spacing:.05em;padding:4px 12px;margin-bottom:12px}
.day-grid{display:block}
@media(min-width:768px){.day-grid{display:grid;grid-template-columns:1.7fr 1fr;gap:32px;align-items:start}.day-side{position:sticky;top:72px}}
.timeline{position:relative;padding-left:72px}
.timeline::before{content:'';position:absolute;left:54px;top:20px;bottom:20px;width:2px;background:var(--am);border-radius:2px}
.tl-item{position:relative;margin-bottom:10px}
.tl-time{position:absolute;left:-72px;width:46px;text-align:right;font-size:12px;font-weight:600;color:var(--a);padding-top:14px;line-height:1.2}
.tl-dot{position:absolute;left:-18px;top:15px;width:12px;height:12px;border-radius:50%;background:#fff;border:2.5px solid var(--a);transform:translateX(-50%)}
.tl-dot.key{background:var(--a)}
.tl-card{background:#fff;border-radius:14px;border:1px solid #E2E8F0;padding:13px 15px}
.tl-card h3{font-size:15px;font-weight:600;margin-bottom:3px}
.tl-card p{font-size:13px;color:#64748B;line-height:1.55}
.tl-card .sub{font-size:12px;color:#94A3B8;margin-top:4px}
.alert{border-radius:14px;padding:14px 16px;margin-bottom:12px}
.alert-w{background:#FFF7ED;border:1px solid #FED7AA}
.alert strong{display:block;font-size:14px;font-weight:600;margin-bottom:3px}
.alert p{font-size:13px;color:#475569;line-height:1.55}
.side-card{background:#fff;border-radius:14px;border:1px solid #E2E8F0;padding:14px 16px;margin-bottom:12px}
.side-label{font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#94A3B8;margin-bottom:6px}
.side-value{font-size:14px;font-weight:600;color:#0F172A;line-height:1.45}
.bottom-nav{position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid #E2E8F0;display:flex;gap:10px;padding:10px 20px;padding-bottom:calc(10px + env(safe-area-inset-bottom));justify-content:center;z-index:100}
.bnav-btn{flex:1;max-width:160px;text-align:center;padding:11px 0;border-radius:12px;font-size:14px;font-weight:600;transition:opacity 150ms}
.bnav-prev{background:#F1F5F9;color:#475569}
.bnav-next{background:var(--a);color:#fff}
.bnav-btn:hover{opacity:.85}
.pb{height:80px}
"""

# 每日主題色對應的淺色（timeline 線與淺底）
TINT = {
 "#B91C1C": ("#FEF2F2", "#FECACA"), "#0369A1": ("#F0F9FF", "#BAE6FD"),
 "#15803D": ("#F0FDF4", "#BBF7D0"), "#047857": ("#ECFDF5", "#A7F3D0"),
 "#6D28D9": ("#F5F3FF", "#DDD6FE"), "#7C3AED": ("#F5F3FF", "#DDD6FE"),
 "#0E7490": ("#ECFEFF", "#A5F3FC"), "#1E3A8A": ("#EFF6FF", "#BFDBFE"),
 "#1E40AF": ("#EEF2FF", "#C7D2FE"), "#9F1239": ("#FFF1F2", "#FECDD3"),
}


def slug(i, d):
    m, day = d.split("/")
    return "day%02d-%02d%02d.html" % (i + 1, int(m), int(day))


def nav(active):
    """active: 'index' / 'map' / 單日頁檔名"""
    p = ['<a href="../../index.html" class="nav-pill" style="padding:4px 10px;font-size:14px">🏠</a>',
         '<span class="nav-dot">·</span>',
         '<a href="index.html" class="nav-logo">%s</a>' % TRIP["logo"],
         '<a href="index.html" class="nav-pill%s">總覽</a>' % (" active" if active == "index" else ""),
         '<a href="map.html" class="nav-pill%s" style="color:#B91C1C;font-weight:600">🗺️ 路線</a>'
         % (" active" if active == "map" else ""),
         '<span class="nav-dot">·</span>']
    for i, d in enumerate(DAYS):
        f = slug(i, d["d"])
        p.append('<a href="%s" class="nav-pill%s">%s</a>' % (f, " active" if active == f else "", d["d"]))
    return '<nav class="nav">\n  <div class="nav-inner">\n    %s\n  </div>\n</nav>' % "\n    ".join(p)


def page(title, css, body, active, accent=TRIP["accent"], head=""):
    return ("""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
%s
%s<style>
%s%s</style>
</head>
<body>

%s

%s

</body>
</html>
""" % (title, FONT, head, BASE_CSS.replace("var(--a)", accent) if "--a" not in css else BASE_CSS,
       css, nav(active), body))


# ── 單日頁 ────────────────────────────────────────────────────
def build_day(i, d):
    al, am = TINT[d["a"]]
    css = DAY_CSS.replace("__A__", d["a"]).replace("__AL__", al).replace("__AM__", am)
    tl = []
    for t, key, h3, p, sub in d["items"]:
        parts = ["<h3>%s</h3>" % h3]
        if p:
            parts.append("<p>%s</p>" % p)
        if sub:
            parts.append('<p class="sub">%s</p>' % sub)
        tl.append(
            '          <div class="tl-item">\n'
            '            <div class="tl-time">%s</div>\n'
            '            <div class="tl-dot%s"></div>\n'
            '            <div class="tl-card">\n              %s\n            </div>\n'
            '          </div>' % (t, " key" if key else "", "\n              ".join(parts)))

    alert = ""
    if d.get("alert"):
        kind, head, txt = d["alert"]
        alert = '      <div class="alert alert-%s"><strong>%s</strong><p>%s</p></div>\n' % (kind, head, txt)

    prev = '<a href="%s" class="bnav-btn bnav-prev">← 前一天</a>' % slug(i - 1, DAYS[i - 1]["d"]) if i else \
           '<a href="index.html" class="bnav-btn bnav-prev">← 總覽</a>'
    nxt = '<a href="%s" class="bnav-btn bnav-next">後一天 →</a>' % slug(i + 1, DAYS[i + 1]["d"]) if i + 1 < len(DAYS) else \
          '<a href="index.html" class="bnav-btn bnav-next">回總覽 →</a>'

    body = """<div class="hero" style="background:linear-gradient(135deg,%s)">
  <div class="hero-inner">
    <div class="day-badge">Day %d · %s（%s）</div>
    <div class="hero-title">%s %s</div>
    <div class="hero-sub">%s</div>
    <div class="hero-tags">
      %s
    </div>
  </div>
</div>

<div class="content">
  <div class="day-grid">
    <div class="day-main">
%s      <div class="sec-label">當日行程</div>
      <div class="timeline">
%s
      </div>
    </div>
    <div class="day-side">
      <div class="sec-label">住宿</div>
      <div class="side-card">
        <div class="side-label">這晚住哪</div>
        <div class="side-value">%s</div>
      </div>
    </div>
  </div>
  <div class="pb"></div>
</div>

<div class="bottom-nav">
  %s
  %s
</div>""" % (d["g"], i + 1, d["d"], d["dow"], d["emoji"], d["title"], d["sub"],
             "\n      ".join('<span class="htag">%s</span>' % t for t in d["tags"]),
             alert, "\n".join(tl), d["stay"], prev, nxt)

    return page("Day %d · %s %s" % (i + 1, d["d"], d["title"].replace("<br>", " ")),
                css, body, slug(i, d["d"]), d["a"])


# ── 總覽頁 ────────────────────────────────────────────────────
INDEX_CSS = """:root{--a:#B91C1C}
.hero{padding:40px 20px 36px}
.hero-eyebrow{font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#FCA5A5;margin-bottom:10px}
.hero-title{font-size:32px;font-weight:700;line-height:1.22;margin-bottom:8px}
.hero-sub{font-size:15px;margin-bottom:24px}
.stats{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:14px;padding:16px 20px;display:flex;gap:18px;align-items:center;flex-wrap:wrap}
.stat{text-align:center;min-width:64px}
.stat-num{font-size:26px;font-weight:700;color:#fff;display:block;line-height:1}
.stat-label{font-size:11px;color:#FCA5A5;margin-top:3px}
.stat-div{color:rgba(255,255,255,.25);font-size:18px}
.days-grid{display:flex;flex-direction:column;gap:10px}
@media(min-width:768px){.days-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.day-card{background:#fff;border-radius:16px;border:1px solid #E2E8F0;overflow:hidden;display:flex;align-items:stretch;transition:transform 150ms,box-shadow 150ms}
.day-card:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.1)}
.day-card-accent{width:5px;flex-shrink:0}
.day-card-body{flex:1;padding:13px 15px}
.day-card-meta{display:flex;align-items:center;justify-content:space-between;margin-bottom:4px}
.day-num{font-size:11px;font-weight:600;color:#94A3B8;text-transform:uppercase;letter-spacing:.06em}
.day-date-badge{font-size:11px;font-weight:500;color:#64748B;background:#F8FAFC;border:1px solid #E2E8F0;padding:2px 8px;border-radius:99px}
.day-card-title{font-size:14px;font-weight:600;color:#0F172A;margin-bottom:5px}
.day-card-tags{display:flex;gap:5px;flex-wrap:wrap}
.tag{font-size:11px;padding:2px 8px;border-radius:99px;font-weight:500;background:#F1F5F9;color:#475569}
.day-card-arrow{display:flex;align-items:center;padding:0 14px 0 0;color:#CBD5E1;font-size:18px}
.note{background:#fff;border:1px solid #E2E8F0;border-radius:14px;padding:14px 16px;font-size:13px;color:#64748B;line-height:1.6}
.note b{color:#0F172A}
.map-link{display:block;background:#fff;border:1px solid #E2E8F0;border-radius:16px;padding:18px 20px;transition:transform 150ms,box-shadow 150ms}
.map-link:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.1)}
.map-link-title{font-size:15px;font-weight:600;margin-bottom:3px}
.map-link-sub{font-size:13px;color:#64748B}
"""


def build_index():
    cards = []
    for i, d in enumerate(DAYS):
        cards.append("""    <a href="%s" class="day-card">
      <div class="day-card-accent" style="background:%s"></div>
      <div class="day-card-body">
        <div class="day-card-meta"><span class="day-num">Day %d</span><span class="day-date-badge">%s（%s）</span></div>
        <div class="day-card-title">%s %s</div>
        <div class="day-card-tags">%s</div>
      </div>
      <div class="day-card-arrow">›</div>
    </a>""" % (slug(i, d["d"]), d["a"], i + 1, d["d"], d["dow"], d["emoji"],
                d["title"].replace("<br>", " "),
                "".join('<span class="tag">%s</span>' % t for t in d["tags"])))

    st = []
    for n, (num, lab) in enumerate(TRIP["stats"]):
        if n:
            st.append('<span class="stat-div">·</span>')
        st.append('<div class="stat"><span class="stat-num">%s</span><div class="stat-label">%s</div></div>' % (num, lab))

    body = """<div class="hero" style="background:%s">
  <div class="hero-inner">
    <div class="hero-eyebrow">%s · 2025</div>
    <div class="hero-title">%s</div>
    <div class="hero-sub">%s</div>
    <div class="stats">
      %s
    </div>
  </div>
</div>

<div class="content">

  <div class="sec-label">路線</div>
  <a href="map.html" class="map-link">
    <div class="map-link-title">🗺️ 看整段路線地圖</div>
    <div class="map-link-sub">倫敦 → 劍橋 → 湖區 → 格拉斯哥 → 高地 → Skye 島 → 愛丁堡 → 約克 → 倫敦</div>
  </a>

  <div class="sec-label">每日行程</div>
  <div class="days-grid">
%s
  </div>

  <div class="sec-label">關於這份紀錄</div>
  <div class="note">
    這是 <b>2025 年 9/27 – 10/10</b> 英國行程的事後整理，資料來自當時的行程規劃表。<br>
    內容以<b>出發前的計畫</b>為底，時間與停留長度都是當初排的；實際走的時候一定有出入
    （例如 <b>10/4</b> 因風暴斷電臨時換了住宿）。想起什麼再補進來就好。
  </div>

</div>""" % (TRIP["grad"], TRIP["name"], TRIP["title"], TRIP["sub"], "\n      ".join(st), "\n".join(cards))

    return page("英國 2025 · 總覽", INDEX_CSS, body, "index")


# ── 地圖頁 ────────────────────────────────────────────────────
MAP_HEAD = ('<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>\n'
            '<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>\n')

MAP_CSS = """:root{--a:#B91C1C}
#map{height:calc(100vh - 52px);min-height:420px;width:100%}
.legend{position:absolute;bottom:20px;left:20px;z-index:500;background:rgba(255,255,255,.94);border:1px solid #E2E8F0;border-radius:12px;padding:12px 14px;font-size:12px;color:#475569;max-width:240px;backdrop-filter:blur(8px)}
.legend b{display:block;color:#0F172A;font-size:13px;margin-bottom:4px}
.leaflet-popup-content{font-family:'Inter',-apple-system,'PingFang TC',sans-serif;font-size:13px}
.leaflet-popup-content b{font-size:14px}
"""


def build_map():
    pins = ",\n ".join('[%r,%s,%s,%r]' % (n, la, lo, note) for n, la, lo, note in PINS)
    body = """<div style="position:relative">
<div id="map"></div>
<div class="legend"><b>🇬🇧 英國 2025 路線</b>倫敦出發，北上湖區與蘇格蘭高地，繞 Skye 島後南下愛丁堡、約克，再回倫敦搭機。<br>點按標記看是第幾天。</div>
</div>

<script>
var PINS = [
 %s
];
var map = L.map('map', {scrollWheelZoom:true}).setView([56.0,-4.0], 6);
L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
  attribution:'&copy; OpenStreetMap &copy; CARTO', maxZoom:19
}).addTo(map);
var latlngs = PINS.map(function(p){ return [p[1],p[2]]; });
L.polyline(latlngs, {color:'#B91C1C', weight:3, opacity:.65, dashArray:'6,6'}).addTo(map);
PINS.forEach(function(p, i){
  L.circleMarker([p[1],p[2]], {radius:7, color:'#fff', weight:2, fillColor:'#B91C1C', fillOpacity:1})
   .addTo(map)
   .bindPopup('<b>'+p[0]+'</b><br>'+p[3]);
});
map.fitBounds(L.latLngBounds(latlngs).pad(0.08));
</script>""" % pins
    return page("英國 2025 · 路線地圖", MAP_CSS, body, "map", head=MAP_HEAD)


# ── 產生 ──────────────────────────────────────────────────────
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    written = []
    for i, d in enumerate(DAYS):
        f = OUT / slug(i, d["d"])
        f.write_text(build_day(i, d), encoding="utf-8")
        written.append(f.name)
    (OUT / "index.html").write_text(build_index(), encoding="utf-8")
    (OUT / "map.html").write_text(build_map(), encoding="utf-8")
    written += ["index.html", "map.html"]
    print("寫入 %d 個檔案到 %s" % (len(written), OUT))
    for n in sorted(written):
        print("  ", n)


if __name__ == "__main__":
    main()
