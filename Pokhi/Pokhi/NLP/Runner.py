from __future__ import absolute_import
from Pokhi.Pokhi.NLP.Helpers import Helpers
from Pokhi.Pokhi.WebScrap.WikiScrap import WikiScrapper
from Pokhi.Pokhi.RawDBAccess.RawDBAccess import RawDBAccess
import re 
from collections import defaultdict


def ScrubImages():
    reg = "logo|edit\-clear|icon|padlock\-silver|blue_pencil|ambox_important|portal\-puzzle|symbol|lock\-green|p_vip" 
    db = RawDBAccess.GetMongoDB()
    collection = db["wikipediaFeed"]
    for doc in collection.find():
        array= doc["images"]
        doc["images"] = [x for x in array if not re.search(reg,x , re.IGNORECASE)]
        collection.save(doc)

def GetFrequencyCountImages():

    images= defaultdict(int)
    db = RawDBAccess.GetMongoDB()
    collection = db["wikipediaFeed"]
    for doc in collection.find():

        for image in doc["images"]:
            images[image] += 1
        
        #doc["summary"]  = re.sub(r"[ ]+" , " ", re.sub(r"[\r\n=]" ," ", doc["summary"])).strip(" ")
        #doc["content"]  = re.sub(r"[ ]+" , " ", re.sub(r"[\r\n=]" ," ", doc["content"])).strip(" ")
        #doc["summary"]  = re.sub(r"[ ]+" , " ", doc["summary"]) 
        #doc["content"]  = re.sub(r"[ ]+" , " ", doc["content"])   
        #collection.save(doc)
    out = ""

    sortedByCount = sorted(images.items() , key = lambda x : x[1])

    out = ["\n" +key + ":" + str(val) for key,val in sortedByCount]

    fi = open("out.txt", "w")
    fi.write("\n".join(out))
    fi.close()

if __name__ == '__main__':
    data ="""
    On September 16, 2016, Terence Crutcher, a 40-year-old man, was fatally shot by police officer Betty Shelby in Tulsa, Oklahoma. He was unarmed during the encounter, in which he was standing near his vehicle in the middle of a street.
The shooting led to protests in Tulsa. On September 22, the Tulsa County District Attorney charged Shelby with first-degree manslaughter and later the shooting was labeled a homicide. On May 17, 2017, a jury found Betty Shelby not guilty of first-degree manslaughter.


== Background ==

Crutcher was a 40-year-old black man. Crutcher's sister described him as a father and said that, at the time of his death, he was enrolled to study music at Tulsa Community College. According to her, he was also involved in his church and sang in the choir. On April 2, 2017, the TV news program \"60 Minutes\" reported that Crutcher had previously served five years in prison for selling crack cocaine and quoted his sister as saying he had an ongoing drug problem.
The officers involved in the incident at Tulsa, Oklahoma, on September 16, 2016, were Betty Shelby and Tyler Turnbough, both of whom are white. Turnbough became an officer in 2009 and Shelby in 2011.


== Incident ==
At 7:36 p.m. on September 16, 2016, police received a 9-1-1 call about an abandoned vehicle in the middle of 36th Street North just west of Lewis Avenue. One caller said: \"Somebody left their vehicle running in the middle of the street with the doors wide open.\" \"The doors are open. The vehicle is still running. It's an SUV. It's like in the middle of the street. It's blocking traffic.\" \"There was a guy running from it, saying it was going to blow up. But I think he's smoking something. I got out and was like, 'Do you need help?'\" \"He was like, 'Come here, come here, I think it's going to blow up.'\" The other caller said: \"There is a car that looks like somebody just jumped out of it and left it in the center of the road on 36th Street North and North Lewis Avenue.\" \"It's dead in the middle of the street.\" \"It's a Navigator. The driver-side door is open like somebody jumped out. It's on the yellow line, blocking traffic. Nobody in the car.\"
Police stated that Crutcher kept reaching into his pocket, refused to show his hands, walked towards his vehicle despite being told to stop, and then angled towards and reached into his vehicle. Turnbough tased Crutcher, and Shelby shot him. Shortly before the shooting, officers in the helicopter conversed with each other: \"This guy's still walking and isn't following commands.\" \"It's time for a taser, I think.\" \"I've got a feeling that's about to happen.\" \"That looks like a bad dude, too, could be on something.\" Approximately two minutes after the shot, an officer checked Crutcher's pockets, and approximately 45 seconds later, someone crouched to offer aid. Police said Crutcher died in the hospital later that day. Tulsa police chief Chuck Jordan said no weapon was recovered from Crutcher's body or vehicle.


== Immediate aftermath ==
Police dashcam and helicopter video as well as the dispatch audio were released by police on September 19, 2016. Tulsa Police Chief Jordan called the video \"disturbing\" and \"difficult to watch\". The officers involved were placed on paid administrative leave.
Crutcher's sister said at a press conference, \"You all want to know who that big, bad dude was? That big, bad dude was my twin brother. That big, bad dude was a father. That big, bad dude was a son. That big, bad dude was enrolled at Tulsa Community College — just wanting to make us proud. That big, bad dude loved God. That big, bad dude was at church, singing, with all his flaws, every week.\"
The Tulsa Police Department started a criminal investigation of the shooting. Homicide Sergeant Dave Walker stated that PCP had been recovered from Crutcher's car. Shelby's attorney had previously stated that she thought Crutcher might be under the influence of PCP based on what she learned during her drug-recognition training. Crutcher's father had stated in a 2012 affidavit that his son had a history of PCP use. They incurred $216,000 in overtime costs for 10 days after the death including increased demonstrations, staffing of patrols, marches, Crutcher’s funeral and news conferences by the district attorney and Crutcher family during which the Incident Management Team also had a command post operating.


== Reactions ==
The United States Department of Justice opened a civil rights probe into the shooting.
Dozens of protestors gathered on September 19 by the courthouse. Ahead of the release of the video and audio recordings, the Tulsa chapter of Black Lives Matter held a protest outside the courthouse.
Crutcher's family, protestors, and the American Civil Liberties Union of Oklahoma have called for Shelby to be charged with his death.


== Criminal charges against officer ==
Tulsa County District Attorney Steve Kunzweiler charged Shelby with first-degree manslaughter. Shelby turned herself in at the Tulsa County Jail on the early morning of September 23, where she was booked and was shortly released after posting a bond of $50,000. The criminal complaint against her said her \"fear resulted in her unreasonable actions which led her to shooting\" Crutcher. Shelby is accused of \"unlawfully and unnecessarily\" shooting Crutcher after he did not comply with her \"lawful orders.\"


== Autopsy results ==
Autopsy results released by the Oklahoma State Medical Examiner indicated that Terence Crutcher had \"acute phencyclidine (PCP) intoxication\" at the time of the shooting. The report stated that Crutcher had 96 nanograms per milliliter of PCP in his blood at the time of death.  The report also indicated that tenocyclidine (TCP), a psychostimulant and hallucinogen which is more potent than PCP, was present.


== See also ==
List of killings by law enforcement officers in the United States
Police brutality in the United States
Shooting of Keith Lamont Scott


== External links ==
White Tulsa Officer Is Acquitted in Fatal Shooting of Black Driver (May 17 2017)


== References ==
    """
    #print(data)
    #print(Helpers.ExtractKeywords(data , 2))
    db = RawDBAccess.GetMongoDB()
    collection = db["wikipediaFeed"]
    for doc in collection.find():
        array= doc["images"]
        doc["images"] = [x for x in array if not re.search("logo|edit\-clear|icon|padlock\-silver|blue_pencil|ambox_important|portal\-puzzle" ,x , re.IGNORECASE)]
        collection.save(doc)
    
    #print(ws.GetLinks())
