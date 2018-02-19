cnt = 0
lim = 50

for x1 in range(0, lim+1):
    for y1 in range(1, lim+1):
        for x2 in range(x1, lim+1):
            for y2 in range(0, y1+1):
                OP = x1**2 + y1**2
                PQ = (x2-x1)**2 + (y1-y2)**2
                QO = x2**2 + y2**2
                if 0 < min(OP,PQ,QO):
                    if OP==PQ+QO or PQ==QO+OP or QO==OP+PQ:
                        cnt += 1

print cnt
