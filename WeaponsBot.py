import praw
import time
from requests.exceptions import HTTPError, ReadTimeout
from prawcore.exceptions import RequestException

reddit = praw.Reddit(
    client_id='#######',
    client_secret='######',
    password='##########',
    user_agent='Weapons Bot by Tom/ /u/FlashinessGotRekt',
    username='TBD'
)

subreddit = reddit.subreddit('FlaxTesting')

bots = ["/u/weaponsbot"]

weapontable = {'ak47': ["AK-47", 20, 223, 700, 3, 18.25, 11, "Barrel, Scope", '30, 40, 75'],
               'ak74': ["AK-74", 17, 184, 650, 2.5, 16.5, 7, "Barrel, Scope", "30, 45, 75"],
               'an94': ["AN-94", 17, 170, 600, 2.75, 16.75, 12, "Barrel, scope", "30, 45, 75"],
               'akm': ["AKM", 20, 200, 600, 2.75, 16.75, 12, "Barrel, scope", "30, 40, 75"],
               'ak104': ["AK-104", 20, 200, 600, 2, 17, 11, "Barrel, Underbarrel + Grip, Scope", "30, 40, 75"],
               'ak12': ["AK-12", 20, 200, 600, 1.75, 19.5, 10, "Barrel, Underbarrel + Grip, Scope", "30, 40, 75"],
               'ots14': ["OTs-14", 20, 233, 700, 3.25, 16, 10, "Barrel, Scope", "30, 40, 75"],
               'scarl': ["SCAR-L", 18, 180, 600, 2.25, 17, 8, "Barrel, Underbarrel + Grip, Scope", "30, 50, 100"],
               'm4a1': ["M4A1", 18, 210, 700, 2, 17.5, 8, "Barrel, Underbarrel + Grip, Scope", "30, 50, 100"],
               'g36k': ["G36K", 18, 225, 750, 1.75, 18, 7, "Barrel, Underbarrel + Grip, Scope", "30, 50, 100"],
               'mp5': ["MP5", 14, 187, 800, 3.5, 14, 6, "Barrel, Underbarrel + Grip, Scope", "30"],
               'aks74u': ["AKS-74U", 17, 198, 700, 3.75, 15.5, 8, "Barrel, Scope", "30, 45, 75"],
               'pp19': ["PP-19", 13, 141, 650, 4, 14.5, 5, "Barrel, Scope", "64"],
               'g3': ["G3", 22, 220, 600, 1.25, 19, 11, "Barrel, Underbarrel + Grip, Scope", "20, 30, 50"],
               'hk417': ["HK417", 22, 220, 600, 1.5, 17, 10, "Barrel, Underbarrel + Grip, Scope", "20, 30, 50"],
               'm14': ["M14", 22, 257, 700, 0.75, 22.25, 10, "Barrel, Underbarrel + Grip, Scope", "20, 30, 50"],
               'fal': ["FAL", 22, 257, 700, 1, 17, 11, "Barrel, Underbarrel + Grip, Scope", "20, 30, 50"],
               'mk17': ["Mk17", 22, 229, 625, 1, 18, 10, "Barrel, Underbarrel + Grip, Scope", "20, 30, 50"],
               'm870': ["M870", 40, "N/A", 100, 30, 37.5, 30, "Underbarrel + Grip, Scope", "8"],
               'm1014': ["M1014", 40, 400, 600, 25, 32.5, 25, "Underbarrel + Grip, Scope", "8"],
               'dbshotgun': ["DB Shotgun", 40, 400, 600, 27.5, 35, 30, "None", "2"],
               'maverick 88': ["Maverick 88", 32, "N/A", 100, 22.5, 27.5, 23, "None", "6"],
               'auto5': ["Auto-5", 32, 320, 600, 25, 30, 18, "None", "6"],
               'm3': ["M3", 14, 105, 405, 4, 15, 6, "None", "30"],
               'mosinnagant': ["Mosin Nagant", 22, "N/A", 100, 0.75, 18, 15, "None", "5"],
               'leeenfield': ["Lee Enfield", 23, "N/A", 100, 1, 18, 15, "None", "10"],
               'm1garand': ["M1 Garand", 22, 220, 600, 1.25, 20, 12, "None", "8"],
               'fedorov': ["Fedorov", 19, 127, 400, 3.5, 18, 11, "None", "25"],
               'sks': ["SKS", 20, 200, 600, 1.5, 19, 11, "None", "10"],
               'ppsh': ["PPSh", 19, 317, 1000, 4.25, 21.75, 10, "None", "35"],
               'rpk': ["RPK", 20, 200, 600, 3, 22.5, 8, "Barrel, Scope", "30, 40, 75"],
               'm249': ["M249", 18, 225, 750, 2.75, 26, 7, "Underbarrel + Grip, Scope", "100"],
               'mk48': ["MK 48", 22, 257, 700, 3, 26.5, 9, "Underbarrel + Grip, Scope", "100"],
               'hk21': ["HK21", 22, 330, 900, 2.75, 25, 9, "Barrel, Underbarrel + Grip, Scope", "20, 30, 50"],
               'tec9': ["TEC-9", 14, 175, 750, 5, 17.75, 9, "Barrel", "20, 32"],
               'm93r': ["M93R", 14, 210, 900, 4.75, 17, 8, "Barrel", "17, 32"],
               'g18': ["G18", 14, 210, 900, 4.75, 17.5, 9, "Barrel, Underbarrel", "17, 32"],
               'uzi': ["UZI", 14, 163, 700, 4, 17.75, 8, "Barrel, Scope", "20, 32"],
               'cbjms': ["CBJ-MS", 14, 163, 700, 3.75, 18, 8, "Barrel, Scope", "20, 32"],
               'g37': ["G37", 19, 190, 600, 4.25, 18.25, 12, "Barrel", "12"],
               'mk23': ["Mk 23", 19, 190, 600, 4, 18.25, 11, "Barrel", "12"],
               'usp45': ["Usp45", 19, 190, 600, 4.5, 19, 11, "Barrel, Underbarrel", "12"],
               'm9': ["M9", 14, 140, 600, 4.5, 17, 9, "Barrel, Underbarrel", "17, 32"],
               'makarov': ["Makarov", 13, 130, 600, 5.25, 17.5, 9, "Barrel", "8"],
               'revolver': ["Revolver", 19, 190, 600, 5, 18.75, 13, "None", "6"],
               'm1911': ["M1911", 19, 190, 600, 4.75, 18.5, 12, "Barrel, Underbarrel", "7"],
               'cz75': ["CZ-75", 14, 140, 600, 4.75, 17, 9, "Barrel, Underbarrel", "12"],
               'model459': ["Model 459", 14, 140, 600, 4.75, 17.75, 8, "Barrel, Underbarrel", "14"],
               'patriot': ["Patriot", 18, 285, 950, "Unknown", "Unknown", 9, "Barrel, Underbarrel + Grip, Scope",
                           "30, 50, 100"],
               'model29': ["Model 29", "Unknown", "Unknown", "Unknown", 3.5, "Unknown", "None", 6]
               }


meleetable = {
    'combat knife': ["Combat Knife", 24, "Fast"],
    'crowbar': ["Crowbar", 26, "Slow"],
    'hatchet': ["Hatchet", 30, "Slow"],
    "sabre": ["Sabre", 30, "Fast"],
    'katana': ['Katana', 'Unknown', 'Fast']
}


def varcheck(string):
    newstring = string.replace('-', '').replace(" ", "")
    return newstring


damage = 0
dps = 0
firerate = 0
ads = 10000
hipfire = 10000
recoil = 10000
#
hdamage = ""
hdps = ""
hfirerate = ""
hads = ""
hhipfire = ""
hrecoil = ""
#
mdamage = 0
hmdamage = ""


def msort(xi):
    for z in meleetable:
        if str(xi) == str(z):
            global mdamage
            global hmdamage
            if isinstance(meleetable[str(z)][1], int):
                if meleetable[str(z)][1] > mdamage:
                    mdamage = meleetable[str(z)][1]
                    hmdamage = str(z)


def mb(xee):
    for zei in meleetable:
        if str(xee) == str(zei):
            returnvals = [str(meleetable[str(zei)][0]) + "|"]
            if str(xee) == hmdamage:
                returnvals.append("**" + str(meleetable[str(xee)][1]) + "**|")
            else:
                returnvals.append(str(meleetable[str(xee)][1]) + "|")
            returnvals.append((str(meleetable[str(xee)][2]) + "|" + "\n"))
            return "".join(returnvals)


def wtw(v):
    for k in weapontable:
        if str(v) == str(k):
            returnvals = [str(weapontable[str(k)][0]) + "|"]
            if str(v) == hdamage:
                returnvals.append("**" + str(weapontable[str(k)][1]) + "**|")
            else:
                returnvals.append(str(weapontable[str(k)][1]) + "|")
            if str(v) == hdps:
                returnvals.append("**" + str(weapontable[str(k)][2]) + "**|")
            else:
                returnvals.append(str(weapontable[str(k)][2]) + "|")
            if str(v) == hfirerate:
                returnvals.append("**" + str(weapontable[str(k)][3]) + "**|")
            else:
                returnvals.append(str(weapontable[str(k)][3]) + "|")
            if str(v) == hads:
                returnvals.append("**" + str(weapontable[str(k)][4]) + "**|")
            else:
                returnvals.append(str(weapontable[str(k)][4]) + "|")
            if str(v) == hhipfire:
                returnvals.append("**" + str(weapontable[str(k)][5]) + "**|")
            else:
                returnvals.append(str(weapontable[str(k)][5]) + "|")
            if str(v) == hrecoil:
                returnvals.append("**" + str(weapontable[str(k)][6]) + "**|")
            else:
                returnvals.append(str(weapontable[str(k)][6]) + "|")
            returnvals.append(str(weapontable[str(k)][7]) + "|")
            returnvals.append(str(weapontable[str(k)][8]) + "|" + '\n')

            return "".join(returnvals)


def sort(a):
    for y in weapontable:
        if str(a) == str(y):
            global damage
            global hdamage
            global dps
            global hdps
            global firerate
            global hfirerate
            global ads
            global hads
            global hipfire
            global hhipfire
            global recoil
            global hrecoil
            if isinstance(weapontable[str(a)][1], int):
                if weapontable[str(a)][1] > damage:
                    damage = weapontable[str(a)][1]
                    hdamage = str(a)
            if isinstance(weapontable[str(a)][2], int):
                if weapontable[str(a)][2] > dps:
                    dps = weapontable[str(a)][2]
                    hdps = str(a)
            if isinstance(weapontable[str(a)][3], int):
                if weapontable[str(a)][3] > firerate:
                    firerate = weapontable[str(a)][3]
                    hfirerate = str(a)
            if isinstance(weapontable[str(a)][4], int):
                if weapontable[str(a)][4] < ads:
                    ads = weapontable[str(a)][4]
                    hads = str(a)
            if isinstance(weapontable[str(a)][5], int):
                if weapontable[str(a)][5] < hipfire:
                    hipfire = weapontable[str(a)][5]
                    hhipfire = str(a)
            if isinstance(weapontable[str(a)][6], int):
                if weapontable[str(a)][6] < recoil:
                    recoil = weapontable[str(a)][6]
                    hrecoil = str(a)


'''def parsesubmissions():
    for submission in subreddit.stream.submissions():
        logwrite = open("ReplyDirectory.txt", "r+")
        botmatch = any(string in submission.selftext.lower() for string in bots)
        weapmatch = any(string in submission.selftext.lower() for string in weapontable)
        body = submission.selftext.lower()
        if botmatch and weapmatch and submission.id not in logwrite.read():
            weapons = []
            if any(string in submission.selftext for string in weapontable):
                final = []
                for z in weapontable:
                    if z in body and z not in weapons:
                        weapons.append(str(z))
                if len(weapons) > 1:
                    for m in weapons:
                        sort(m)
                for wep in weapons:
                    final.append(str(wtw(wep)))
                t = "".join(final)
                submission.reply("Weapon|Damage|DPS|Firerate|ADS Spread|Hipfire Spread|"
                                 "Recoil|Attachment Capabilities|Magazine Capacities"
                                 "\n :-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-: \n" + t + '\n \n' "*Underbarrel + Grip "
                                                                                   "= Takes "
                                                                                   "grips, Underbarrel = Doesn't take "
                                                                                   "grips (only takes flashlight and "
                                                                                   "laser)*")
                print(str(submission.id) + " - " + str(submission.author) + " - " + str(submission.title))
                logwrite.write(str(submission.id) + '\n')'''



def CheckLog(id):
    with open("ReplyDirectory.txt", "r+") as file:
        found = any(str(id) in line.split() for line in file)
        if found:
            return True
        else:
            return False


def parsecomments():
    for comment in subreddit.stream.comments():
        botmatch = any(string in comment.body.lower() for string in bots)
        weapmatch = any(string in comment.body.lower() for string in weapontable)
        melmatch = any(string in comment.body.lower() for string in meleetable)
        alreadyreplied = False
        if CheckLog(str(comment.id)):
            alreadyreplied = True
        body = comment.body.lower()
        hasmelee = False
        if botmatch and melmatch:
            hasmelee = True
        if botmatch and weapmatch and not alreadyreplied and not hasmelee:
            weapons = []
            if any(string in comment.body for string in weapontable):
                final = []
                for z in weapontable:
                    if z in varcheck(body) and z not in weapons:
                        weapons.append(str(z))
                if len(weapons) > 1:
                    for m in weapons:
                        sort(m)
                for wep in weapons:
                    final.append(str(wtw(wep)))
                t = "".join(final)
                comment.reply(r"Weapon|Damage|DPS|Firerate|ADS Spread|Hipfire Spread|"
                              r"Recoil|Attachment Capabilities|Magazine Capacities"
                              "\n :-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:| \n" + t + '\n \n' "*Underbarrel + Grip "
                                                                                 "= Takes "
                                                                                 "grips, Underbarrel = Doesn't take "
                                                                                 "grips (only takes flashlight and "
                                                                                 "laser)* \n \n *Unknown = Accurate"
                                                                                 "weapon statistic currently unknown.*")
                print(str(comment.id) + " - " + str(comment.author))
                open("ReplyDirectory.txt", "a").write(str(comment.id) + " \n")
        elif botmatch and weapmatch and not alreadyreplied and hasmelee:
            weapons = []
            melees = []
            if any(string in comment.body for string in weapontable):
                final = []
                mfinal = []
                for z in weapontable:
                    if z in varcheck(body) and z not in weapons:
                        weapons.append(str(z))
                for v in meleetable:
                    if v in varcheck(body) and v not in melees:
                        melees.append(str(v))
                if len(weapons) > 1:
                    for m in weapons:
                        sort(m)
                if len(melees) > 1:
                    for mi in melees:
                        msort(mi)
                for wep in weapons:
                    final.append(str(wtw(wep)))
                for mel in melees:
                    mfinal.append(str(mb(mel)))
                t = "".join(final)
                mj = "".join(mfinal)
                comment.reply(r"Weapon|Damage|DPS|Firerate|ADS Spread|Hipfire Spread|"
                              r"Recoil|Attachment Capabilities|Magazine Capacities|"
                              "\n :-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:| \n" + t + '\n \n' "*Underbarrel + Grip "
                                                                                 "= Takes "
                                                                                 "grips, Underbarrel = Doesn't take "
                                                                                 "grips (only takes flashlight and "
                                                                                 "laser)* \n \n *Unknown = Accurate"
                                                                                 "weapon statistic currently unknown.*"
                              + '\n \n' +
                              "Weapon|Damage|Speed| \n :-:|:-:|:-:| \n" + mj)
                print(str(comment.id) + " - " + str(comment.author))
                open("ReplyDirectory.txt", "a").write(str(comment.id) + " \n")
        elif botmatch and not weapmatch and not alreadyreplied and hasmelee:
            melees = []
            if any(string in comment.body for string in meleetable):
                mfinal = []
                for v in meleetable:
                    if v in varcheck(body) and v not in melees:
                        melees.append(str(v))
                    if len(melees) > 1:
                        for mi in melees:
                            msort(mi)
                    for mel in melees:
                        mfinal.append(str(mb(mel)))
                    mj = "".join(mfinal)
                    comment.reply(
                                  "Weapon|Damage|Speed| \n :-:|:-:|:-:| \n" + mj + "\n \n *Unknown = Accurate "
                                                                                   "weapon statistic currently unknown.*"
                    )
                    print(str(comment.id) + " - " + str(comment.author))
                    open("ReplyDirectory.txt", "a").write(str(comment.id) + " \n")


while True:
    try:
        parsecomments()
    except (
            praw.exceptions.APIException, praw.exceptions.ClientException, praw.exceptions.PRAWException,
            RequestException,
            HTTPError, ReadTimeout
    ) as x:
        print(x)
        time.sleep(1)

