from database import Neo4jClient

uri = "neo4j+s://7cd6de48.databases.neo4j.io"
user = "neo4j"
password = "K66_yjtvUhALE5pbfomI5e9A4D3FCW10mfDZUsKz_aw"

client = Neo4jClient(uri, user, password)

print("Quem da família é Engenheiro?")
print(client.is_engenheiro("João"))
print(client.is_engenheiro("Maria"))

print("Fulano de tal é pai de quem?")
print(client.pai_de_quem("João"))

print("Quem da família tem pet?")
print(client.tem_pet())

client.close()
