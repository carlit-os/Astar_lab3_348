import common
import student_code

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

def check_result(title, map1, map2):
	result=True
	print(title)
	for y in range(0,common.constants.MAP_HEIGHT):
		v=""
		for x in range(0,common.constants.MAP_WIDTH):
			if (map1[y][x]==map2[y][x]):
				v+=bcolors.GREEN+str(map1[y][x])+bcolors.NORMAL
			else:
				result = False
				v+=bcolors.RED+str(map1[y][x])+bcolors.NORMAL
		print(v)
	if (result):
		print("Test Result: " + bcolors.GREEN+"Passed"+bcolors.NORMAL)
	else:
		print("Test Result: " + bcolors.RED+"Failed"+bcolors.NORMAL)
	return result
	
data1 = ("2000001111"
"1111101111"
"1111101111"
"1001101111"
"1101101111"
"1100000011"
"1110111011"
"1100111011"
"1101030011"
"1111110111"
"1111110111"
"1000000001")
			  
gold_df1 = ("5555551111"
"1111151111"
"1111151111"
"1001151111"
"1101151111"
"1104455511"
"1114111511"
"1104111511"
"1101055511"
"1111110111"
"1111110111"
"1000000001")
					 

data2 = ("1000120011"
"1010101011"
"1010101011"
"1010101011"
"1010101011"
"1010101011"
"1310101011"
"1010001011"
"1011111011"
"1000000011"
"1111111111"
"1111111111")
			  
gold_df2 = ("1000155511"
  "1010141511"
  "1014141511"
  "1014141511"
  "1014141511"
  "1014141511"
  "1514141511"
  "1514441511"
  "1511111511"
  "1555555511"
  "1111111111"
  "1111111111")
					 

data3 = ("1112311111"
"1111111111"
"1111111111"
"1111111111"
"1111111111"
"1111111111"
"1111111111"
"1111111111"
"1111111111"
"1111111111"
"1111111111"
"1111111111")
			  
gold_df3 = ("1115511111"
  "1111111111"
  "1111111111"
  "1111111111"
  "1111111111"
  "1111111111"
  "1111111111"
  "1111111111"
  "1111111111"
  "1111111111"
  "1111111111"
  "1111111111")

data4 = ("1112000110"
  "1111110110"
  "1111110111"
  "1111110111"
  "1110010001"
  "1110110111"
  "1110110111"
  "1110110111"
  "1110110111"
  "1100000111"
  "1111110100"
  "1111110103")
  
gold_df4 = ("1114444110"
  "1111114110"
  "1111114111"
  "1111114111"
  "1114414441"
  "1114114111"
  "1114114111"
  "1114114111"
  "1114114111"
  "1144444111"
  "1111114100"
  "1111114103")

data5 = ("0000200000"
  "0111111110"
  "0100000000"
  "0111111110"
  "0000000110"
  "1111111110"
  "0110000010"
  "0110111010"
  "0110131010"
  "0110101010"
  "0110001010"
  "0000111000")

gold_df5 = ("4444555555"
  "4111111115"
  "4144444445"
  "4111111115"
  "4444444115"
  "1111111115"
  "0115555515"
  "0115111515"
  "0115151515"
  "0115151515"
  "0115551515"
  "0000111555")

  
all_passed = True

gold_dfmap1 = common.init_map();
common.set_map(gold_dfmap1, gold_df1)

dfmap1 = common.init_map()
common.set_map(dfmap1, data1)
df1 = student_code.astar_search(dfmap1)
tdf1 ="Reachable goal:"
cdf1 = check_result(tdf1,dfmap1,gold_dfmap1)

all_passed = all_passed and cdf1 and df1  

gold_dfmap2 = common.init_map();
common.set_map(gold_dfmap2, gold_df2)

dfmap2 = common.init_map()
common.set_map(dfmap2, data2)
df2 = student_code.astar_search(dfmap2)
tdf2 ="Reachable goal:"
cdf2 = check_result(tdf2,dfmap2,gold_dfmap2)

all_passed = all_passed and cdf2 and df2 

gold_dfmap3 = common.init_map();
common.set_map(gold_dfmap3, gold_df3)

dfmap3 = common.init_map()
common.set_map(dfmap3, data3)
df3 = student_code.astar_search(dfmap3)
tdf3 ="Reachable goal:"
cdf3 = check_result(tdf3,dfmap3,gold_dfmap3)


all_passed = all_passed and cdf3 and df3  


gold_dfmap4 = common.init_map();
common.set_map(gold_dfmap4, gold_df4)

dfmap4 = common.init_map()
common.set_map(dfmap4, data4)
df4 = student_code.astar_search(dfmap4)
tdf4 = "Unreachable goal:"
cdf4 = check_result(tdf4,dfmap4,gold_dfmap4)


all_passed = all_passed and cdf4 and not df4 

gold_dfmap5 = common.init_map();
common.set_map(gold_dfmap5, gold_df5)

dfmap5 = common.init_map()
common.set_map(dfmap5, data5)
df5 = student_code.astar_search(dfmap5)
tdf5 ="Reachable goal:"
cdf5 = check_result(tdf5,dfmap5,gold_dfmap5)


all_passed = all_passed and cdf5 and df5

if all_passed:
	exit(0)
else:
	exit(1)
