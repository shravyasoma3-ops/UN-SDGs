import database

def normalize(value) -> str:
    return str(value or "").strip().lower()

def is_forest_land(district: str, taluk: str, village: str, syno: str) -> bool:
    df = database.get_dataframe()
    
    mask = (
        (df['District'] == normalize(district)) &
        (df['Taluk'] == normalize(taluk)) &
        (df['Village'] == normalize(village)) &
        (df['SyNo'] == normalize(syno))
    )
    return not df[mask].empty
