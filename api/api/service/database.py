from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert

from ..model.database import db

class Database:
    @classmethod
    def format_record(cls, record):
        return record
    
    @classmethod
    def bulk_upsert(cls, model, data, index=['id'], formatter=None):
        session = sessionmaker(bind=db.engine)()
        try:
            records = [formatter(item) if formatter else item for item in data]
            stmt = insert(model).values(records)
            stmt = stmt.on_conflict_do_update(
                index_elements=index,
                set_={c.key: c for c in stmt.excluded if c.key not in index}
            )
            session.execute(stmt)
            session.commit()
            return records
        except Exception as e:
            session.rollback()
            raise e
