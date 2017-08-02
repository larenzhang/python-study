def triangles(num):
    latest = [1]
    yield latest
    for i in range(num):
        new = [1]
        for j in range(len(latest)-1):
            new.append(latest[j]+latest[j+1])
        new.append(1)
        latest = new
        yield new

def main():
    g=triangles(10)
    while True:
        try:
            x=next(g)
            print(x)
        except StopIteration as e:
            break

if __name__ == "__main__":
    main()
