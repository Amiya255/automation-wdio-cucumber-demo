def frange(start,stop,step=0.25):
    curr = float(start)
    while curr < stop:
        yield curr
        curr += step

print(list(frange(1.1,3)))
print(list(frange(1,3,0.33)))
print(list(frange(1,3,1)))
print(list(frange(3,1)))
print(list(frange(1,3,0)))
print(list(frange(-1,-0.5,0.1)))

for num in frange(3.142,12):
    print(f"{num:05.2f}")

# Finally:
#     print(frange(1,2))

def frange2(start,stop=None,step=.25):
    if stop is None:
        stop = start
        curr = 0.0
    else:
        curr=float(start)

    while curr<stop:
        yield curr
        curr += step

print(list(frange(1.1,3)))
print(list(frange(1,3,0.33)))
print(list(frange(1,3,1)))
print(list(frange(3,1)))
print(list(frange(1,3,0)))
print(list(frange(-1,-0.5,0.1)))
