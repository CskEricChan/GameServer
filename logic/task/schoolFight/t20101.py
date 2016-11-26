# -*- coding: utf-8 -*-
from task.defines import *
from task.object import TeamTask as customTask

#导表开始
class Task(customTask):
	parentId = 20101
	targetType = TASK_TARGET_TYPE_NPC
	icon = 0
	title = '''门派试炼'''
	intro = '''找#C02$target#n接受挑战'''
	detail = '''#C03$map#n的#C02$target#n已经摆好架势等待挑战'''
	rewardDesc = ''''''
	goAheadScript = ''''''
	initScript = '''E(9001,1001)'''

	npcInfo = {
	}

	eventInfo = {
		1001:{"点击":"SB1016","回复":"1:$checkF1000","成功":"DONE,TD1007","失败":"TD1008"},
	}

	rewardInfo = {
		1001:{"经验":lambda ALV:ALV*122+8750,"宠物经验":lambda ALV:ALV*122+8750,"银币":lambda ALV:ALV*69+3500,"物品":[1001]},
		1002:{"经验":lambda ALV:ALV*209+8750,"宠物经验":lambda ALV:ALV*209+8750,"银币":lambda ALV:ALV*121+3500,"物品":[1002]},
		1003:{"经验":lambda ALV:ALV*296+8750,"宠物经验":lambda ALV:ALV*296+8750,"银币":lambda ALV:ALV*173+3500,"物品":[1003]},
		1004:{"经验":lambda ALV:ALV*383+8750,"宠物经验":lambda ALV:ALV*383+8750,"银币":lambda ALV:ALV*225+3500,"物品":[1004]},
		1005:{"经验":lambda ALV:ALV*470+8750,"宠物经验":lambda ALV:ALV*470+8750,"银币":lambda ALV:ALV*277+3500,"物品":[1005]},
		1006:{"经验":lambda ALV:ALV*557+8750,"宠物经验":lambda ALV:ALV*557+8750,"银币":lambda ALV:ALV*329+3500,"物品":[1006]},
	}

	rewardPropsInfo = {
		1001:(
			{"权重":5,"物品":"224001","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":5,"物品":"224002","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":5,"物品":"224003","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":5,"物品":"224004","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":5,"物品":"224005","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":5,"物品":"224006","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":5,"物品":"224007","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":5,"物品":"224008","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":5,"物品":"224009","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":5,"物品":"224010","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":96,"物品":"224101","数量":"1","绑定":0,"传闻":0},
			{"权重":5,"物品":"224102","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":30,"物品":"230103","数量":"1","绑定":0,"传闻":0},
			{"权重":30,"物品":"234901","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":1,"物品":"234902","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":3,"物品":"234903","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":35,"物品":"245001","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246001","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246002","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246003","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246004","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246005","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246006","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246007","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246008","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246009","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246010","数量":"1","绑定":0,"传闻":0},
			{"权重":400,"物品":"0","数量":"0","绑定":0,"传闻":0},
		),
		1002:(
			{"权重":8,"物品":"224001","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":8,"物品":"224002","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":8,"物品":"224003","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":8,"物品":"224004","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":8,"物品":"224005","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":8,"物品":"224006","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":8,"物品":"224007","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":8,"物品":"224008","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":8,"物品":"224009","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":8,"物品":"224010","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":80,"物品":"224101","数量":"1","绑定":0,"传闻":0},
			{"权重":8,"物品":"224102","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":20,"物品":"230103","数量":"1","绑定":0,"传闻":0},
			{"权重":20,"物品":"234901","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":1,"物品":"234902","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":6,"物品":"234903","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":35,"物品":"245001","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246001","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246002","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246003","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246004","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246005","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246006","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246007","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246008","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246009","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246010","数量":"1","绑定":0,"传闻":0},
			{"权重":400,"物品":"0","数量":"0","绑定":0,"传闻":0},
		),
		1003:(
			{"权重":10,"物品":"224001","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":10,"物品":"224002","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":10,"物品":"224003","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":10,"物品":"224004","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":10,"物品":"224005","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":10,"物品":"224006","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":10,"物品":"224007","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":10,"物品":"224008","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":10,"物品":"224009","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":10,"物品":"224010","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":99,"物品":"224101","数量":"1","绑定":0,"传闻":0},
			{"权重":10,"物品":"224102","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":50,"物品":"230103","数量":"1","绑定":0,"传闻":0},
			{"权重":50,"物品":"234901","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":1,"物品":"234902","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":5,"物品":"234903","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":35,"物品":"245001","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246001","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246002","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246003","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246004","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246005","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246006","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246007","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246008","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246009","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246010","数量":"1","绑定":0,"传闻":0},
			{"权重":300,"物品":"0","数量":"0","绑定":0,"传闻":0},
		),
		1004:(
			{"权重":15,"物品":"224001","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":15,"物品":"224002","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":15,"物品":"224003","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":15,"物品":"224004","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":15,"物品":"224005","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":15,"物品":"224006","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":15,"物品":"224007","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":15,"物品":"224008","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":15,"物品":"224009","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":15,"物品":"224010","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":50,"物品":"224101","数量":"1","绑定":0,"传闻":0},
			{"权重":15,"物品":"224102","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":47,"物品":"230103","数量":"1","绑定":0,"传闻":0},
			{"权重":47,"物品":"234901","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":1,"物品":"234902","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":5,"物品":"234903","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":35,"物品":"245001","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246001","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246002","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246003","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246004","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246005","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246006","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246007","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246008","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246009","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246010","数量":"1","绑定":0,"传闻":0},
			{"权重":300,"物品":"0","数量":"0","绑定":0,"传闻":0},
		),
		1005:(
			{"权重":18,"物品":"224001","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":18,"物品":"224002","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":18,"物品":"224003","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":18,"物品":"224004","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":18,"物品":"224005","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":18,"物品":"224006","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":18,"物品":"224007","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":18,"物品":"224008","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":18,"物品":"224009","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":18,"物品":"224010","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":50,"物品":"224101","数量":"1","绑定":0,"传闻":0},
			{"权重":19,"物品":"224102","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":53,"物品":"230103","数量":"1","绑定":0,"传闻":0},
			{"权重":53,"物品":"234901","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":1,"物品":"234902","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":9,"物品":"234903","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":35,"物品":"245001","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246001","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246002","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246003","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246004","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246005","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246006","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246007","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246008","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246009","数量":"1","绑定":0,"传闻":0},
			{"权重":35,"物品":"246010","数量":"1","绑定":0,"传闻":0},
			{"权重":250,"物品":"0","数量":"0","绑定":0,"传闻":0},
		),
		1006:(
			{"权重":20,"物品":"224001","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":20,"物品":"224002","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":20,"物品":"224003","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":20,"物品":"224004","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":20,"物品":"224005","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":20,"物品":"224006","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":20,"物品":"224007","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":20,"物品":"224008","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":20,"物品":"224009","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":20,"物品":"224010","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":50,"物品":"224101","数量":"1","绑定":0,"传闻":0},
			{"权重":25,"物品":"224102","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":80,"物品":"230103","数量":"1","绑定":0,"传闻":0},
			{"权重":80,"物品":"234901","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":2,"物品":"234902","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":11,"物品":"234903","数量":"1","绑定":0,"传闻":"SM6001"},
			{"权重":32,"物品":"245001","数量":"1","绑定":0,"传闻":0},
			{"权重":32,"物品":"246001","数量":"1","绑定":0,"传闻":0},
			{"权重":32,"物品":"246002","数量":"1","绑定":0,"传闻":0},
			{"权重":32,"物品":"246003","数量":"1","绑定":0,"传闻":0},
			{"权重":32,"物品":"246004","数量":"1","绑定":0,"传闻":0},
			{"权重":32,"物品":"246005","数量":"1","绑定":0,"传闻":0},
			{"权重":32,"物品":"246006","数量":"1","绑定":0,"传闻":0},
			{"权重":32,"物品":"246007","数量":"1","绑定":0,"传闻":0},
			{"权重":32,"物品":"246008","数量":"1","绑定":0,"传闻":0},
			{"权重":32,"物品":"246009","数量":"1","绑定":0,"传闻":0},
			{"权重":32,"物品":"246010","数量":"1","绑定":0,"传闻":0},
			{"权重":200,"物品":"0","数量":"0","绑定":0,"传闻":0},
		),
	}

	groupInfo = {
		9001:(20201,20202,20203,20205,20206,20208,20301,20302,20303,20304,20402,20501,20601,20602,20801,20802,20902,20903,),
	}

	chatInfo = {
		1001:'''六大门派弟子广布天下，其中不乏武力高强深藏不露者。你们要去和他们切磋下吗？\nQ以武会友\nQ快捷组队''',
		1002:'''对方人多势众，活动需要#C04队伍人数≥3#n''',
		1003:'''请先召回暂离队员''',
		1004:'''刀剑无眼，不要带上小朋友。玩家#C04等级需≥40级#n''',
		1005:'''你已经有任务，快去完成吧''',
		1006:'''#C03$map#n的#C02$target#n集合了一群众门派弟子在等待你们去挑战，快去证明自己吧！''',
		1007:'''少侠们好武功，青出于蓝而胜于蓝。你们的成绩是#C02$time#n''',
		1008:'''你们一共闯过了#C02$number#n关，功力还是稍欠火候，准备一下再来继续挑战吧。''',
		1009:'''蜀山弟子''',
		1010:'''唐门弟子''',
		1011:'''武林盟弟子''',
		1012:'''魔宫弟子''',
		1013:'''苗疆弟子''',
		1014:'''佛门弟子''',
		1015:'''该我出手了，你们注意啦''',
		1016:'''$chat\nQ以武会友''',
		6001:'''#C01$roleName#n在#L1<14,25>*[门派试炼]*02#n中表现出色，获得了$lnkProps''',
		6002:'''#L1<14,25>*[门派试炼]*02#n将在#C0220:00#n准时开始，请各位少侠做好准备，前往等待活动开始''',
		6003:'''#L1<14,25>*[门派试炼]*02#n已经开始，已经准备好的少侠快前往领取任务，挑战诸大门派''',
		6004:'''本次#L1<14,25>*[门派试炼]*02#n已经结束，表现最好的队伍为：#C01$team1#n（#C02$time1#n）;#C01$team2#n（#C02$time2#n）;#C01$team3#n（#C02$time3#n）''',
	}

	branchInfo = {
	}

	fightInfo = {
		1000:(
			{"类型":1,"名称":"$npc","造型":"$npc","能力编号":"1001","数量":"1","技能":(1133,1211,1323,1413,1532,1623,),"站位":(1,)},
		),
		1001:(
			{"类型":0,"名称":"蜀山弟子","造型":"1111(1,1,1,1,1,0)","能力编号":"1002","数量":"5","技能":(1111,1122,1131,),"站位":(2,3,6,7,10,)},
			{"类型":0,"名称":"蜀山弟子","造型":"1121(1,1,1,1,1,0)","能力编号":"1002","数量":"4","技能":(1112,1121,1132,),"站位":(4,5,8,9,)},
		),
		1002:(
			{"类型":0,"名称":"唐门弟子","造型":"1211(1,1,1,1,1,0)","能力编号":"1003","数量":"4","技能":(1212,1221,1232,),"站位":(4,5,8,9,)},
			{"类型":0,"名称":"唐门弟子","造型":"1211(1,1,1,1,1,0)","能力编号":"1003","数量":"5","技能":(1211,1222,1231,),"站位":(2,3,6,7,10,)},
		),
		1003:(
			{"类型":0,"名称":"武林盟弟子","造型":"1321(1,1,1,1,1,0)","能力编号":"1004","数量":"5","技能":(1312,1321,1332,),"站位":(2,3,6,7,10,)},
			{"类型":0,"名称":"武林盟弟子","造型":"1321(1,1,1,1,1,0)","能力编号":"1004","数量":"4","技能":(1311,1322,1331,),"站位":(4,5,8,9,)},
		),
		1004:(
			{"类型":0,"名称":"苗疆弟子","造型":"1411(1,1,1,1,1,0)","能力编号":"1005","数量":"4","技能":(1412,1421,1432,),"站位":(4,5,8,9,)},
			{"类型":0,"名称":"苗疆弟子","造型":"1411(1,1,1,1,1,0)","能力编号":"1005","数量":"5","技能":(1411,1422,1431,),"站位":(2,3,6,7,10,)},
		),
		1005:(
			{"类型":0,"名称":"魔宫弟子","造型":"1521(1,1,1,1,1,0)","能力编号":"1006","数量":"5","技能":(1511,1522,1531,),"站位":(2,3,6,7,10,)},
			{"类型":0,"名称":"魔宫弟子","造型":"1521(1,1,1,1,1,0)","能力编号":"1006","数量":"4","技能":(1512,1521,1532,),"站位":(4,5,8,9,)},
		),
		1006:(
			{"类型":0,"名称":"佛门弟子","造型":"1621(1,1,1,1,1,1)","能力编号":"1007","数量":"4","技能":(1611,1622,1631,),"站位":(4,5,8,9,)},
			{"类型":0,"名称":"佛门弟子","造型":"1621(1,1,1,1,1,1)","能力编号":"1007","数量":"5","技能":(1612,1621,1632,),"站位":(2,3,6,7,10,)},
		),
	}

	ableInfo = {
		1001:{"等级":"ALV","生命":"B*2","真气":"B*1","物理伤害":"B*1","法术伤害":"B*1","物理防御":"B*1","法术防御":"B*1","速度":"B*1.5","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1002:{"等级":"ALV","生命":"B*0.8","真气":"B*1","物理伤害":"B*0.6","法术伤害":"B*0.6","物理防御":"B*0.6","法术防御":"B*0.6","速度":"B*0.6"},
		1003:{"等级":"ALV","生命":"B*0.8","真气":"B*1","物理伤害":"B*0.4","法术伤害":"B*0.4","物理防御":"B*1","法术防御":"B*1","速度":"B*1"},
		1004:{"等级":"ALV","生命":"B*0.8","真气":"B*1","物理伤害":"B*0.6","法术伤害":"B*0.6","物理防御":"B*0.6","法术防御":"B*0.6","速度":"B*0.6"},
		1005:{"等级":"ALV","生命":"B*0.8","真气":"B*1","物理伤害":"B*0.4","法术伤害":"B*0.4","物理防御":"B*1","法术防御":"B*1","速度":"B*1"},
		1006:{"等级":"ALV","生命":"B*0.8","真气":"B*1","物理伤害":"B*0.6","法术伤害":"B*0.6","物理防御":"B*0.6","法术防御":"B*0.6","速度":"B*0.6"},
		1007:{"等级":"ALV","生命":"B*0.8","真气":"B*1","物理伤害":"B*0.4","法术伤害":"B*0.4","物理防御":"B*1","法术防御":"B*1","速度":"B*1"},
	}

	lineupInfo = {
	}

	configInfo = {
		"生成路径":"schoolFight",
	}
#导表结束

	def setup(self, who):#override
		'''配置
		'''
		pass

	def getTime(self):
		actObj = activity.schoolFight.getActivity()
		surplusTime = actObj.getSurplusTime()
		return surplusTime

	def getIntro(self, who):
		npcObj = self.getTargetNpc()
		mapName = scene.getScene(npcObj.sceneId).name
		content = self.intro
		content = content.replace("$target", npcObj.name)
		return content

	def getDetail(self, who):
		npcObj = self.getTargetNpc()
		mapName = scene.getScene(npcObj.sceneId).name
		content = self.detail
		content = content.replace("$map", mapName)
		content = content.replace("$target", npcObj.name)
		return content

	def teamCheck(self, who, npcObj):
		actObj = activity.schoolFight.getActivity()
		teamObj = who.getTeamObj()
		if not teamObj or not teamObj.isLeader(who.id):
			npcObj.say(who, "只有队长才能接取任务。")
			return False
		elif teamObj.leaveList:
			npcObj.say(who, actObj.getText(1003))
			return False
		elif not who.validInTeamSize(3):
			npcObj.say(who, actObj.getText(1002))
			return False
		return True

	def taskAddCheck(self, who, npcObj):
		'''任务接取条件判定
		'''
		if not self.teamCheck(who, npcObj):
			return False
		teamObj = who.getTeamObj()
		actObj = activity.schoolFight.getActivity()
		lLevelCheck = []
		lRingCheck = []
		for pid in teamObj.getInTeamList():
			obj = getRole(pid)
			if not obj:
				return False
			if obj.level < 40:
				lLevelCheck.append("#C09{}#n".format(obj.name))
		if lLevelCheck:
			npcObj.say(who, actObj.getText(1004))
			return False
		return True

	def customEvent(self, who, npcObj, eventName, *args):
		m = re.match("check(\S+)", eventName)
		if m:
			subEvent = m.group(1)
			myGreenlet.cGreenlet.spawn(self.handleCheck, who.id, npcObj.id, subEvent)

	def handleCheck(self, pid, npcId, eventName):
		who = getRole(pid)
		if not who:
			return
		npcObj = getNpc(npcId)
		if not npcObj:
			return
		if not self.teamCheck(who, npcObj):
			return
		self.doScript(who, npcObj, eventName)

	def onStartWar(self, w):
		if w.side == TEAM_SIDE_2 and w.monsterType == MONSTER_TYPE_BOSS:
			w.war.say(w, "六门派弟子即将登场，准备好接受挑战吧！")

	def onAddWarrior(self, w):
		if w.side == TEAM_SIDE_2 and w.monsterType == MONSTER_TYPE_BOSS:
			w.addFunc("onNewRound", onNewRoundForSummon)
			w.addApply("速度", 99999)
			w.addApply("物理躲闪率", 100)
			w.addApply("法术躲闪率", 100)
			w.addApply("隐身", 100)

	def customEscapeRatio(self, w):
		'''自定义逃跑成功率
		'''
		if w.side == TEAM_SIDE_2 and w.monsterType == MONSTER_TYPE_BOSS:
			return 100
		return None

	def transString(self, content, pid=0):
		'''转化字符串
		'''
		if "$number" in content:
			content = content.replace("$number", str(self.fetch("wave")))
		if "$time" in content:
			content = content.replace("$time", formatTime(self.fetch("warTime")))
		if "$map" in content:
			npcObj = self.getTargetNpc()
			mapName = scene.getScene(npcObj.sceneId).name
			content = content.replace("$map", mapName)
		if "$chat" in content:
			npcObj = self.getTargetNpc()
			content = content.replace("$chat", npcObj.getChat())
		return customTask.transString(self, content, pid)

	def customCheckBoutLimit(self, warObj):
		if warObj.bout >= 99:
			warObj.isEnd = True
			warObj.winner = TEAM_SIDE_2
		return True

	def setupWar(self, warObj, who, npcObj):
		'''战斗设置
		'''
		warObj.noLost = True
		warObj.autoFight = False

	def warWin(self, warObj, npcObj, warriorList):
		'''战斗胜利
		'''
		self.set("warTime", warObj.calTime())
		self.recordTime()
		for w in warriorList:
			if not w.isRole():
				continue
			who = getRole(w.id)
			if not who:
				continue
			if not self.inGame(who):
				continue

			self.onWarWin(warObj, npcObj, w)

	def warFail(self, warObj, npcObj, warriorList):
		'''战斗失败
		'''
		self.add("wave", -1)
		for w in warriorList:
			if w.isRole():
				self.onWarFail(warObj, npcObj, w)
		self.delete("wave")
		self.delete("passSchool")
		self.delete("curSchool")

	def onWarWin(self, warObj, npcObj, w):
		'''战斗胜利时
		'''
		who = getRole(w.id)
		if who and npcObj:
			self.waveBonus(who, npcObj, self.fetch("wave"))
			self.doEventScript(who, npcObj, "成功")

	def onWarFail(self, warObj, npcObj, w):
		'''战斗失败时
		'''
		who = getRole(w.id)
		if who and npcObj:
			self.waveBonus(who, npcObj, self.fetch("wave"))
			actObj = activity.schoolFight.getActivity()
			if actObj.state == 0:
				self.doScript(who, npcObj, "DONE")
			else:
				self.doEventScript(who, npcObj, "失败")

	def onEscaped(self, warObj, npcObj, w):
		'''逃跑成功时
		'''
		who = getRole(w.id)
		if who and npcObj:
			self.waveBonus(who, npcObj, self.fetch("wave")-1)
			txt = self.chatInfo.get(1008, "")
			txt = txt.replace("$number", str(self.fetch("wave")-1))
			npcObj.say(who, txt)

	def schoolBuffBonus(self, warObj):
		'''通关门派BUFF奖励
		'''
		if warObj.bout == 1:
			return
		passed = self.fetch("passSchool", [])
		cur = self.fetch("curSchool")
		if cur not in passed:
			passed.append(cur)
			self.set("passSchool", passed)
		for _w in warObj.teamList[TEAM_SIDE_1].values():
			if not _w.isLineupEye():
				_w.addHP(_w.getHPMax()*0.1)
				_w.addMP(_w.getMPMax()*0.1)
			if not _w.isRole():
				continue
			who = getRole(_w.getPID())
			if not who:
				continue
			if who.school == self.fetch("curSchool"):
				bonus = buffBonus.get(who.school)
				buff.addOrReplace(_w, bonus[1], 99)

	def waveBonus(self, who, npcObj, w):
		wb = who.day.fetch("schoolFightWB")
		if wb >= w:
			return
		for i in xrange(wb, w):
			idx = 1001 + i
			self.doScript(who, npcObj, "R{}".format(idx))
		if not who.day.fetch("schoolFightWB"):
			who.addActPoint(20)
		who.day.set("schoolFightWB", w)

	def recordTime(self):
		'''记录完成时间
		'''
		nameList = []
		idList = []
		for roleObj in self.getRoleList():
			nameList.append(roleObj.name)
			idList.append(roleObj.id)
		record = "、".join(nameList)
		actObj = activity.schoolFight.getActivity()
		actObj.recordTime(idList, self.fetch("warTime"))

	def inGame(self, who):
		'''是否在活动或任务中
		'''
		return 1


def onNewRoundForSummon(w):
	'''回合前设置召唤指令
	'''
	warObj = w.war
	gameObj = warObj.game
	side = w.side
	isEscape = False
	if len(warObj.teamList[side]) == 1:
		if gameObj.fetch("wave") < 6:
			gameObj.schoolBuffBonus(warObj)
			war.commands.setCommand(warObj, w, CMD_TYPE_SUMMON)
			w.addFunc("onCommand", onCommandForSummon)
		else:
			war.commands.setCommand(warObj, w, CMD_TYPE_ESCAPE)
	else:
		war.commands.setCommand(warObj, w, CMD_TYPE_DEFEND)

def onCommandForSummon(w):
	warObj = w.war
	gameObj = warObj.game
	passed = gameObj.fetch("passSchool", [])
	surplus = list(set(schoolGroups) - set(passed))
	fightIdx = 1000 + surplus[rand(len(surplus))] % 10
	warObj.say(w, schoolWords[fightIdx])
	fightList = gameObj.getFightInfo(fightIdx)
	ableData, lineupData = gameObj.getAbleInfo(), gameObj.getLineupInfo()
	who = gameObj.getOwnerObj()
	monsterList = war.warctrl.createMonsterList(who, fightIdx, fightList, ableData, lineupData)
	for monsterObj in monsterList.get(MONSTER_TYPE_NORMAL, []):
		monsterW = warObj.addMonsterFight(monsterObj, TEAM_SIDE_2)
		warObj.rpcAddWarrior(monsterW, None)
		warObj.rpcWarAllBuff(monsterW)
	w.removeFunc("onCommand")
	gameObj.add("wave", 1)
	gameObj.set("curSchool", fightIdx % 1000 + 10)

schoolGroups = [11, 12, 13, 14, 15, 16]
fightGroups = [1001, 1002, 1003, 1004, 1005, 1006]

schoolWords = {
1001: "蜀山弟子",
1002: "唐门弟子",
1003: "武林盟弟子",
1004: "苗疆弟子",
1005: "魔宫弟子",
1006: "佛门弟子",
}

buffBonus = {
11: ("物理伤害加成", 508),
12: ("抵抗封印加成", 509),
13: ("物理伤害加成", 510),
14: ("封印命中加成", 511),
15: ("法术伤害加成", 512),
16: ("治疗强度加成", 513),
}


import re
from common import *
import activity.schoolFight
import myGreenlet
from war.defines import *
import war.warctrl
import scene
import buff
