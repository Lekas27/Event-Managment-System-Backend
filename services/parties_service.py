from typing import Annotated, Optional, Sequence
from fastapi.params import Depends
from model.user_model import User
from repository.parties_repository import PartyRepository
from schemas.parties import PartyCreate
from model.parties_model import Party

class PartiesService:
    def __init__(self, repository: Annotated[PartyRepository, Depends(PartyRepository)]):
        self.repository = repository

    async def add_party(self, create_request: PartyCreate, user: User) -> Party:
        db_party = self.map_create_party(create_request, user)
        return await self.repository.create_parties(db_party)

    async def get_all_parties(self,
                              name_party: Optional[str] = None,
                              name_organizer: Optional[str] = None,
                              name_town: Optional[str] = None,
                              name_country: Optional[str] = None,
                              date_start: Optional[str] = None) -> Sequence[Party]:
        return await self.repository.get_all_parties(name_party, name_organizer, name_town, name_country, date_start)

    async def get_party_by_id(self, party_id: int) -> Optional[Party]:
        return await self.repository.get_party_by_id(party_id)

    async def update_party(self, party_id: int, update_request: dict) -> Party:
        return await self.repository.update_party(party_id, update_request)

    async def delete_party(self, party_id: int) -> None:
        await self.repository.delete_party(party_id)

    def map_create_party(self, party_request: PartyCreate, user: User) -> Party:
        return Party(
            name_party=party_request.name_party,
            url_image_full=party_request.url_image_full,
            name_organizer=user.username,
            date_start=party_request.date_start,
            date_end=party_request.date_end,
            name_town=party_request.name_town,
            name_country=party_request.name_country,
            name_type=party_request.name_type,
            text_entry_fee=party_request.text_entry_fee,
            text_more=party_request.text_more,
            url_organizer=party_request.url_organizer,
            url_party=party_request.url_party,
            user_id=user.id
        )
