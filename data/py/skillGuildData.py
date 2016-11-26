#-*- coding: utf-8 -*-

def getConfig(iNo,sKey,uDefault=0):
	if iNo not in gdData:
		raise PlannerError,'不存在编号为{}的帮派技能'.format(iNo)
	return gdData[iNo].get(sKey,uDefault)

#导表开始
gdData={
	501:{"名称":"强身术","银币":"3*B","帮贡":"2*B","技能效果":"hpMax:SLV*10"},
	502:{"名称":"冥想","银币":"3*B","帮贡":"2*B","技能效果":"mpMax:SLV*10"},
	503:{"名称":"厨艺","银币":"2*B","帮贡":"1*B","效果值":lambda SLV,RND:SLV*RND(80,100)/100,"活力":"LV*0.5+20","效果物品":"220001,220002,220003,220004,220005,220006,220007,220008,220009"},
	504:{"名称":"炼丹术","银币":"2*B","帮贡":"1*B","效果值":lambda SLV,RND:SLV*RND(50,100)/100,"活力":"LV*0.5+20","效果物品":"221001,221002,221301,221302,221303,221304"},
	505:{"名称":"打造技巧","银币":"2*B","帮贡":"1*B","活力":"LV/10*10","效果物品":"241000+LV/10"},
	506:{"名称":"裁缝技巧","银币":"2*B","帮贡":"1*B","活力":"LV/10*10","效果物品":"241100+LV/10"},
	507:{"名称":"炼金技巧","银币":"2*B","帮贡":"1*B","活力":"LV/10*10","效果物品":"241200+LV/10"},
}
#导表结束