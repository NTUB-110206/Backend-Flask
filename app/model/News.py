from marshmallow import fields
from app import db, ma


class Category(db.Model):
    __tablename__ = 'bcd_category'
    category_id = db.Column(db.Integer, primary_key=True)
    category_label = db.Column(db.String(255))


class News(db.Model):
    __tablename__ = 'bcd_news'
    news_id = db.Column(db.Integer, primary_key=True)
    news_datetime = db.Column(db.DateTime)
    news_title = db.Column(db.String(255))
    news_content = db.Column(db.String(255))
    news_website = db.Column(db.String(255))
    news_link = db.Column(db.String(255))
    img_link = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('bcd_category.category_id'), nullable=False)
    category_label = db.relationship(Category, backref="bcd_category.category_label")
    # trend = db.Column(db.String(255))

class CategorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Category
        fields=("category_id", "category_label")
        load_instance = True

class NewsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = News
        include_fk = True
        load_instance = True