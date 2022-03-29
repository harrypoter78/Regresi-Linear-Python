import pandas as pd

def sigma1(inp):
    arr = []
    out = 0
    for x in range(n):
        arr.append(inp[x])
        out += arr[x]
    return out, arr

def sigma2(inpX, inpY):
    arr = []
    out = 0
    for x in range(n):
        arr.append((inpX[x] * inpY[x]))
        out += arr[x]
    return out, arr

def sigpow1(inp):
    arr = []
    out = 0
    for x in range(n):
        arr.append((inp[x] ** 2))
        out += arr[x]
    return out, arr

def cariA(inpX, inpY, inpN):
    Yi = sigma1(inpY)[0]
    Xi2 = sigpow1(inpX)[0]
    Xi = sigma1(inpX)[0]
    XiYi = sigma2(inpX, inpY)[0]
    out = round(((Yi * Xi2) - (Xi * XiYi))
                / ((inpN * Xi2) - (Xi ** 2)), 3)
    return out

def cariB(inpX, inpY, inpN):
    Yi = sigma1(inpY)[0]
    Xi = sigma1(inpX)[0]
    Xi2 = sigpow1(inpX)[0]
    XiYi = sigma2(inpX, inpY)[0]
    out = round(((inpN * XiYi) - (Xi * Yi))
                / ((inpN * Xi2) - (Xi ** 2)), 3)
    return out


if __name__ == '__main__':
    data = pd.read_csv("data.csv")

    X = data.columns[1]
    Y = data.columns[2]

    x = data[X]
    y = data[Y]

    n = len(data)

    a = cariA(x, y, n)
    b = cariB(x, y, n)
    print('Nilai Konstanta = ', a)
    print('Nilai Koefisien = ', b)
    print(f'Persamaan Y = {a} {b:+} X')

    # Percobaan user untuk memprediksi nilai Gradient
    inp = input("\nMasukan Nilai X: ")
    print(f'Y = {a} {b:+} * {inp} = {a + (b * int(inp)):.3f}')



