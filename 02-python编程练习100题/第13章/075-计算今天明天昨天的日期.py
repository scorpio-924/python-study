import datetime

def diff_days(days):
	pdate_obj = datetime.datetime.now()
	time_gap = datetime.timedelta(days=days)
	pdate_result = pdate_obj - time_gap
	return pdate_result.strftime("%Y-%m-%d")
print(f"今天：{diff_days(0)}，明天：{diff_days(-1)}，昨天：{diff_days(1)}，一周前：{diff_days(7)}，一周后：{diff_days(-7)}")