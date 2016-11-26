# -*- coding: utf-8 -*-
from task.defines import *
from task.weekAnswer.t20001 import Task as customTask

#导表开始
class Task(customTask):
	parentId = 20001
	targetType = TASK_TARGET_TYPE_NPC
	icon = 2
	title = '''天问初试-第16题'''
	intro = '''前往$target处答题'''
	detail = '''前往$target处完成天问初试的第16题答题'''
	rewardDesc = ''''''
	goAheadScript = ''''''
	initScript = '''$EXAM1016'''
#导表结束