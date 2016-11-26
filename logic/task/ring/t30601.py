# -*- coding: utf-8 -*-
from task.defines import *
from task.object import Task as customTask

MAX_RING = 200 # 最大环数

#导表开始
class Task(customTask):
	parentId = 30601
	targetType = TASK_TARGET_TYPE_NPC
	icon = 0
	title = '''入世修行'''
	intro = '''寻找$target'''
	detail = '''这个世界很大，人很多。每个地方每个人值得我们去见识一番，去找$target交流一下'''
	rewardDesc = ''''''
	goAheadScript = ''''''
	initScript = '''E(9015,1001)'''

	npcInfo = {
		1001:{"名称":"高手","造型":"4502(0,1,0,0,0)","位置":"1040,0,0,0","称谓":"高手"},
		1002:{"名称":"传说","造型":"4502(0,1,0,0,0)","位置":"1040,0,0,0","称谓":"高手"},
	}

	eventInfo = {
		1001:{"点击":"DONE,DEFF,R1001"},
		1002:{"点击":"SB4023","回复":"1:ANSWER","成功":"DONE,DEFF,R1001","失败":"SB4024"},
		1003:{"点击":"POPI","成功":"DONE,DEFF,R1001","失败":"D4020"},
		1004:{"点击":"POPI","成功":"DONE,DEFF,R1001","失败":"D4021"},
		1005:{"点击":"SB4022","回复":"1:E(0,2001),$checkSchool","成功":"DONE,DEFF,R1001"},
		1006:{"点击":"F2001","成功":"LEGENDS"},
		1012:{"点击":"DONE,DEFF,R1001"},
		1013:{"点击":"DONE,DEFF,R1001"},
		1014:{"点击":"DONE,DEFF,R1001"},
		1015:{"点击":"DONE,DEFF,R1001"},
		1016:{"点击":"DONE,DEFF,R1001"},
		1017:{"点击":"DONE,DEFF,R1001"},
		2001:{"点击":"$checkSchool","成功":"DONE,DEFF,R1001","失败":"E(0,1005)"},
		3001:{"点击":"DONE,DEFF,R1001,LOOK"},
	}

	rewardInfo = {
		1001:{"经验":lambda LV,R:(R/10+R%10+2)*(150+LV*20)},
		6050:{"物品":[1001]},
		6060:{"物品":[1011]},
		6070:{"物品":[1021]},
		6080:{"物品":[1031]},
		6090:{"物品":[1041]},
		6100:{"物品":[1051]},
		7050:{"物品":[1001]},
		7060:{"物品":[1011]},
		7070:{"物品":[1021]},
		7080:{"物品":[1031]},
		7090:{"物品":[1041]},
		7100:{"物品":[1051]},
	}

	rewardPropsInfo = {
		1001:(
			{"权重":60,"物品":"241305","数量":"1","绑定":0,"传闻":0},
			{"权重":40,"物品":"241306","数量":"1","绑定":0,"传闻":0},
			{"权重":60,"物品":"247002","数量":"1","绑定":0,"传闻":"RSM5001"},
			{"权重":40,"物品":"247003","数量":"1","绑定":0,"传闻":"RSM5001"},
			{"权重":100,"物品":"245001","数量":"5","绑定":0,"传闻":0},
		),
		1011:(
			{"权重":60,"物品":"241306","数量":"1","绑定":0,"传闻":0},
			{"权重":40,"物品":"241307","数量":"1","绑定":0,"传闻":0},
			{"权重":60,"物品":"247003","数量":"1","绑定":0,"传闻":"RSM5001"},
			{"权重":40,"物品":"247004","数量":"1","绑定":0,"传闻":"RSM5001"},
			{"权重":100,"物品":"245001","数量":"6","绑定":0,"传闻":0},
		),
		1021:(
			{"权重":60,"物品":"241307","数量":"1","绑定":0,"传闻":0},
			{"权重":40,"物品":"241308","数量":"1","绑定":0,"传闻":0},
			{"权重":60,"物品":"247004","数量":"1","绑定":0,"传闻":"RSM5001"},
			{"权重":40,"物品":"247005","数量":"1","绑定":0,"传闻":"RSM5001"},
			{"权重":100,"物品":"245001","数量":"7","绑定":0,"传闻":0},
		),
		1031:(
			{"权重":60,"物品":"241308","数量":"1","绑定":0,"传闻":0},
			{"权重":40,"物品":"241309","数量":"1","绑定":0,"传闻":0},
			{"权重":60,"物品":"247005","数量":"1","绑定":0,"传闻":"RSM5001"},
			{"权重":40,"物品":"247006","数量":"1","绑定":0,"传闻":"RSM5001"},
			{"权重":100,"物品":"245001","数量":"8","绑定":0,"传闻":0},
		),
		1041:(
			{"权重":60,"物品":"241309","数量":"1","绑定":0,"传闻":0},
			{"权重":40,"物品":"241310","数量":"1","绑定":0,"传闻":0},
			{"权重":60,"物品":"247006","数量":"1","绑定":0,"传闻":"RSM5001"},
			{"权重":40,"物品":"247007","数量":"1","绑定":0,"传闻":"RSM5001"},
			{"权重":100,"物品":"245001","数量":"9","绑定":0,"传闻":0},
		),
		1051:(
			{"权重":60,"物品":"241310","数量":"1","绑定":0,"传闻":0},
			{"权重":40,"物品":"241311","数量":"1","绑定":0,"传闻":0},
			{"权重":60,"物品":"247007","数量":"1","绑定":0,"传闻":"RSM5001"},
			{"权重":40,"物品":"247008","数量":"1","绑定":0,"传闻":"RSM5001"},
			{"权重":100,"物品":"245001","数量":"10","绑定":0,"传闻":0},
		),
	}

	groupInfo = {
		9001:(1001,1002,1003,),
		9002:(1004,1005,1006,),
		9003:(1016,1017,1018,),
		9004:(1007,1008,1009,),
		9005:(1010,1011,1012,),
		9006:(1013,1014,1015,),
		9007:(1001,),
		9008:(1002,),
		9009:(1003,),
		9010:(1004,),
		9011:(1005,),
		9012:(1006,),
		9013:(3001,),
		9014:(3002,),
		9015:(20201,20202,20203,20204,20205,20206,20208,20301,20302,20303,20304,20401,20402,20501,20601,20602,20603,20701,20702,20801,20802,20803,20901,20902,20903,),
		9016:(100004,100054,100104,100154,100204,100254,100304,100354,100404,100454,100504,100554,101004,101104,101204,101304,101404,101504,101604,220002,220003,220004,220005,220006,220007,220008,220009,221101,221102,221103,221104,246001,246002,246003,246004,246005,246006,246007,246008,246009,246010,),
		9017:(100005,100006,100055,100056,100105,100106,100155,100156,100205,100206,100255,100256,100305,100306,100355,100356,100405,100406,100455,100456,100505,100506,100555,100556,101005,101006,101105,101106,101205,101206,101305,101306,101405,101406,101505,101506,101605,101606,234101,234102,234103,234104,234105,234106,234107,234108,234109,234110,234111,234112,234113,234114,234115,234116,234117,234118,234119,234120,234121,234122,234123,234124,234125,234126,234127,234128,234129,234130,234131,234132,234133,234134,234135,234136,234137,234138,234139,234140,234141,234142,234143,234144,234145,234146,234147,234148,234149,234150,234151,234152,234153,),
		9018:(241001,241101,),
		9019:(1030,1040,1060,1130,1140,2030,2040,),
		30601:(4001,4002,4003,),
		30602:(4004,4005,4006,),
		30603:(4007,4008,4009,),
		30604:(4010,4011,4012,),
		30605:(4013,4014,4015,),
		9020:(100004,100054,100104,100154,100204,100254,100304,100354,100404,100454,100504,100554,101004,101104,101204,101304,101404,101504,101604,),
		9021:(221101,221102,221103,221104,220002,220003,220004,220005,220006,220007,220008,220009,),
		9022:(102,),
		9023:(100005,100006,100055,100056,100105,100106,100155,100156,100205,100206,100255,100256,100305,100306,100355,100356,100405,100406,100455,100456,100505,100506,100555,100556,101005,101006,101105,101106,101205,101206,101305,101306,101405,101406,101505,101506,101605,101606,),
		9024:(101,),
	}

	chatInfo = {
		4001:'''*3*帮我找下$target''',
		4002:'''*3*帮我带些话给$target''',
		4003:'''*3*$target正在找你，去看看吧！''',
		4004:'''*3*听闻$target正在收集$props，请帮助找回来。''',
		4005:'''*3*之前我不小心惹恼了$target，帮我寻找$props送给$target。''',
		4006:'''*3*$target最近愁眉不展，据闻是遍寻$props不得，你能帮一下$target吗？''',
		4007:'''*3*听闻$target正在收集$props，请帮助找回来。''',
		4008:'''*3*之前我不小心惹恼了$target，帮我寻找$props送给$target。''',
		4009:'''*3*$target最近愁眉不展，据闻是遍寻$props不得，你能帮一下$target吗？''',
		4010:'''*3*听闻排行榜高手$target的消息，你可以去请教一番。''',
		4011:'''*3*排行榜高手$target就再附近，你敢去挑战他吗？''',
		4012:'''*3*听闻排行榜高手$target的消息，与其切磋，对你自身修行，大有益处。''',
		4013:'''*3*听说$target那里有一道难题急需人解答，去看看吧。''',
		4014:'''*3*麻烦你帮我向$target传话，切莫耽误''',
		4015:'''*3*麻烦你帮我向$target传话，切莫耽误''',
		4016:'''$N#n你好，每周在我这里可以领取任务链哦，在封妖塔挂机击杀怪物有可能获得任务需要物品，帮助其他玩家击杀环怪可以获得侠义值''',
		4017:'''你已经领取到任务链了，不要在此胡闹！''',
		4018:'''你本周已领取过一次任务链，请下周再来吧。''',
		4019:'''1.大于或等于50级的玩家可领取任务链\n2.任务链由200环任务组成，每完成一环任务都可以获得经验奖励\n3.每完成100环任务可获得物品奖励\n4.任务链战斗可组队完成\n5.遇到难度太大的任务可尝试发送任务链求助''',
		4020:'''我要的找来了吗？''',
		4021:'''我需要的不是这个，不要在这寻我开心！''',
		4022:'''指教说不上，但切磋交流正合我意，来吧！\nQ进入战斗''',
		4023:'''我这有问题一道，敢接受挑战吗？\nQ答题''',
		4024:'''答不上来吧？要不再来一道简单的？\nQ答题''',
		4025:'''#C01$roleName#n的入世修行求助已被#C01$roleName#n完成''',
		4026:'''此入世修行求助已完成''',
		4027:'''你没有可取消的入世修行任务''',
		4028:'''入世修行任务已放弃''',
		4029:'''无法完成自己发送的求助链接''',
		4030:'''已有入世修行任务所需物品''',
		4031:'''对方已拥有该物品''',
		4032:'''#C01$roleName#n建议你选择答案：#C02$answer#n''',
		5001:'''#C01$roleName#n在#L1<14,20>*[入世修行]*02#n中潜心修炼，突然眼前金光一闪，一个$lnkProps掉在了他的面前#42''',
	}

	branchInfo = {
		1001:(
			{"条件":0,"脚本":"L(9016,1)"},
		),
		1002:(
			{"条件":0,"脚本":"L(9017,1)"},
		),
		1003:(
			{"条件":50,"脚本":"R6050"},
			{"条件":60,"脚本":"R6060"},
			{"条件":70,"脚本":"R6070"},
			{"条件":80,"脚本":"R6080"},
			{"条件":90,"脚本":"R6090"},
			{"条件":100,"脚本":"R6100"},
		),
		1004:(
			{"条件":50,"脚本":"R7050"},
			{"条件":60,"脚本":"R7060"},
			{"条件":70,"脚本":"R7070"},
			{"条件":80,"脚本":"R7080"},
			{"条件":90,"脚本":"R7090"},
			{"条件":100,"脚本":"R7100"},
		),
	}

	fightInfo = {
		1001:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1001","数量":"1","技能":(1111,1112,1113,),"站位":(1,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1211(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(6,)},
			{"类型":0,"名称":"修行者·武林","造型":"1321(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(7,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(8,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1621(1,1,1,1,1,1)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1002:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1001","数量":"1","技能":(1121,1122,1123,),"站位":(1,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1221(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(6,)},
			{"类型":0,"名称":"修行者·武林","造型":"1311(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(7,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(8,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1621(1,1,1,1,1,1)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1003:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1001","数量":"1","技能":(1131,1132,1133,),"站位":(1,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1211(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(6,)},
			{"类型":0,"名称":"修行者·武林","造型":"1311(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(7,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(8,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1621(1,1,1,1,1,1)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1004:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1002","数量":"1","技能":(1211,1212,1213,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1111(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·武林","造型":"1311(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(7,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(8,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1621(1,1,1,1,1,1)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1005:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1002","数量":"1","技能":(1221,1222,1223,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1121(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·武林","造型":"1321(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(7,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(8,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1611(0,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1006:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1002","数量":"1","技能":(1231,1232,1233,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1121(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·武林","造型":"1311(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(7,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(8,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1621(1,1,1,1,1,1)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1007:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1003","数量":"1","技能":(1311,1312,1313,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1111(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1221(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(7,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(8,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1611(0,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1008:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1003","数量":"1","技能":(1321,1322,1323,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1121(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1211(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(7,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(8,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1611(0,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1009:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1003","数量":"1","技能":(1331,1332,1333,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1111(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1211(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(7,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(8,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1621(1,1,1,1,1,1)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1010:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1004","数量":"1","技能":(1411,1412,1413,1423,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1111(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1221(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(7,)},
			{"类型":0,"名称":"修行者·武林","造型":"1321(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(8,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1611(0,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1011:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1004","数量":"1","技能":(1421,1422,1423,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1121(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1221(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(7,)},
			{"类型":0,"名称":"修行者·武林","造型":"1311(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(8,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1621(1,1,1,1,1,1)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1012:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1004","数量":"1","技能":(1431,1432,1433,1423,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1111(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1211(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(7,)},
			{"类型":0,"名称":"修行者·武林","造型":"1311(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(8,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1611(0,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1013:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1005","数量":"1","技能":(1511,1512,1513,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1111(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1211(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(7,)},
			{"类型":0,"名称":"修行者·武林","造型":"1321(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(8,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1621(1,1,1,1,1,1)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1014:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1005","数量":"1","技能":(1521,1522,1523,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1121(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1221(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(7,)},
			{"类型":0,"名称":"修行者·武林","造型":"1321(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(8,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1611(0,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1015:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1005","数量":"1","技能":(1521,1522,1523,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1111(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1221(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(7,)},
			{"类型":0,"名称":"修行者·武林","造型":"1311(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(8,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(9,)},
			{"类型":0,"名称":"修行者·佛门","造型":"1621(1,1,1,1,1,1)","染色":"0,0,0,0,0,0","能力编号":"2006","数量":"1","技能":(1621,1622,1623,),"站位":(10,)},
		),
		1016:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1006","数量":"1","技能":(1611,1612,1613,1621,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1111(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1211(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(7,)},
			{"类型":0,"名称":"修行者·武林","造型":"1311(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(8,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(9,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(10,)},
		),
		1017:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1006","数量":"1","技能":(1621,1622,1623,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1121(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1221(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(7,)},
			{"类型":0,"名称":"修行者·武林","造型":"1321(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(8,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(9,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(10,)},
		),
		1018:(
			{"类型":1,"名称":"$npc","造型":"$npc","染色":"0,0,0,0,0,0","能力编号":"1006","数量":"1","技能":(1621,1631,1632,1633,),"站位":(1,)},
			{"类型":0,"名称":"修行者·蜀山","造型":"1121(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1121,1122,1123,),"站位":(6,)},
			{"类型":0,"名称":"修行者·唐门","造型":"1221(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2002","数量":"1","技能":(1221,1222,1223,),"站位":(7,)},
			{"类型":0,"名称":"修行者·武林","造型":"1311(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2003","数量":"1","技能":(1321,1322,1323,),"站位":(8,)},
			{"类型":0,"名称":"修行者·苗疆","造型":"1411(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2004","数量":"1","技能":(1421,1422,1423,),"站位":(9,)},
			{"类型":0,"名称":"修行者·魔宫","造型":"1521(1,1,1,1,1,0)","染色":"0,0,0,0,0,0","能力编号":"2005","数量":"1","技能":(1521,1522,1523,),"站位":(10,)},
		),
		2001:(
			{"类型":0,"名称":"草妖","造型":"3006(0,1,0,0,0,0)","染色":"0,2,0,0,0,0","能力编号":"3001","数量":"2","技能":(5401,5402,5403,5404,5405,),"站位":(4,5,)},
			{"类型":0,"名称":"草妖","造型":"3006(0,1,0,0,0,0)","染色":"0,3,0,0,0,0","能力编号":"3001","数量":"1","技能":(5406,),"站位":(1,)},
			{"类型":0,"名称":"妖猴","造型":"3007(0,1,0,0,0,0)","染色":"0,3,0,0,0,0","能力编号":"3002","数量":"2","站位":(7,8,)},
			{"类型":0,"名称":"妖猴","造型":"3007(0,1,0,0,0,0)","染色":"0,4,0,0,0,0","能力编号":"3002","数量":"1","技能":(5417,),"站位":(2,)},
			{"类型":0,"名称":"灵狐","造型":"3008(0,1,0,0,0,0)","染色":"0,2,0,0,0,0","能力编号":"3003","数量":"2","技能":(5411,5412,5413,5414,5415,),"站位":(9,10,)},
			{"类型":0,"名称":"灵狐","造型":"3008(0,1,0,0,0,0)","染色":"0,4,0,0,0,0","能力编号":"3003","数量":"1","技能":(5408,),"站位":(3,)},
		),
	}

	ableInfo = {
		1001:{"等级":"ALV+1","生命":"B*1.13","真气":"B*1","物理伤害":"B*0.97","法术伤害":"B*0.67","物理防御":"B*0.84","法术防御":"B*0.59","速度":"B*0.96","治疗强度":"B*0.67","封印命中":"B*0","抵抗封印":"B*0.96","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1002:{"等级":"ALV+1","生命":"B*1.13","真气":"B*1","物理伤害":"B*0.97","法术伤害":"B*0.97","物理防御":"B*0.72","法术防御":"B*0.72","速度":"B*0.96","治疗强度":"B*0.67","封印命中":"B*0","抵抗封印":"B*0.96","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1003:{"等级":"ALV+1","生命":"B*1.13","真气":"B*1","物理伤害":"B*0.97","法术伤害":"B*0.67","物理防御":"B*0.84","法术防御":"B*0.59","速度":"B*0.96","治疗强度":"B*0.67","封印命中":"B*0","抵抗封印":"B*0.96","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1004:{"等级":"ALV+1","生命":"B*1.13","真气":"B*1","物理伤害":"B*0.97","法术伤害":"B*0.97","物理防御":"B*0.72","法术防御":"B*0.72","速度":"B*1.02","治疗强度":"B*0.67","封印命中":"B*0.96","抵抗封印":"B*0.96","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1005:{"等级":"ALV+1","生命":"B*1.13","真气":"B*1","物理伤害":"B*0.67","法术伤害":"B*0.97","物理防御":"B*0.59","法术防御":"B*0.84","速度":"B*0.96","治疗强度":"B*0.67","封印命中":"B*0","抵抗封印":"B*0.96","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1006:{"等级":"ALV+1","生命":"B*1.13","真气":"B*1","物理伤害":"B*0.67","法术伤害":"B*0.67","物理防御":"B*0.72","法术防御":"B*0.72","速度":"B*0.96","治疗强度":"B*0.96","封印命中":"B*0","抵抗封印":"B*0.96","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		2001:{"等级":"ALV","生命":"B*0.9","真气":"B*1","物理伤害":"B*0.81","法术伤害":"B*0.56","物理防御":"B*0.7","法术防御":"B*0.49","速度":"B*0.8","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		2002:{"等级":"ALV","生命":"B*0.9","真气":"B*1","物理伤害":"B*0.81","法术伤害":"B*0.81","物理防御":"B*0.6","法术防御":"B*0.6","速度":"B*0.8","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		2003:{"等级":"ALV","生命":"B*0.9","真气":"B*1","物理伤害":"B*0.81","法术伤害":"B*0.56","物理防御":"B*0.7","法术防御":"B*0.49","速度":"B*0.8","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		2004:{"等级":"ALV","生命":"B*0.9","真气":"B*1","物理伤害":"B*0.81","法术伤害":"B*0.81","物理防御":"B*0.6","法术防御":"B*0.6","速度":"B*0.85","治疗强度":"B*0.56","封印命中":"B*0.8","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		2005:{"等级":"ALV","生命":"B*0.9","真气":"B*1","物理伤害":"B*0.56","法术伤害":"B*0.81","物理防御":"B*0.49","法术防御":"B*0.7","速度":"B*0.8","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		2006:{"等级":"ALV","生命":"B*0.9","真气":"B*1","物理伤害":"B*0.56","法术伤害":"B*0.56","物理防御":"B*0.6","法术防御":"B*0.6","速度":"B*0.8","治疗强度":"B*0.8","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		3001:{"等级":"LV","生命":"B*0.3","真气":"B*1","物理伤害":"B*0.4","法术伤害":"B*0.4","物理防御":"B*0.3","法术防御":"B*0.3","速度":"B*0.4","治疗强度":"B*0.28","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		3002:{"等级":"LV","生命":"B*0.3","真气":"B*1","物理伤害":"B*0.4","法术伤害":"B*0.4","物理防御":"B*0.3","法术防御":"B*0.3","速度":"B*0.4","治疗强度":"B*0.28","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		3003:{"等级":"LV","生命":"B*0.3","真气":"B*1","物理伤害":"B*0.4","法术伤害":"B*0.4","物理防御":"B*0.3","法术防御":"B*0.3","速度":"B*0.4","治疗强度":"B*0.28","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
	}

	lineupInfo = {
	}

	configInfo = {
		"生成路径":"ring",
		1001:200000,
		1002:"LV*50+1000",
		1003:2,
		1004:1,
		1005:50,
		5001:"(R/10+R%10+2)*(150+LV*20)",
		5002:"90+(int(R/10)-5)*4+rand(0,5)",
		5003:"20+int(LV/5)",
		5004:"20+int(LV/5)",
		5005:"(20+int(LV/5))*4",
		5006:"(20+int(LV/5))*4",
		5007:5,
		5008:"(S-3)*20",
	}

	ringTask = {
		0:(
			{"编号":30601,"权重":60},
			{"编号":30602,"权重":15},
			{"编号":30603,"权重":5},
			{"编号":30604,"权重":10},
			{"编号":30605,"权重":10},
		),
		30:(
			{"编号":30601,"权重":50},
			{"编号":30602,"权重":22},
			{"编号":30603,"权重":8},
			{"编号":30604,"权重":10},
			{"编号":30605,"权重":10},
		),
		70:(
			{"编号":30601,"权重":40},
			{"编号":30602,"权重":30},
			{"编号":30603,"权重":10},
			{"编号":30604,"权重":10},
			{"编号":30605,"权重":10},
		),
		120:(
			{"编号":30601,"权重":20},
			{"编号":30602,"权重":47},
			{"编号":30603,"权重":13},
			{"编号":30604,"权重":10},
			{"编号":30605,"权重":10},
		),
		160:(
			{"编号":30601,"权重":10},
			{"编号":30602,"权重":65},
			{"编号":30603,"权重":15},
			{"编号":30604,"权重":5},
			{"编号":30605,"权重":5},
		),
	}

	propsWeight = {
		1001:(
			{"权重":100,"脚本":"L(9020,1)"},
			{"权重":50,"脚本":"L(9021,1)"},
			{"权重":20,"脚本":"L(9022,1)"},
		),
		1002:(
			{"权重":100,"脚本":"L(9023,1)"},
			{"权重":50,"脚本":"L(9024,1)"},
		),
	}
#导表结束

	def onBorn(self, who, npcObj, **kwargs):
		customTask.onBorn(self, who, npcObj, **kwargs)
		self.set("uniqueId", getSecond())

	def getUniqueId(self):
		uid = self.fetch("uniqueId")
		if not uid:
			uid = getSecond()
			self.set("uniqueId", uid)
		return uid

	def getPropsName(self, propsNo, amount):
		if propsGroupData.isPropsGroup(propsNo):
			name = propsGroupData.getConfig(propsNo, "名字")
		else:
			propsObj = props.getCacheProps(propsNo)
			name = propsObj.name
		if amount > 1:
			name = "#C01%sx%d#n" % (name, amount)
		else:
			name = "#C01%s#n" % name
		return name

	def canAbort(self):
		'''是否可以放弃任务
		'''
		return 0

	def getTitle(self, who):
		title = self.transString(self.title, who.id)
		return "%s#C07(%d/%d)#n" % (title, self.getRing(who), MAX_RING)

	def getRing(self, who):
		return who.taskCtn.fetch("ringRing") + 1

	def getBranchCondition(self, who, npcObj, branchIdx, flag):
		if flag == "lv":
			lst = [info["条件"] for info in self.getBranchInfo(branchIdx)]
			lst.sort(reverse=True)
			for lv in lst:
				if who.level >= lv:
					return lv
		elif flag == "wt":
			info = self.getBranchInfo(branchIdx)
			idx = chooseKey(info, total=total, key="条件")
			if idx is None:
				return
			info = info[idx]
		return customTask.getBranchCondition(self, who, npcObj, branchIdx, flag)

	def getValueByVarName(self, varName, who):
		if varName == "R":
			if who:
				helpRing = self.fetch("helpRing")
				ring = helpRing if helpRing else who.taskCtn.fetch("ringRing")
				return ring
			return 0
		return customTask.getValueByVarName(self, varName, who)

	def onMissionDone(self, who, npcObj):
		ring = who.taskCtn.add("ringRing", 1)
		if ring == 100:
			self.doScript(who, npcObj, "B(1003,lv)") # 100环奖励
		elif ring == MAX_RING:
			self.doScript(who, npcObj, "B(1004,lv)") # 200环物品奖励
			who.taskCtn.delete("ringRing")
			return
		# 自动给任务
		taskObj = task.ring.randRingTask(who, npcObj)
		if taskObj:
			self.doChat(who, npcObj, taskObj)
			taskObj.timerMgr.run(functor(taskObj.autoGoAhead, who.id), 1, 0, "ring_%s%s"%(taskObj.id, who.id))

	def autoGoAhead(self, pid):
		who = getRole(pid)
		if who:
			self.goAhead(who)

	def doChat(self, who, npcObj, taskObj):
		'''领取任务后的对话
		'''
		chatIdx = taskObj.transIdxByGroup(taskObj.id)
		chatScript = "D{}".format(chatIdx)
		taskObj.doScript(who, npcObj, chatScript)

	def askForHelp(self, who):
		'''求助
		'''
		if self.targetType == TASK_TARGET_TYPE_ITEM and self.hasAllNeededProps(who):
			message.tips(who, self.getText(4030))
			return
		oGuild = who.getGuildObj()
		if not oGuild:
			message.tips(who, "您没有加入仙盟")
			return
		sHelpCnt = self.configInfo.get(5004, "20")
		helpCnt = eval(sHelpCnt.replace("LV", str(who.level)))
		if who.week.fetch("ringHelp", 0) >= helpCnt:
			message.tips(who, "入世修行求助次数不足，请等待下周或提升等级后再次尝试")
			return
		sLink = self.getHyperLink(who)
		if not sLink:
			return
		message.guildRoleMessage(who.id, oGuild.id, sLink)
		message.tips(who, "仙盟求助已发出")

	def offerHelp(self, who):
		'''提供帮助
		'''
		message.tips(who, "该功能暂未开放")

	def hasAllNeededProps(self, who):
		'''是否有任务所需的全部物品
		'''
		for propsNo, amount in self.getPropsNeeded().iteritems():
			if propsGroupData.isPropsGroup(propsNo):
				propsNoList = propsGroupData.getConfig(propsNo, "列表", [])
				hasAmount = sum(who.propsCtn.getPropsAmountByNos(*propsNoList))
			else:
				hasAmount = who.propsCtn.getPropsAmountByNos(propsNo)[0]
			if hasAmount < amount:
				return 0
		return 1

	def handlePropsGroup(self, propsNoListNeeded):
		# 特殊处理，对于组物品序号，转换成相应的列表
		for groupNo in propsGroupData.getGroupNos():
			if groupNo in propsNoListNeeded:
				propsNoListNeeded.remove(groupNo)
				noList = propsGroupData.getConfig(groupNo, "列表", [])
				propsNoListNeeded.extend(list(noList))
		return propsNoListNeeded

	def popPropsUI(self, who, npcObj):
		'''弹出上交物品界面
		'''
		if not self.hasAllNeededProps(who):
			self.notCompleteTakeProps(who, npcObj)
			return
		propsNeeded = self.getPropsNeeded()
		propsNoListNeeded = propsNeeded.keys()
		propsNoListNeeded = self.handlePropsGroup(propsNoListNeeded)
		propsObjList = list(who.propsCtn.getPropsGroupByNo(*propsNoListNeeded))
		propsObjList = props.tidy.sortList(propsObjList)
		propsIdList = [propsObj.id for propsObj in propsObjList]
		message.popPropsUI(who, functor(self.responsePopPropsUI, npcObj.id) , "任务物品选择", propsIdList)

	def responsePopPropsUI(self, who, propsList, npcId):
		npcObj = getNpc(npcId)
		if not npcObj:
			return
		propsNeeded = self.getPropsNeeded()
		propsNoListNeeded = propsNeeded.keys()
		propsNoListNeeded = self.handlePropsGroup(propsNoListNeeded)
		propsObjList = []
		propsNoListTmp = {}
		for propsId, amount in propsList.iteritems():
			propsObj = who.propsCtn.getItem(propsId)
			if not propsObj:
				message.tips(who, "你身上没有此物品")
				return
			if propsObj.idx not in propsNoListNeeded:
# 				message.tips(who, "上交的物品不对")
				self.notCompleteTakeProps(who, npcObj)
				return
			if amount > propsObj.stack():
				message.tips(who, "上交的数量不对")
				return
			propsObjList.append(propsObj)
			propsNoListTmp[propsObj.idx] = propsNoListTmp.get(propsObj.idx, 0) + amount
		
		# if propsNoListTmp != propsNeeded: #这个也特殊
		if sum(propsNoListTmp.values()) < sum(propsNeeded.values()):
			message.tips(who, "上交的数量不对")
			return
		
		if self.checkTakeProps(who, npcObj, propsObjList):
			for propsObj in propsObjList:
				amount = propsList[propsObj.id]
				who.propsCtn.addStack(propsObj, -amount)
			self.completeTakeProps(who, npcObj, propsObjList)
		else:
			self.notCompleteTakeProps(who, npcObj, propsObjList)

	def popHelpPropsUI(self, who, npcObj):
		'''弹出上交物品界面
		'''
		propsNeeded = self.getPropsNeeded()
		propsNoListNeeded = propsNeeded.keys()
		propsNoListNeeded = self.handlePropsGroup(propsNoListNeeded)
		propsObjList = list(who.propsCtn.getPropsGroupByNo(*propsNoListNeeded))
		propsObjList = props.tidy.sortList(propsObjList)
		propsIdList = [propsObj.id for propsObj in propsObjList]
		message.popPropsUI(who, functor(self.responsePopHelpPropsUI, npcObj.id), "任务物品选择", propsIdList)
		
	def responsePopHelpPropsUI(self, who, propsList, npcId):
		npcObj = getNpc(npcId)
		owner = self.getOwnerObj()
		if not owner or not npcObj:
			return
		
		propsNeeded = self.getPropsNeeded()
		propsNoListNeeded = propsNeeded.keys()
		propsNoListNeeded = self.handlePropsGroup(propsNoListNeeded)
		propsObjList = []
		propsNoListTmp = {}
		for propsId, amount in propsList.iteritems():
			propsObj = who.propsCtn.getItem(propsId)
			if not propsObj:
				message.tips(who, "你身上没有此物品")
				return
			if propsObj.idx not in propsNoListNeeded:
# 				message.tips(who, "上交的物品不对")
				self.notCompleteTakeProps(who, npcObj)
				return
			if amount > propsObj.stack():
				message.tips(who, "上交的数量不对")
				return
			propsObjList.append(propsObj)
			propsNoListTmp[propsObj.idx] = propsNoListTmp.get(propsObj.idx, 0) + amount
		# if propsNoListTmp != propsNeeded: #这个也特殊
		if sum(propsNoListTmp.values()) < sum(propsNeeded.values()):
			message.tips(who, "上交的数量不对")
			return
		if self.checkTakeProps(who, npcObj, propsObjList):
			for propsObj in propsObjList:
				amount = propsList[propsObj.id]
				who.propsCtn.addStack(propsObj, -amount)
			self.set("helpRoleId", who.id)
			self.set("helpRing", owner.taskCtn.fetch("ringRing")+1)
			self.completeTakeProps(owner, npcObj, propsObjList)
			who.week.add("ringHelped", 1)
			owner.week.add("ringHelp", 1)
			txt = "#C01{}#n的#L1<14,20>*[入世修行]*02#n求助已被#C01{}#n完成".format(owner.name, who.name)
			message.guildMessage(owner.getGuildId(), txt)
		else:
			self.notCompleteTakeProps(who, npcObj, propsObjList)

	def reward(self, who, rwdIdx, npcObj=None):
		helpId = self.fetch("helpRoleId")
		if helpId:
			helpObj = getRole(helpId)
			if helpObj:
				who = helpObj
		template.Template.reward(self, who, rwdIdx, npcObj)

	def warEnd(self, warObj, npcObj):
		'''战斗结束
		'''
		who = self.getOwnerObj()
		if who:
			who.triggerWarTime = getSecond()

	def handleLegends(self, who, npcObj, *args):
		if rand(100) < self.configInfo.get(5007, 5):
			neededProps = self.getPropsNeeded()
			for propsNo, amount in neededProps.iteritems():
				if propsGroupData.isPropsGroup(propsNo):
					propsNo = 234145 if propsNo == 101 else 246010
				launch.launchBySpecify(who, propsNo, amount, True, "任务链传说", None)
			message.tips(who, "任务物品已获得")
			gevent.spawn(task.goAhead, who.id, self.id)
			who.propsCtn.removePropsByNo(203021)
			self.timerMgr.cancel("timeOut")
			self.delete("endTime")
			task.service.refreshTask(who, self)
		elif self.timerMgr.hasTimerId("timeOut"):
			gevent.spawn(walkGuard, who.id)

	def customTriggerRatio(self, who):
		'''触发暗雷几率:全局配置表5008
		'''
		if not hasattr(self, "lastCheckTime"):
			self.lastCheckTime = getSecond()
		elif getSecond() - self.lastCheckTime < 1:
			return
		else:
			self.lastCheckTime = getSecond()
		subTime = getSecond() - who.triggerWarTime
		if not subTime:
			return
		sRatio = self.configInfo.get(5008, "20").replace("S", str(subTime))
		ratio = eval(sRatio)
		if rand(100) < ratio:
			return True
		return False

	def triggerWar(self, who):
		'''触发暗雷
		'''
		if not self.timerMgr.hasTimerId("timeOut"):
			return
		sceneId = who.sceneId
		for data in self.getAnlei():
			if sceneId in data["sceneList"]:
				npcObj = self.addTempNpc(data["npcIdx"], who)
				npcObj.eventIdx = data["eventIdx"]
				script = self.getEventScript(who, npcObj, "点击")
				self.doScript(who, npcObj, script)
				return 1
		return 0

	def timeOut(self):
		'''超时
		'''
		if self.timerMgr.hasTimerId("timeOut"):
			self.timerMgr.cancel("timeOut")
		self.delete("endTime")
		who = self.getOwnerObj()
		if not who:
			return
		who.propsCtn.removePropsByNo(203021)
		message.tips(who, "倒计时结束，任务物品已无法获得")
		message.message(who, "倒计时结束，任务物品已无法获得")
		task.service.refreshTask(who, self)

	def getScriptHandler(self, script):#override
		for pattern, handler in gScriptHandlerList.iteritems():
			m = re.match(pattern, script)
			if not m:
				continue
			args = m.groups()
			return handler, args
		return customTask.getScriptHandler(self, script)

	def handlePropsWeight(self, who, npcObj, *args):
		'''任务物品权重处理
		'''
		info = self.getRefObj().propsWeight[int(args[0])]
		idx = chooseKey(info, key="权重")
		if idx is None:
			return
		info = info[idx]
		self.doScript(who, npcObj, info["脚本"])

	def taskHyperlink(self, who, targetRole, taskId, *args):
		if not targetRole or len(args) < 1:
			return
		uniqueId = int(args[0])
		if not uniqueId:
			import task.service
			msgObj = task.service.packet4Hyperlink(targetRole, self)
			who.endPoint.rpcTaskHyperlink(msgObj)
			return
		taskObj = targetRole.taskCtn.getItem(taskId)
		print 'taskHyperLINK', uniqueId, taskObj.getUniqueId()
		if not taskObj or taskObj.getUniqueId() != uniqueId:
			message.tips(who, taskObj.getText(4026))
			return
		elif who.id == targetRole.id:
			message.tips(who, taskObj.getText(4029))
			return
		taskObj.offerHelp(who)

	def popHelpGoodsUI(self, who):
		npcObj = self.getGoodsNpc()
		if not npcObj:
			message.tips(who, self.getText(4031))
			return
		if npcObj.kind == "商店":
			import shop
			shop.openShop(who, npcObj.idx, 0, self.getPropsNeeded().keys()[0], True)
		elif npcObj.kind == "交易":
			import trade
			trade.openTradeCenter(who, self)


def walkGuard(roleId):
	who = getRole(roleId)
	if not who:
		return
	scene.walkGuard(who, 2010)


def handleAnswer(taskObj, who, npcObj, *args):
	'''答题
	'''
	taskObj.handleAnswer(who, npcObj, *args)

def handleLegends(taskObj, who, npcObj, *args):
	'''传说物品
	'''
	taskObj.handleLegends(who, npcObj, *args)

def handlePropsWeight(taskObj, who, npcObj, *args):
	'''任务物品权重
	'''
	taskObj.handlePropsWeight(who, npcObj, *args)


# 脚本处理函数
gScriptHandlerList = {
	"ANSWER":handleAnswer,
	"LEGENDS":handleLegends,
	"PW(\d+)": handlePropsWeight,
}


import gevent
from common import *
import message
import props
import task
import task.ring
import task.service
import template
import scene
import launch
import propsGroupData
