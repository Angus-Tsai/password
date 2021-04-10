n = 3 #剩餘機會
while n > 0:
	password = input('請輸入密碼: ')
	n = n - 1
	if password == 'a123456':
		print('登入成功')
		break
	else:
		if n == 0:
			print('登入失敗')
			break
		else:
			print('你還剩', n, '次機會')
