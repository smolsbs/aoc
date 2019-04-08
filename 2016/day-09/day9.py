#! python
def decompress(_string, times, part2):
    newString = ''
    for _ in range(times):
        newString += _string

    # For part 2, checks if there are more decompressions to be made.
    # Enters in a recursion to decompress everything
    if '(' in _string and part2:         
        return crawler(newString, part2)

    return len(newString)

def crawler(text, part2=False):
    size = len(text)
    i = 0
    inside = False
    params = ''
    decompressedString = 0

    # goes through the text char by char. If it finds a '(' char, starts storing the info into the params variable
    # so it can be processed into the amount of chars being decompressed and the amount of times it should decompress
    # Everything is stored into a variable called decompressedString that is return at the end of the fucntion
    while i < size:
        if text[i] == '(':
            inside = True
            params = ''

        elif text[i] == ')':
            inside = False
            tParams = tuple(map(int, params.split('x')))
            subString = text[i+1: i+tParams[0]+1]
            decompressedString += decompress(subString, tParams[1], part2)
            i += tParams[0] # skips the cursor to the end of the text variable to further process the decompression

        elif inside:
            params += text[i]

        else:
            decompressedString += 1
        i += 1

    return decompressedString


def main():
    with open('input') as fp:
        origText = fp.read().strip()
    
    p1 = crawler(origText)
    print("Part 1: %d" % p1)
    
    p2 = crawler(origText, True)
    print("Part 2: %d" % p2)


if __name__ == '__main__':
    main()