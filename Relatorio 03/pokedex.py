from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")


class Pokedex:
    def __init__(self, db: Database):
        self.db = db

    def getPokemonByName(self, name: str):
        return db.collection.find({"name": name})

    def getPokemonFire(self):
        return db.collection.find({"$or": [{"type": "Fire"}, {"weaknesses": "Fire"}]})

    def getPokemonquenaoEvoluem(self):
        return db.collection.find({"next_evolution": {"$exists": False}})

    def getPokemoncomMultipliers(self):
        return db.collection.find({"multipliers": {"$exists": True}})

    def getPokemonSpawn(self):
        return db.collection.find({"spawn_chance": {"$lt": 0.3}})


p = Pokedex(db)

pnome = p.getPokemonByName("Pikachu")

writeAJson(pnome, "Pesquisa por nome")

pfogo = p.getPokemonFire()

writeAJson(pfogo, "Pesquisa por pokemons que são de fogo ou fracos contra fogo")

pevo = p.getPokemonquenaoEvoluem()

writeAJson(pevo, "Pesquisa por pokemons que não evoluem")

pmult = p.getPokemoncomMultipliers()

writeAJson(pmult, "Pesquisa por pokémons com o campo multipliers")

pspawn = p.getPokemonSpawn()

writeAJson(pspawn, "pesquisa por pokemons com chance de spawn menor que 0,3")

db.resetDatabase()
