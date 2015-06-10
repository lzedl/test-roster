

def fuzzyFilter(pattern, words):
    def gen(pattern, words):
        for word in words:
            lower = word.lower()
            score = 0
            cn = -1
            wl = len(lower)
            for n, c in enumerate(pattern, 1):
                for cn in xrange(cn + 1, wl):
                    c2 = lower[cn]
                    if c == c2:
                        break
                    else:
                        score += n
                else:
                    break
            else:
                yield score, word

    result = [x for x in gen(pattern.replace(" ", "").lower(), words)]
    result.sort(key=lambda x: x[0])
    return tuple(x[1] for x in result)

