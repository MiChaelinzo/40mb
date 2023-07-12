from filesplit.split import Split
split = Split("phenom_reportview_all.csv", "C:/Users/micha/Documents")
split.bysize(size = 1024*1000*40, newline=True) # 40MB
