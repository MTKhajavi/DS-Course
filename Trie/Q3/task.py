class Node:
    def __init__(self):
        self.cnt = 0
        self.next_node = [None]*26

root = Node()
def trie_insert(s):
    current = root
    for i in range(len(s)):
        c = ord(s[i]) - ord('a')
        if current.next_node[c] == None:
            current.next_node[c] = Node()
        current = current.next_node[c]
        current.cnt += 1

def trie_delete(s):
    current = root
    for i in range(len(s)):
        c = ord(s[i]) - ord('a')
        current = current.next_node[c]
        current.cnt += -1

def find_max_letters(word):
    current = root
    cnts = list()
    for i in range(len(word)):
        c = ord(word[i]) - ord('a')
        if current.next_node[c] != None:
            current = current.next_node[c]
            cnts.append(current.cnt)
        else:
            break
    #print(word, cnts)
    if len(cnts) == 0:
        return 0
    
    ans = len(cnts)
    tmp = cnts[-1] - 1
    for i in range(1 , len(cnts)):
        j = len(cnts) - i - 1
        tmp += cnts[j] - cnts[j+1] - 1
        if tmp < 0:
            ans -= 1
            tmp += 1
    return min(ans , len(cnts) )

def main(mina_words, mohammad_words):
    ans = 0
    root.next_node = [None]*26
    for word in mohammad_words:
        trie_insert(word)
    for word in mina_words:
        ans += find_max_letters(word)
    return ans

# n, m = map(int , input().split())
# m1 = list()
# m2 = list()
# for i in range(n):
#     string  = input()
#     m1.append(string)
# for i in range(m):
#     string = input()
#     m2.append(string)
#
# print(main(m1, m2))
