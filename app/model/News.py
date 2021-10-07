from marshmallow import fields
from app import db, ma


class Category(db.Model):
    __tablename__ = 'bcd_category'
    category_id = db.Column(db.Integer, primary_key=True)
    category_label = db.Column(db.String(255))

class Trend(db.Model):
    __tablename__ = 'bcd_trend'
    trend_id = db.Column(db.Integer, primary_key=True)
    trend_label = db.Column(db.String(255))

class News(db.Model):
    __tablename__ = 'bcd_news'
    news_id = db.Column(db.Integer, primary_key=True)
    news_datetime = db.Column(db.DateTime)
    news_title = db.Column(db.String(255))
    news_content = db.Column(db.String(255))
    news_website = db.Column(db.String(255))
    news_link = db.Column(db.String(255))
    img_link = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('bcd_category.category_id'))
    category = db.relationship("Category", backref="bcd_news")
    trend_id = db.Column(db.Integer, db.ForeignKey('bcd_trend.trend_id'))
    trend = db.relationship("Trend", backref="bcd_news")


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
    # bcd_news = ma.auto_field()


class TrendSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trend


class NewsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = News
        load_instance = True
        include_relationships = True
        include_fk = True
        exclude=["category_id", "trend_id"]
    category = fields.Nested(CategorySchema)
    trend = fields.Nested(TrendSchema)
