import requests
import time
import datetime

mainAuth = {
    'authorization': "MjI4MjkyNTQ0ODU5OTk2MTYw.G82_Sv.IPUAL_3Up20F_D3sf924Xvm_vyigHIV_Q83xmU"
}

bobbybot1 = {
    'authorization': "Mzc4Njc5GHvbOTE4ODcxMDQx.G2OldJ.RNHFxbhjRGue2sYj9YkmXJht3vcvAGrsRMuerI"
}

bobbybot2 = {
    'authorization': "MSnfwbMzNTEzMTIuhsXCHScxOQ.GxyYtv.KyVuP6B1V8_kgHfn1cvXx3Bx2Tm0fW40tBDM"
}

authList = {"bobbybot2": bobbybot2,
            "bobbybot1": bobbybot1
    }

#mainAuth": mainAuth,
def serve(id):
    return "https://discord.com/api/v9/channels/{0}/messages".format(id)

#===================================================
#LOST NEMO CHANNELS
worldChannel = serve(734717853965615124)
seedsChannel = serve(1105154359114875072)
farmableChannel = serve(846678373635457024)
roleDropChannel = serve(782718661336760380)
farmsChannel = serve(846678280928624650)
bountifulChannel = serve(782718872498208778)
scienceChannel = serve(762448042011000842)
neckChannel = serve(944660041636659271)
handsChannel = serve(889195913275408455)
blocksChannel = serve(1104057271215984741)
providersChannel = serve(880294786236579860)
botChannel = serve(1106333041791598654)
#===================================================

#growtopia channels
growWorld = serve(691266751505104926)
growBlock = serve(691266691522363444)
growSeeds = serve(1012887781418205255)
#==================================================
#test server
advertising1 = serve(1176297197139144716)
advertising2 = serve(1176297257847492669)
advertising3 = serve(1176297243138064385)

#==================================================

seedsList = {"seedsChannel" : seedsChannel,
            "farmableChannel": farmableChannel,
            "scienceChannel": scienceChannel,
            "neckChannel": neckChannel,
            "handsChannel": handsChannel,
            "blocksChannel": blocksChannel,
            "providersChannel": providersChannel
            }


growSeedsList = {"growBlock" : growBlock,
                 "growSeeds" : growSeeds

}

testList = {"advertising1": advertising1,
            "advertising2": advertising2,
            "advertising3": advertising3
            }



#=======================




def printTime(): 
    return("{}:{}:{} | {}/{}".format(time.localtime()[3],time.localtime()[4],time.localtime()[5],time.localtime()[1],time.localtime()[2]))

def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
 
def iterateChannels(dic, timeout, message, accounts):
    for i in range(len(dic)):
        for j in range(len(accounts)):
            print(list(dic.keys())[i],"|", printTime(), "|", list(accounts.keys())[j])
            r = requests.post(dic.get(list(dic.keys())[i]), data=message, headers = accounts.get(list(accounts.keys())[j]))
            countdown(int(((timeout)/len(dic) /len(accounts))))

        # print(list(seedsList.keys())[i], printTime())
        # r = requests.post(seedsList.get(list(seedsList.keys())[i]), data=payload, headers = header)
        # countdown(int((2*60*60+5)/len(seedsList)))


seedsAd = {
    'content': """
SELL UN SCIENCE STATION 2/1 HAVE TONS GO **JNBOJ**
SELL UN SCIENCE STATION 2/1 HAVE TONS GO **JNBOJ**
SELL UN SCIENCE STATION 2/1 HAVE TONS GO **JNBOJ**
**OR 200/75 MSG ME**

SELL TOXIC WASTE BARREL SEED 200/140 DM ME HAVE TONS

BUY LIST:
BUY BARREL SEED 40/1 MSG ME
"""

}
worldAd = {
    'content': """sell worlds (can offer)
BUYDISCOBALLBLOCKS - 5 DL (HAVE DESIGN + CLEAR + STOCK)
BFGMAMALINK - 1 DL
TRADESX3 - 75 WL
BUYGGALAXYS - 50 WL"""
}

editingAd = {
    'content': """ **Selling YouTube Intros  |  24hr Return Time!**
Click to see templates! Free Revisions!
https://www.fiverr.com/bobbybotbop/create-a-vaporwave-youtube-intro
"""
}
        
print("================================================================================================")
while True:
    
    #world
    # print("worldChannel", printTime())
    # a = requests.post(worldChannel, data=worldAd, headers = mainAuth)
    # countdown(5)
    iterateChannels(testList, 31, editingAd, authList)

    