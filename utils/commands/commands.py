from config import username, owner
def PM(userSearch, command: str):
   return f'|pm|{userSearch}|{username}|@{command}'
def spheal(user: str):
   return f'|/pm {user}, spheal'
async def runall(msg, websocket, userSearch):
    global owner
    global username
    owner = owner.replace(' ', '')
    owner = owner.lower()
    username = username.replace(' ', '')
    username = username.lower()
    if msg.replace(' ', '').lower() == PM(userSearch, 'spheal'):
        await websocket.send(spheal(user=userSearch))
    if msg.replace(' ', '').lower() == PM(userSearch, 'timer'):
        print(msg.replace(' ', '').lower())