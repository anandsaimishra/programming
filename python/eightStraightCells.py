#  Property of Godslayer™
#  Code wirtten by Anand Sai Mishra
#  On : 12/25/19, 9:53 AM
def cellCompete(c, days):
    for _ in range(days):
        for i in range(8):
            n = c[i]
            a = n

        if i > 0 and i < 7:
            c[i]=0 if c[i+1] == 1 else 1
        elif i == 0:
            c[i] = 0 if c[i+1] == 0 else 1
        else:
            c[i]=0 if a==0 else 1
    return c


def main():
    print(cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1))
    print(cellCompete([1, 1, 1, 0, 1, 1, 1, 1], 2))


if __name__ == '__main__':
    main()