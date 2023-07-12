from filesplit.split import Split
split = Split("YOUR_FILE.csv", "C:/Users/user/Documents")
split.bysize(size = 1024*1000*40, newline=True) # 40MB
