import csv
from dataclasses import field
from db_backup.config import Session
from db_backup.models import Review, Product

from sqlalchemy.sql import func

session = Session()

review_statement = (
    session.query(
        Review.product_id,
        func.count("*").label("review_count"),
        func.avg(Review.rating).label("avg_rating"),
    )
    .group_by(Review.product_id)
    .subquery()
)

products = []

for product, review_count, avg_rating in (
    session.query(
        Product, review_statement.c.review_count, review_statement.c.avg_rating
    )
    .outerjoin(review_statement, Product.id == review_statement.c.product_id)
    .limit(6)
):
    products.append(
        {
            "name": product.name,
            "level": product.level,
            "published": product.published,
            "created_on": str(product.created_on.date()),
            "review_count": review_count,
            "avg_rating": round(float(avg_rating), 4) if avg_rating else 0,
        }
    )

import json

with open(".ignoreme/ratings.json", "w") as json_file:
    json.dump(products, json_file)
