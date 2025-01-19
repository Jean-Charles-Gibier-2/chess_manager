class Player:
    def __init__(self, ime, name, surname, birth, rank):
        self.ime = ime
        self.name = name
        self.surname = surname
        self.birth = birth
        self.rank = rank

    def serialize(self):
        return {
            "ime": self.ime,
            "name": self.name,
            "surname": self.surname,
            "birth": self.birth,
            "rank": self.rank
        }

    @staticmethod
    def deserialize(json_value):
        return Player(**json_value)