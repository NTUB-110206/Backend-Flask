from app import db, ma

class News(db.Model):
    __tablename__ = 'bcd_news'
    news_id = db.Column(db.Integer, primary_key=True)
    news_title = db.Column(db.String(255))
    news_content = db.Column(db.String(255))
    news_website = db.Column(db.String(255))

class NewsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=News
        load_instance = True
