class JogoDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name, id):
        query = "CREATE (:Player {name: $name,id: $id})"
        parameters = {"name": name, "id": id}
        self.db.execute_query(query, parameters)

    def create_match(self, ganhador, id):
        query = "CREATE (:Match {ganhador: $ganhador,id: $id})"
        parameters = {"ganhador": ganhador, "id": id}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_matchs(self):
        query = "MATCH (a:Match) RETURN a.id AS id"
        results = self.db.execute_query(query)
        return [result["id"] for result in results]

    def update_Player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def insert_player_match(self, player_name, match_id):
        query = "MATCH (a:Player {name: $player_name}) MATCH (b:Match {id: $match_id}) CREATE (a)-[:JOGA]->(b)"
        parameters = {"player_name": player_name, "match_id": match_id}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_match(self, id):
        query = "MATCH (a:Match {id: $id}) DETACH DELETE a"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)
