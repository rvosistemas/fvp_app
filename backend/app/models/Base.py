from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_by = Column(String, nullable=True, default="admin")
    updated_by = Column(String, nullable=True, default="admin")
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    is_active = Column(Boolean, default=True)

    def deactivate(self):
        """
        Deactivates the current instance by setting `is_active` to False
        and updates the `updated_at` timestamp to the current time.
        """
        self.is_active = False
        self.updated_at = func.now()
