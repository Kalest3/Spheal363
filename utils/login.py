import json
import requests
import websockets
from config import *
from utils.commands.commands import *
async def Login(websocket):
    global battleOn
    global logCons
    loginDone = False
    battleOn = False
    logCons = None
    while True:
        msg = await websocket.recv()
        msg = str(msg)
        if msg[0:10] == '|challstr|':
            challstr = msg[0:99999]
            challstr = challstr.replace('|challstr|', '')
            challstr = challstr.strip()
            postlogin = requests.post('https://play.pokemonshowdown.com/~~showdown/action.php', data={'act':'login','name':username,'pass':password,'challstr':challstr})
            assertion = json.loads(postlogin.text[1:])["assertion"]
            await websocket.send(f'|/trn {username},0,{assertion}')
            await websocket.send(f'|/avatar {avatar}')
            for room in rooms:
                await websocket.send(f'|/j {room}')
            loginDone = True
        if loginDone != False:
            await onLogin(msg=msg, websocket=websocket)
async def onLogin(msg, websocket):
    if '|pm|' in msg:
        userSearch = msg.split('|')[2]
        userSearch = userSearch.replace(' ', '')
        userSearch = userSearch.lower()
        userSearch = userSearch.strip()
        await runall(msg=msg, websocket=websocket, userSearch=userSearch)