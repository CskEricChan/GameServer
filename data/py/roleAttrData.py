#-*-coding:utf-8-*-
#作者:叶伟龙@龙川县赤光镇
def getConfig(iLv,sKey,uDefault=0):
	if iLv not in gdData:
		raise PlannerError,'角色属性表没有{}级的属性'.format(iLv)
	return gdData[iLv].get(sKey,uDefault)

#导表开始
gdData={
	1:{"exp":15,"att":96,"def":31,"crit":5,"hit":100,"dodge":0,"hpMax":633,"mpMax":100,"spi":200},
	2:{"exp":30,"att":113,"def":33,"crit":5,"hit":100,"dodge":0,"hpMax":666,"mpMax":100,"spi":200},
	3:{"exp":50,"att":130,"def":35,"crit":5,"hit":100,"dodge":0,"hpMax":699,"mpMax":100,"spi":200},
	4:{"exp":80,"att":147,"def":37,"crit":5,"hit":100,"dodge":0,"hpMax":732,"mpMax":100,"spi":200},
	5:{"exp":120,"att":164,"def":39,"crit":5,"hit":100,"dodge":0,"hpMax":765,"mpMax":100,"spi":200},
	6:{"exp":170,"att":181,"def":41,"crit":5,"hit":100,"dodge":0,"hpMax":798,"mpMax":100,"spi":200},
	7:{"exp":230,"att":198,"def":43,"crit":5,"hit":100,"dodge":0,"hpMax":831,"mpMax":100,"spi":200},
	8:{"exp":310,"att":215,"def":45,"crit":5,"hit":100,"dodge":0,"hpMax":864,"mpMax":100,"spi":200},
	9:{"exp":400,"att":232,"def":47,"crit":5,"hit":100,"dodge":0,"hpMax":897,"mpMax":100,"spi":200},
	10:{"exp":500,"att":249,"def":49,"crit":5,"hit":100,"dodge":0,"hpMax":930,"mpMax":100,"spi":200},
	11:{"exp":650,"att":266,"def":51,"crit":5,"hit":100,"dodge":0,"hpMax":963,"mpMax":100,"spi":200},
	12:{"exp":852,"att":283,"def":53,"crit":5,"hit":100,"dodge":0,"hpMax":996,"mpMax":100,"spi":200},
	13:{"exp":983,"att":300,"def":55,"crit":5,"hit":100,"dodge":0,"hpMax":1029,"mpMax":100,"spi":200},
	14:{"exp":1124,"att":317,"def":57,"crit":5,"hit":100,"dodge":0,"hpMax":1062,"mpMax":100,"spi":200},
	15:{"exp":1275,"att":334,"def":59,"crit":5,"hit":100,"dodge":0,"hpMax":1095,"mpMax":100,"spi":200},
	16:{"exp":1436,"att":351,"def":61,"crit":5,"hit":100,"dodge":0,"hpMax":1128,"mpMax":100,"spi":200},
	17:{"exp":1607,"att":368,"def":63,"crit":5,"hit":100,"dodge":0,"hpMax":1161,"mpMax":100,"spi":200},
	18:{"exp":1788,"att":385,"def":65,"crit":5,"hit":100,"dodge":0,"hpMax":1194,"mpMax":100,"spi":200},
	19:{"exp":1979,"att":402,"def":67,"crit":5,"hit":100,"dodge":0,"hpMax":1227,"mpMax":100,"spi":200},
	20:{"exp":2200,"att":419,"def":69,"crit":5,"hit":100,"dodge":0,"hpMax":1260,"mpMax":100,"spi":200},
	21:{"exp":3440,"att":436,"def":71,"crit":5,"hit":100,"dodge":0,"hpMax":1293,"mpMax":100,"spi":200},
	22:{"exp":4740,"att":453,"def":73,"crit":5,"hit":100,"dodge":0,"hpMax":1326,"mpMax":100,"spi":200},
	23:{"exp":6100,"att":470,"def":75,"crit":5,"hit":100,"dodge":0,"hpMax":1359,"mpMax":100,"spi":200},
	24:{"exp":7520,"att":487,"def":77,"crit":5,"hit":100,"dodge":0,"hpMax":1392,"mpMax":100,"spi":200},
	25:{"exp":9000,"att":504,"def":79,"crit":5,"hit":100,"dodge":0,"hpMax":1425,"mpMax":100,"spi":200},
	26:{"exp":10540,"att":521,"def":81,"crit":5,"hit":100,"dodge":0,"hpMax":1458,"mpMax":100,"spi":200},
	27:{"exp":12140,"att":538,"def":83,"crit":5,"hit":100,"dodge":0,"hpMax":1491,"mpMax":100,"spi":200},
	28:{"exp":13800,"att":555,"def":85,"crit":5,"hit":100,"dodge":0,"hpMax":1524,"mpMax":100,"spi":200},
	29:{"exp":15520,"att":572,"def":87,"crit":5,"hit":100,"dodge":0,"hpMax":1557,"mpMax":100,"spi":200},
	30:{"exp":17300,"att":589,"def":89,"crit":5,"hit":100,"dodge":0,"hpMax":1590,"mpMax":100,"spi":200},
	31:{"exp":19140,"att":606,"def":91,"crit":5,"hit":100,"dodge":0,"hpMax":1623,"mpMax":100,"spi":200},
	32:{"exp":21040,"att":623,"def":93,"crit":5,"hit":100,"dodge":0,"hpMax":1656,"mpMax":100,"spi":200},
	33:{"exp":23000,"att":640,"def":95,"crit":5,"hit":100,"dodge":0,"hpMax":1689,"mpMax":100,"spi":200},
	34:{"exp":25020,"att":657,"def":97,"crit":5,"hit":100,"dodge":0,"hpMax":1722,"mpMax":100,"spi":200},
	35:{"exp":27100,"att":674,"def":99,"crit":5,"hit":100,"dodge":0,"hpMax":1755,"mpMax":100,"spi":200},
	36:{"exp":29240,"att":691,"def":101,"crit":5,"hit":100,"dodge":0,"hpMax":1788,"mpMax":100,"spi":200},
	37:{"exp":31440,"att":708,"def":103,"crit":5,"hit":100,"dodge":0,"hpMax":1821,"mpMax":100,"spi":200},
	38:{"exp":33700,"att":725,"def":105,"crit":5,"hit":100,"dodge":0,"hpMax":1854,"mpMax":100,"spi":200},
	39:{"exp":36020,"att":742,"def":107,"crit":5,"hit":100,"dodge":0,"hpMax":1887,"mpMax":100,"spi":200},
	40:{"exp":38400,"att":759,"def":109,"crit":5,"hit":100,"dodge":0,"hpMax":1920,"mpMax":100,"spi":200},
	41:{"exp":40840,"att":776,"def":111,"crit":5,"hit":100,"dodge":0,"hpMax":1953,"mpMax":100,"spi":200},
	42:{"exp":43340,"att":793,"def":113,"crit":5,"hit":100,"dodge":0,"hpMax":1986,"mpMax":100,"spi":200},
	43:{"exp":45900,"att":810,"def":115,"crit":5,"hit":100,"dodge":0,"hpMax":2019,"mpMax":100,"spi":200},
	44:{"exp":48520,"att":827,"def":117,"crit":5,"hit":100,"dodge":0,"hpMax":2052,"mpMax":100,"spi":200},
	45:{"exp":51200,"att":844,"def":119,"crit":5,"hit":100,"dodge":0,"hpMax":2085,"mpMax":100,"spi":200},
	46:{"exp":53940,"att":861,"def":121,"crit":5,"hit":100,"dodge":0,"hpMax":2118,"mpMax":100,"spi":200},
	47:{"exp":56740,"att":878,"def":123,"crit":5,"hit":100,"dodge":0,"hpMax":2151,"mpMax":100,"spi":200},
	48:{"exp":59600,"att":895,"def":125,"crit":5,"hit":100,"dodge":0,"hpMax":2184,"mpMax":100,"spi":200},
	49:{"exp":62520,"att":912,"def":127,"crit":5,"hit":100,"dodge":0,"hpMax":2217,"mpMax":100,"spi":200},
	50:{"exp":65500,"att":929,"def":129,"crit":5,"hit":100,"dodge":0,"hpMax":2250,"mpMax":100,"spi":200},
	51:{"exp":67737,"att":946,"def":131,"crit":5,"hit":100,"dodge":0,"hpMax":2283,"mpMax":100,"spi":200},
	52:{"exp":72568,"att":963,"def":133,"crit":5,"hit":100,"dodge":0,"hpMax":2316,"mpMax":100,"spi":200},
	53:{"exp":77493,"att":980,"def":135,"crit":5,"hit":100,"dodge":0,"hpMax":2349,"mpMax":100,"spi":200},
	54:{"exp":82512,"att":997,"def":137,"crit":5,"hit":100,"dodge":0,"hpMax":2382,"mpMax":100,"spi":200},
	55:{"exp":87625,"att":1014,"def":139,"crit":5,"hit":100,"dodge":0,"hpMax":2415,"mpMax":100,"spi":200},
	56:{"exp":92832,"att":1031,"def":141,"crit":5,"hit":100,"dodge":0,"hpMax":2448,"mpMax":100,"spi":200},
	57:{"exp":98133,"att":1048,"def":143,"crit":5,"hit":100,"dodge":0,"hpMax":2481,"mpMax":100,"spi":200},
	58:{"exp":103528,"att":1065,"def":145,"crit":5,"hit":100,"dodge":0,"hpMax":2514,"mpMax":100,"spi":200},
	59:{"exp":109017,"att":1082,"def":147,"crit":5,"hit":100,"dodge":0,"hpMax":2547,"mpMax":100,"spi":200},
	60:{"exp":11460000,"att":1099,"def":149,"crit":5,"hit":100,"dodge":0,"hpMax":2580,"mpMax":100,"spi":200},
	61:{"exp":120277,"att":1116,"def":151,"crit":5,"hit":100,"dodge":0,"hpMax":2613,"mpMax":100,"spi":200},
	62:{"exp":126048,"att":1133,"def":153,"crit":5,"hit":100,"dodge":0,"hpMax":2646,"mpMax":100,"spi":200},
	63:{"exp":131913,"att":1150,"def":155,"crit":5,"hit":100,"dodge":0,"hpMax":2679,"mpMax":100,"spi":200},
	64:{"exp":137872,"att":1167,"def":157,"crit":5,"hit":100,"dodge":0,"hpMax":2712,"mpMax":100,"spi":200},
	65:{"exp":143925,"att":1184,"def":159,"crit":5,"hit":100,"dodge":0,"hpMax":2745,"mpMax":100,"spi":200},
	66:{"exp":150072,"att":1201,"def":161,"crit":5,"hit":100,"dodge":0,"hpMax":2778,"mpMax":100,"spi":200},
	67:{"exp":156313,"att":1218,"def":163,"crit":5,"hit":100,"dodge":0,"hpMax":2811,"mpMax":100,"spi":200},
	68:{"exp":162648,"att":1235,"def":165,"crit":5,"hit":100,"dodge":0,"hpMax":2844,"mpMax":100,"spi":200},
	69:{"exp":169077,"att":1252,"def":167,"crit":5,"hit":100,"dodge":0,"hpMax":2877,"mpMax":100,"spi":200},
	70:{"exp":175600,"att":1269,"def":169,"crit":5,"hit":100,"dodge":0,"hpMax":2910,"mpMax":100,"spi":200},
	71:{"exp":182217,"att":1286,"def":171,"crit":5,"hit":100,"dodge":0,"hpMax":2943,"mpMax":100,"spi":200},
	72:{"exp":188928,"att":1303,"def":173,"crit":5,"hit":100,"dodge":0,"hpMax":2976,"mpMax":100,"spi":200},
	73:{"exp":195733,"att":1320,"def":175,"crit":5,"hit":100,"dodge":0,"hpMax":3009,"mpMax":100,"spi":200},
	74:{"exp":202632,"att":1337,"def":177,"crit":5,"hit":100,"dodge":0,"hpMax":3042,"mpMax":100,"spi":200},
	75:{"exp":209625,"att":1354,"def":179,"crit":5,"hit":100,"dodge":0,"hpMax":3075,"mpMax":100,"spi":200},
	76:{"exp":216712,"att":1371,"def":181,"crit":5,"hit":100,"dodge":0,"hpMax":3108,"mpMax":100,"spi":200},
	77:{"exp":223893,"att":1388,"def":183,"crit":5,"hit":100,"dodge":0,"hpMax":3141,"mpMax":100,"spi":200},
	78:{"exp":231168,"att":1405,"def":185,"crit":5,"hit":100,"dodge":0,"hpMax":3174,"mpMax":100,"spi":200},
	79:{"exp":238537,"att":1422,"def":187,"crit":5,"hit":100,"dodge":0,"hpMax":3207,"mpMax":100,"spi":200},
	80:{"exp":246000,"att":1439,"def":189,"crit":5,"hit":100,"dodge":0,"hpMax":3240,"mpMax":100,"spi":200},
	81:{"exp":259645,"att":1456,"def":191,"crit":5,"hit":100,"dodge":0,"hpMax":3273,"mpMax":100,"spi":200},
	82:{"exp":271840,"att":1473,"def":193,"crit":5,"hit":100,"dodge":0,"hpMax":3306,"mpMax":100,"spi":200},
	83:{"exp":284185,"att":1490,"def":195,"crit":5,"hit":100,"dodge":0,"hpMax":3339,"mpMax":100,"spi":200},
	84:{"exp":296680,"att":1507,"def":197,"crit":5,"hit":100,"dodge":0,"hpMax":3372,"mpMax":100,"spi":200},
	85:{"exp":309325,"att":1524,"def":199,"crit":5,"hit":100,"dodge":0,"hpMax":3405,"mpMax":100,"spi":200},
	86:{"exp":322120,"att":1541,"def":201,"crit":5,"hit":100,"dodge":0,"hpMax":3438,"mpMax":100,"spi":200},
	87:{"exp":335065,"att":1558,"def":203,"crit":5,"hit":100,"dodge":0,"hpMax":3471,"mpMax":100,"spi":200},
	88:{"exp":348160,"att":1575,"def":205,"crit":5,"hit":100,"dodge":0,"hpMax":3504,"mpMax":100,"spi":200},
	89:{"exp":361405,"att":1592,"def":207,"crit":5,"hit":100,"dodge":0,"hpMax":3537,"mpMax":100,"spi":200},
	90:{"exp":374800,"att":1609,"def":209,"crit":5,"hit":100,"dodge":0,"hpMax":3570,"mpMax":100,"spi":200},
	91:{"exp":388345,"att":1626,"def":211,"crit":5,"hit":100,"dodge":0,"hpMax":3603,"mpMax":100,"spi":200},
	92:{"exp":402040,"att":1643,"def":213,"crit":5,"hit":100,"dodge":0,"hpMax":3636,"mpMax":100,"spi":200},
	93:{"exp":415885,"att":1660,"def":215,"crit":5,"hit":100,"dodge":0,"hpMax":3669,"mpMax":100,"spi":200},
	94:{"exp":429880,"att":1677,"def":217,"crit":5,"hit":100,"dodge":0,"hpMax":3702,"mpMax":100,"spi":200},
	95:{"exp":444025,"att":1694,"def":219,"crit":5,"hit":100,"dodge":0,"hpMax":3735,"mpMax":100,"spi":200},
	96:{"exp":458320,"att":1711,"def":221,"crit":5,"hit":100,"dodge":0,"hpMax":3768,"mpMax":100,"spi":200},
	97:{"exp":472765,"att":1728,"def":223,"crit":5,"hit":100,"dodge":0,"hpMax":3801,"mpMax":100,"spi":200},
	98:{"exp":487360,"att":1745,"def":225,"crit":5,"hit":100,"dodge":0,"hpMax":3834,"mpMax":100,"spi":200},
	99:{"exp":502105,"att":1762,"def":227,"crit":5,"hit":100,"dodge":0,"hpMax":3867,"mpMax":100,"spi":200},
	100:{"exp":517000,"att":1779,"def":229,"crit":5,"hit":100,"dodge":0,"hpMax":3900,"mpMax":100,"spi":200},
}
#导表结束

MAX_ROLE_LV=max(gdData)

import u