def more(text, numlines=5):
    lines = text.splitlines()
    while lines: 
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if not lines: break


if __name__=='__main__':
    import sys
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        nore(open(sys.argv[1]).read())
