def decoder(encoded, marker):
    chunks = encoded.split(marker)
    org1 = "".join([chunks[i] for i in range(len(chunks)) if i % 2 == 0])
    org2 = "".join([chunks[i][::-1] for i in range(len(chunks)-1, 0, -1) if i % 2 == 1])
    return org1 + org2


print(decoder("Lor-.tile gnicsipida rutetcesnoc ,tema tis rolod muspi me", '-'))

"Lorem ipsum dolor sit amet, consectetur adipiscing elit."
