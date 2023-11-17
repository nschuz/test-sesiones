from datetime import date, datetime

from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class CardModel(Base):
    __tablename__ = "cards"

    created = Column(DateTime(True), nullable=False, default=datetime.utcnow())
    modified = Column(DateTime(True), nullable=False, default=datetime.utcnow())
    is_removed = Column(Boolean, nullable=False, default=False)
    id = Column(UUID, primary_key=True)
    provider_card_id = Column(String(144))
    number = Column(String(4))
    status = Column(String(50), nullable=False)
    alias = Column(String(244), nullable=False)
    request_date = Column(Date, nullable=False, default=date.today())
    base_limit = Column(Float(53), nullable=False)
    last_tribal_update = Column(DateTime(True))
    metadata_ = Column("metadata", JSONB(astext_type=Text()))

    requested_by_id = Column(
        UUID,
        #ForeignKey(CompanyMemberModel.id, deferrable=True, initially="DEFERRED"),
        index=True,
    )
    contract_id = Column(
        UUID,
        #ForeignKey(ContractModel.id, deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    affinity_id = Column(String(100))
    provider_type = Column(String(50), default="pomelo")

    def as_dict(self) -> dict:
        """This method convert sqlalchemy obejecr to dict.

        Returns:
            dict: dict with all values from sqlalchemy object
        """
        return {
            column.name: str(getattr(self, column.name))
            for column in self.__table__.columns
            if column.name not in ["metadata", "last_tribal_update"]
        }
