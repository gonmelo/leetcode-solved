def rabin_karp(text: str, pattern: str):
    """
    Return all starting indices where pattern appears in text.
    """
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []

    p = 131
    M = 10**9 + 7

    p_m_1 = pow(p, m-1, M)

    def char_code(c):
        return ord(c) - 64

    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * p + char_code(pattern[i])) % M
        window_hash = (window_hash * p + char_code(text[i])) % M

    result = []

    for i in range(n-m+1):
        if pattern_hash == window_hash:
            if text[i:i+m] == pattern:
                result.append(i)

        if i < n-m:
            left = char_code(text[i]) * p_m_1 % M
            window_hash = (window_hash - left) % M
            window_hash = (window_hash * p + char_code(text[i+m])) % M

    return result


if __name__ == "__main__":
    text = "ABABCABABCEABABC"
    pattern = "ABABC"
    print(rabin_karp(text, pattern))  # e.g. [0, 5, 11]
