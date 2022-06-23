import sqlalchemy as sa
from rce.database.sqlalchemybase import SqlAlchemyBase


class CommentRaw(SqlAlchemyBase):
    __tablename__ = "comment_raw"

    subreddit_id = sa.Column(sa.String(10), primary_key=True)
    comment_id = sa.Column(sa.String(10), primary_key=True)
    data = sa.Column(sa.JSON)

    @staticmethod
    def from_pmaw(data):
        _data = dict(
            id=data["id"],
            subreddit_id=data["subreddit_id"],
            subreddit=data["subreddit"],
            author=data["author"],
            author_fullname=data.get("author_fullname"),
            parent_id=data["parent_id"],
            body=data["body"],
            link_id=data["link_id"],
            permalink=data["permalink"],
            retrieved_on=data.get("retrieved_on"),
            created_utc=data["created_utc"],
        )
        return dict(
            subreddit_id=data["subreddit_id"], comment_id=data["id"], data=_data
        )

    def __repr__(self):
        return f"CommentRaw(data={self.data['id']}"
