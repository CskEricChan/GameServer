#-*-coding:utf-8-*-
#作者:叶伟龙@龙川县赤光镇
#导表开始
gdData={
	1:{"活动名称":"降魔任务","经验公式":lambda LV,R:LV*2*R+LV*10+1100,"每轮次数":10,"轮数":8,"转化率":0.4},
	2:{"活动名称":"师门任务","经验公式":lambda LV,R:(LV*32+40)*R+LV*400+1000,"每轮次数":10,"轮数":2,"转化率":0.4},
	4:{"活动名称":"封妖","经验公式":lambda LV:LV*300+1500,"次数":10,"转化率":0.4},
	5:{"活动名称":"单人竞技场","经验公式":lambda LV:LV*360+700,"次数":5,"转化率":0.4},
	11:{"活动名称":"每日答题","经验公式":lambda LV:LV*38+8000,"次数":10,"转化率":0.4},
	16:{"活动名称":"竹林除妖","经验公式":lambda LV:LV*1850+20000,"次数":1,"转化率":0.4},
	17:{"活动名称":"天问初试","经验公式":lambda LV,N:3500+(10+N*5)*LV,"每轮次数":20,"轮数":1,"转化率":0.4},
	21:{"活动名称":"仙盟大战","经验公式":lambda LV:LV*625+6250,"次数":1,"转化率":0.4},
	22:{"活动名称":"幻波池","经验公式":lambda LV:LV*2400+30000,"次数":1,"转化率":0.4},
	23:{"活动名称":"邪道煞星","经验公式":lambda LV:LV*1000+20000,"次数":3,"转化率":0.4},
	24:{"活动名称":"组队竞技场","经验公式":lambda LV:LV*600+60000,"次数":1,"转化率":0.4},
	26:{"活动名称":"北斗七星","经验公式":lambda LV:LV*272+24000,"次数":7,"转化率":0.4},
	27:{"活动名称":"五岳帝君","经验公式":lambda LV:LV*500+25000,"次数":5,"转化率":0.4},
	102:{"活动名称":"魔教入侵","经验公式":lambda LV:LV*85+900,"次数":10,"转化率":0.4},
	25:{"活动名称":"门派试炼","经验公式":lambda LV:LV*2037+52500,"次数":1,"转化率":0.4},
	28:{"活动名称":"仙盟迷宫","经验公式":lambda LV:LV*500+45000,"次数":1,"转化率":0.4},
}
#导表结束