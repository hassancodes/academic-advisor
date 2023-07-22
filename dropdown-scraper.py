import json
import requests
from bs4 import BeautifulSoup
import pprint
import unicodedata



targetlinks = [
    "https://online.nvcc.edu/faqs.html",
    "https://www.nvcc.edu/medical/apply/steps/faq.html",
    "https://www.nvcc.edu/campus-auxiliary-services/faq.html",
    "https://online.nvcc.edu/testinginfo.html",
    "https://online.nvcc.edu/fservices/index.html",
    "https://www.nvcc.edu/transcripts/faq.html"]


# total 54 panesl on this link 
# first we will get all the title of questions
# then their answers, next will will make them in a json file
questions_list =[]
answer_list = []
currentlink = "https://www.nvcc.edu/transcripts/faq.html"
req = requests.get(currentlink)
soup = BeautifulSoup(req.content, "lxml")
# print(soup)
mydict = {}

 
# # mydict = {'https://online.nvcc.edu/faqs.html': {'How do I apply to teach for NOVA Online?': 'If you are qualified to teach online and are interested in teaching for us, please send a resume/CV and cover letter to\xa0TeachOnline@nvcc.edu.\xa0 Your experience and credentials will be reviewed, you will be contacted for further information if necessary, and your background will be examined to see if you might fit with our current staffing needs.\xa0 If your experience does fit our current needs, NOVA Online will put you in contact with an Academic Dean on one of the NOVA campuses, who will interview you and complete the actual hiring process.'}}
for i in range(1,40):
    string = f"#panel{i}"
    question = soup.find("a",{"href": string})
    answer = soup.find("div",{'id':string[1:]})
    if question ==None:
        pass
    else:
        question =  str(unicodedata.normalize("NFKD",question.text.strip()).replace("\n","")).encode("ascii","ignore").decode().replace('\"',"'")
    
    if answer==None:
        pass
    else: 
        answer = str(unicodedata.normalize("NFKD",answer.text.strip()).replace("\n","")).encode("ascii","ignore").decode().replace('\"',"'")
        
    
#     question = soup.find("a",{"href":string})
#     answer = soup.find("div",{'id':string[1:]}).text
    # question =  str(unicodedata.normalize("NFKD",soup.find("a",{"href":string}).text.strip()).replace("\n","")).encode("ascii","ignore").decode().replace('\"',"'")
    # answer = str(unicodedata.normalize("NFKD",soup.find("div",{'id':string[1:]}).text.strip()).replace("\n","")).encode("ascii","ignore").decode().replace('\"',"'")
    if len(mydict)==0:
        mydict[currentlink] = {question:answer}
    elif (len(mydict)==1):
        mydict[currentlink].update({question:answer})
        
 
# print(mydict)  
with open("faqs.json", "r+") as fp:
    a = json.load(fp)
    a.update(mydict)
    json.dump(a,fp)

