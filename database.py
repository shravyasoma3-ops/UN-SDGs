import io
import time
from abc import ABC, abstractmethod
import pandas as pd
_FOREST_DF = None
def normalize_string(value) -> str:
    if value is None:
        return ""
    return str(value).strip().lower()
def load_forest_registry():
    """Loads the 144 records into a globally indexed, pre-normalized DataFrame."""
    global _FOREST_DF

    raw_csv_data = """District,Range,Taluk,Hobli,Village,SyNo,Extent_Ha
Bagalkot,Bagalkot,Bagalkot,Sitimani,Mugalolli,37/1A,1.05
Bagalkot,Bagalkot,Bagalkot,Sitimani,Chikkahodlur,46,25.90
Bagalkot;Hungund; Hungund; Amingad,Kamatagi,101,12.50
Bagalkot,Bagalkot,Bagalkot,Sitimani,Mugalolli,25/1A,72.87
Bagalkot,Bagalkot,Bagalkot,Bagalkot,Mudapaljivi,3/1A,40.46
Bagalkot,Bagalkot,Bagalkot,Sitimani,Rampur,26/32,165.12
Belagavi,Athani,Athani,Athani,Athani,963,39.30
Belagavi,Athani,Athani,Athani,Athani,1220,6.09
Belagavi,Athani,Athani,Athani,Athani,1228,6.92
Belagavi,Athani,Athani,Athani,Athani,1240,9.76
Belagavi,Athani,Athani,Athani,Athani,1386,17.85
Belagavi,Athani,Athani,Athani,Athani,1008/A,9.03
Belagavi,Athani,Athani,Athani,Darur,16,3.64
Belagavi,Athani,Athani,Athani,Darur,18,9.00
Belagavi,Athani,Athani,Athani,Satti,526,21.13
Belagavi,Athani,Athani,Athani,Satti,667,40.51
Belagavi,Athani,Athani,Athani,Savadi,18,17.12
Belagavi,Athani,Athani,Athani,Shirahatti,433,18.62
Belagavi,Athani,Athani,Kagawad,Ainapur,154,11.47
Belagavi,Athani,Athani,Kagawad,Ainapur,407,5.32
Belagavi,Athani,Athani,Kagawad,Ainapur,507,8.50
Belagavi,Athani,Athani,Kagawad,Ainapur,527,21.47
Belagavi,Athani,Athani,Kagawad,Ainapur,530,22.80
Belagavi,Athani,Athani,Telsanga,Aigali,102,5.39
Belagavi,Athani,Athani,Telsanga,Aigali,224,17.88
Belagavi,Athani,Athani,Telsanga,Aigali,502,9.74
Belagavi,Athani,Athani,Telsanga,Aigali,581,0.55
Belagavi,Athani,Athani,Telsanga,Badagi,55,17.86
Belagavi,Athani,Athani,Telsanga,Kokatnur,1231,74.99
Belagavi,Athani,Athani,Telsanga,Nandagaon,582,98.80
Belagavi,Athani,Athani,Telsanga,Telasang,545,6.94
Belagavi,Athani,Athani,Telsanga,Telasang,729,28.38
Belagavi,Athani,Athani,Telsanga,Telasang,767,157.83
Belagavi,Athani,Athani,Telsanga,Telasang,985,2.17
Belagavi,Athani,Athani,Telsanga,Telasang,994,5.71
Belagavi,Athani,Athani,Telsanga,Telasang,995,6.54
Belagavi,Athani,Athani,Telsanga,Telasang,996,6.17
Belagavi,Athani,Athani,Telsanga,Telasang,997,6.14
Belagavi,Athani,Athani,Telsanga,Telasang,1001,5.36
Belagavi,Athani,Athani,Telsanga,Telasang,1003,5.67
Belagavi,Athani,Athani,Telsanga,Telasang,1004,5.73
Belagavi,Athani,Athani,Telsanga,Telasang,1005,5.41
Belagavi,Nesargi,Belagavi,Bagewadi,Kardiguddi,180,208.41
Belagavi,Nesargi,Belagavi,Bagewadi,Kardiguddi,181,155.40
Belagavi,Nesargi,Belagavi,Bagewadi,Kardiguddi,182,169.55
Belagavi,Kakati,Belagavi,Kakati,Heggeri,105,174.17
Belagavi,Gujanal,Belagavi,Kakati,Malamardi (hudali),129/1,23.95
Belagavi,Kakati,Belagavi,Kakati,Ramdurga,27,4.19
Belagavi,Kakati,Belagavi,Kakati,Sutagatti,58,255.47
Belagavi,Kakati,Belagavi,Kakati,Sutagatti,59,232.75
Belagavi,Kakati,Belagavi,Kakati,Sutagatti,66,6.14
Belagavi,Kakati,Belagavi,Kakati,Sutagatti,67,8.50
Belagavi,Kakati,Belagavi,Kakati,Sutagatti,68,151.40
Belagavi,khanapur,Belagavi,Uchagaon,Bakanur,13,3.83
Belagavi,khanapur,Belagavi,Uchagaon,Bakanur,19,3.91
Belagavi,khanapur,Belagavi,Uchagaon,Bakanur,23,7.35
Belagavi,khanapur,Belagavi,Uchagaon,Bakanur,26,4.07
Belagavi,khanapur,Belagavi,Uchagaon,Bakanur,44,3.42
Belagavi,khanapur,Belagavi,Uchagaon,Bakanur,46,3.83
Belagavi,Belagavi,Belagavi,Uchagaon,Dhamane,11/A,0.65
Belagavi,Belagavi,Belagavi,Uchagaon,Dhamane,16/2,0.30
Belagavi,Belagavi,Belagavi,Uchagaon,Dhamane,20/2,0.52
Belagavi,Belagavi,Belagavi,Uchagaon,Dhamane,21/2.,4.94
Belagavi,Belagavi,Belagavi,Uchagaon,Dhamane,38/A,3.95
Belagavi,Belagavi,Belagavi,Uchagaon,Dhamane,5/A,5.99
Belagavi,Belagavi,Belagavi,Uchagaon,Dhamane,6/2.,3.64
Belagavi,Belagavi,Belagavi,Uchagaon,Dhamane,8/2.,4.72
Belagavi,Belagavi,Belagavi,Uchagaon,Dhamane,9/2.,5.67
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,24/3,5.92
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,3/2,2.30
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,30/2,0.41
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,33/2,0.16
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,34/2,2.47
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,35/2,2.25
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,36/2,2.48
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,37/2,4.19
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,39/10,5.48
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,39/11,9.01
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,4/2,1.28
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,43/2,3.01
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,5/2,2.84
Belagavi,Belagavi,Belagavi,Uchagaon,Karle,7/2,20.06
Belagavi,Gujanal,Belagavi,Yamakanamaradi,Shabandar,90,4.37
Belagavi,Gujanal,Belagavi,Yamakanamaradi,Shabandar,91,7.59
Belagavi,Gujanal,Belagavi,Yamakanamaradi,Shabandar,110,4.73
Belagavi,Gujanal,Belagavi,Yamakanamaradi,Yallapur,327,136.13
Belagavi,Chikkodi,Chikkodi,Chikkodi,Chinchani,103,19.73
Belagavi,Chikkodi,Chikkodi,Chikkodi,Pattankudi,258,20.32
Belagavi,Chikkodi,Chikkodi,Chikkodi,Pattankudi,259,3.69
Belagavi,Chikkodi,Chikkodi,Chikkodi,Pattankudi,264,0.49
Belagavi,Chikkodi,Chikkodi,Chikkodi,Pattankudi,265,13.44
Belagavi,Chikkodi,Chikkodi,Chikkodi,Pattankudi,267,0.95
Belagavi,Chikkodi,Chikkodi,Chikkodi,Pattankudi,269,63.62
Belagavi,Chikkodi,Chikkodi,Chikkodi,Walki,52,34.17
Belagavi,Chikkodi,Chikkodi,Nagarmunnoli,Jainapur,33,18.23
Belagavi,Chikkodi,Chikkodi,Nagarmunnoli,Jainapur,43,11.50
Belagavi,Chikkodi,Chikkodi,Nagarmunnoli,Jainapur,44,5.26
Belagavi,Chikkodi,Chikkodi,Nagarmunnoli,Jainapur,73,0.67
Belagavi,Chikkodi,Chikkodi,Nagarmunnoli,Jainapur,74,0.10
Belagavi,Chikkodi,Chikkodi,Nagarmunnoli,Jainapur,241,2.62
Belagavi,Chikkodi,Chikkodi,Nagarmunnoli,Jainapur,305,4.19
Belagavi,Chikkodi,Chikkodi,Nagarmunnoli,Jainapur,312,1.79
Belagavi,Chikkodi,Chikkodi,Nagarmunnoli,Jainapur,325,2.44
Belagavi,Chikkodi,Chikkodi,Nagarmunnoli,Jainapur,54A/1,8.66
Belagavi,Chikkodi,Chikkodi,Nippani,Adi,305,12.21
Belagavi,Chikkodi,Chikkodi,Nippani,Adi,310,16.13
Belagavi,Chikkodi,Chikkodi,Nippani,Adi,350,19.82
Belagavi,Chikkodi,Chikkodi,Nippani,Adi,358,28.44
Belagavi,Chikkodi,Chikkodi,Nippani,Adi,376,8.97
Belagavi,Chikkodi,Chikkodi,Nippani,Adi,462,6.36
Belagavi,Chikkodi,Chikkodi,Nippani,Gavan,40/1,26.74
Belagavi,Chikkodi,Chikkodi,Nippani,Gavani,40A,30.86
Belagavi,Chikkodi,Chikkodi,Nippani,Sendur,249,30.85
Belagavi,Chikkodi,Chikkodi,Nippani,Sendur,264,1.29
Belagavi,Chikkodi,Chikkodi,Nippani,Sendur,319,51.41
Belagavi,Chikkodi,Chikkodi,Nippani,Sendur,336,11.02
Belagavi,Chikkodi,Chikkodi,Nippani,Sendur,362,34.50
Belagavi,Chikkodi,Chikkodi,Nippani,Sendur,2.17,2.17
Belagavi,Chikkodi,Chikkodi,Nippani,Sendur,333A,32.44
Belagavi,Chikkodi,Chikkodi,Nippani,Sendur,333C,28.75
Belagavi,Chikkodi,Chikkodi,Nippani,Shendur,249,30.98
Belagavi,Chikkodi,Chikkodi,Nippani,Shendur,264,5.45
Belagavi,Chikkodi,Chikkodi,Nippani,Shendur,319,51.43
Belagavi,Chikkodi,Chikkodi,Nippani,Shendur,336,11.19
Belagavi,Chikkodi,Chikkodi,Nippani,Shendur,333/1A,32.54
Belagavi,Chikkodi,Chikkodi,Nippani,Soundagalga,278,12.57
Belagavi,Chikkodi,Chikkodi,Nippani,Soundagalga,280,7.37
Belagavi,Chikkodi,Chikkodi,Nippani,Soundagalga,282,6.88
Belagavi,Chikkodi,Chikkodi,Nippani,Soundagalga,290,11.37
Belagavi,Chikkodi,Chikkodi,Nippani,Soundagalga,321,24.58
Belagavi,Chikkodi,Chikkodi,Nippani,Yaranal,77,3.31
Belagavi,Chikkodi,Chikkodi,Nippani,Yaranal,78,8.59
Belagavi,Chikkodi,Chikkodi,Nippani,Yaranal,190,0.57
Belagavi,Chikkodi,Chikkodi,Nippani,Yaranal,191,7.81
Belagavi,Chikkodi,Chikkodi,Nippani,Yaranal,111A,35.29
Belagavi,Chikkodi,Chikkodi,Sankeswar,Bairapur,110,30.67
Belagavi,Chikkodi,Chikkodi,Sankeswar,Haragapur,335A/1,137.94
Belagavi,Chikkodi,Chikkodi,Sankeswar,Hitni,145,11.43
Belagavi,Chikkodi,Chikkodi,Sankeswar,Kanagala,315,69.67
Belagavi,Chikkodi,Chikkodi,Sankeswar,Kesti,452,47.68
Belagavi,Chikkodi,Chikkodi,Sankeswar,Mattiwad,96/1,7.28
Belagavi,Chikkodi,Chikkodi,Sankeswar,Solapur,352,35.93
Belagavi,Chikkodi,Chikkodi,Sankeswar,Solapur,428,62.61
Belagavi,Gokak,Gokak,Gokak,Hoolikatti,117,101.65
"""

    types_dict = {col: str for col in ['District', 'Range', 'Taluk', 'Hobli', 'Village', 'SyNo']}
    _FOREST_DF = pd.read_csv(io.StringIO(raw_csv_data), dtype=types_dict)
    return _FOREST_DF

    def verify_parcel(self, district: str, taluk: str, village: str, syno: str) -> dict:
        """
        Executes highly optimized backend column matching.
        Returns a dictionary with the lookup result. """