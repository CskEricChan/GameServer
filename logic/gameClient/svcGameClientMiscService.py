#-*-coding:utf-8-*-
#作者:叶伟龙@龙川县赤光镇
import serviceMisc_pb2
import endPoint

class cService(serviceMisc_pb2.gameClientMiscService):
	@endPoint.result
	def rpcHeHeHe(self,ep,ctrlr,reqMsg):		
		print 'rpcHeHeHe called'
