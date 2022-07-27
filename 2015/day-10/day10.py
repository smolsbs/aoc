#! python



def run(values: str, runs=50):
    run = values
    for j in range(runs):
        nextRun = ""
        v = 1
        lastChar = run[0]
        for i in range(1, len(run)):
            c = run[i]
            if c == lastChar:
                v += 1
            else:
                nextRun += f"{v}{lastChar}"
                v = 1
            lastChar = c
        nextRun += f"{v}{c}"
        run = nextRun

        if j == 39:
            p1 = len(run)
        if j == 49:
            p2 = len(run)

    return (p1, p2)


if __name__ == '__main__':

    p1, p2 = run("1113122113")

    print(f"Part 1: {p1}\nPart 2: {p2}")
