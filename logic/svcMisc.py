#-*-coding:utf-8-*-
#作者:叶伟龙@龙川县赤光镇
import serviceMisc_pb2
import endPoint
import misc


class cService(serviceMisc_pb2.gameServerMiscService):
	@endPoint.result
	def rpcHaHaHa(self,ep,who,reqMsg):return rpcHaHaHa(self,ep,who,reqMsg)


def rpcHaHaHa(self,ep,who,reqMsg):
	print 'receive...','rpcHaHaHa'
	ep.rpcHeHeHe()
	pass

import c
import timeU
import u
import log