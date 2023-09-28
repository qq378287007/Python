# python
import gzip

with open('favicon.ico', 'rb') as file:
    bs = file.read()
    value = gzip.compress(bs)
    #print(f'{bs}-{value}')
    print(f'{len(bs)}-{len(value)}')
    
    compressed = gzip.decompress(value)
    print("Decompressed value is: ", len(compressed))
