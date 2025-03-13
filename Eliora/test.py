import os
import pandas
import re
import numpy
from unidecode import unidecode

def registrar_material(
    title: str,
    year: int,
    thumbnail: str,
    topic: str,
    filename: str,
    author: str,
    level: str,
    alttext: str
):
    with open("_data/material/entrenamientos.csv", 'a') as f:
        f.write(f""""{title}","{unidecode(title)}",{year},{thumbnail},{topic},{filename},"{author}",{level},"{alttext}"\n""")
    
registrar_material("arst", 2022, "sta","asrt", "astas","arsta","asrtasr","asta")