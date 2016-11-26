# -*- coding: utf-8 -*-
from task.defines import *
from task.object import Task as customTask

#导表开始
class Task(customTask):
	parentId = 50001
	targetType = TASK_TARGET_TYPE_NPC
	icon = 2
	title = '''玄武龟·原因'''
	intro = '''与$target对话，了解始末'''
	detail = '''与仙子对话，了解她找你何事。'''
	rewardDesc = ''''''
	goAheadScript = ''''''
	initScript = '''E(10208,1001)'''

	npcInfo = {
		1001:{"名称":"赤身教门下","造型":"4504(0,1,0,0,0,0,0)","位置":"1130,46,82,6"},
		1002:{"名称":"人形螺旋草","造型":"1121(0,1,0,0,0,0,0)","位置":"1040,11,33,8"},
		1003:{"名称":"心术不正者","造型":"1211(0,1,0,0,0,0,0)","位置":"1040,9,32,4"},
		1004:{"名称":"灵猴","造型":"3007(0,1,0,0,0,0,0)","位置":"1130,30,70,6"},
		1005:{"名称":"慈云寺恶徒","造型":"4504(0,1,0,0,0,0,0)","位置":"1130,54,53,8"},
		1006:{"名称":"文雀","造型":"3005(0,1,0,0,0,0,0)","位置":"1040,80,34,6"},
		1007:{"名称":"魔道修士","造型":"4502(0,1,0,0,0,0,0)","位置":"1040,79,34,4"},
		1008:{"名称":"云狐","造型":"3008(0,1,0,0,0,0,0)","位置":"1130,40,72,8"},
		1009:{"名称":"惊惶的书生","造型":"2005(0,1,0,0,0,0,0)","位置":"1030,53,41,2"},
		1010:{"名称":"带伤巨蛇","造型":"3012(0,1,0,0,0,0,0)","位置":"2040,37,41,3"},
		1011:{"名称":"史家小女儿","造型":"3010(0,1,0,0,0,0,0)","位置":"2040,48,41,6"},
		1012:{"名称":"谜独行","造型":"4005(0,1,0,0,0,0,0)","位置":"2010,18,49,8","称谓":"怪妖"},
		1013:{"名称":"明珠","造型":"4508(0,1,0,0,0,0,0)","位置":"2010,106,19,8","称谓":"血神教圣女"},
		1014:{"名称":"谜独行","造型":"4005(0,1,0,0,0,0,0)","位置":"2010,18,49,8","称谓":"怪妖"},
		1015:{"名称":"明珠","造型":"4508(0,1,0,0,0,0,0)","位置":"2010,24,46,5","称谓":"血神教圣女"},
		1016:{"名称":"毕方","造型":"3013(0,1,0,0,0,0,0)","位置":"2030,35,59,4"},
		1017:{"名称":"地痞头目","造型":"5002(0,1,0,0,0,0,0)","位置":"1130,25,41,6"},
		1018:{"名称":"毕方","造型":"3013(0,1,0,0,0,0,0)","位置":"2030,35,59,4"},
		1019:{"名称":"鸠盘婆分神","造型":"4509(0,1,0,0,0,0,0)","位置":"2030,39,55,4"},
		1020:{"名称":"金姝","造型":"4008(0,1,0,0,0,0,0)","位置":"1060,55,44,5","称谓":"鸠盘婆大弟子"},
		1021:{"名称":"句芒","造型":"3009(0,1,0,0,0,0,0)","位置":"2010,54,59,5","称谓":"春神"},
		1022:{"名称":"明修罗","造型":"4006(0,1,0,0,0,0,0)","位置":"2010,59,58,6","称谓":"修罗宫宫主"},
		1023:{"名称":"红花姥姥","造型":"4008(0,1,0,0,0,0,0)","位置":"2010,72,57,6","称谓":"修罗宫副宫主"},
		1024:{"名称":"句芒","造型":"3009(0,1,0,0,0,0,0)","位置":"2010,54,59,5","称谓":"春神"},
		1025:{"名称":"阎王蝎","造型":"3015(0,1,0,0,0,0,0)","位置":"2040,29,42,8","称谓":"蝎子头领"},
		1026:{"名称":"毒尸","造型":"4005(0,1,0,0,0,0,0)","位置":"2040,85,12,8"},
	}

	eventInfo = {
		1001:{"点击":"D1001,DONE,T50002"},
		1002:{"点击":"$NPCTRI"},
		1003:{"点击":"D1002,DONE,T50003"},
		1004:{"点击":"SB1003","回复":"1:F1001;2:D1005","成功":"D1004,DONE,T50004","失败":"D1005"},
		1005:{"点击":"SB1006","回复":"1:R1004,TPM1046,DONE,DEFF"},
		1006:{"点击":"D1007,DONE,T50022"},
		1007:{"点击":"D1008,DONE,T50023"},
		1008:{"点击":"SB1009","回复":"1:F1002;2:D1011","成功":"D1010,DONE,T50024","失败":"D1011"},
		1009:{"点击":"POPI","成功":"D1012,DONE,T50025","失败":"D1013"},
		1010:{"点击":"SB1014","回复":"1:F1003;2:D1016","成功":"D1015,DONE,T50026","失败":"D1016"},
		1011:{"点击":"R1011,D1017,TPM1048,DONE"},
		1012:{"点击":"F1001"},
		1013:{"点击":"F1002"},
		1014:{"点击":"F1003"},
		1015:{"点击":"D1018,DONE,T50032"},
		1016:{"点击":"D1019,DONE,T50033"},
		1017:{"点击":"SB1020","回复":"1:F1004;2:D1022","成功":"D1021,DONE,T50034","失败":"D1022"},
		1018:{"点击":"D1023,DONE,T50035"},
		1019:{"点击":"SB1024","回复":"1:F1005;2:D1026","成功":"D1025,DONE,T50036","失败":"D1026"},
		1020:{"点击":"SB1027","回复":"1:R1020,TPM1047,DONE,DEFF"},
		1021:{"点击":"D1028,DONE,T50042"},
		1022:{"点击":"D1029,DONE,T50043"},
		1023:{"点击":"POPI","成功":"D1030,DONE,T50044","失败":"D1031"},
		1024:{"点击":"D1032,DONE,T50045"},
		1025:{"点击":"SB1033","回复":"1:F1006;2:D1035","成功":"D1034,DONE,T50046","失败":"D1035"},
		1026:{"点击":"SB1036","回复":"1:R1026,TPM1049,DONE,DEFF"},
		1027:{"点击":"D1037,DONE,T50052"},
		1028:{"点击":"SB1038","回复":"1:F1007;2:D1040","成功":"D1039,DONE,T50053","失败":"D1040"},
		1029:{"点击":"D1041,DONE,T50054"},
		1030:{"点击":"POPI","成功":"D1042,DONE,T50055","失败":"D1043"},
		1031:{"点击":"D1044,DONE,T50056"},
		1032:{"点击":"SB1045","回复":"1:R1032,TPM1050,DONE,DEFF"},
		1033:{"点击":"D1051,DONE,T50062"},
		1034:{"点击":"D1052,DONE,T50063"},
		1035:{"点击":"SB1053","回复":"1:F1008;2:D1055","成功":"D1054,DONE,T50064","失败":"D1055"},
		1036:{"点击":"D1056,DONE,T50065"},
		1037:{"点击":"POPI","成功":"D1057,DONE,T50066","失败":"D1058"},
		1038:{"点击":"D1059,DONE,T50067"},
		1039:{"点击":"SB1060","回复":"1:R1034,TPM1061,DONE,DEFF"},
		1040:{"点击":"D1062,DONE,T50072"},
		1041:{"点击":"D1063,DONE,T50073"},
		1042:{"点击":"D1064,DONE,T50074"},
		1043:{"点击":"SB1065","回复":"1:D1067;2:D1066,DONE,T50075"},
		1044:{"点击":"SB1068","回复":"1:F1009;2:D1070","成功":"D1069,DONE,T50076","失败":"D1070"},
		1045:{"点击":"D1071,DONE,T50077"},
		1046:{"点击":"D1072,DONE,T50078"},
		1047:{"点击":"SB1073","回复":"1:F1010;2:D1075","成功":"D1074,DONE,T50079","失败":"D1075"},
		1048:{"点击":"D1076,DONE,T50080"},
		1049:{"点击":"SB1077","回复":"1:R1035,TPM1078,DONE,DEFF"},
		1050:{"点击":"D1079,DONE,T50092"},
		1051:{"点击":"D1080,DONE,T50093"},
		1052:{"点击":"D1081,DONE,T50094"},
		1053:{"点击":"D1082,DONE,T50095"},
		1054:{"点击":"SB1083","回复":"1:F1011;2:D1085","成功":"D1084,DONE,T50096","失败":"D1085"},
		1055:{"点击":"D1086,DONE,T50097"},
		1056:{"点击":"D1087,DONE,T50098"},
		1057:{"点击":"SB1088","回复":"1:F1012;2:D1090","成功":"D1089,DONE,T50099","失败":"D1090"},
		1058:{"点击":"SB1091","回复":"1:R1036,TPM1092,DONE,DEFF"},
		1059:{"点击":"D1093,DONE,T50102"},
		1060:{"点击":"D1094,DONE,T50103"},
		1061:{"点击":"D1095,DONE,T50104"},
		1062:{"点击":"SB1096","回复":"1:F1013;2:D1098","成功":"D1097,DONE,T50105","失败":"D1098"},
		1063:{"点击":"D1099,DONE,T50106"},
		1064:{"点击":"SB1100","回复":"1:F1014;2:D1102","成功":"D1101,DONE,T50107","失败":"D1102"},
		1065:{"点击":"SB1103","回复":"1:F1015;2:D1105","成功":"D1104,DONE,T50108","失败":"D1105"},
		1066:{"点击":"D1106,DONE,T50109"},
		1067:{"点击":"SB1107","回复":"1:R1037,TPM1108,DONE,DEFF"},
		1068:{"点击":"D1109,DONE,T50112"},
		1069:{"点击":"D1110,DONE,T50113"},
		1070:{"点击":"D1111,DONE,T50114"},
		1071:{"点击":"SB1112","回复":"1:F1016;2:D1114","成功":"D1113,DONE,T50115","失败":"D1114"},
		1072:{"点击":"D1115,DONE,T50116"},
		1073:{"点击":"SB1116","回复":"1:F1017;2:D1118","成功":"D1117,DONE,T50117","失败":"D1118"},
		1074:{"点击":"SB1119","回复":"1:R1038,TPM1120,DONE,DEFF"},
	}

	rewardInfo = {
		1001:{},
		1002:{},
		1003:{},
		1004:{"宠物":(1002,1,)},
		1005:{},
		1006:{},
		1007:{},
		1008:{},
		1009:{},
		1010:{},
		1011:{},
		1012:{},
		1013:{},
		1014:{},
		1015:{},
		1016:{},
		1017:{},
		1018:{},
		1019:{},
		1020:{"宠物":(1005,1,)},
		1021:{},
		1022:{},
		1023:{},
		1024:{},
		1025:{},
		1026:{"宠物":(1003,1,)},
		1027:{},
		1028:{},
		1029:{},
		1030:{},
		1031:{},
		1032:{"宠物":(1004,1,)},
		1033:{},
		1034:{"宠物":(1006,1,)},
		1035:{"宠物":(1007,1,)},
		1036:{"宠物":(1008,1,)},
		1037:{"宠物":(1010,0,)},
		1038:{"宠物":(1009,1,)},
	}

	rewardPropsInfo = {}

	groupInfo = {
		9003:(20109,),
		9001:(1005,1006,1007,1008,),
		9002:(1013,1014,1015,1016,),
	}

	chatInfo = {
		1001:'''你愿意前来相助，很好。此次是因为我算出潜修的玄武龟将逢灾劫，但又无暇前去，可否请你走一趟？''',
		1002:'''此去与魔道交手时需多加小心，避免惹出大事。''',
		1003:'''多管闲事的家伙，让你尝尝厉害！\nQ出手教训\nQ只是路过''',
		1004:'''可恶……等师父回来……一定会替我报仇……''',
		1005:'''知道自己分量，胆怯了吧？''',
		1006:'''魔人虽灭，但潜修处已不安全。与其再找，不如与$SEX1一同上路，互相督促修行吧。如此一来，修行之路虽漫长，却不会寂寞了。\nQ带异兽走\nQ考虑一下''',
		1007:'''给异兽治伤的灵药已所剩无几，麻烦$SEX1替我去找螺旋草，向它要一罐灵药吧。''',
		1008:'''死缠不放，魔道之人真是恶心。''',
		1009:'''居然追到这里，那只能和你打一场了！\nQ先行一战\nQ先行解释''',
		1010:'''啊……我还以为$SEX1是来追杀这名坠崖之人的，误会了，真是抱歉。''',
		1011:'''哼，还以为有多大本事。''',
		1012:'''啊——！你！你没受伤！''',
		1013:'''$SEX1，这人急需药物救治。''',
		1014:'''哼，终于抓到这异兽了，快把所有灵蜜交出，否则给你点颜色瞧瞧！\nQ与之交手\nQ稍待片刻''',
		1015:'''……居然……输了……''',
		1016:'''哼，自不量力。''',
		1017:'''异兽亦有善良之心，这是好事；但也容易被邪恶之人趁机利用，以后需多加提防。''',
		1018:'''淘气的灵猴出走了，有人在城南见过它，$SEX1能替我走一趟吗？''',
		1019:'''你是仙子派来找我的人？	*A*nA**SS*$S1S$(为何灵猴像在计划着什么……)\n嗯。仙子说外头危险，让你回去鼎中继续修行。''',
		1020:'''想让我回去，得先问过我的棍子！\nQ一试高低\nQ等等再说''',
		1021:'''嘿嘿，终于来了个帮手！''',
		1022:'''要等到什么时候？''',
		1023:'''其实……是城西有慈云寺的恶徒盘踞，我对付不了他，你刚好来做个帮手！\n除了那恶人，我就跟你回去！	*A*nA**SS*$S2S$原来是这个打算……不愧是猴子……''',
		1024:'''多个帮手，就以为能对付我了？\nQ斩妖除魔\nQ临阵退缩''',
		1025:'''我……败给……这等……无名小辈……不服……''',
		1026:'''不是对手，就赶快滚！''',
		1027:'''原来是为了保护百姓，而不是淘气玩耍，这次尚可原谅。	既然你觉得禹鼎中太过苦闷，那就与$SEX1做个伴儿吧。\nQ带异兽走\nQ考虑一下''',
		1028:'''隐居碧凝崖的文雀自从出过门后，就一直闷闷不乐，请$SEX1替我去问问它为何会这样吧。''',
		1029:'''上次，我看到在天上飞的大鹏，我也想飞，可我太胖了……	*A*nA**SS*$S2S$因为这个，你才闷闷不乐？	*A文雀A**S3005S*$S1S$我……我修为太低，又太胖，所以飞不起来……我听说杜仲能轻身健体，$SEX1能替我找来吗？''',
		1030:'''多谢$SEX1！''',
		1031:'''$SEX1……杜仲……''',
		1032:'''文雀只知其一却不知其二，杜仲确能轻身健体，但对异兽来说则不一定。	你回去看看文雀，确认它是否还安好。	*A*nA**SS*$S1S$（原来异兽与人有这等分别，快回去看看文雀。）嗯！''',
		1033:'''这小家伙修为太低，做道下酒菜倒还可以。\nQ救下文雀\nQ袖手旁观''',
		1034:'''哼，今天先不跟你计较！''',
		1035:'''先掂量好自己的本事！''',
		1036:'''即使是药，服用对象不同，后果也不同。	文雀就是个教训。只看到别人成功，自己盲目模仿，未必能像别人一样成功。\nQ带异兽走\nQ考虑一下''',
		1037:'''我在城南感受到了云狐一脉的气息，应是有云狐被抓来了。\n请$SEX1前去救出那可怜的孩子，送它回山吧。	*A*nA**SS*$S2S$是，我这就去。''',
		1038:'''可恶的人类！\nQ打败云狐\nQ试图解释''',
		1039:'''人类杀了我的父母，还剥下了他们的皮……我一定要报仇！''',
		1040:'''人类说的每一个字每一句话，我都不会听！''',
		1041:'''既然输给你，要杀就杀，别啰嗦！	*A*nA**SS*$S2S$喂，我不是……	*A云狐A**S3008S*$S1S$不用多说了！	*A*nA**SS*$S2S$（它什么都听不进，还是先给它找来治伤药物吧。）你留在这，我稍后就送你回山。''',
		1042:'''别以为一点小恩小惠我就会原谅人类！''',
		1043:'''不就是想要毛皮吗，何必故弄玄虚？''',
		1044:'''你真的要放我回去？	*A*nA**SS*$S2S$我又没必要骗你，快走吧。	*A云狐A**S3008S*$S1S$……哼，就算你放了我，我也绝对不会原谅人类。	*A*nA**SS*$S2S$嗯，我能理解你，回去吧。\n别再让人类抓到了。''',
		1045:'''云狐一脉本身并无过错，只是由于人的贪婪才使它们遭受劫难。	希望云狐一脉能延续下去，不致于被捕杀净尽吧。\nQ带异兽走\nQ考虑一下''',
		1046:'''恭喜获得异兽·#C05玄武龟#n''',
		1047:'''恭喜获得异兽·#C05灵猴#n''',
		1048:'''恭喜获得异兽·#C05螺旋草#n''',
		1049:'''恭喜获得异兽·#C05文雀#n''',
		1050:'''恭喜获得异兽·#C05云狐#n''',
		1051:'''你来得正好，最近城中有不少小孩无故失踪，史镖头家的小女儿一个时辰前也被怪物掳走,请你赶快前去寻找那孩子。	*A*nA**SS*$S2S$好，只是不知道那怪物长什么样，向哪个方向逃了？	*A齐霞儿A**S4508S*$S1S$据史夫人所说，那怪物高大魁梧，力气极大，一路往西逃跑了。	*A*nA**SS*$S2S$好，我这就前去！''',
		1052:'''好、好可怕……救命啊！怪、怪物！	*A*nA**SS*$S2S$这么害怕，你看到了什么？	*A惊惶的书生A**S2005S*$S1S$我、我刚才看到一条好大的蛇和一只巨熊在搏、搏斗……\n我差点就被它们弄死……好不容易才逃掉……	*A*nA**SS*$S2S$（蛇？还有熊？怎么回事？）\n我知道了，你这书生赶快回去休息吧。''',
		1053:'''咝咝——咝咝——（巨蛇吐着信子，死死盯着你）\nQ收拾巨蛇\nQ休整片刻''',
		1054:'''（巨蛇横尸就地，毒涎流到的地方草木焦枯）''',
		1055:'''咝咝——咝咝——（巨蛇流着毒涎看着你）''',
		1056:'''呜呜呜，你是个好人，大熊为了保护我受了伤，你能不能帮我找来给大熊治伤的药？	*A*nA**SS*$S2S$（这只巨熊确实伤势不轻，先替它找来伤药吧）好，你在这里等我。	*A史家小女儿A**S3010S*$S1S$好，我在这里等你，你一定要回来啊。''',
		1057:'''谢谢好心$SEX1！''',
		1058:'''呜呜……大熊流了好多血……大熊不能死……呜呜……''',
		1059:'''呜呜……我在家附近玩的时候，被这蛇叼走了，大熊为了保护我，就和这蛇打架……后面……也不知道怎么来到这里了——	听大熊说，那蛇是赤、赤身教的人变成的，专门抓小孩子……	*A*nA**SS*$S2S$嗯？赤身教？\n（之前玄武龟也是他们……这回……）	看来这个赤身教不是什么好东西，得回去跟仙子说一下才行。	小姑娘，我送你回家吧。	*A史家小女儿A**S3010S*$S1S$好……谢谢好心$SEX1！''',
		1060:'''你说这是赤身教徒所为？这是苗疆教派，一贯行事诡秘，教主鸠盘婆脾气乖僻，但未听闻有什么恶行。	此事……我抽空向父亲汇报一下吧，你日后遇见赤身教徒的话，行事也需小心。	那史家姑娘与巨熊身具仙缘，可与你一起修行，你愿意把他们带上吗？\nQ带异兽走\nQ考虑一下''',
		1061:'''恭喜获得异兽·#C05傀儡熊#n''',
		1062:'''金鹏被妖人的毒焰灼伤，到现在还没有好转，$SEX1麻烦你帮我走一趟蜀山，问问我父亲妙一真人该如何医治吧。	*A*nA**SS*$S2S$好，我这就去！''',
		1063:'''不必多礼。找我何事？	*A*nA**SS*$S1S$金鹏被妖人毒焰灼伤，一直不见好转，霞儿仙子让我来问要如何医治。	*A齐漱溟A**S4502S*$S2S$原来如此。\n要医治并不难，但所需的药只有怪妖谜独行有，然而它在锁妖塔中……塔中妖物众多，入内需万分小心。	*A*nA**SS*$S1S$怪妖？	*A齐漱溟A**S4502S*$S2S$这妖脾气古怪又无比吝啬，喜欢给人出谜语，所以称为怪妖。	*A*nA*SS*$S1S$多谢前辈指点，晚辈这就入塔找那怪妖去！''',
		1064:'''嘘——别吵！老妖我正在想谜语！	*A*nA**SS*$S2S$(这家伙……看来要想想办法)\n自己给自己出谜语，是怕太简单被别人解答出来，所以不敢让别人听到吧？	*A谜独行A**S4005S*$S1S$胡说八道！老妖我的谜语肯定没几个人能解出来！	*A*nA**SS*$S2S$（嘿嘿，果然行得通）\n你把你的谜语说出来，我一定能猜到！不过要是我猜出你的谜语，你要把身上的灵药给我，敢不敢？	*A谜独行A**S4005S*$S1S$哼！有什么不敢的！''',
		1065:'''哼——听好了！我的谜语是：一阴一暗，一短一长，一昼一夜，一热一凉。猜一个字，你说是什么字吧——\nQ二\nQ明''',
		1066:'''我、我的题目就这样被解开了？……药给你，滚！我要想更多的谜语了！''',
		1067:'''哼，只会说大话的愚蠢之辈，滚吧！''',
		1068:'''哈，终于等到你了！\n我是血神教圣女明珠，把怪妖的灵药交出，可免你一死，否则别怪我下手无情！\nQ与之交手\nQ再等片刻''',
		1069:'''你……你修为这么低，怎么能够打败我？''',
		1070:'''呵，怕了就赶快把药交出来！''',
		1071:'''交出灵药，不然我、我就杀了你！	*A*nA**SS*$S2S$等等——！你先说为什么要这药？说不定我能想个办法。	*A明珠A**S4508S*$S1S$真的？骗我的话，我也会杀了你哟。	*A*nA**SS*$S2S$（这血神教的圣女……怎么老把杀挂在嘴边……）\n不骗你，你说吧。	*A明珠A**S4508S*$S1S$我……听说神貅角能治所有的伤，所以想把我哥坐骑的角锯下来……	没想到神貅被割了角之后，就、就一直流血，停不下来……	*A*nA**SS*$S2S$这……我回去谜独行那，看他能不能再给一份灵药？''',
		1072:'''你怎么又回来了？快滚！	*A*nA**SS*$S2S$喂喂喂，别这么急着赶人，我再答一道你的谜语，你再给我一份灵药，怎么样？	*A谜独行A**S4005S*$S1S$(谜独行瞪眼看着你)\n你……你！	*A*nA**SS*$S2S$咦，你怎么头发竖起来了？	*A谜独行A**S4005S*$S1S$你！！欺妖太甚！找死！''',
		1073:'''谁敢再动我的灵药，我就吃掉谁！\nQ动手教训\nQ迟疑片刻''',
		1074:'''滚！你们连老妖怪的东西都抢！什么名门正道！''',
		1075:'''老妖我一定要吃掉你！说什么也晚了！''',
		1076:'''嘻嘻，谢谢你啦，这家伙实在不好对付，这回终于拿到药了。\n以后遇到修罗宫的人，你就说你是我的朋友，这样他们就不会为难你了。	*A*nA**SS*$S2S$朋友……你可是血神教的圣女……	*A明珠A**S4508S*$S1S$难道血神教圣女就一定是阴险毒辣，连个朋友都不能交吗？	*A*nA**SS*$S2S$这……倒也不是。	*A明珠A**S4508S*$S1S$那就这样说好了，做个朋友吧——我先回宫给神貅上药，日后有机会再见！''',
		1077:'''嗯？这就是从怪妖那取得的灵药？这药见效好快，金鹏的伤已经好了大半。	感谢你为金鹏奔波劳碌，如今它也恢复得差不多了，就让它在你身边做个帮手吧。\nQ带异兽走\nQ考虑一下''',
		1078:'''恭喜获得异兽·#C05金鹏#n''',
		1079:'''在凌云大佛那潜修的毕方，羽毛无故消失了许多，修为也倒退大半，麻烦你帮我查探其中内情，看看到底是怎么回事。	*A*nA**SS*$S2S$好，我这就去！''',
		1080:'''是仙子让你来找我的？	*A*nA**SS*$S2S$是，仙子很担心你，所以让我来问问是怎么回事。	*A毕方A**S3010S*$S2S$请你回报仙子，我什么事都没有，请她不要担心。	*A*nA**SS*$S1S$这……好吧。''',
		1081:'''嗯——毕方不说也在我意料之内。	不过我发现唐百草那有毕方羽毛制成的羽衣出售，想来是毕方自愿送给她的，请你帮我问问唐百草，这到底是怎么回事吧。	*A*nA**SS*$S1S$毕方羽毛做的羽衣？好，我去问问。''',
		1082:'''$SEX1想要这件羽衣吗？	*A*nA**SS*$S2S$不，我只是觉得这羽衣巧夺天工，想知道来源而已。	*A唐百草A**S2004S*$S1S$这衣服？这衣服是我义女织的，只是她现在……现在……唉，我也不知道她去哪了……	嗯？糟了，那、那不是城里有名的地痞头子吗？	肯定是他们想来抢这羽衣，这，$SEX1能不能帮帮老太婆，教训他们一顿？''',
		1083:'''老子想要什么，你们就得乖乖交上！不然让你们好看！\nQ痛揍一顿\nQ路过而已''',
		1084:'''哎哟——今天大爷不舒服，下、下次再给你好看！''',
		1085:'''嘿嘿，怕了的话就乖乖交上羽衣！''',
		1086:'''你去过我义母那了？唉，既然你知道了，那就告诉你吧。	我上次变成人形偷溜出去，不小心遇到暴风雪，是她救了我，我想报答她，就做了她的义女。	但后面我修为损耗太多，在她眼前现出兽形，就慌忙逃走了……	*A*nA**SS*$S2S$那你为什么不说出来？	*A毕方A**S3013S*$S1S$我……我怕吓到她，所以就不敢说出来……	既然你知道了，你帮我去问问，是否有吓着她吧。''',
		1087:'''嫌恶？唉……老太婆活了这么久，什么人没见过？坏起来的人，能比野兽更凶狠十倍！	请$SEX1转告她，只要是好的，管她是人是兽，老太婆我根本就不在意啊。	*A*nA**SS*$S1S$嗯，我这就回去告诉她！''',
		1088:'''你就是那个教训了我门下弟子的家伙？哼，虽然他们作了恶，但也轮不到你这些外人来替我清理门户！	能击败我的分神的话，暂且饶你一命，否则便马上将你拘回苗疆发落！\nQ冒险一试\nQ犹豫片刻''',
		1089:'''哼，实力勉强可以。\n这是告诫，苗疆有自己的规矩，无需外人插手！''',
		1090:'''哼，原来是草包一个。''',
		1091:'''是人是兽，都在于一颗心而已。毕方能解开心结，实在幸运。	只是它修为损耗太过，我无法照顾它，不知$SEX1你是否愿意把它带在身边？\nQ带异兽走\nQ考虑一下''',
		1092:'''恭喜获得异兽·#C05毕方#n''',
		1093:'''你来了。如今已是春天，但依然冰封三尺，严寒迫人，我们都束手无策。	听闻苗疆人信奉女娲大神，或能从他们大族长那得知为何春天不来的原因。	*A*nA**SS*$S2S$是，我这就前往苗疆。''',
		1094:'''春天不来？哼，女娲大神的旨意也不是随便能告诉你们这些人的，否则岂不是亵渎了大神？你回去吧！	*A*nA**SS*$S2S$这……好吧。''',
		1095:'''喂——过来过来。师父让我告诉你，应该是春神被人用邪术拘禁了，所以才会一直冬天。	*A*nA**SS*$S2S$师父？但是……	*A金姝A**S4008S*$S1S$哎呀，师父是为了立威而已啦，不然随随便便就把神旨告诉外人，其他苗疆理老很容易不服的。	师父还说，春神应该是被拘在锁妖塔里了，你前去时要多加小心。	*A*nA**SS*$S2S$好，我知道了！''',
		1096:'''恶、恶徒……还我法器！可恶！一定要惩治你这种恶徒才行！受死！\nQ制服句芒\nQ稍待片刻''',
		1097:'''你……你不是那些修罗宫的恶人？''',
		1098:'''恶人！受死！''',
		1099:'''头好痛……你、你不是那些修罗宫的恶人？	*A*nA*SS*$S2S$我是来找你的，你一直没有出现，现在春天已到，却还是冬天的样子。	*A句芒A**S3009S*$S1S$春天已到？！等等……糟了！快逃！这是个陷阱！	*A*nA*SS*$S2S$陷阱？！	*A句芒A**S3009S*$S1S$这是修罗宫的人设下的陷阱！''',
		1100:'''想逃？已经晚了！\n本来以为能引来三英二云，没想到来的只是个无名小卒！	哼，也罢，如今所需的法器已经到手，就让你死得痛快点！\nQ与之交手\nQ犹豫再三''',
		1101:'''本尊倒是小看了你。''',
		1102:'''如此无用的家伙，实在令人恶心。''',
		1103:'''想到哪去？你的对手是姥姥我！留下来吧！\nQ击败红花\nQ犹豫片刻''',
		1104:'''你……果然不能小视！''',
		1105:'''看来能逃过宫主攻击，也只是靠运气而已。''',
		1106:'''那些恶人把我的法器抢走了，也不知道他们在谋划什么……	如今状况，我只能长驻人间，等找到法器再回去吧。	*A*nA**SS*$S1S$那我带你去见异兽仙子，相信她会安排好你的。''',
		1107:'''修罗宫……他们到底在谋划什么呢？春神的话……请她与你作伴吧。	毕竟修罗宫的人与你已有过节，日后相遇时伺机抢回法器，也不是不可能的事。\nQ带异兽走\nQ考虑一下''',
		1108:'''恭喜获得异兽·#C05句芒#n''',
		1109:'''$SEX1，最近云顶村发生不少怪事，麻烦你走一趟，看看到底是怎么回事吧。	*A*nA**SS*$S1S$怪事？	*A齐霞儿A**S4508S*$S2S$嗯。但具体什么情况我还不清楚，只能请你前往了。	*A*nA**SS*$S1S$好，我这就动身前去。''',
		1110:'''哇——！$SEX1你回来了！	*A*nA**SS*$S1S$嗯，听说村里最近发生不少怪事，我特地回来的。\n你能告诉我，最近村里都发生过什么怪事吗？	*A小虎儿A**S2006S*$S2S$怪事啊？等我想想……	噢，最近村子里多了好多蜇人的蝎子，好多人被蛰了，娘亲都不让我和小翠儿出来玩了。	*A*nA**SS*$S1S$(奇怪，这不是蝎子活动的季节啊？)\n那……小虎儿你知道哪里的蝎子最多吗？	*A小虎儿A**S2006S*$S2S$知道啊！从莽苍山那条路过来，密密麻麻都是蝎子呢！''',
		1111:'''嘎！人类！吃了这个人类！！孩儿们，为了抢回洞府，把这个人吃了！	*A*nA**SS*$S1S$这群蝎子——糟糕！得小心它们的毒！''',
		1112:'''据说人心最毒，为了抢回洞府，把这个人吃了！\nQ打败蝎王\nQ落荒而逃''',
		1113:'''嘎……这个人类我们吃不了……''',
		1114:'''孩儿们！别让这人跑了！''',
		1115:'''为什么要吃人？嘎，因为一个毒尸霸占了我们的洞府，我们的毒性拼不过它，嘎，所以被赶出来了……	听说人心最毒，嘎，所以我们要变得更毒，抢回洞府！	*A*nA**SS*$S2S$这……你们不明白，人心的毒和你们的毒不是同一种意思。	*A阎王蝎A**S3004S*$S1S$嘎？什么意思？嘎，不明白……反正、反正你想让我们不吃人的话，就帮我们把洞府抢回来！''',
		1116:'''想帮那些傻蝎子？哈哈哈哈——就看看你有多少本事吧！\nQ除去毒尸\nQ休整片刻''',
		1117:'''不……不可能！我是不生不死的毒尸，怎么、怎么会败……''',
		1118:'''胆怯？心虚？哈哈哈哈，晚了！''',
		1119:'''云顶村的怪事原来是阎王蝎所为，如今平息了就好。但阎王蝎本身带有戾气，如果不加修炼，则容易落入邪道，你是否愿意把它带在身边，与它一同修行？\nQ带异兽走\nQ考虑一下''',
		1120:'''恭喜获得异兽·#C05阎王蝎#n''',
	}

	branchInfo = {
		1001:(
			{"条件":0,"脚本":"L(9004,2)"},
			{"条件":10,"脚本":"L(9005,1)"},
			{"条件":20,"脚本":"L(9006,1)"},
		),
	}

	fightInfo = {
		1002:(
			{"类型":1,"名称":"人形螺旋草","造型":"1121(1,1,1,1,1)","染色":"0,0,0,0,0","能力编号":"2001","数量":"1","技能":(1111,1112,),"站位":(1,)},
			{"类型":0,"名称":"螺旋草","造型":"3003(0,1,0,0,0)","染色":"0,0,0,0,0","能力编号":"2001","数量":"3","站位":(6,7,8,)},
		),
		1003:(
			{"类型":1,"名称":"心术不正者","造型":"1211(1,1,1,1,1)","染色":"0,0,0,0,0","能力编号":"2001","数量":"1","技能":(5401,),"站位":(1,)},
			{"类型":0,"名称":"草怪","造型":"3003(0,1,0,0,0)","染色":"0,0,0,0,0","能力编号":"2001","数量":"3","站位":(6,7,8,)},
		),
		1004:(
			{"类型":1,"名称":"灵猴","造型":"3007(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1001","数量":"1","技能":(5307,5203,5420,),"站位":(1,)},
			{"类型":0,"名称":"灵草","造型":"3006(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1002","数量":"3","站位":(6,7,8,)},
		),
		1005:(
			{"类型":1,"名称":"慈云寺恶人","造型":"4504(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1003","数量":"1","技能":(5201,5202,5410,5420,),"站位":(1,)},
			{"类型":0,"名称":"小妖","造型":"3006(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1004","数量":"3","站位":(6,7,8,)},
		),
		1001:(
			{"类型":1,"名称":"赤身教门下","造型":"4504(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1005","数量":"1","技能":(5209,5210,5406,5416,),"站位":(1,)},
			{"类型":0,"名称":"花妖","造型":"3009(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1006","数量":"3","站位":(6,7,8,)},
		),
		1006:(
			{"类型":1,"名称":"魔道修士","造型":"4502(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1007","数量":"1","技能":(5209,5210,5408,5418,),"站位":(1,)},
			{"类型":0,"名称":"旁门左道","造型":"4001(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1008","数量":"4","技能":(5403,5413,),"站位":(7,8,9,10,)},
		),
		1007:(
			{"类型":1,"名称":"云狐","造型":"3008(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1009","数量":"1","技能":(5312,5210,5407,),"站位":(1,)},
			{"类型":0,"名称":"草妖","造型":"3006(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1010","数量":"4","技能":(5402,5412,),"站位":(7,8,9,10,)},
		),
		1008:(
			{"类型":1,"名称":"带伤巨蛇","造型":"3012(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1011","数量":"1","技能":(5416,5411,),"站位":(1,)},
			{"类型":0,"名称":"小妖","造型":"3006(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1012","数量":"4","技能":(5401,),"站位":(7,8,9,10,)},
		),
		1009:(
			{"类型":1,"名称":"明珠","造型":"4508(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1013","数量":"1","技能":(5409,5404,),"站位":(1,)},
			{"类型":0,"名称":"修罗侍女","造型":"4509(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1014","数量":"4","技能":(5404,),"站位":(2,3,4,5,)},
		),
		1010:(
			{"类型":1,"名称":"谜独行","造型":"4005(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1015","数量":"1","技能":(5420,5415,),"站位":(1,)},
			{"类型":0,"名称":"好奇小妖","造型":"3005(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1016","数量":"4","技能":(5415,),"站位":(6,7,8,9,)},
		),
		1011:(
			{"类型":1,"名称":"地痞头目","造型":"5002(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1017","数量":"1","技能":(5409,5404,),"站位":(1,)},
			{"类型":0,"名称":"地痞喽啰","造型":"4001(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1018","数量":"6","技能":(5414,),"站位":(2,3,6,7,8,9,)},
		),
		1012:(
			{"类型":1,"名称":"鸠盘婆分神","造型":"4509(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1019","数量":"1","技能":(5407,5402,),"站位":(1,)},
			{"类型":0,"名称":"苗女","造型":"4008(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1020","数量":"5","技能":(5411,),"站位":(6,7,8,9,10,)},
		),
		1013:(
			{"类型":1,"名称":"句芒","造型":"3009(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1021","数量":"1","技能":(5406,5401,),"站位":(1,)},
			{"类型":0,"名称":"花精","造型":"3006(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1022","数量":"4","技能":(5401,),"站位":(7,8,9,10,)},
		),
		1014:(
			{"类型":1,"名称":"明修罗","造型":"4006(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1021","数量":"1","技能":(5408,5403,),"站位":(1,)},
			{"类型":0,"名称":"修罗宫弟子","造型":"4504(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1022","数量":"4","技能":(5413,),"站位":(7,8,9,10,)},
		),
		1015:(
			{"类型":1,"名称":"红花姥姥","造型":"4008(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1021","数量":"1","技能":(5410,5405,),"站位":(1,)},
			{"类型":0,"名称":"妖狐","造型":"3008(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1022","数量":"4","技能":(5404,),"站位":(6,7,8,9,)},
		),
		1016:(
			{"类型":1,"名称":"阎王蝎","造型":"3015(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1017","数量":"1","技能":(5418,5413,),"站位":(1,)},
			{"类型":0,"名称":"花妖","造型":"3009(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1018","数量":"4","技能":(5415,),"站位":(7,8,9,10,)},
		),
		1017:(
			{"类型":1,"名称":"毒尸","造型":"4005(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1019","数量":"1","技能":(5406,5401,),"站位":(1,)},
			{"类型":0,"名称":"妖灵","造型":"4001(0,1,0,0,0,0,0)","染色":"0,0,0,0,0","能力编号":"1020","数量":"5","技能":(5401,),"站位":(6,7,8,9,10,)},
		),
	}

	ableInfo = {
		2001:{"等级":"LV","生命":"B*1","真气":"B*1","物理伤害":"B*1","法术伤害":"B*1","物理防御":"B*1","法术防御":"B*1","速度":"B*1","治疗强度":"B*1","封印命中":"B*1","抵抗封印":"B*1","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1001:{"等级":"21","生命":"B*0.75","真气":"B*1","物理伤害":"B*0.81","法术伤害":"B*0.56","物理防御":"B*0.7","法术防御":"B*0.49","速度":"B*0.8","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1002:{"等级":"20","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.65","法术伤害":"B*0.65","物理防御":"B*0.48","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1003:{"等级":"22","生命":"B*0.75","真气":"B*1","物理伤害":"B*0.81","法术伤害":"B*0.81","物理防御":"B*0.6","法术防御":"B*0.6","速度":"B*0.8","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1004:{"等级":"21","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.65","法术伤害":"B*0.65","物理防御":"B*0.48","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1005:{"等级":"11","生命":"B*0.75","真气":"B*1","物理伤害":"B*0.56","法术伤害":"B*0.81","物理防御":"B*0.49","法术防御":"B*0.7","速度":"B*0.8","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1006:{"等级":"10","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.65","法术伤害":"B*0.65","物理防御":"B*0.48","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1007:{"等级":"12","生命":"B*0.75","真气":"B*1","物理伤害":"B*0.81","法术伤害":"B*0.81","物理防御":"B*0.6","法术防御":"B*0.6","速度":"B*0.8","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1008:{"等级":"10","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.65","法术伤害":"B*0.65","物理防御":"B*0.48","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1009:{"等级":"22","生命":"B*0.75","真气":"B*1","物理伤害":"B*0.56","法术伤害":"B*0.81","物理防御":"B*0.49","法术防御":"B*0.7","速度":"B*0.8","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1010:{"等级":"20","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.65","法术伤害":"B*0.65","物理防御":"B*0.48","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1011:{"等级":"33","生命":"B*0.75","真气":"B*1","物理伤害":"B*0.81","法术伤害":"B*0.65","物理防御":"B*0.48","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1012:{"等级":"30","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.56","法术伤害":"B*0.65","物理防御":"B*0.48","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1013:{"等级":"33","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.65","法术伤害":"B*0.81","物理防御":"B*0.48","法术防御":"B*0.7","速度":"B*0.64","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1014:{"等级":"30","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.56","法术伤害":"B*0.65","物理防御":"B*0.48","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1015:{"等级":"33","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.81","法术伤害":"B*0.65","物理防御":"B*0.49","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1016:{"等级":"30","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.65","法术伤害":"B*0.65","物理防御":"B*0.49","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1017:{"等级":"43","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.81","法术伤害":"B*0.65","物理防御":"B*0.49","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1018:{"等级":"40","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.65","法术伤害":"B*0.65","物理防御":"B*0.49","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1019:{"等级":"43","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.65","法术伤害":"B*0.81","物理防御":"B*0.48","法术防御":"B*0.7","速度":"B*0.64","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1020:{"等级":"41","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.65","法术伤害":"B*0.65","物理防御":"B*0.48","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1021:{"等级":"53","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.65","法术伤害":"B*0.81","物理防御":"B*0.48","法术防御":"B*0.7","速度":"B*0.64","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1022:{"等级":"51","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.56","法术伤害":"B*0.65","物理防御":"B*0.48","法术防御":"B*0.49","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1023:{"等级":"53","生命":"B*0.75","真气":"B*1","物理伤害":"B*0.81","法术伤害":"B*0.65","物理防御":"B*0.6","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.56","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
		1024:{"等级":"51","生命":"B*0.6","真气":"B*1","物理伤害":"B*0.56","法术伤害":"B*0.65","物理防御":"B*0.48","法术防御":"B*0.48","速度":"B*0.64","治疗强度":"B*0.45","封印命中":"B*0","抵抗封印":"B*0.8","物理抗性":0,"法术抗性":0,"攻击修炼":0,"物防修炼":0,"法防修炼":0},
	}

	lineupInfo = {
	}

	configInfo = {
		"生成路径":"pett",
	}

	groupTask = {
		15:(
			{"标题":"玄武龟","宠物编号":1002,"任务":(50001,50002,50003,50004,)},
			{"标题":"文雀","宠物编号":1003,"任务":(50041,50042,50043,50044,50045,50046,)},
		),
		25:(
			{"标题":"灵猴","宠物编号":1005,"任务":(50031,50032,50033,50034,50035,50036,)},
			{"标题":"云狐","宠物编号":1004,"任务":(50051,50052,50053,50054,50055,50056,)},
		),
		35:(
			{"标题":"傀儡熊","宠物编号":1006,"任务":(50061,50062,50063,50064,50065,50066,50067,)},
			{"标题":"金鹏","宠物编号":1007,"任务":(50071,50072,50073,50074,50075,50076,50077,50078,50079,50080,)},
		),
		45:(
			{"标题":"毕方","宠物编号":1008,"任务":(50091,50092,50093,50094,50095,50096,50097,50098,50099,)},
			{"标题":"阎王蝎","宠物编号":1009,"任务":(50111,50112,50113,50114,50115,50116,50117,)},
		),
		55:(
			{"标题":"句芒","宠物编号":1010,"任务":(50101,50102,50103,50104,50105,50106,50107,50108,50109,)},
		),
	}
#导表结束
	def abort(self, who):
		'''放弃任务
		'''
		customTask.abort(self, who)
		lv,taskList = self.findTaskGroupList(self.id)
		if lv:
			petCompleteNo = who.taskCtn.fetch("petCom", {})
			comList = petCompleteNo.get(lv, [])
			for no in taskList:
				if no in comList:
					comList.remove(no)
			petCompleteNo[lv] = comList
			who.taskCtn.set("petCom", petCompleteNo)
		task.pett.autoPetTask(who)

	def findTaskGroupList(self, id):
		'''根据任务编号返回属于哪一组
		'''
		for lv,allInfo in self.groupTask.iteritems():
			for index,info in enumerate(allInfo):
				if self.id in info.get("任务", []):
					return lv,info.get("任务", [])
		return 0,[]

	def findTaskGroup(self, id):
		'''根据任务编号返回属于哪一组
		'''
		for lv,allInfo in self.groupTask.iteritems():
			for index,info in enumerate(allInfo):
				if self.id in info.get("任务", []):
					return lv, index
		return 0,0

	def canRemoveLeadTad(self, who):
		'''是否可以删除50000任务
		'''
		petComplete = who.taskCtn.fetch("petCom", {})
		lvKeys = self.groupTask.keys()
		lvKeys.sort()
		count = len(lvKeys)
		for i,lv in enumerate(lvKeys):
			if lv > who.level:	#等级不足，可以删除
				return True
			completeTask = petComplete.get(lv, [])
			allInfo = self.groupTask[lv]
			for info in allInfo:
				taskList = info.get("任务", [])
				for no in taskList:
					if no not in completeTask:
						#还没全部完成，不能删除
						return False
		return True


	def onMissionDone(self, who, npcObj):
		'''
		'''
		#找出属性哪个等级组任务
		lv,index = self.findTaskGroup(self.id)
		if not lv:
			return

		#保存已完成过的编号
		petCompleteNo = who.taskCtn.fetch("petCom", {})
		if self.id not in petCompleteNo.get(lv, []):
			petCompleteNo.setdefault(lv, []).append(self.id)
			who.taskCtn.set("petCom", petCompleteNo)

		#检查要不要删除50000任务
		taskNo = self.groupTask[lv][index].get("任务", [])
		allComplete = True
		for no in taskNo:
			if no not in petCompleteNo.get(lv, []):
				#这一系列任务还没完成
				allComplete = False
				break
				
		if allComplete:
			task.pett.autoPetTask(who)
		# 	if self.canRemoveLeadTad(who):
		# 		task.removeTask(who, task.pett.PET_TASK_LEAD_NO)
				

	def rewardPet(self, who, val):
		petId = val[0]
		petObj = pet.new(petId, 0)
		if not petObj:
			return
		petObj = pet.addPet(who, petObj)
		if not petObj:#增加宠物任务
			return
		if val[1] == 1:
			if who.petCtn.carryCount() < who.petCtn.carrayCountMax():
				who.petCtn.setCarry(petObj, True)
			# who.endPoint.rpcPetShow(petObj.id)
		openUIPanel.openPetRewardUi(who, petObj.id)
			
import task
import task.pett
import pet
import openUIPanel 