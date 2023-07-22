import json
import requests
from bs4 import BeautifulSoup
import pprint
import unicodedata

links = [
    "https://www.nvcc.edu/business-offices/faq.html",
    "https://www.nvcc.edu/parking/faq.html",
    "https://www.nvcc.edu/transfer/faq/",
    "https://www.nvcc.edu/nova-esl/college/faq/index.html",
    "https://www.nvcc.edu/novaconnect/students/faq.html",
    "https://www.nvcc.edu/ithd/students/faq.html"
    "https://www.nvcc.edu/novaconnect/faculty/faq.html",
    "https://www.nvcc.edu/emergency/closing/faq.html"
]

# https://www.nvcc.edu/employment/faq.html
# https://www.nvcc.edu/employment/faq.html
# https://www.nvcc.edu/academics/pathways/health-sciences/veterinary-technology/program/faq.html
# https://www.nvcc.edu/osi/assessment/academic-program-review/faq.html
questionlist=[]
answerlist=[]

currentlink = "https://www.nvcc.edu/business-offices/faq.html"
req = requests.get(currentlink)
soup = BeautifulSoup(req.content, "lxml")
mydict= {}
for i in range(1,8):
    if len(questionlist)==0:
       questionlist=[x.text for x in soup.find_all("span",{"class":"faq"})]
    else:pass
    
    string = f"faq{i}"
    rawQnA = soup.find("p",{"id":string})
    rawQnA.find("span").decompose()
    answer = rawQnA.text
    if len(mydict)==0:
        mydict[currentlink]={questionlist[i-1]:answer}
    else: 
        mydict[currentlink].update({questionlist[i-1]:answer})

print(mydict)

    # print(soup.find("p",{"id":string}).text)
    # print(soup.find("a",{"href":string}).text) 
    # print(soup.find("div",{'id':string[1:]}).text)
    # question =  str(unicodedata.normalize("NFKD",soup.find("a",{"href":string}).text.strip()).replace("\n","")).encode("ascii","ignore").decode().replace('\"',"'")
    # answer = str(unicodedata.normalize("NFKD",soup.find("div",{'id':string[1:]}).text.strip()).replace("\n","")).encode("ascii","ignore").decode().replace('\"',"'")
    # if len(mydict)==0:
    #     mydict[currentlink] = {question:answer}
    # elif (len(mydict)==1):
    #     mydict[currentlink].update({question:answer})


