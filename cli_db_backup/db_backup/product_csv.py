import csv
from dataclasses import field
from db_backup.config import Session
from db_backup.models import Review, Product

from sqlalchemy.sql import func
import csv

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

csv_file = open(".ignoreme/ratings.csv", "w")
fields = ["name", "level", "published", "created_on", "review_count", "avg_rating"]
csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
csv_writer.writeheader()

for product, review_count, avg_rating in (
    session.query(
        Product, review_statement.c.review_count, review_statement.c.avg_rating
    )
    .outerjoin(review_statement, Product.id == review_statement.c.product_id)
    .limit(6)
):
    csv_writer.writerow(
        {
            "name": product.name,
            "level": product.level,
            "published": product.published,
            "created_on": product.created_on,
            "review_count": review_count,
            "avg_rating": round(float(avg_rating), 4) if avg_rating else 0,
        }
    )
