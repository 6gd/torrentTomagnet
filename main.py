import os
from fastapi import FastAPI
from pydantic import BaseModel
while True:
    try:
        import magneturi
        import requests
        break
    except:
        os.system("pip install magneturi")
        os.system("pip install requests")
        continue
app = FastAPI()

class Msg(BaseModel):
    msg: str



@app.get("/TorrentToMagnet")
async def get_mangeurl(urlTorrnet: str):
    response = requests.get(urlTorrnet)
    magnet_link = magneturi.from_torrent_data(response.content)
    print("Done")
    return {"magnet":magnet_link}
