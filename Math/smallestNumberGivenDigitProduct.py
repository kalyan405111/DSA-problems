class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        F = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        # Factorize t into 2,3,5,7
        need = [0, 0, 0, 0]
        primes = [2, 3, 5, 7]

        for i, p in enumerate(primes):
            while t % p == 0:
                need[i] += 1
                t //= p

        if t != 1:
            return "-1"

        n = len(num)

        def sub(a, b):
            return [a[i] - b[i] for i in range(4)]

        def enough(x):
            return all(v <= 0 for v in x)

        def min_digits(x):
            a, b, c, d = [max(0, v) for v in x]

            res = c + d
            res += a // 3
            a %= 3
            if a:
                res += 1

            res += b // 2
            b %= 2
            if b:
                res += 1

            return res

        def build(length, rem):
            a, b, c, d = [max(0, v) for v in rem]
            digits = []

            while a >= 3:
                digits.append('8')
                a -= 3
            if a == 2:
                digits.append('4')
            elif a == 1:
                digits.append('2')

            while b >= 2:
                digits.append('9')
                b -= 2
            if b == 1:
                digits.append('3')

            digits += ['5'] * c
            digits += ['7'] * d

            digits += ['1'] * (length - len(digits))
            digits.sort()

            return ''.join(digits)

        # Check num itself
        rem = need[:]
        ok = True

        for ch in num:
            if ch == '0':
                ok = False
                break
            rem = sub(rem, F[int(ch)])

        if ok and enough(rem):
            return num

        # Prefix remaining requirements
        pref = [need[:]]

        for ch in num:
            cur = pref[-1][:]
            if ch != '0':
                cur = sub(cur, F[int(ch)])
            pref.append(cur)

        # Try to increase one digit
        for i in range(n - 1, -1, -1):
            cur = int(num[i])

            for dgt in range(max(1, cur + 1), 10):
                rem = sub(pref[i], F[dgt])
                left = n - i - 1

                if min_digits(rem) <= left:
                    return num[:i] + str(dgt) + build(left, rem)

        # Need longer length
        length = max(n + 1, min_digits(need))
        return build(length, need)
