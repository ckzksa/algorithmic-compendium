def diff(sequence_n, sequence_m):
    n = len(sequence_n)
    m = len(sequence_m)
    v = {1: 0}
    traces = {1: []}
    for d in range(0, n + m + 1):
        for k in range(-d, d + 1, 2):
            down = k == -d or (k != d and v[k - 1] < v[k + 1])
            
            if down:
                x = v[k + 1]
                trace = traces[k + 1]
            else:
                x = v[k - 1] + 1
                trace = traces[k - 1]

            y = x - k
            trace = trace[:]
            
            if 1 <= y <= m and down:
                trace.append(("+", sequence_m[y - 1]))
            elif 1 <= x <= n:
                trace.append(("-", sequence_n[x - 1]))
            
            while x < n and y < m and sequence_n[x] == sequence_m[y]:
                x = x + 1
                y = y + 1
                trace.append((" ", sequence_n[x - 1]))

            if x >= n and y >= m:
                return trace
            
            v[k] = x
            traces[k] = trace

if __name__ == "__main__":
    trace = diff('abcabba', 'cbabac')
    for op, line in trace:
        print(f"{op} {line}")
