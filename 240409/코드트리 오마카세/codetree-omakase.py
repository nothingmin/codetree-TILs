l, q = map(int, input().split())

customers = {}
sushis = {}
prints = []
for _ in range(q):
    line = input().split()
    if line[0] == '100':
        t = int(line[1])
        x = int(line[2])
        name = line[3]
        if name not in sushis.keys():
            sushis[name] = [[t, x]]
        else:
            sushis[name].append([t, x])
    elif line[0] == '200':
        t = int(line[1])
        x = int(line[2])
        name = line[3]
        n = int(line[4])
        if name not in customers.keys():
            customers[name] = [t, x, n]
    else:
        t = int(line[1])
        prints.append(t)


# print(customers) ## t,x,n
# print(sushi) # t, x
# print(prints)

def x_at_t(init, x, cur):
    init = init % l
    cur = cur % l
    return (x - init + cur) % l


for t in prints:
    sushi_count = 0
    customers_count = 0
    for name in customers.keys():
        customer_time = customers[name][0]
        customer_x = customers[name][1]
        customer_n = customers[name][2]
        if customers[name][0] <= t:
            customers_count += 1
    for name in sushis.keys():
        for sushi in sushis[name]:
            sushi_time = sushi[0]
            sushi_init_x = sushi[1]
            if sushi_time <= t:
                sushi_count += 1
    for name in customers.keys():
        customer_time = customers[name][0]
        customer_x = customers[name][1]
        customer_n = customers[name][2]
        if customers[name][0] > t:
            continue
        for sushi in sushis[name]:
            sushi_time = sushi[0]
            sushi_init_x = sushi[1]
            if sushi_time > t:
                continue
            if sushi_time < customer_time:
                sushi_init_x = (customer_time - sushi_time + sushi_init_x)%l
                sushi_time = customer_time
            if t - sushi_time >= l - 1:
                sushi_count -= 1
                customer_n -= 1
            elif sushi_init_x > customer_x:
                if (sushi_init_x + t - sushi_time) % l >= customer_x:
                    sushi_count -= 1
                    customer_n -= 1
            elif sushi_init_x < customer_x:
                if sushi_init_x + t - sushi_time >= customer_x:
                    sushi_count -= 1
                    customer_n -= 1
            else:
                sushi_count -= 1
                customer_n -= 1
        if customer_n == 0:
            customers_count -= 1
    print(customers_count, sushi_count)