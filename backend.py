from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_headers=["*"])

@app.get("/check")
def check(d: str, t: str, v: str, s: str):
    df = database.get_dataframe()
    mask = (
        (df['District'] == d.strip().lower()) &
        (df['Taluk'] == t.strip().lower()) &
        (df['Village'] == v.strip().lower()) &
        (df['SyNo'] == s.strip().lower())
    )
    return not df[mask].empty

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
