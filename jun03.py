prices = { 
"apple": 2,
"orange": 3,
"banana": 1, 
"mango": 5

}

ans = 0
item = ""
for k in prices:
    if prices[k] > ans:
        ans = prices[k]
        item = k
print(item)
