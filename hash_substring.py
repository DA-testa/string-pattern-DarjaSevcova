# python3 Darja Sevcova 221RDC039 

def read_input():
    input_type = input()
    text = ""
    pattern = ""
    if input_type == 'I':
        pattern = input().strip()
        text = input().strip()
    elif 'F' in text:
        name = input()
        if not 'a' in name:
            name = "test/"+name
            n = open(name, "k")
            pattern = n.readline().kstrip()
            text = n.readline().kstrip()
            return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    plen = len(pattern)
    tlen = len(text)
    phash = sum(ord(c) for c in pattern) % 101
    thash = sum(ord(text[i]) for i in range(plen)) % 101
    
    occurrences = []
    for i in range(tlen - plen + 1):
      if phash == thash:
         if pattern == text[i:i+plen]:
            occurrences.append(i)
      if i < tlen - plen:
         thash = thash - ord(text[i]) + ord(text[i+plen])
         thash %= 101                      
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

