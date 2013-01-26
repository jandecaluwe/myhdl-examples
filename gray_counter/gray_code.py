def gray_code(n):
    assert 1 <= n <= 20
    if n == 1:
        return ['0', '1']
    else:
        G = gray_code(n-1)
        G0 = ['0' + w for w in G]
        G1 = ['1' + w for w in G]
        G1.reverse()
        return G0 + G1

if __name__ == '__main__':
    for i in range(1, 5):
        print gray_code(i)
