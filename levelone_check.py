from typing import Union
from pydantic import BaseModel
from enum import Enum
import json



class emailpayload(BaseModel):
    emailbody:str
    emailsender:str





class threatlevel(Enum):
    good="good"
    sus="sus"
    bad="bad"


class checkstatus(BaseModel):
    status:threatlevel
    suswords:list[str]





def levelone_check(data:emailpayload):
    emailid = data.emailsender
    emailbody  = data.emailbody.split(" ")
    suswordjson =json.load(open("suswords.json","r"))
    suswords =suswordjson["words"]
    wordsfound = []
    for word in emailbody:
        if word in suswords:
            print("found sus word")
            wordsfound.append(word)

    suswordscount = len(wordsfound)
    if(suswordscount>0 and suswordscount<3):
        return checkstatus(status=threatlevel.sus,suswords=wordsfound)
    elif(suswordscount>3):
        return checkstatus(status=threatlevel.bad,suswords=wordsfound)
    else:
        return checkstatus(status=threatlevel.good,suswords=wordsfound)

