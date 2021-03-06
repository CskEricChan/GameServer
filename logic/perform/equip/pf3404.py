# -*- coding: utf-8 -*-
from perform.defines import *
from perform.object import Perform as CustomPerform

#导表开始
class Perform(CustomPerform):
	id = 3404
	name = "坚志"
	configInfo = {
		"概率":3,
	}
#导表结束
#受到法术伤害时有3%的几率将伤害变为1点

	def onSetup(self, w):
		self.addFunc(w, "onAbsorb", self.onAbsorb)
		
	def onAbsorb(self, att, vic, dp, attackType):
		if attackType.attackType == ATTACK_TYPE_PERFORM_MAG and rand(100) < self.configInfo["概率"]:
			return 1
		return dp


from common import *
from war.defines import *