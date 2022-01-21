import datetime

from core.database import metadata
import sqlalchemy

user = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("username", sqlalchemy.String, nullable=False, index=True),
    sqlalchemy.Column("email", sqlalchemy.String, nullable=False, index=True),
    sqlalchemy.Column("password", sqlalchemy.String, nullable=False, index=True),
    sqlalchemy.Column("is_verified", sqlalchemy.Boolean, default=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, nullable=True, default=datetime.datetime.utcnow()),
)

business = sqlalchemy.Table(
    "business",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("business_name", sqlalchemy.String, nullable=False, index=True),
    sqlalchemy.Column("city", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("region", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("business_description", sqlalchemy.Text, nullable=True),
    sqlalchemy.Column("logo", sqlalchemy.String, nullable=True, default="default_logo.jpg"),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, nullable=True, default=datetime.datetime.utcnow()),

    sqlalchemy.Column("owner", sqlalchemy.Integer, nullable=True),
)

product = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("category", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("original_price", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("new_price", sqlalchemy.Float, nullable=True),
    sqlalchemy.Column("percentage", sqlalchemy.Integer, nullable=True),
    sqlalchemy.Column("offer_expire_date", sqlalchemy.DateTime, nullable=True, default=datetime.datetime.utcnow()),
    sqlalchemy.Column("image", sqlalchemy.String, nullable=True, default="default_product.jpg"),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, nullable=True, default=datetime.datetime.utcnow()),

    sqlalchemy.Column("business", sqlalchemy.Integer, nullable=True),
)
