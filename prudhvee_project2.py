
import collections
import sys

dictG=[['',0]]
queryG=[]
listC=[['',0]] 
docsG=[]
tfdf={}
docs=[]



#filename = '/Users/prudhveer/Desktop/input_corpus.txt'
#query ='/Users/prudhveer/Desktop/input_queries.txt'



filename=sys.argv[1]
outputfile = sys.argv[2]
queries = sys.argv[3]

sys.stdout = open(outputfile, 'w')

def search(element,index_list,lastindex,comparisons):
    for i in range(lastindex,len(index_list)):
        comparisons+=1
        if(index_list[lastindex]==element):
            lastindex+=1
            return [True,lastindex,comparisons]
        elif index_list[lastindex]>element:
            return [False,lastindex,comparisons]
        else:
            lastindex+=1
    return [False,lastindex,comparisons]

def DaatAnd(test):
    if len(test)==0:
        return
    printtext = test
    test=sorted(test,key=lambda x:len(d[x]))
    results=d[test[0]]
    temp=list(results)
    comparisons=0
    for word in test[1:]:
        if(len(results)==0):
            print("Results are \n",results)
            print("comparisons are",comparisons)
            return
        lastindex=0
        for element in results:
            got=search(element,d[word],lastindex,comparisons)
            lastindex=got[1]
            comparisons=got[2]
            if not got[0]:
                temp.remove(element)
        results=temp
    print("DaatAnd")
    print(" ".join(printtext))


    length_of_result= len(results)
    if (length_of_result != 0):
        print("Results:",end="")
        for l in results:
            print("",l,end="")
    else:
        print("Results: empty",end="")
    print("\nNumber of documents in results:", end=" ")
    print(length_of_result)
   # print("Results are \n",results)
    print("Number of comparisons:", end=" ")
    print(comparisons)
    #print("\n")
    if (length_of_result != 0):
        tf_idf(test,results)
    else:
        print("TF-IDF")
        print("Results: empty",end="")











def DaatOR(test):

    if len(test)==0:
        return
    printtext = test
    test = sorted(test,key=lambda x:-len(d[x]))

    results=set(d[test[0]])
    comparisons=0;
    temp=set(results)
    temp1=[]

    for word in test[1:]:
        for element in results:
            comparisons+=1
            for ele in d[word]:
                if ele != element:
                    temp.add(ele)
        results=set(temp)
    results = sorted(results)

    print("\nDaatOr")
    print(" ".join(printtext))

    print("Results:",end="")
    for l in results:
        print("",l,end="")
    length_of_result= len(results)
    print("\nNumber of documents in results:", end=" ")
    print(length_of_result)
   # print("Results are \n",results)
    print("Number of comparisons:", end=" ")
    print(comparisons)
    tf_idfOR(test,results)
























    # print(len(workd))

    # lend = len(workd)
    # result = []


    # list1 = list(workd.values())[0]
    # list2 = list(workd.values())[1]
    # print (list1)
    # print (list2)

    # for x in list1:
    #     for y in list2:
    #         if(x == y):
    #             result.append(x)


    # print("#####")
    # print (result)











def getpostings(test):



    and_array =[]
    work=[]
    count1 = 0;
    count=len(test)
    for i in test:
        count1= count1+1
        k=[]
        p=[]
        k=d[i]
        work.append([i,d[i]])
        print('GetPostings')
        print(i)
        print("Postings list:",end=" ")
        for l in k:
            #print("",l,end="")
            p.append(l)
        print (" ".join(p))


    #print("\n")
    workd = {e[0] : e[1:] for e in work}
    #print(workd)


    DaatAnd(test)
    DaatOR(test)
    print("\n")




    """

    for i in range (len(work)):
       
        print(work[i])
        print(work.count(work[i]))
        

        if(work.count(work[i]) == count1):
            and_array.append(work[i])
    and_li = list(dict.fromkeys(and_array))

    print("And list:",end="")
    for l in and_li:
        print(" ",l,end="")

 """










def operations(test) :

    getpostings(test)


docs=[]
tddf={}
d={}

def buildIndex(docID, data):
    words = set()
    wordslist=[]
    listT=data.split()
    for word in listT:
            words.add(word)
            wordslist.append(word)

    totaltermcount=len(wordslist)
    flagD=0
    flagDuplicateDoc=0
    for word in words:
        #print(word)
        termoccurence=wordslist.count(word)
        if word not in tfdf.keys():
            tfdf[word]={}
        tfdf[word][docID]=termoccurence/totaltermcount
        for element in dictG:
            if(element[0]==word):
                flagD=1
                for x in element[1:]:
                    if(x==docID):
                        flagDuplicateDoc=1
                        break
                if(flagDuplicateDoc==0):
                    element.append(docID)
                if(flagDuplicateDoc==1):
                    flagDuplicateDoc=0
        if(flagD==0):
            dictG.append([word,docID])
        if(flagD==1):
            flagD=0



"""commands = {}"""
with open(filename) as fh:
    for line in fh:
        doc_id,doc_data = line.strip().split("\t")
        docs.append(doc_id)
        buildIndex(doc_id,doc_data)


"""print (dictG)"""

d = {e[0] : e[1:] for e in dictG}



for key,value in d.items():
    if key!='':
        tfdf[key]['idf']=len(docs)/len(value)
#print(d)

#print(d)


# tfdf['bending']


# terms=['bending', 'Chamounix.']
# results=['9958', '2554', '8449', '4961', '2906', '4803', '2968']

def tf_idf(terms,results):

    ws={}
    temp=[]
    for doc in results:
        w=0
        for term in terms:
            if doc in tfdf[term].keys():
                w+=tfdf[term][doc]*tfdf[term]['idf']
        ws[doc]=w

    ws=sorted(ws.items(), key = lambda x: (x[1],-int(x[0])))

    print("TF-IDF")
    for i in range (len (ws)):
        temp.append(ws[i][0])
    temp.reverse()
    print("Results:",end="")
    for t in temp:
        print("",t,end="")


def tf_idfOR(terms,results):

    ws={}
    temp=[]
    for doc in results:
        w=0
        for term in terms:
            if doc in tfdf[term].keys():
                w+=tfdf[term][doc]*tfdf[term]['idf']
        ws[doc]=w

    ws=sorted(ws.items(), key = lambda x: (x[1],-int(x[0])))

    print("TF-IDF")
    for i in range (len (ws)):
        temp.append(ws[i][0])
    temp.reverse()
    print("Results:",end="")
    for t in temp:
        print("",t,end="")


    # for i in range (len(ws)):
    #         if (ws[i-1][1])==(ws[i][1]):
    #             a=int((ws[i][0]))
    #             temp =[]
    #             print (a)
    #             print (ws[i-1][0])
    #             b=int (ws[i-1][0])
    #             if a>b:
    #                 temp=  ws[i][0]
    #                 temp1 = ws[i-1][0]
    #                 ws[i][0] = temp1
    #                 ws[i-1][0]= temp







#print(tf_idf(terms,results))


"""
print (d)

print (type(d))
"""

"""
for key, value in d.items() :
    print (value)


term_search = input("Enter a term to search  : ")



if term_search in d.keys():
    print (d[term_search])
else:
    print ("Not Found")



input_query = input ("Enter the query: ")

split_query = input_query.split()

split_dict = {};

for i in split_query:
    if i in d.keys():
        # Adding a new key value pair
        split_dict.update ( {i: d[i]} )
        print(i)
        print (d[i])

print (split_dict)

print(type(split_dict))


"""



with open(queries) as testfile:

        for line in testfile:
            test=[]
            t=line.split()
            for i in t:
                test.append(i)


            operations(test)




















