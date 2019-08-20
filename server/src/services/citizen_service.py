from src.entities.citizen import Citizen
from src.form.citizenEditForm import CitizenEditForm
from src.repository.CitizenRepo import CitizenRepo


class CitizenService:
    def editCitizen(self, citizen: Citizen, form: CitizenEditForm):
        if citizen.relatives != form.data.get('relatives'):
            oldRelavites = set(citizen.relatives)
            newRelatives = set(form.data.get('relatives'))
            form.loadFromDict()
            CitizenRepo().saveWithRelation(
                citizen=citizen,
                forDelete=oldRelavites.difference(newRelatives),
                forAdded=newRelatives.difference(oldRelavites)
            )
        else:
            form.loadFromDict()
            CitizenRepo().save(citizen=citizen)
