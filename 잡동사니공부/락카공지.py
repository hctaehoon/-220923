from datetime import datetime
now  = datetime.now()
print("현재 :", now)	# 현재 : 2021-01-09 21:51:33.170644

date_to_compare = datetime.strptime(input(str()), "%Y%m%d")
print("비교할 날짜 :", date_to_compare)	# 비교할 날짜 00: : 00:00

date_diff = now - date_to_compare
print("차이 :", date_diff, ", Type :", type(date_diff))	# 차이 : 15 days, 21:51:33.170644 , Type : <class 'datetime.timedelta'>

print("일 수 차이 :", date_diff.days)	# 일 수 차이 : 15

print("회원님의 헬스장 이용이 {0}일 경과하였습니다.락카 소지품 회수 부탁 드립니다. 감사합니다.  \
".format(date_diff.days))