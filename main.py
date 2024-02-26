def main():
    def sort(dict):
        return dict["num"]
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        wordCount = 0
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        i = 0
        j = 0
        k = 0
        l = 0
        m = 0
        n = 0
        o = 0
        p = 0
        q = 0
        r = 0
        s = 0
        t = 0
        u = 0
        v = 0
        w = 0
        x = 0
        y = 0
        z = 0
        for count in words:
            wordCount += 1
            letters = count.lower()
            letterCount = [
                {"letter": "a", "num": a},
                {"letter": "b", "num": b},
                {"letter": "c", "num": c},
                {"letter": "d", "num": d},
                {"letter": "e", "num": e},
                {"letter": "f", "num": f},
                {"letter": "g", "num": g},
                {"letter": "h", "num": h},
                {"letter": "i", "num": i},
                {"letter": "j", "num": j},
                {"letter": "k", "num": k},
                {"letter": "l", "num": l},
                {"letter": "m", "num": m},
                {"letter": "n", "num": n},
                {"letter": "o", "num": o},
                {"letter": "p", "num": p},
                {"letter": "q", "num": q},
                {"letter": "r", "num": r},
                {"letter": "s", "num": s},
                {"letter": "t", "num": t},
                {"letter": "u", "num": u},
                {"letter": "v", "num": v},
                {"letter": "w", "num": w},
                {"letter": "x", "num": x},
                {"letter": "y", "num": y},
                {"letter": "z", "num": z}
            ]
            letterCount.sort(reverse=True, key=sort)
            for count2 in letters:
                if count2 == "a":
                    a += 1
                elif count2 == "b":
                    b += 1
                elif count2 == "c":
                    c += 1
                elif count2 == "d":
                    d += 1
                elif count2 == "e":
                    e += 1
                elif count2 == "f":
                    f += 1
                elif count2 == "g":
                    g += 1
                elif count2 == "h":
                    h += 1
                elif count2 == "i":
                    i += 1
                elif count2 == "j":
                    j += 1
                elif count2 == "k":
                    k += 1
                elif count2 == "l":
                    l += 1
                elif count2 == "m":
                    m += 1
                elif count2 == "n":
                    n += 1
                elif count2 == "o":
                    o += 1
                elif count2 == "p":
                    p += 1
                elif count2 == "q":
                    q += 1
                elif count2 == "r":
                    r += 1
                elif count2 == "s":
                    s += 1
                elif count2 == "t":
                    t += 1
                elif count2 == "u":
                    u += 1
                elif count2 == "v":
                    v += 1
                elif count2 == "w":
                    w += 1
                elif count2 == "x":
                    x += 1
                elif count2 == "y":
                    y += 1
                elif count2 == "z":
                    z += 1

    print(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordCount} words found in the document")
    print("")
    index = 0
    for i in range(0, len(letterCount) - 1):
        print(f"The character {(letterCount[index])["letter"]} was found {(letterCount[index])["num"]} times")
        index += 1
    print(f"The character {(letterCount[index])["letter"]} was found {(letterCount[index])["num"]} times")
    print("--- End report ---")

main()