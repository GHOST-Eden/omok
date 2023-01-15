import os
clear = lambda : os.system('cls')

N = 10

#make place
place = [[chr(32) for col in range(N)] for row in range(N)]
#---------------

#print place
def pp(): 
	for i in range(N):
		for j in range(N):
			print(place[i][j], end="")
		print()
#---------------

#please re-enter
def pr():
	print("[ 다시 입력해주세요. ]\n")
	pp()
#---------------

#int check
def IC(n):
	n = n.replace(" ", "")
	if(n != "" and n.isdigit()):
		return int(n)
	else:
		return False
#---------------

#checking omok
def ocheck(arr):
	checkC, returnM = [9675, 9679], ["true1", "true2"]
	dr, dc = [0,1,1,1], [1,0,1,-1]
	for cc in range(2):
		for s_r in range(N):
			for s_c in range(N):
				if arr[s_r][s_c] == chr(checkC[cc]):
					for d in range(4):
						r = s_r
						c = s_c
						cnt = 0
						while 0 <= r <= N-1 and 0 <= c <= N-1 and arr[r][c] == chr(checkC[cc]):
							cnt += 1
							r += dr[d]
							c += dc[d]
							if cnt >= 5:
								return returnM[cc]
	return "false"
#---------------

#make case
count1 = 0
for k in range(0,N):
	place[0][k] = count1
	count1 += 1

count2 = 0
for l in range(0,N):
	place[l][0] = count2
	count2 += 1

place[0][0] = "X"
#---------------


clear() #print("\x1B[H\x1B[J")
pp()

#main function
count = 0
while(count >= N-1*N-1):
	ck = ocheck(place)
	if ck == "true1":
		print("[ 흑돌의 오목으로 종료되었습니다. ]")
		break
	elif ck == "true2":
		print("[ 백돌의 오목으로 종료되었습니다. ]")
		break
	mapping = input("좌표를 입력해 주세요[ex) n,n] : ")
	clear() #print("\x1B[H\x1B[J")
	if(("," in mapping) and (mapping.count(',') == 1)):
		x, y = map(IC, mapping.split(","))
		if(x != False and y != False):
			if ck == "false":
				if(x<N and y<N and place[x][y] == chr(32)):
					count += 1
					lastP = "마지막 돌의 위치 : "+"("+str(x)+","+str(y)+")"
					if count%2 == 1:
						place[x][y] = chr(9675)
						pp()
						print(lastP)
					else:
						place[x][y] = chr(9679)
						pp()
						print(lastP)
				else:
					print("[ 여기에는 놓을 수 없습니다. ]\n")
					pp()
					print("마지막 돌의 위치 : "+"("+str(x)+","+str(y)+")")
			else:
				pr()
				print("마지막 돌의 위치 : "+"("+str(x)+","+str(y)+")")
		else:
			pr()
			print("마지막 돌의 위치 : "+"("+str(x)+","+str(y)+")")
	else:
		pr()
else:
	print("아쉽지만! 비겼습니다.")
#---------------
