from datetime import datetime

from src.entities.citizen import Citizen


class CitizenEditForm:
    citizen = Citizen()
    data = {}

    def __init__(self, citizen: Citizen, data: dict):
        self.citizen = citizen
        self.data = data

    def loadFromDict(self):
        if self.data.get('name'):
            self.citizen.name = self.data.get('name')

        if self.data.get('gender'):
            self.citizen.gender = self.data.get('gender')

        if self.data.get('birth_date'):
            self.citizen.birth_date = datetime.strptime(self.data.get('birth_date'), '%d.%m.%Y')

        if None != self.data.get('relatives'):
            self.citizen.relatives = self.data.get('relatives')

        if self.data.get('town'):
            self.citizen.town = self.data.get('town')

        if self.data.get('street'):
            self.citizen.street = self.data.get('street')

        if self.data.get('building'):
            self.citizen.building = self.data.get('building')

        if self.data.get('apartment'):
            self.citizen.apartment = self.data.get('apartment')

    def validate(self) -> bool:
        isEmpty = True
        for element in self.data:
            if self.data.get(element):
                isEmpty = False
                break
        if isEmpty:
            return False

        if self.data.get('relatives'):
            if not self._relative_validate(self.data.get('relatives')):
                return False

        if self.data.get('birth_date'):
            try:
                birthday = datetime.strptime(self.data.get('birth_date'), '%d.%m.%Y')
                if birthday > datetime.now():
                    raise ValueError
            except ValueError:
                return False

        return True

    def _relative_validate(self, relatives) -> bool:
        if not relatives:
            return True

        countCitizen = Citizen.query.filter(Citizen.citizen_id.in_(relatives)).filter(
            Citizen.import_id == self.citizen.import_id).count()
        if countCitizen != len(set(relatives)):
            return False

        return True
