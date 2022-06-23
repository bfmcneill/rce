import logging
import sqlalchemy as sa
from sqlalchemy.orm import Session
from pmaw import PushshiftAPI
from rce.settings import config_json_path
from rce.secret.auth_secret import AuthSecret
from rce.secret.app_secret import AppSecret
from rce.secret.database_secret import DatabaseSecret
from rce.database.comment_raw import CommentRaw

logger = logging.getLogger(__name__)

# app_secret = AppSecret.from_json_config(config_json_path)
# auth_secret = AuthSecret.from_json_config(config_json_path)
db_secret = DatabaseSecret.from_json_config(config_json_path)

api = PushshiftAPI(num_workers=20)

engine = sa.create_engine(db_secret.uri, echo=False, future=True)


def comments(subreddit, after, before):
    print(f"search comments for `{subreddit}` after={after} before={before}")

    gen = api.search_comments(
        mem_safe=True,
        safe_exit=True,
        subreddit=subreddit,
        after=after,
        before=before,
    )

    print("begin generator enumeration")
    for idx, c in enumerate(gen):
        data = CommentRaw.from_pmaw(c)
        comment_raw = CommentRaw(**data)
        with Session(engine) as session:
            session.merge(comment_raw)
            session.commit()

        if idx % 5000 == 0:
            print(f"processed: {idx}")

    print(f"processed: {idx+1}")
