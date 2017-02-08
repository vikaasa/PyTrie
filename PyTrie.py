class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.leaf = True
    
class Trie:
    def __init__(self):
        self.root = Node('.')
        self.root.leaf = False
        self.nodeList = []
        self.count = 0
                
    def call_insert(self, node, word):
        curr = node
        curr_pos = 0
        for letter in word:
            #print letter, word
            curr_pos += 1
            if letter in curr.children:
                #print "letter exists"
                curr = curr.children[letter]
                try:
                    if curr.leaf == True:
                        #print "if curr node is a leaf: "
                        curr.children[curr.data[curr_pos]] = Node(curr.data)
                        curr.data = None
                        curr.leaf = False
                except:
                    continue
            else:
                #print "first insert"
                self.count += 1
                if curr.data==None:
                    curr.leaf = False
                curr.children[letter] = Node(word)
                break
        
    def insert(self, word):
        curr = self.root
        self.call_insert(curr, word)
    
    def getAllWords(self):
        curr = self.root
        allWords = self.getAllWordsFromSubtree(curr)
        return allWords

    def getAllWordsFromSubtree(self, node):
        self.nodeList = []
        return self.callGetAllWordsFromSubtree(node)
    
    def callGetAllWordsFromSubtree(self, node):
        curr = node
        if curr.leaf != False:
            self.nodeList.append(curr.data)
        for i in curr.children:
            self.callGetAllWordsFromSubtree(curr.children[i])
        return self.nodeList
    
    def getAllPrefixes(self, prefix):
        node = self.root
        #self.nodeList = []
        return self.callGetAllPrefixes(node, prefix)
        
    def callGetAllPrefixes(self, curr, prefix):
        res = []
        for letter in prefix:
            #print letter, word
            if curr.leaf == True:
                if curr.data.startsWith(prefix):
                    res.append(curr.data)
                    return res
                    
            elif letter in curr.children:
                #print "letter exists: " + str(letter)
                curr = curr.children[letter]
                
            else:
                print "prefix does not exist!"
                return
        #print curr.children
        return self.getAllWordsFromSubtree(curr)
        #return res
    
    def search(self, word):
        node = self.root
        searchResult = self.callSearch(node, word)
        #print "SEARCH RESULT: "
        #print searchResult, searchResult[0].children[word[searchResult[1]]]
        return searchResult[0].children[word[searchResult[1]]] if searchResult != False else False
        
    def callSearch(self, curr, word):
        res = []
        for i in range(len(word)-1):
            #print curr.children, curr.children[word[i]].children
            if word[i] in curr.children and word[i+1] in curr.children[word[i]].children and curr.children[word[i]].children[word[i+1]].leaf is True:
                if curr.children[word[i]].children[word[i+1]].data == word:
                    #print "yay, found"
                    return (curr.children[word[i]], i+1)
                else:
                    return False
                    
            elif word[i] in curr.children and word[i+1] in curr.children[word[i]].children:
                #print "letter exists: " + str(letter)
                curr = curr.children[word[i]]
                
            else:
                print "word does not exist!"
                return False
            
        '''if curr.children[word[i+1]].leaf == True:
            if curr.children[word[i+1]].data == word:
                return curr.children[word[i]]
            else:
                return False'''
        
    def delete(self, word):
        node = self.root
        checkExists = self.callSearch(node, word)
        self.callDelete(word, checkExists) if checkExists != False else False
    
    def callDelete(self, word, searchResult):
        if searchResult[0].children[word[searchResult[1]]].children == {}:
            del searchResult[0].children[word[searchResult[1]]]
        else:
            searchResult[0].children[word[searchResult[1]]].data = None
            searchResult[0].children[word[searchResult[1]]].leaf = False
        #print searchResult[0].children, searchResult[0].leaf, searchResult[0].data