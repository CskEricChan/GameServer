# -*- coding: utf-8 -*-
from perform.defines import *
from perform.object import SealPerform as CustomPerform

#导表开始
class Perform(CustomPerform):
	id = 1422
	name = "破血咒"
	targetType = PERFORM_TARGET_ENEMY
	targetCount = 1
	bout = lambda self,SLV,VLV:(SLV-VLV+2)/10+4
	boutMax = 4
	consumeList = {
		"真气": lambda SLV:SLV*1.2+30,
		"符能": 10,
	}
	buffId = 110
	speRatio = 100
	hitRatio = lambda self,SLV,VLV:(SLV-VLV)*2+70
#导表结束