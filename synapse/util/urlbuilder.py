import beautifurl

def urlbuilder(s):
    res = ""
    i = 0
    while i < len(s):
        if s[i] == "^":
            i += 1
            res += beautifurl.Beautifurl().get_random_url(s[i])
        else:
            res += s[i]
        i += 1
    return res
