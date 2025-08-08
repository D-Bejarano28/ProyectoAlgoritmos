from MetroArt import MetroArt
from api_management import * 
from db_nacionalidades import db_nacionalidades

def main():
    db_departamentos = get_departamentos()
    arte = MetroArt(db_departamentos,db_nacionalidades)
    arte.inicio()

main()