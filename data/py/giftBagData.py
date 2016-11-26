#-*-coding:utf-8-*-
#作者:马昭@曹县闫店楼镇
def getBagData(bagNo):
	if bagNo not in gdGiftBag:
		raise PlannerError,'没有编号为{}的礼包'.format(bagNo)
	return gdGiftBag[bagNo]

def getBranchData(branchNo):
	if branchNo not in gdBranch:
		raise PlannerError,'没有编号为{}的礼包分支'.format(branchNo)
	return gdBranch[branchNo]
def getGemBagData(gemNo):
	if gemNo not in gdgembag:
		raise PlannerError,'没有编号为{}的宝石礼包分支'.format(gemNo)
	return gdgembag[gemNo]

#导表开始
gdGiftBag={
	201001:(
		{"物品":201002,"数量":1,"绑定":1},
		{"物品":221401,"数量":1,"绑定":1},
		{"物品":221403,"数量":1,"绑定":1},
		{"物品":200001,"数量":100000,"绑定":1},
		{"物品":200002,"数量":1000,"绑定":1},
	),
	201002:(
		{"物品":201003,"数量":1,"绑定":1},
		{"物品":101,"条件类型":"造型","数量":1,"绑定":1},
		{"物品":102,"条件类型":"性别","数量":1,"绑定":1},
		{"物品":103,"条件类型":"性别","数量":1,"绑定":1},
		{"物品":101401,"数量":1,"绑定":1,"效果":{"抵抗封印":60,"法术防御":10,"真气上限":55,"打造":1}},
		{"物品":101501,"数量":1,"绑定":1,"效果":{"速度":17,"生命上限":64,"打造":1}},
		{"物品":101601,"数量":1,"绑定":1,"效果":{"法术防御":10,"速度":17,"打造":1}},
		{"物品":200001,"数量":300000,"绑定":1},
		{"物品":200002,"数量":3000,"绑定":1},
	),
	201003:(
		{"物品":201004,"数量":1,"绑定":1},
		{"物品":200001,"数量":600000,"绑定":1},
		{"物品":200002,"数量":6000,"绑定":1},
		{"物品":221401,"数量":2,"绑定":1},
		{"物品":221403,"数量":2,"绑定":1},
		{"物品":230101,"数量":10,"绑定":1},
		{"物品":230102,"数量":10,"绑定":1},
	),
	201004:(
		{"物品":201005,"数量":1,"绑定":1},
		{"物品":201,"条件类型":"造型","数量":1,"绑定":1},
		{"物品":202,"条件类型":"性别","数量":1,"绑定":1},
		{"物品":203,"条件类型":"性别","数量":1,"绑定":1},
		{"物品":101402,"数量":1,"绑定":1,"效果":{"抵抗封印":90,"法术防御":16,"真气上限":95,"打造":1}},
		{"物品":101502,"数量":1,"绑定":1,"效果":{"速度":25,"生命上限":96,"打造":1}},
		{"物品":101602,"数量":1,"绑定":1,"效果":{"法术防御":16,"速度":25,"打造":1}},
		{"物品":200001,"数量":1000000,"绑定":1},
		{"物品":200002,"数量":10000,"绑定":1},
		{"物品":230001,"数量":5,"绑定":1},
	),
	201005:(
		{"物品":201006,"数量":1,"绑定":1},
		{"物品":301,"条件类型":"造型","数量":1,"绑定":1},
		{"物品":302,"条件类型":"性别","数量":1,"绑定":1},
		{"物品":303,"条件类型":"性别","数量":1,"绑定":1},
		{"物品":101403,"数量":1,"绑定":1,"效果":{"抵抗封印":120,"法术防御":23,"真气上限":135,"打造":1}},
		{"物品":101503,"数量":1,"绑定":1,"效果":{"速度":32,"生命上限":128,"打造":1}},
		{"物品":101603,"数量":1,"绑定":1,"效果":{"法术防御":23,"速度":32,"打造":1}},
		{"物品":200001,"数量":1500000,"绑定":1},
		{"物品":200002,"数量":15000,"绑定":1},
		{"物品":221402,"数量":1,"绑定":1},
		{"物品":221404,"数量":1,"绑定":1},
		{"物品":202043,"数量":10,"绑定":1},
		{"物品":202044,"数量":10,"绑定":1},
		{"物品":202045,"数量":10,"绑定":1},
	),
	201006:(
		{"物品":201007,"数量":1,"绑定":1},
		{"物品":401,"条件类型":"造型","数量":1,"绑定":1},
		{"物品":402,"条件类型":"性别","数量":1,"绑定":1},
		{"物品":403,"条件类型":"性别","数量":1,"绑定":1},
		{"物品":101404,"数量":1,"绑定":1,"效果":{"抵抗封印":150,"法术防御":29,"真气上限":175,"打造":1}},
		{"物品":101504,"数量":1,"绑定":1,"效果":{"速度":40,"生命上限":160,"打造":1}},
		{"物品":101604,"数量":1,"绑定":1,"效果":{"法术防御":29,"速度":40,"打造":1}},
		{"物品":200001,"数量":2000000,"绑定":1},
		{"物品":200002,"数量":20000,"绑定":1},
		{"物品":221402,"数量":1,"绑定":1},
		{"物品":221404,"数量":1,"绑定":1},
		{"物品":245001,"数量":40,"绑定":1},
	),
	201007:(
		{"物品":201008,"数量":1,"绑定":1},
		{"物品":501,"条件类型":"造型","数量":1,"绑定":1},
		{"物品":502,"条件类型":"性别","数量":1,"绑定":1},
		{"物品":503,"条件类型":"性别","数量":1,"绑定":1},
		{"物品":101405,"数量":1,"绑定":1,"效果":{"抵抗封印":180,"法术防御":36,"真气上限":215,"打造":1}},
		{"物品":101505,"数量":1,"绑定":1,"效果":{"速度":48,"生命上限":192,"打造":1}},
		{"物品":101605,"数量":1,"绑定":1,"效果":{"法术防御":36,"速度":48,"打造":1}},
		{"物品":200001,"数量":2500000,"绑定":1},
		{"物品":200002,"数量":25000,"绑定":1},
		{"物品":221402,"数量":1,"绑定":1},
		{"物品":221404,"数量":1,"绑定":1},
		{"物品":245001,"数量":50,"绑定":1},
		{"物品":202024,"数量":10,"绑定":1},
		{"物品":202025,"数量":10,"绑定":1},
	),
	201008:(
		{"物品":601,"条件类型":"造型","数量":6,"绑定":1},
		{"物品":241306,"数量":6,"绑定":1},
		{"物品":245001,"数量":60,"绑定":1},
		{"物品":200001,"数量":3000000,"绑定":1},
		{"物品":200002,"数量":30000,"绑定":1},
	),
}

gdBranch={
	101:(
		{"条件":1111,"物品":100001,"效果":{"物理伤害":94,"法术伤害":94,"治疗强度":47,"封印命中":120,"力量":8,"打造":1}},
		{"条件":1121,"物品":100051,"效果":{"物理伤害":94,"法术伤害":94,"治疗强度":47,"封印命中":120,"力量":8,"打造":1}},
		{"条件":1211,"物品":100101,"效果":{"物理伤害":94,"法术伤害":94,"治疗强度":47,"封印命中":120,"法力":8,"打造":1}},
		{"条件":1221,"物品":100151,"效果":{"物理伤害":94,"法术伤害":94,"治疗强度":47,"封印命中":120,"法力":8,"打造":1}},
		{"条件":1311,"物品":100201,"效果":{"物理伤害":94,"法术伤害":94,"治疗强度":47,"封印命中":120,"力量":8,"打造":1}},
		{"条件":1321,"物品":100251,"效果":{"物理伤害":94,"法术伤害":94,"治疗强度":47,"封印命中":120,"力量":8,"打造":1}},
		{"条件":1411,"物品":100301,"效果":{"物理伤害":94,"法术伤害":94,"治疗强度":47,"封印命中":120,"法力":8,"打造":1}},
		{"条件":1421,"物品":100351,"效果":{"物理伤害":94,"法术伤害":94,"治疗强度":47,"封印命中":120,"法力":8,"打造":1}},
		{"条件":1511,"物品":100401,"效果":{"物理伤害":94,"法术伤害":94,"治疗强度":47,"封印命中":120,"法力":8,"打造":1}},
		{"条件":1521,"物品":100451,"效果":{"物理伤害":94,"法术伤害":94,"治疗强度":47,"封印命中":120,"法力":8,"打造":1}},
		{"条件":1611,"物品":100501,"效果":{"物理伤害":94,"法术伤害":94,"治疗强度":47,"封印命中":120,"法力":8,"打造":1}},
		{"条件":1621,"物品":100551,"效果":{"物理伤害":94,"法术伤害":94,"治疗强度":47,"封印命中":120,"法力":8,"打造":1}},
	),
	102:(
		{"条件":1,"物品":101001,"效果":{"抵抗封印":60,"物理防御":10,"真气上限":55,"打造":1}},
		{"条件":2,"物品":101101,"效果":{"抵抗封印":60,"物理防御":10,"真气上限":55,"打造":1}},
	),
	103:(
		{"条件":1,"物品":101201,"效果":{"物理防御":10,"生命上限":64,"体质":8,"打造":1}},
		{"条件":2,"物品":101301,"效果":{"物理防御":10,"生命上限":64,"体质":8,"打造":1}},
	),
	201:(
		{"条件":1111,"物品":100002,"效果":{"物理伤害":158,"法术伤害":158,"治疗强度":79,"封印命中":180,"力量":11,"打造":1}},
		{"条件":1121,"物品":100052,"效果":{"物理伤害":158,"法术伤害":158,"治疗强度":79,"封印命中":180,"力量":11,"打造":1}},
		{"条件":1211,"物品":100102,"效果":{"物理伤害":158,"法术伤害":158,"治疗强度":79,"封印命中":180,"法力":11,"打造":1}},
		{"条件":1221,"物品":100152,"效果":{"物理伤害":158,"法术伤害":158,"治疗强度":79,"封印命中":180,"法力":11,"打造":1}},
		{"条件":1311,"物品":100202,"效果":{"物理伤害":158,"法术伤害":158,"治疗强度":79,"封印命中":180,"力量":11,"打造":1}},
		{"条件":1321,"物品":100252,"效果":{"物理伤害":158,"法术伤害":158,"治疗强度":79,"封印命中":180,"力量":11,"打造":1}},
		{"条件":1411,"物品":100302,"效果":{"物理伤害":158,"法术伤害":158,"治疗强度":79,"封印命中":180,"法力":11,"打造":1}},
		{"条件":1421,"物品":100352,"效果":{"物理伤害":158,"法术伤害":158,"治疗强度":79,"封印命中":180,"法力":11,"打造":1}},
		{"条件":1511,"物品":100402,"效果":{"物理伤害":158,"法术伤害":158,"治疗强度":79,"封印命中":180,"法力":11,"打造":1}},
		{"条件":1521,"物品":100452,"效果":{"物理伤害":158,"法术伤害":158,"治疗强度":79,"封印命中":180,"法力":11,"打造":1}},
		{"条件":1611,"物品":100502,"效果":{"物理伤害":158,"法术伤害":158,"治疗强度":79,"封印命中":180,"法力":11,"打造":1}},
		{"条件":1621,"物品":100552,"效果":{"物理伤害":158,"法术伤害":158,"治疗强度":79,"封印命中":180,"法力":11,"打造":1}},
	),
	202:(
		{"条件":1,"物品":101002,"效果":{"抵抗封印":90,"物理防御":16,"真气上限":95,"打造":1}},
		{"条件":2,"物品":101102,"效果":{"抵抗封印":90,"物理防御":16,"真气上限":95,"打造":1}},
	),
	203:(
		{"条件":1,"物品":101202,"效果":{"物理防御":16,"生命上限":96,"体质":11,"打造":1}},
		{"条件":2,"物品":101302,"效果":{"物理防御":16,"生命上限":96,"体质":11,"打造":1}},
	),
	301:(
		{"条件":1111,"物品":100003,"效果":{"物理伤害":222,"法术伤害":222,"治疗强度":111,"封印命中":240,"力量":14,"打造":1}},
		{"条件":1121,"物品":100053,"效果":{"物理伤害":222,"法术伤害":222,"治疗强度":111,"封印命中":240,"力量":14,"打造":1}},
		{"条件":1211,"物品":100103,"效果":{"物理伤害":222,"法术伤害":222,"治疗强度":111,"封印命中":240,"法力":14,"打造":1}},
		{"条件":1221,"物品":100153,"效果":{"物理伤害":222,"法术伤害":222,"治疗强度":111,"封印命中":240,"法力":14,"打造":1}},
		{"条件":1311,"物品":100203,"效果":{"物理伤害":222,"法术伤害":222,"治疗强度":111,"封印命中":240,"力量":14,"打造":1}},
		{"条件":1321,"物品":100253,"效果":{"物理伤害":222,"法术伤害":222,"治疗强度":111,"封印命中":240,"力量":14,"打造":1}},
		{"条件":1411,"物品":100303,"效果":{"物理伤害":222,"法术伤害":222,"治疗强度":111,"封印命中":240,"法力":14,"打造":1}},
		{"条件":1421,"物品":100353,"效果":{"物理伤害":222,"法术伤害":222,"治疗强度":111,"封印命中":240,"法力":14,"打造":1}},
		{"条件":1511,"物品":100403,"效果":{"物理伤害":222,"法术伤害":222,"治疗强度":111,"封印命中":240,"法力":14,"打造":1}},
		{"条件":1521,"物品":100453,"效果":{"物理伤害":222,"法术伤害":222,"治疗强度":111,"封印命中":240,"法力":14,"打造":1}},
		{"条件":1611,"物品":100503,"效果":{"物理伤害":222,"法术伤害":222,"治疗强度":111,"封印命中":240,"法力":14,"打造":1}},
		{"条件":1621,"物品":100553,"效果":{"物理伤害":222,"法术伤害":222,"治疗强度":111,"封印命中":240,"法力":14,"打造":1}},
	),
	302:(
		{"条件":1,"物品":101003,"效果":{"抵抗封印":120,"物理防御":23,"真气上限":135,"打造":1}},
		{"条件":2,"物品":101103,"效果":{"抵抗封印":120,"物理防御":23,"真气上限":135,"打造":1}},
	),
	303:(
		{"条件":1,"物品":101203,"效果":{"物理防御":23,"生命上限":128,"体质":14,"打造":1}},
		{"条件":2,"物品":101303,"效果":{"物理防御":23,"生命上限":128,"体质":14,"打造":1}},
	),
	401:(
		{"条件":1111,"物品":100004,"效果":{"物理伤害":286,"法术伤害":286,"治疗强度":143,"封印命中":300,"力量":17,"打造":1}},
		{"条件":1121,"物品":100054,"效果":{"物理伤害":286,"法术伤害":286,"治疗强度":143,"封印命中":300,"力量":17,"打造":1}},
		{"条件":1211,"物品":100104,"效果":{"物理伤害":286,"法术伤害":286,"治疗强度":143,"封印命中":300,"法力":17,"打造":1}},
		{"条件":1221,"物品":100154,"效果":{"物理伤害":286,"法术伤害":286,"治疗强度":143,"封印命中":300,"法力":17,"打造":1}},
		{"条件":1311,"物品":100204,"效果":{"物理伤害":286,"法术伤害":286,"治疗强度":143,"封印命中":300,"力量":17,"打造":1}},
		{"条件":1321,"物品":100254,"效果":{"物理伤害":286,"法术伤害":286,"治疗强度":143,"封印命中":300,"力量":17,"打造":1}},
		{"条件":1411,"物品":100304,"效果":{"物理伤害":286,"法术伤害":286,"治疗强度":143,"封印命中":300,"法力":17,"打造":1}},
		{"条件":1421,"物品":100354,"效果":{"物理伤害":286,"法术伤害":286,"治疗强度":143,"封印命中":300,"法力":17,"打造":1}},
		{"条件":1511,"物品":100404,"效果":{"物理伤害":286,"法术伤害":286,"治疗强度":143,"封印命中":300,"法力":17,"打造":1}},
		{"条件":1521,"物品":100454,"效果":{"物理伤害":286,"法术伤害":286,"治疗强度":143,"封印命中":300,"法力":17,"打造":1}},
		{"条件":1611,"物品":100504,"效果":{"物理伤害":286,"法术伤害":286,"治疗强度":143,"封印命中":300,"法力":17,"打造":1}},
		{"条件":1621,"物品":100554,"效果":{"物理伤害":286,"法术伤害":286,"治疗强度":143,"封印命中":300,"法力":17,"打造":1}},
	),
	402:(
		{"条件":1,"物品":101004,"效果":{"抵抗封印":150,"物理防御":29,"真气上限":175,"打造":1}},
		{"条件":2,"物品":101104,"效果":{"抵抗封印":150,"物理防御":29,"真气上限":175,"打造":1}},
	),
	403:(
		{"条件":1,"物品":101204,"效果":{"物理防御":29,"生命上限":160,"体质":17,"打造":1}},
		{"条件":2,"物品":101304,"效果":{"物理防御":29,"生命上限":160,"体质":17,"打造":1}},
	),
	501:(
		{"条件":1111,"物品":100005,"效果":{"物理伤害":350,"法术伤害":350,"治疗强度":175,"封印命中":360,"力量":20,"打造":1}},
		{"条件":1121,"物品":100055,"效果":{"物理伤害":350,"法术伤害":350,"治疗强度":175,"封印命中":360,"力量":20,"打造":1}},
		{"条件":1211,"物品":100105,"效果":{"物理伤害":350,"法术伤害":350,"治疗强度":175,"封印命中":360,"法力":20,"打造":1}},
		{"条件":1221,"物品":100155,"效果":{"物理伤害":350,"法术伤害":350,"治疗强度":175,"封印命中":360,"法力":20,"打造":1}},
		{"条件":1311,"物品":100205,"效果":{"物理伤害":350,"法术伤害":350,"治疗强度":175,"封印命中":360,"力量":20,"打造":1}},
		{"条件":1321,"物品":100255,"效果":{"物理伤害":350,"法术伤害":350,"治疗强度":175,"封印命中":360,"力量":20,"打造":1}},
		{"条件":1411,"物品":100305,"效果":{"物理伤害":350,"法术伤害":350,"治疗强度":175,"封印命中":360,"法力":20,"打造":1}},
		{"条件":1421,"物品":100355,"效果":{"物理伤害":350,"法术伤害":350,"治疗强度":175,"封印命中":360,"法力":20,"打造":1}},
		{"条件":1511,"物品":100405,"效果":{"物理伤害":350,"法术伤害":350,"治疗强度":175,"封印命中":360,"法力":20,"打造":1}},
		{"条件":1521,"物品":100455,"效果":{"物理伤害":350,"法术伤害":350,"治疗强度":175,"封印命中":360,"法力":20,"打造":1}},
		{"条件":1611,"物品":100505,"效果":{"物理伤害":350,"法术伤害":350,"治疗强度":175,"封印命中":360,"法力":20,"打造":1}},
		{"条件":1621,"物品":100555,"效果":{"物理伤害":350,"法术伤害":350,"治疗强度":175,"封印命中":360,"法力":20,"打造":1}},
	),
	502:(
		{"条件":1,"物品":101005,"效果":{"抵抗封印":180,"物理防御":36,"真气上限":215,"打造":1}},
		{"条件":2,"物品":101105,"效果":{"抵抗封印":180,"物理防御":36,"真气上限":215,"打造":1}},
	),
	503:(
		{"条件":1,"物品":101205,"效果":{"物理防御":36,"生命上限":192,"体质":20,"打造":1}},
		{"条件":2,"物品":101305,"效果":{"物理防御":36,"生命上限":192,"体质":20,"打造":1}},
	),
	601:(
		{"条件":1111,"物品":241406},
		{"条件":1121,"物品":241456},
		{"条件":1211,"物品":241506},
		{"条件":1221,"物品":241556},
		{"条件":1311,"物品":241606},
		{"条件":1321,"物品":241656},
		{"条件":1411,"物品":241706},
		{"条件":1421,"物品":241756},
		{"条件":1511,"物品":241806},
		{"条件":1521,"物品":241856},
		{"条件":1611,"物品":241906},
		{"条件":1621,"物品":241956},
	),
}

gdgembag={
	2241021:(
		{"权重":10,"物品":224001,"数量":1,"绑定":0},
		{"权重":10,"物品":224002,"数量":1,"绑定":0},
		{"权重":10,"物品":224003,"数量":1,"绑定":0},
		{"权重":10,"物品":224004,"数量":1,"绑定":0},
		{"权重":10,"物品":224005,"数量":1,"绑定":0},
		{"权重":10,"物品":224006,"数量":1,"绑定":0},
		{"权重":10,"物品":224007,"数量":1,"绑定":0},
		{"权重":10,"物品":224008,"数量":1,"绑定":0},
		{"权重":10,"物品":224009,"数量":1,"绑定":0},
		{"权重":10,"物品":224010,"数量":1,"绑定":0},
	),
	2460511:(
		{"权重":10,"物品":246001,"数量":1,"绑定":0},
		{"权重":10,"物品":246002,"数量":1,"绑定":0},
		{"权重":10,"物品":246003,"数量":1,"绑定":0},
		{"权重":10,"物品":246004,"数量":1,"绑定":0},
		{"权重":10,"物品":246005,"数量":1,"绑定":0},
		{"权重":10,"物品":246006,"数量":1,"绑定":0},
		{"权重":10,"物品":246007,"数量":1,"绑定":0},
		{"权重":10,"物品":246008,"数量":1,"绑定":0},
		{"权重":10,"物品":246009,"数量":1,"绑定":0},
		{"权重":10,"物品":246010,"数量":1,"绑定":0},
	),
	2349011:(
		{"权重":112,"物品":234101,"数量":1,"绑定":0},
		{"权重":112,"物品":234102,"数量":1,"绑定":0},
		{"权重":168,"物品":234103,"数量":1,"绑定":0},
		{"权重":168,"物品":234104,"数量":1,"绑定":0},
		{"权重":168,"物品":234105,"数量":1,"绑定":0},
		{"权重":168,"物品":234106,"数量":1,"绑定":0},
		{"权重":168,"物品":234107,"数量":1,"绑定":0},
		{"权重":168,"物品":234108,"数量":1,"绑定":0},
		{"权重":112,"物品":234109,"数量":1,"绑定":0},
		{"权重":112,"物品":234110,"数量":1,"绑定":0},
		{"权重":168,"物品":234111,"数量":1,"绑定":0},
		{"权重":112,"物品":234112,"数量":1,"绑定":0},
		{"权重":112,"物品":234113,"数量":1,"绑定":0},
		{"权重":112,"物品":234114,"数量":1,"绑定":0},
		{"权重":112,"物品":234115,"数量":1,"绑定":0},
		{"权重":112,"物品":234116,"数量":1,"绑定":0},
		{"权重":112,"物品":234117,"数量":1,"绑定":0},
		{"权重":112,"物品":234118,"数量":1,"绑定":0},
		{"权重":168,"物品":234119,"数量":1,"绑定":0},
		{"权重":168,"物品":234120,"数量":1,"绑定":0},
		{"权重":337,"物品":234121,"数量":1,"绑定":0},
		{"权重":168,"物品":234122,"数量":1,"绑定":0},
		{"权重":168,"物品":234123,"数量":1,"绑定":0},
		{"权重":168,"物品":234124,"数量":1,"绑定":0},
		{"权重":337,"物品":234125,"数量":1,"绑定":0},
		{"权重":337,"物品":234126,"数量":1,"绑定":0},
		{"权重":337,"物品":234127,"数量":1,"绑定":0},
		{"权重":168,"物品":234128,"数量":1,"绑定":0},
		{"权重":112,"物品":234129,"数量":1,"绑定":0},
		{"权重":112,"物品":234130,"数量":1,"绑定":0},
		{"权重":168,"物品":234131,"数量":1,"绑定":0},
		{"权重":168,"物品":234132,"数量":1,"绑定":0},
		{"权重":168,"物品":234133,"数量":1,"绑定":0},
		{"权重":112,"物品":234134,"数量":1,"绑定":0},
		{"权重":112,"物品":234135,"数量":1,"绑定":0},
		{"权重":112,"物品":234136,"数量":1,"绑定":0},
		{"权重":168,"物品":234137,"数量":1,"绑定":0},
		{"权重":112,"物品":234138,"数量":1,"绑定":0},
		{"权重":168,"物品":234139,"数量":1,"绑定":0},
		{"权重":168,"物品":234140,"数量":1,"绑定":0},
		{"权重":168,"物品":234141,"数量":1,"绑定":0},
		{"权重":168,"物品":234142,"数量":1,"绑定":0},
		{"权重":337,"物品":234143,"数量":1,"绑定":0},
		{"权重":168,"物品":234144,"数量":1,"绑定":0},
		{"权重":337,"物品":234145,"数量":1,"绑定":0},
		{"权重":337,"物品":234146,"数量":1,"绑定":0},
		{"权重":337,"物品":234147,"数量":1,"绑定":0},
		{"权重":337,"物品":234148,"数量":1,"绑定":0},
		{"权重":337,"物品":234149,"数量":1,"绑定":0},
		{"权重":168,"物品":234150,"数量":1,"绑定":0},
		{"权重":337,"物品":234151,"数量":1,"绑定":0},
		{"权重":337,"物品":234152,"数量":1,"绑定":0},
		{"权重":168,"物品":234153,"数量":1,"绑定":0},
	),
	2349021:(
		{"权重":149,"物品":234201,"数量":1,"绑定":0},
		{"权重":149,"物品":234202,"数量":1,"绑定":0},
		{"权重":186,"物品":234203,"数量":1,"绑定":0},
		{"权重":186,"物品":234204,"数量":1,"绑定":0},
		{"权重":186,"物品":234205,"数量":1,"绑定":0},
		{"权重":186,"物品":234206,"数量":1,"绑定":0},
		{"权重":186,"物品":234207,"数量":1,"绑定":0},
		{"权重":186,"物品":234208,"数量":1,"绑定":0},
		{"权重":149,"物品":234209,"数量":1,"绑定":0},
		{"权重":149,"物品":234210,"数量":1,"绑定":0},
		{"权重":186,"物品":234211,"数量":1,"绑定":0},
		{"权重":149,"物品":234212,"数量":1,"绑定":0},
		{"权重":149,"物品":234213,"数量":1,"绑定":0},
		{"权重":149,"物品":234214,"数量":1,"绑定":0},
		{"权重":149,"物品":234215,"数量":1,"绑定":0},
		{"权重":149,"物品":234216,"数量":1,"绑定":0},
		{"权重":149,"物品":234217,"数量":1,"绑定":0},
		{"权重":149,"物品":234218,"数量":1,"绑定":0},
		{"权重":186,"物品":234219,"数量":1,"绑定":0},
		{"权重":186,"物品":234220,"数量":1,"绑定":0},
		{"权重":248,"物品":234221,"数量":1,"绑定":0},
		{"权重":186,"物品":234222,"数量":1,"绑定":0},
		{"权重":186,"物品":234223,"数量":1,"绑定":0},
		{"权重":186,"物品":234224,"数量":1,"绑定":0},
		{"权重":248,"物品":234225,"数量":1,"绑定":0},
		{"权重":248,"物品":234226,"数量":1,"绑定":0},
		{"权重":248,"物品":234227,"数量":1,"绑定":0},
		{"权重":186,"物品":234228,"数量":1,"绑定":0},
		{"权重":149,"物品":234229,"数量":1,"绑定":0},
		{"权重":149,"物品":234230,"数量":1,"绑定":0},
		{"权重":186,"物品":234231,"数量":1,"绑定":0},
		{"权重":186,"物品":234232,"数量":1,"绑定":0},
		{"权重":186,"物品":234233,"数量":1,"绑定":0},
		{"权重":149,"物品":234234,"数量":1,"绑定":0},
		{"权重":149,"物品":234235,"数量":1,"绑定":0},
		{"权重":149,"物品":234236,"数量":1,"绑定":0},
		{"权重":186,"物品":234237,"数量":1,"绑定":0},
		{"权重":149,"物品":234238,"数量":1,"绑定":0},
		{"权重":186,"物品":234239,"数量":1,"绑定":0},
		{"权重":186,"物品":234240,"数量":1,"绑定":0},
		{"权重":186,"物品":234241,"数量":1,"绑定":0},
		{"权重":186,"物品":234242,"数量":1,"绑定":0},
		{"权重":248,"物品":234243,"数量":1,"绑定":0},
		{"权重":186,"物品":234244,"数量":1,"绑定":0},
		{"权重":248,"物品":234245,"数量":1,"绑定":0},
		{"权重":248,"物品":234246,"数量":1,"绑定":0},
		{"权重":248,"物品":234247,"数量":1,"绑定":0},
		{"权重":248,"物品":234248,"数量":1,"绑定":0},
		{"权重":248,"物品":234249,"数量":1,"绑定":0},
		{"权重":186,"物品":234250,"数量":1,"绑定":0},
		{"权重":248,"物品":234251,"数量":1,"绑定":0},
		{"权重":248,"物品":234252,"数量":1,"绑定":0},
		{"权重":186,"物品":234253,"数量":1,"绑定":0},
	),
	2349031:(
		{"权重":666,"物品":234401,"数量":1,"绑定":0},
		{"权重":666,"物品":234402,"数量":1,"绑定":0},
		{"权重":666,"物品":234403,"数量":1,"绑定":0},
		{"权重":666,"物品":234404,"数量":1,"绑定":0},
		{"权重":666,"物品":234405,"数量":1,"绑定":0},
		{"权重":333,"物品":234406,"数量":1,"绑定":0},
		{"权重":333,"物品":234407,"数量":1,"绑定":0},
		{"权重":333,"物品":234408,"数量":1,"绑定":0},
		{"权重":333,"物品":234409,"数量":1,"绑定":0},
		{"权重":333,"物品":234410,"数量":1,"绑定":0},
		{"权重":666,"物品":234411,"数量":1,"绑定":0},
		{"权重":666,"物品":234412,"数量":1,"绑定":0},
		{"权重":666,"物品":234413,"数量":1,"绑定":0},
		{"权重":666,"物品":234414,"数量":1,"绑定":0},
		{"权重":666,"物品":234415,"数量":1,"绑定":0},
		{"权重":333,"物品":234416,"数量":1,"绑定":0},
		{"权重":333,"物品":234417,"数量":1,"绑定":0},
		{"权重":333,"物品":234418,"数量":1,"绑定":0},
		{"权重":333,"物品":234419,"数量":1,"绑定":0},
		{"权重":333,"物品":234420,"数量":1,"绑定":0},
	),
	2349041:(
		{"权重":95,"物品":234101,"数量":1,"绑定":0},
		{"权重":95,"物品":234102,"数量":1,"绑定":0},
		{"权重":143,"物品":234103,"数量":1,"绑定":0},
		{"权重":143,"物品":234104,"数量":1,"绑定":0},
		{"权重":143,"物品":234105,"数量":1,"绑定":0},
		{"权重":143,"物品":234106,"数量":1,"绑定":0},
		{"权重":143,"物品":234107,"数量":1,"绑定":0},
		{"权重":143,"物品":234108,"数量":1,"绑定":0},
		{"权重":95,"物品":234109,"数量":1,"绑定":0},
		{"权重":95,"物品":234110,"数量":1,"绑定":0},
		{"权重":143,"物品":234111,"数量":1,"绑定":0},
		{"权重":95,"物品":234112,"数量":1,"绑定":0},
		{"权重":95,"物品":234113,"数量":1,"绑定":0},
		{"权重":95,"物品":234114,"数量":1,"绑定":0},
		{"权重":95,"物品":234115,"数量":1,"绑定":0},
		{"权重":95,"物品":234116,"数量":1,"绑定":0},
		{"权重":95,"物品":234117,"数量":1,"绑定":0},
		{"权重":95,"物品":234118,"数量":1,"绑定":0},
		{"权重":143,"物品":234119,"数量":1,"绑定":0},
		{"权重":143,"物品":234120,"数量":1,"绑定":0},
		{"权重":286,"物品":234121,"数量":1,"绑定":0},
		{"权重":143,"物品":234122,"数量":1,"绑定":0},
		{"权重":143,"物品":234123,"数量":1,"绑定":0},
		{"权重":143,"物品":234124,"数量":1,"绑定":0},
		{"权重":286,"物品":234125,"数量":1,"绑定":0},
		{"权重":286,"物品":234126,"数量":1,"绑定":0},
		{"权重":286,"物品":234127,"数量":1,"绑定":0},
		{"权重":143,"物品":234128,"数量":1,"绑定":0},
		{"权重":95,"物品":234129,"数量":1,"绑定":0},
		{"权重":95,"物品":234130,"数量":1,"绑定":0},
		{"权重":143,"物品":234131,"数量":1,"绑定":0},
		{"权重":143,"物品":234132,"数量":1,"绑定":0},
		{"权重":143,"物品":234133,"数量":1,"绑定":0},
		{"权重":95,"物品":234134,"数量":1,"绑定":0},
		{"权重":95,"物品":234135,"数量":1,"绑定":0},
		{"权重":95,"物品":234136,"数量":1,"绑定":0},
		{"权重":143,"物品":234137,"数量":1,"绑定":0},
		{"权重":95,"物品":234138,"数量":1,"绑定":0},
		{"权重":143,"物品":234139,"数量":1,"绑定":0},
		{"权重":143,"物品":234140,"数量":1,"绑定":0},
		{"权重":143,"物品":234141,"数量":1,"绑定":0},
		{"权重":143,"物品":234142,"数量":1,"绑定":0},
		{"权重":286,"物品":234143,"数量":1,"绑定":0},
		{"权重":143,"物品":234144,"数量":1,"绑定":0},
		{"权重":286,"物品":234145,"数量":1,"绑定":0},
		{"权重":286,"物品":234146,"数量":1,"绑定":0},
		{"权重":286,"物品":234147,"数量":1,"绑定":0},
		{"权重":286,"物品":234148,"数量":1,"绑定":0},
		{"权重":286,"物品":234149,"数量":1,"绑定":0},
		{"权重":143,"物品":234150,"数量":1,"绑定":0},
		{"权重":286,"物品":234151,"数量":1,"绑定":0},
		{"权重":286,"物品":234152,"数量":1,"绑定":0},
		{"权重":143,"物品":234153,"数量":1,"绑定":0},
		{"权重":11,"物品":234201,"数量":1,"绑定":0},
		{"权重":11,"物品":234202,"数量":1,"绑定":0},
		{"权重":14,"物品":234203,"数量":1,"绑定":0},
		{"权重":14,"物品":234204,"数量":1,"绑定":0},
		{"权重":14,"物品":234205,"数量":1,"绑定":0},
		{"权重":14,"物品":234206,"数量":1,"绑定":0},
		{"权重":14,"物品":234207,"数量":1,"绑定":0},
		{"权重":14,"物品":234208,"数量":1,"绑定":0},
		{"权重":11,"物品":234209,"数量":1,"绑定":0},
		{"权重":11,"物品":234210,"数量":1,"绑定":0},
		{"权重":14,"物品":234211,"数量":1,"绑定":0},
		{"权重":11,"物品":234212,"数量":1,"绑定":0},
		{"权重":11,"物品":234213,"数量":1,"绑定":0},
		{"权重":11,"物品":234214,"数量":1,"绑定":0},
		{"权重":11,"物品":234215,"数量":1,"绑定":0},
		{"权重":11,"物品":234216,"数量":1,"绑定":0},
		{"权重":11,"物品":234217,"数量":1,"绑定":0},
		{"权重":11,"物品":234218,"数量":1,"绑定":0},
		{"权重":14,"物品":234219,"数量":1,"绑定":0},
		{"权重":14,"物品":234220,"数量":1,"绑定":0},
		{"权重":19,"物品":234221,"数量":1,"绑定":0},
		{"权重":14,"物品":234222,"数量":1,"绑定":0},
		{"权重":14,"物品":234223,"数量":1,"绑定":0},
		{"权重":14,"物品":234224,"数量":1,"绑定":0},
		{"权重":19,"物品":234225,"数量":1,"绑定":0},
		{"权重":19,"物品":234226,"数量":1,"绑定":0},
		{"权重":19,"物品":234227,"数量":1,"绑定":0},
		{"权重":14,"物品":234228,"数量":1,"绑定":0},
		{"权重":11,"物品":234229,"数量":1,"绑定":0},
		{"权重":11,"物品":234230,"数量":1,"绑定":0},
		{"权重":14,"物品":234231,"数量":1,"绑定":0},
		{"权重":14,"物品":234232,"数量":1,"绑定":0},
		{"权重":14,"物品":234233,"数量":1,"绑定":0},
		{"权重":11,"物品":234234,"数量":1,"绑定":0},
		{"权重":11,"物品":234235,"数量":1,"绑定":0},
		{"权重":11,"物品":234236,"数量":1,"绑定":0},
		{"权重":14,"物品":234237,"数量":1,"绑定":0},
		{"权重":11,"物品":234238,"数量":1,"绑定":0},
		{"权重":14,"物品":234239,"数量":1,"绑定":0},
		{"权重":14,"物品":234240,"数量":1,"绑定":0},
		{"权重":14,"物品":234241,"数量":1,"绑定":0},
		{"权重":14,"物品":234242,"数量":1,"绑定":0},
		{"权重":19,"物品":234243,"数量":1,"绑定":0},
		{"权重":14,"物品":234244,"数量":1,"绑定":0},
		{"权重":19,"物品":234245,"数量":1,"绑定":0},
		{"权重":19,"物品":234246,"数量":1,"绑定":0},
		{"权重":19,"物品":234247,"数量":1,"绑定":0},
		{"权重":19,"物品":234248,"数量":1,"绑定":0},
		{"权重":19,"物品":234249,"数量":1,"绑定":0},
		{"权重":14,"物品":234250,"数量":1,"绑定":0},
		{"权重":19,"物品":234251,"数量":1,"绑定":0},
		{"权重":19,"物品":234252,"数量":1,"绑定":0},
		{"权重":14,"物品":234253,"数量":1,"绑定":0},
		{"权重":47,"物品":234401,"数量":1,"绑定":0},
		{"权重":47,"物品":234402,"数量":1,"绑定":0},
		{"权重":47,"物品":234403,"数量":1,"绑定":0},
		{"权重":47,"物品":234404,"数量":1,"绑定":0},
		{"权重":47,"物品":234405,"数量":1,"绑定":0},
		{"权重":23,"物品":234406,"数量":1,"绑定":0},
		{"权重":23,"物品":234407,"数量":1,"绑定":0},
		{"权重":23,"物品":234408,"数量":1,"绑定":0},
		{"权重":23,"物品":234409,"数量":1,"绑定":0},
		{"权重":23,"物品":234410,"数量":1,"绑定":0},
		{"权重":47,"物品":234411,"数量":1,"绑定":0},
		{"权重":47,"物品":234412,"数量":1,"绑定":0},
		{"权重":47,"物品":234413,"数量":1,"绑定":0},
		{"权重":47,"物品":234414,"数量":1,"绑定":0},
		{"权重":47,"物品":234415,"数量":1,"绑定":0},
		{"权重":23,"物品":234416,"数量":1,"绑定":0},
		{"权重":23,"物品":234417,"数量":1,"绑定":0},
		{"权重":23,"物品":234418,"数量":1,"绑定":0},
		{"权重":23,"物品":234419,"数量":1,"绑定":0},
		{"权重":23,"物品":234420,"数量":1,"绑定":0},
	),
	2470011:(
		{"权重":10,"物品":241404,"数量":1,"绑定":0},
		{"权重":10,"物品":241454,"数量":1,"绑定":0},
		{"权重":10,"物品":241504,"数量":1,"绑定":0},
		{"权重":10,"物品":241554,"数量":1,"绑定":0},
		{"权重":10,"物品":241604,"数量":1,"绑定":0},
		{"权重":10,"物品":241654,"数量":1,"绑定":0},
		{"权重":10,"物品":241704,"数量":1,"绑定":0},
		{"权重":10,"物品":241754,"数量":1,"绑定":0},
		{"权重":10,"物品":241804,"数量":1,"绑定":0},
		{"权重":10,"物品":241854,"数量":1,"绑定":0},
		{"权重":10,"物品":241904,"数量":1,"绑定":0},
		{"权重":10,"物品":241954,"数量":1,"绑定":0},
		{"权重":10,"物品":243004,"数量":1,"绑定":0},
		{"权重":10,"物品":243054,"数量":1,"绑定":0},
		{"权重":10,"物品":243104,"数量":1,"绑定":0},
		{"权重":10,"物品":243154,"数量":1,"绑定":0},
		{"权重":10,"物品":243204,"数量":1,"绑定":0},
		{"权重":10,"物品":243304,"数量":1,"绑定":0},
		{"权重":10,"物品":243404,"数量":1,"绑定":0},
	),
	2470021:(
		{"权重":10,"物品":241405,"数量":1,"绑定":0},
		{"权重":10,"物品":241455,"数量":1,"绑定":0},
		{"权重":10,"物品":241505,"数量":1,"绑定":0},
		{"权重":10,"物品":241555,"数量":1,"绑定":0},
		{"权重":10,"物品":241605,"数量":1,"绑定":0},
		{"权重":10,"物品":241655,"数量":1,"绑定":0},
		{"权重":10,"物品":241705,"数量":1,"绑定":0},
		{"权重":10,"物品":241755,"数量":1,"绑定":0},
		{"权重":10,"物品":241805,"数量":1,"绑定":0},
		{"权重":10,"物品":241855,"数量":1,"绑定":0},
		{"权重":10,"物品":241905,"数量":1,"绑定":0},
		{"权重":10,"物品":241955,"数量":1,"绑定":0},
		{"权重":10,"物品":243005,"数量":1,"绑定":0},
		{"权重":10,"物品":243055,"数量":1,"绑定":0},
		{"权重":10,"物品":243105,"数量":1,"绑定":0},
		{"权重":10,"物品":243155,"数量":1,"绑定":0},
		{"权重":10,"物品":243205,"数量":1,"绑定":0},
		{"权重":10,"物品":243305,"数量":1,"绑定":0},
		{"权重":10,"物品":243405,"数量":1,"绑定":0},
	),
	2470031:(
		{"权重":10,"物品":241406,"数量":1,"绑定":0},
		{"权重":10,"物品":241456,"数量":1,"绑定":0},
		{"权重":10,"物品":241506,"数量":1,"绑定":0},
		{"权重":10,"物品":241556,"数量":1,"绑定":0},
		{"权重":10,"物品":241606,"数量":1,"绑定":0},
		{"权重":10,"物品":241656,"数量":1,"绑定":0},
		{"权重":10,"物品":241706,"数量":1,"绑定":0},
		{"权重":10,"物品":241756,"数量":1,"绑定":0},
		{"权重":10,"物品":241806,"数量":1,"绑定":0},
		{"权重":10,"物品":241856,"数量":1,"绑定":0},
		{"权重":10,"物品":241906,"数量":1,"绑定":0},
		{"权重":10,"物品":241956,"数量":1,"绑定":0},
		{"权重":10,"物品":243006,"数量":1,"绑定":0},
		{"权重":10,"物品":243056,"数量":1,"绑定":0},
		{"权重":10,"物品":243106,"数量":1,"绑定":0},
		{"权重":10,"物品":243156,"数量":1,"绑定":0},
		{"权重":10,"物品":243206,"数量":1,"绑定":0},
		{"权重":10,"物品":243306,"数量":1,"绑定":0},
		{"权重":10,"物品":243406,"数量":1,"绑定":0},
	),
	2470041:(
		{"权重":10,"物品":241407,"数量":1,"绑定":0},
		{"权重":10,"物品":241457,"数量":1,"绑定":0},
		{"权重":10,"物品":241507,"数量":1,"绑定":0},
		{"权重":10,"物品":241557,"数量":1,"绑定":0},
		{"权重":10,"物品":241607,"数量":1,"绑定":0},
		{"权重":10,"物品":241657,"数量":1,"绑定":0},
		{"权重":10,"物品":241707,"数量":1,"绑定":0},
		{"权重":10,"物品":241757,"数量":1,"绑定":0},
		{"权重":10,"物品":241807,"数量":1,"绑定":0},
		{"权重":10,"物品":241857,"数量":1,"绑定":0},
		{"权重":10,"物品":241907,"数量":1,"绑定":0},
		{"权重":10,"物品":241957,"数量":1,"绑定":0},
		{"权重":10,"物品":243007,"数量":1,"绑定":0},
		{"权重":10,"物品":243057,"数量":1,"绑定":0},
		{"权重":10,"物品":243107,"数量":1,"绑定":0},
		{"权重":10,"物品":243157,"数量":1,"绑定":0},
		{"权重":10,"物品":243207,"数量":1,"绑定":0},
		{"权重":10,"物品":243307,"数量":1,"绑定":0},
		{"权重":10,"物品":243407,"数量":1,"绑定":0},
	),
	2470051:(
		{"权重":10,"物品":241408,"数量":1,"绑定":0},
		{"权重":10,"物品":241458,"数量":1,"绑定":0},
		{"权重":10,"物品":241508,"数量":1,"绑定":0},
		{"权重":10,"物品":241558,"数量":1,"绑定":0},
		{"权重":10,"物品":241608,"数量":1,"绑定":0},
		{"权重":10,"物品":241658,"数量":1,"绑定":0},
		{"权重":10,"物品":241708,"数量":1,"绑定":0},
		{"权重":10,"物品":241758,"数量":1,"绑定":0},
		{"权重":10,"物品":241808,"数量":1,"绑定":0},
		{"权重":10,"物品":241858,"数量":1,"绑定":0},
		{"权重":10,"物品":241908,"数量":1,"绑定":0},
		{"权重":10,"物品":241958,"数量":1,"绑定":0},
		{"权重":10,"物品":243008,"数量":1,"绑定":0},
		{"权重":10,"物品":243058,"数量":1,"绑定":0},
		{"权重":10,"物品":243108,"数量":1,"绑定":0},
		{"权重":10,"物品":243158,"数量":1,"绑定":0},
		{"权重":10,"物品":243208,"数量":1,"绑定":0},
		{"权重":10,"物品":243308,"数量":1,"绑定":0},
		{"权重":10,"物品":243408,"数量":1,"绑定":0},
	),
	2470061:(
		{"权重":10,"物品":241409,"数量":1,"绑定":0},
		{"权重":10,"物品":241459,"数量":1,"绑定":0},
		{"权重":10,"物品":241509,"数量":1,"绑定":0},
		{"权重":10,"物品":241559,"数量":1,"绑定":0},
		{"权重":10,"物品":241609,"数量":1,"绑定":0},
		{"权重":10,"物品":241659,"数量":1,"绑定":0},
		{"权重":10,"物品":241709,"数量":1,"绑定":0},
		{"权重":10,"物品":241759,"数量":1,"绑定":0},
		{"权重":10,"物品":241809,"数量":1,"绑定":0},
		{"权重":10,"物品":241859,"数量":1,"绑定":0},
		{"权重":10,"物品":241909,"数量":1,"绑定":0},
		{"权重":10,"物品":241959,"数量":1,"绑定":0},
		{"权重":10,"物品":243009,"数量":1,"绑定":0},
		{"权重":10,"物品":243059,"数量":1,"绑定":0},
		{"权重":10,"物品":243109,"数量":1,"绑定":0},
		{"权重":10,"物品":243159,"数量":1,"绑定":0},
		{"权重":10,"物品":243209,"数量":1,"绑定":0},
		{"权重":10,"物品":243309,"数量":1,"绑定":0},
		{"权重":10,"物品":243409,"数量":1,"绑定":0},
	),
	2470071:(
		{"权重":10,"物品":241410,"数量":1,"绑定":0},
		{"权重":10,"物品":241460,"数量":1,"绑定":0},
		{"权重":10,"物品":241510,"数量":1,"绑定":0},
		{"权重":10,"物品":241560,"数量":1,"绑定":0},
		{"权重":10,"物品":241610,"数量":1,"绑定":0},
		{"权重":10,"物品":241660,"数量":1,"绑定":0},
		{"权重":10,"物品":241710,"数量":1,"绑定":0},
		{"权重":10,"物品":241760,"数量":1,"绑定":0},
		{"权重":10,"物品":241810,"数量":1,"绑定":0},
		{"权重":10,"物品":241860,"数量":1,"绑定":0},
		{"权重":10,"物品":241910,"数量":1,"绑定":0},
		{"权重":10,"物品":241960,"数量":1,"绑定":0},
		{"权重":10,"物品":243010,"数量":1,"绑定":0},
		{"权重":10,"物品":243060,"数量":1,"绑定":0},
		{"权重":10,"物品":243110,"数量":1,"绑定":0},
		{"权重":10,"物品":243160,"数量":1,"绑定":0},
		{"权重":10,"物品":243210,"数量":1,"绑定":0},
		{"权重":10,"物品":243310,"数量":1,"绑定":0},
		{"权重":10,"物品":243410,"数量":1,"绑定":0},
	),
	2470081:(
		{"权重":10,"物品":241411,"数量":1,"绑定":0},
		{"权重":10,"物品":241461,"数量":1,"绑定":0},
		{"权重":10,"物品":241511,"数量":1,"绑定":0},
		{"权重":10,"物品":241561,"数量":1,"绑定":0},
		{"权重":10,"物品":241611,"数量":1,"绑定":0},
		{"权重":10,"物品":241661,"数量":1,"绑定":0},
		{"权重":10,"物品":241711,"数量":1,"绑定":0},
		{"权重":10,"物品":241761,"数量":1,"绑定":0},
		{"权重":10,"物品":241811,"数量":1,"绑定":0},
		{"权重":10,"物品":241861,"数量":1,"绑定":0},
		{"权重":10,"物品":241911,"数量":1,"绑定":0},
		{"权重":10,"物品":241961,"数量":1,"绑定":0},
		{"权重":10,"物品":243011,"数量":1,"绑定":0},
		{"权重":10,"物品":243061,"数量":1,"绑定":0},
		{"权重":10,"物品":243111,"数量":1,"绑定":0},
		{"权重":10,"物品":243161,"数量":1,"绑定":0},
		{"权重":10,"物品":243211,"数量":1,"绑定":0},
		{"权重":10,"物品":243311,"数量":1,"绑定":0},
		{"权重":10,"物品":243411,"数量":1,"绑定":0},
	),
	2020611:(
		{"权重":10,"物品":200001,"数量":1000000,"绑定":0},
	),
	2020621:(
		{"权重":10,"物品":200002,"数量":10000,"绑定":0},
	),
	2259011:(
		{"权重":10,"物品":225001,"数量":1,"绑定":0},
		{"权重":10,"物品":225002,"数量":1,"绑定":0},
		{"权重":10,"物品":225003,"数量":1,"绑定":0},
		{"权重":10,"物品":225004,"数量":1,"绑定":0},
		{"权重":10,"物品":225005,"数量":1,"绑定":0},
		{"权重":10,"物品":225006,"数量":1,"绑定":0},
		{"权重":10,"物品":225007,"数量":1,"绑定":0},
		{"权重":10,"物品":225008,"数量":1,"绑定":0},
		{"权重":10,"物品":225009,"数量":1,"绑定":0},
		{"权重":10,"物品":225010,"数量":1,"绑定":0},
	),
	2259021:(
		{"权重":10,"物品":225001,"数量":5,"绑定":0},
		{"权重":10,"物品":225002,"数量":5,"绑定":0},
		{"权重":10,"物品":225003,"数量":5,"绑定":0},
		{"权重":10,"物品":225004,"数量":5,"绑定":0},
		{"权重":10,"物品":225005,"数量":5,"绑定":0},
		{"权重":10,"物品":225006,"数量":5,"绑定":0},
		{"权重":10,"物品":225007,"数量":5,"绑定":0},
		{"权重":10,"物品":225008,"数量":5,"绑定":0},
		{"权重":10,"物品":225009,"数量":5,"绑定":0},
		{"权重":10,"物品":225010,"数量":5,"绑定":0},
	),
	2259031:(
		{"权重":10,"物品":225001,"数量":10,"绑定":0},
		{"权重":10,"物品":225002,"数量":10,"绑定":0},
		{"权重":10,"物品":225003,"数量":10,"绑定":0},
		{"权重":10,"物品":225004,"数量":10,"绑定":0},
		{"权重":10,"物品":225005,"数量":10,"绑定":0},
		{"权重":10,"物品":225006,"数量":10,"绑定":0},
		{"权重":10,"物品":225007,"数量":10,"绑定":0},
		{"权重":10,"物品":225008,"数量":10,"绑定":0},
		{"权重":10,"物品":225009,"数量":10,"绑定":0},
		{"权重":10,"物品":225010,"数量":10,"绑定":0},
	),
	2242011:(
		{"权重":10,"物品":224103,"数量":1,"绑定":0},
		{"权重":10,"物品":224104,"数量":1,"绑定":0},
		{"权重":10,"物品":224105,"数量":1,"绑定":0},
		{"权重":10,"物品":224106,"数量":1,"绑定":0},
		{"权重":10,"物品":224107,"数量":1,"绑定":0},
	),
	2242021:(
		{"权重":10,"物品":224103,"数量":3,"绑定":0},
		{"权重":10,"物品":224104,"数量":3,"绑定":0},
		{"权重":10,"物品":224105,"数量":3,"绑定":0},
		{"权重":10,"物品":224106,"数量":3,"绑定":0},
		{"权重":10,"物品":224107,"数量":3,"绑定":0},
	),
	2242031:(
		{"权重":10,"物品":224103,"数量":5,"绑定":0},
		{"权重":10,"物品":224104,"数量":5,"绑定":0},
		{"权重":10,"物品":224105,"数量":5,"绑定":0},
		{"权重":10,"物品":224106,"数量":5,"绑定":0},
		{"权重":10,"物品":224107,"数量":5,"绑定":0},
	),
	2242041:(
		{"权重":10,"物品":224103,"数量":10,"绑定":0},
		{"权重":10,"物品":224104,"数量":10,"绑定":0},
		{"权重":10,"物品":224105,"数量":10,"绑定":0},
		{"权重":10,"物品":224106,"数量":10,"绑定":0},
		{"权重":10,"物品":224107,"数量":10,"绑定":0},
	),
}
#导表结束