import os
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv
from sqlalchemy.orm import Session

load_dotenv()


def test_load_env_variable():
    with patch.dict(
        os.environ,
        {
            "POSTGRES_DATABASE_URL": "postgresql://test_user:test_password@localhost/test_db"
        },
    ):
        from ...config.database import DATABASE_URL

        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        db = os.getenv("POSTGRES_DB")
        port = os.getenv("POSTGRES_PORT")
        assert (
            DATABASE_URL
            == f"postgresql+psycopg2://{user}:{password}@postgres_db:{port}/{db}"
        )


def test_get_db():
    mock_session = MagicMock(spec=Session)

    with patch("app.app.config.database.SessionLocal", return_value=mock_session):

        from ...config.database import get_db

        gen = get_db()
        session = next(gen)

        assert session == mock_session

        with patch.object(mock_session, "close") as mock_close:
            try:
                next(gen)
            except StopIteration:
                pass
            mock_close.assert_called_once()
