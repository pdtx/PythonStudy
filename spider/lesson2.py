def cal():
    str = input()
    sum = 0
    for i in range(len(str)):
        if( str[i] != '-' ):
            sum += int(str[i])
        else:
            sum -= (int(str[1+i]))*2
    return sum


if __name__ == '__main__':
    for i in range(int(input())):
        print(cal())
