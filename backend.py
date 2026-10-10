import database

def normalise(value) -> str:
    return str(value or "").strip().lower()

def is_forest_land(district: str, taluk: str, village: str, syno: str) -> bool:
    df = database.get_dataframe()
    
    mask = (
        (df['District'] == normalise(district)) &
        (df['Taluk'] == normalise(taluk)) &
        (df['Village'] == normalise(village)) &
        (df['SyNo'] == normalise(syno))
    )
    return not df[mask].empty
