# -*- coding: utf-8 -*-
from perform.defines import *
from perform.object import MagAttackPerform as CustomPerform

#导表开始
class Perform(CustomPerform):
	id = 1221
	name = "花醉针"
	targetType = PERFORM_TARGET_ENEMY
	targetCount = 1
	bout = 2
	damage = lambda self,SLV:SLV*2+20
	power = 60
	consumeList = {
		"真气": lambda SLV:SLV*1.2+20,
	}
	recoverList = {
		"符能": 15,
	}
	buffId = 102
	speRatio = 100
#导表结束

	def afterAttack(self, att, vic, vicCast, dp, targetCount):
		CustomPerform.afterAttack(self, att, vic, vicCast, dp, targetCount)
		if dp > 0 and vic.inWar():
			bout = self.calBout(att, vic, self.buffId)
			buff.addOrReplace(vic, self.buffId, bout, att)
		
import buff