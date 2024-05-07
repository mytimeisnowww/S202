from database import Database
from jogo_database import JogoDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.236.166.29:7687", "neo4j", "tabulation-superintendent-halts")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
jogo_db = JogoDatabase(db)

jogo_db.create_player("Marcos", 1)
jogo_db.create_player("Bruno", 2)

jogo_db.create_match("Marcos", 1)
jogo_db.create_match("none", 2)

jogo_db.update_Player("Bruno","Bruninho")
jogo_db.insert_player_match("Marcos", 1)
jogo_db.insert_player_match("Bruninho", 1)

jogo_db.get_matchs()
jogo_db.get_players()

jogo_db.delete_player("Marcos")
jogo_db.delete_match(2)
