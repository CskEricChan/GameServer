﻿编号	点击_S	回复_S	成功_S	失败_S
1001	DONE,DEFF,R1001			
1002	SB4023	1:ANSWER	DONE,DEFF,R1001	SB4024
1003	POPI		DONE,DEFF,R1001	D4020
1004	POPI		DONE,DEFF,R1001	D4021
1005	SB4022	1:E(0,2001),$checkSchool	DONE,DEFF,R1001	
1006	F2001		LEGENDS	
1012	DONE,DEFF,R1001			
1013	DONE,DEFF,R1001			
1014	DONE,DEFF,R1001			
1015	DONE,DEFF,R1001			
1016	DONE,DEFF,R1001			
1017	DONE,DEFF,R1001			
2001	$checkSchool		DONE,DEFF,R1001	E(0,1005)
3001	DONE,DEFF,R1001,LOOK			