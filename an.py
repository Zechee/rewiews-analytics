data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line.strip())
		if count % 10000 == 0:
			print(len(data))

print('一共有', len(data), '笔留言。')

sum_len = 0
for d in data:
	sum_len += len(d)

print('平均每则留言的长度是', sum_len / len(data), '。')
