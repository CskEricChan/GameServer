﻿编号	父任务编号	目标类型_S	图标	标题_S	简介_S	详情_S	奖励描述_S	前往脚本_S	初始化脚本_S
1		寻人	0	测试寻人	传话给$target	替师父为$target传话，切莫耽误			N1001,E(1001,1001)
2		巡逻战斗	1	测试暗雷战斗	去$scene收集$props	师门$props消耗过大，去$scene收集一些。			L(9001,1),ANLEI(1001,1002,9003)
3		寻物	0	测试寻物	去帮师父找个$props来(拥有$process)	师父准备闭关炼药，急需$props作为药引，请尽快找回来。			B(1001,lv),E(master,1003)
4		寻物	0	测试寻物并上交	去帮师父找个$props来(拥有$process)	师父准备闭关炼药，急需$props作为药引，请尽快找回来。			B(1001,lv),E(master,1004)
5		寻人	1	试炼	与$target战斗	击败$target，证明你的根基	200001,221102		NE(5001,5001),NIE(5002,5002),E(10102,5003)
