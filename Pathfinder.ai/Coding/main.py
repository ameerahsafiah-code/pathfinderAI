import pandas as pd
import random

def generate_visual_data():
    """
    Menjana data simulasi trend keperluan industri untuk tempoh 5 tahun akan datang.
    Data ini digunakan oleh Plotly Express di dalam App.py.
    """
    years = ["Tahun 1", "Tahun 2", "Tahun 3", "Tahun 4", "Tahun 5"]
    demand_growth = [
        random.randint(60, 70),
        random.randint(68, 78),
        random.randint(75, 85),
        random.randint(80, 90),
        random.randint(88, 98)
    ]
    
    data = {
        'tahun': years,              # Mewakili paksi X (Timeline)
        'Minat Pasaran': demand_growth # Mewakili paksi Y (Keperluan Industri %)
    }
    
    return pd.DataFrame(data)