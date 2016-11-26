#-*-coding:utf-8-*-
#作者:叶伟龙@龙川县赤光镇
import makeData.txtParser

#奖励表分析器
class cTxtParser(makeData.txtParser.cTxtParser):

	#override
	def getParseTxt(self):
		tFieldName=("Ratio","Item","Amount","IsBind","Announce","Class","TaskNo")
		lKey=[]
		lVal=[]
		lTupleItem=[]
		lLines=self.parseTxtTo2dGroup()
		sKey0=""

		for iRow,lLine in enumerate(lLines):
			sTemp=self.makeDict(tFieldName,lLine[1:],False)
			lTupleItem.append(sTemp)
			if lLine[0]!="":
				sKey0=lLine[0]
			if self.isLastInGroup(lLines,iRow,0):
				lKey.append(sKey0)
				sTemp=self.makeTuple(lTupleItem,True,2)
				lVal.append(sTemp)
				lTupleItem=[]

		return self.makeDict(lKey,lVal,True,1)





