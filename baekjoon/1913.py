n = int(input())
find = int(input())
base = [[9,2,3],[8,1,4],[7,6,5]]
x, y = 0, 0
for i in range(5, n+1, 2):
	left =  i * i
	right = i*i - 3*i + 3
	top = [[left] + [i for i in range((i-2)*(i-2)+1, right+1)]] 
	for j in range(i-2):
		base[j] = [left-j-1] + base[j] + [right+j+1]
	bottom = [[i for i in range(left-i+1, right+i-2, -1)]]
	base = top + base + bottom

for i in range(len(base)):
	tmp = base[i]
	print(*tmp)
	if find in tmp:
		x = i + 1
		y = tmp.index(find) + 1
print(x, y)
