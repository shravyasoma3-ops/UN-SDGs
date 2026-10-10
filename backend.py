import io
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
_FOREST_DF = pd.read_csv(io.StringIO("""District,Range,Taluk,Hobli,Village,SyNo,Extent_Ha
Bagalkot,Bagalkot,Bagalkot,Sitimani,Mugalolli,37/1A,1.05
Bagalkot,Bagalkot,Bagalkot,Sitimani,Chikkahodlur,46,25.90
Belagavi,Athani,Athani,Athani,Athani,963,39.30
"""), dtype=str)

cols = ['District', 'Taluk', 'Village', 'SyNo']
_FOREST_DF[cols] = _FOREST_DF[cols].apply(lambda x: x.str.strip().str.lower())

@app.get("/check")
def check(d: str, t: str, v: str, s: str):
    mask = (_FOREST_DF['District'] == d.strip().lower()) & \
           (_FOREST_DF['Taluk'] == t.strip().lower()) & \
           (_FOREST_DF['Village'] == v.strip().lower()) & \
           (_FOREST_DF['SyNo'] == s.strip().lower())
    return not _FOREST_DF[mask].empty

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
