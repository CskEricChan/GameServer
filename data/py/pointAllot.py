#-*-coding:utf-8-*-
#作者:马昭@曹县闫店楼镇

def getPointInfo(iSchool):
	return gdData.get(iSchool,{})

#导表开始
gdData={
	11:{"体质":1,"魔力":0,"力量":3,"耐力":1,"精神":0,"敏捷":0},
	12:{"体质":1,"魔力":3,"力量":0,"耐力":0,"精神":1,"敏捷":0},
	13:{"体质":1,"魔力":0,"力量":3,"耐力":1,"精神":0,"敏捷":0},
	14:{"体质":1,"魔力":3,"力量":0,"耐力":0,"精神":1,"敏捷":0},
	15:{"体质":1,"魔力":3,"力量":0,"耐力":0,"精神":1,"敏捷":0},
	16:{"体质":1,"魔力":3,"力量":0,"耐力":0,"精神":1,"敏捷":0},
}
#导表结束