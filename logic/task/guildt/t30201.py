# -*- coding: utf-8 -*-
from task.defines import *
from task.object import Task as customTask

MAX_RING = 10 # 每轮最大环数

#导表开始
class Task(customTask):
	parentId = 30201
	targetType = TASK_TARGET_TYPE_NPC
	icon = 0
	title = '''仙盟-扶老济贫'''
	intro = '''前往看望$target'''
	detail = '''我们仙盟素有扶老济贫的传统，你去看望一下$target,看看是否缺衣少食。'''
	rewardDesc = ''''''
	goAheadScript = ''''''
	initScript = '''E(9001,1001)'''

	npcInfo = {
		1001:{"名称":"飞贼","造型":"4502(0,1,0,0,0,0)","位置":"1130,0,0,0"},
		1002:{"名称":"飞贼","造型":"4504(0,1,0,0,0,0)","位置":"1130,0,0,0"},
		1003:{"名称":"恶人陈长泰","造型":"4504(0,1,0,0,0,0)","位置":"1040,0,0,0"},
		1004:{"名称":"恶人黎半风","造型":"4502(0,1,0,0,0,0)","位置":"1020,0,0,0"},
		1005:{"名称":"恶人罗文林","造型":"4502(0,1,0,0,0,0)","位置":"1040,0,0,0"},
		1006:{"名称":"恶人萨若耶","造型":"4502(0,1,0,0,0,0)","位置":"2040,0,0,0"},
		1007:{"名称":"恶人司马寿","造型":"4504(0,1,0,0,0,0)","位置":"1130,0,0,0"},
		1008:{"名称":"恶人朱赤午","造型":"4502(0,1,0,0,0,0)","位置":"1130,0,0,0"},
		1009:{"名称":"恶人马庚仙","造型":"4506(0,1,0,0,0,0)","位置":"1040,0,0,0"},
		1010:{"名称":"恶人倪兰心","造型":"4508(0,1,0,0,0,0)","位置":"1030,0,0,0"},
		1011:{"名称":"恶人施龙姑","造型":"4509(0,1,0,0,0,0)","位置":"1130,0,0,0"},
		1012:{"名称":"杂草","造型":"8003(0,1,0,0,0,0)","位置":"guild,0,0,0","动作":5},
		1013:{"名称":"杂草","造型":"8003(0,1,0,0,0,0)","位置":"guild,0,0,0","动作":5},
		1014:{"名称":"杂草","造型":"8003(0,1,0,0,0,0)","位置":"guild,0,0,0","动作":5},
	}

	eventInfo = {
		1001:{"点击":"DONE,DEFF,R1001,D9002"},
		1002:{"点击":"POPI","成功":"DONE,DEFF,R1003,D1008","失败":"D1007"},
		1003:{"点击":"F1001","成功":"DONE,DEFF,R1001,D1009"},
		1004:{"点击":"SB1004","回复":"1:E(0,2001),F9004"},
		1005:{"点击":"""PB("除草中",0,1,1)""","成功":"DONE,DEFF,R1001"},
		1006:{"点击":"F9004","成功":"DONE,DEFF,R1001,D1012","失败":"D1013"},
		2001:{"点击":"F9004","成功":"DONE,T(30209,2004)","失败":"E(0,1004),D1011"},
		2002:{"点击":"R1001,DONE,DEFF,D1014"},
		2003:{"点击":"DONE,DEFF,R1001"},
		2004:{"点击":"E(101,2002)"},
		1008:{"点击":"POPI","成功":"DONE,DEFF,R1003,D1008","失败":"D1007"},
	}

	rewardInfo = {
		1001:{"经验":lambda LV,R:LV*R*11+LV*42+500,"宠物经验":lambda PLV:PLV*100,"物品":[1001,1002]},
		1002:{"物品":[1003]},
		1003:{"经验":lambda :1000,"宠物经验":lambda :1000,"银币":lambda :1000},
	}

	rewardPropsInfo = {
		1001:(
			{"权重":10,"物品":"200009","数量":lambda R:1+R},
		),
		1002:(
			{"权重":10,"物品":"200051","数量":lambda LV,R:(R+10)*(LV*5+100)},
		),
		1003:(
			{"权重":10,"物品":"200009","数量":lambda :5},
		),
	}

	groupInfo = {
		9001:(20201,20202,20203,),
		9002:(1005,1006,),
		9003:(1003,1004,1005,1006,1007,1008,1009,1010,1011,),
		9004:(1003,1004,1005,1006,),
		9005:(100000,100050,100100,100150,),
		9006:(100001,100051,100101,100151,),
		9007:(100002,100052,100102,100152,),
		9008:(100003,100053,100103,100153,),
		9009:(241004,241104,100004,100054,100104,100154,),
		9010:(241005,241105,100005,100055,100105,100155,),
		9011:((1130,79,77),(1130,63,84),(1130,34,43),(1130,163,64),),
		9012:(220002,220003,),
		9013:(220002,220003,),
		9014:(220002,220003,),
		9015:(220003,220004,),
		9016:(220004,220005,),
		9017:(220005,220006,),
	}

	chatInfo = {
		1001:'''仙盟中大小事务都是我在管理，实在是累得慌啊……要是有人替我分担就好了。\nQ仙盟任务\nQ打个招呼''',
		1002:'''欢迎加入#C02$union#n仙盟，[仙盟编号：#C02$id#n]$purpose，#C02[申请加入]#n''',
		1003:'''$player，你确认带来了仙盟所需物品？\n（请检查是否购买了道具，或把道具存入了仓库）''',
		1004:'''$union不过一群乌合之众，就没一个能让我看得上的对手——\nQ教训一番\nQ只是路过''',
		1005:'''*2*承蒙贵盟总管一直惦记着，幸好老天爷赏脸，也不至于沦落到生活无着的境况。''',
		1006:'''*2*替我谢过你们总管啦……你们都是好人。''',
		1007:'''*2*你并没带来我所要的东西。''',
		1008:'''*2*每人都应为仙盟出一分力，聚沙成塔，集腋成裘。''',
		1009:'''*2*哎呀……下手真狠，我把偷的东西还回来还不行么……''',
		1010:'''*2*哎呀……下手真狠，我把偷的东西还回来还不行么……''',
		1011:'''*2*嘿嘿，我可不会把到手的东西交出来的！''',
		1012:'''*2*不就是凭着师门长辈嘛！光欺负我们算什么好汉！''',
		1013:'''*2*嘿嘿，果然是没有长辈就派不上用场的家伙。''',
		1014:'''*2*做得好，不可让造谣的人坏了我们仙盟的名声。''',
		1015:'''*2*人心齐，泰山移，多一个人，就多一分力量。''',
		1016:'''*2*掐指一算，你剩余的仙盟任务还有$residues环，今日合共可完成$number环。''',
		1017:'''*2*领取仙盟任务需达到20级''',
	}

	branchInfo = {
		1001:(
			{"条件":0,"脚本":"L(9005,1)"},
			{"条件":10,"脚本":"L(9006,1)"},
			{"条件":20,"脚本":"L(9007,1)"},
			{"条件":30,"脚本":"L(9008,1)"},
			{"条件":40,"脚本":"L(9009,1)"},
			{"条件":50,"脚本":"L(9010,1)"},
		),
		1002:(
			{"条件":0,"脚本":"L(9012,1)"},
			{"条件":10,"脚本":"L(9013,1)"},
			{"条件":20,"脚本":"L(9014,1)"},
			{"条件":30,"脚本":"L(9015,1)"},
			{"条件":40,"脚本":"L(9016,1)"},
			{"条件":50,"脚本":"L(9017,1)"},
		),
	}

	fightInfo = {
		1001:(
			{"类型":1,"名称":"飞贼","造型":"4502(0,1,0,0,0,0)","能力编号":"1001","数量":"1","技能":(1112,1531,),"站位":(1,)},
			{"类型":0,"名称":"同伙","造型":"4504(0,1,0,0,0,0)","能力编号":"1002","数量":"2","技能":(5401,5402,5403,5404,5405,),"站位":(2,3,)},
			{"类型":0,"名称":"女贼","造型":"4506(0,1,0,0,0,0)","能力编号":"1003","数量":"2","技能":(5411,5412,5413,5414,5415,),"站位":(4,5,)},
		),
		1002:(
			{"类型":1,"名称":"飞贼","造型":"4502(0,1,0,0,0,0)","能力编号":"1001","数量":"1","技能":(1112,1531,),"站位":(1,)},
			{"类型":0,"名称":"同伙","造型":"4504(0,1,0,0,0,0)","能力编号":"1002","数量":"2","技能":(5401,5402,5403,5404,5405,),"站位":(2,3,)},
			{"类型":0,"名称":"女贼","造型":"4506(0,1,0,0,0,0)","能力编号":"1003","数量":"2","技能":(5411,5412,5413,5414,5415,),"站位":(4,5,)},
		),
		1003:(
			{"类型":1,"名称":"$npc","造型":"$npc","能力编号":"1001","数量":"1","技能":(1113,1533,),"站位":(1,)},
			{"类型":0,"名称":"男贼","造型":"4502(0,1,0,0,0,0)","能力编号":"1002","数量":"2","技能":(5401,),"站位":(2,3,)},
			{"类型":0,"名称":"小妖","造型":"4001(0,1,0,0,0,0)","能力编号":"1003","数量":"2","技能":(5411,),"站位":(4,5,)},
		),
		1004:(
			{"类型":1,"名称":"$npc","造型":"$npc","能力编号":"1001","数量":"1","技能":(1113,1533,),"站位":(1,)},
			{"类型":0,"名称":"帮凶","造型":"4504(0,1,0,0,0,0)","能力编号":"1002","数量":"2","技能":(5402,),"站位":(2,3,)},
			{"类型":0,"名称":"小贼","造型":"4001(0,1,0,0,0,0)","能力编号":"1003","数量":"2","技能":(5412,),"站位":(4,5,)},
		),
		1005:(
			{"类型":1,"名称":"$npc","造型":"$npc","能力编号":"1001","数量":"1","技能":(1113,1533,),"站位":(1,)},
			{"类型":0,"名称":"帮凶","造型":"4502(0,1,0,0,0,0)","能力编号":"1002","数量":"2","技能":(5403,),"站位":(2,3,)},
			{"类型":0,"名称":"恶徒","造型":"4506(0,1,0,0,0,0)","能力编号":"1003","数量":"2","技能":(5413,),"站位":(4,5,)},
		),
		1006:(
			{"类型":1,"名称":"$npc","造型":"$npc","能力编号":"1001","数量":"1","技能":(1113,1533,),"站位":(1,)},
			{"类型":0,"名称":"歹徒","造型":"4502(0,1,0,0,0,0)","能力编号":"1002","数量":"2","技能":(5404,),"站位":(2,3,)},
			{"类型":0,"名称":"御灵","造型":"4001(0,1,0,0,0,0)","能力编号":"1003","数量":"2","技能":(5414,),"站位":(4,5,)},
		),
	}

	ableInfo = {
		1001:{"等级":"LV+1","生命":"B*0.98","真气":"B*1","物理伤害":"B*0.81","法术伤害":"B*0.81","物理防御":"B*0.6","法术防御":"B*0.6","速度":"B*0.8","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1002:{"等级":"LV","生命":"B*0.75","真气":"B*1","物理伤害":"B*0.45","法术伤害":"B*0.65","物理防御":"B*0.39","法术防御":"B*0.56","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1003:{"等级":"LV","生命":"B*0.75","真气":"B*1","物理伤害":"B*0.65","法术伤害":"B*0.45","物理防御":"B*0.56","法术防御":"B*0.39","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
	}

	lineupInfo = {
	}

	configInfo = {
		"生成路径":"guildt",
	}

	ringTask = {
		0:(
			{"编号":30201,"权重":20},
			{"编号":30202,"权重":20},
			{"编号":30203,"权重":20},
			{"编号":30206,"权重":20},
			{"编号":30207,"权重":20},
		),
	}

	lastRingTask = {
		0:(
			{"编号":30204,"权重":50},
			{"编号":30205,"权重":50},
			{"编号":30208,"权重":40},
		),
	}
#导表结束

	def onBorn(self, who, npcObj, **kwargs):
		customTask.onBorn(self, who, npcObj, **kwargs)
		self.autoGoAhead(who)

	def canAbort(self):
		'''是否可以放弃任务
		'''
		return 1

	def getTitle(self, who):
		title = self.transString(self.title, who.id)
		return "%s#C07(%d/%d)#n" % (title, self.getRing(who), MAX_RING)

	def getHyperlinkIntro(self, who):
		content = self.getIntro(who)
		if "$process" in content:
			propsNeeded = self.getPropsNeeded()
			needCnt = sum(propsNeeded.values())
			ownCnt = sum(who.propsCtn.getPropsAmountByNos(*propsNeeded.keys()))
			content = content.replace("$process", "{}/{}".format(ownCnt, needCnt))
		return content

	def getRing(self, who):
		return who.taskCtn.fetch("guildRing") + 1

	def onMissionDone(self, who, npcObj):
		ring = who.taskCtn.add("guildRing", 1)
		dayRing = who.day.add("guildRing", 1)
		weekRing = who.week.add("guildRing", 1)
		if who.day.fetch("guildRing") <= 20:
			who.addActPoint(1)

		if ring == 10:  # 第10环额外奖励
			who.taskCtn.delete("guildRing")
		if not task.guildt.canTakeGuildTask(who):
			return
		# 自动给任务
		if ring == 9:
			taskObj = task.guildt.randGuildTask(who, npcObj, True)
		else:
			taskObj = task.guildt.randGuildTask(who, npcObj)

	def getBranchCondition(self, who, npcObj, branchIdx, flag):
		if flag == "lv":
			lst = [info["条件"] for info in self.getBranchInfo(branchIdx)]
			lst.sort(reverse=True)
			for lv in lst:
				if who.level >= lv:
					return lv
			
		return customTask.getBranchCondition(self, who, npcObj, branchIdx, flag)			

	def completeTakeProps(self, who, npcObj, propsList=None):
		'''上交物品成功
		'''
		#物品品质
		needQu = self.fetch("propsQu", 0)
		if needQu and propsList:
			propsQuality = getattr(propsList[0], "quality", 0)
			if propsQuality >= needQu:
				self.propsQuality = propsQuality

		customTask.completeTakeProps(self, who, npcObj, propsList)

	def setQuality(self, who, npcObj, args):
		'''设置品质
		'''
		if args:
			propsNeedQuality = int(args[0])
			self.set("propsQu", propsNeedQuality)

	def getValueByVarName(self, varName, who):
		if varName == "R":
			if who:
				ring = who.taskCtn.fetch("guildRing") % 10
				return ring if ring else 10
			return 0
		return customTask.getValueByVarName(self, varName, who)

	def getNpcByIdx(self, npcIdx):
		'''根据npc导表编号获取npc
		'''
		if npcIdx == 101:
			who = self.getOwnerObj()
			if who:
				guildObj = who.getGuildObj()
				if not guildObj:
					return None
				return guildObj.getNpcByType("总管")
			return npcIdx
		for lst in self.npcList.itervalues():
			for npcObj in lst:
				if npcObj.idx == npcIdx:
					return npcObj
		return None

	def transString(self, content, pid=0):
		'''转化字符串
		'''
		who = None
		if pid:
			who = getRole(pid)
		if who:
			guildObj = who.getGuildObj()
			if "$union" in content:
				content = content.replace("$union", guildObj.name)
		return customTask.transString(self, content)


from common import *
import re
import task
import task.guildt
import message
import scene
import launch
import npc
