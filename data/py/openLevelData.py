#-*-coding:utf-8-*-
#作者:叶伟龙@龙川县赤光镇
#导表开始
gdData={
	50:{"开启等级":3,"开启天数":1},
	60:{"开启等级":3,"开启天数":1},
	70:{"开启等级":2,"开启天数":2},
	75:{"开启等级":2,"开启天数":4},
	80:{"开启等级":1,"开启天数":6},
	85:{"开启等级":1,"开启天数":8},
	90:{"开启等级":1,"开启天数":10},
	95:{"开启等级":1,"开启天数":12},
	100:{"开启等级":1,"开启天数":14},
}
#导表结束


def getConfig(level,key):
	levelData = findSort.getLeftValue(level,gdData)
	return levelData[key]

import findSort