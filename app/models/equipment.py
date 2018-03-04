from datetime import datetime
from app.db import db

#Base = declarative_base()  # 创建对象的基类


class Equipment(db.Model):
    """设备信息"""
    __tablename__ = 'equipment'

    # 表的结构
    ID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    EQP_ID = db.Column(db.String(45), nullable=False)
    Location = db.Column(db.String(45))
    Longitude = db.Column(db.Numeric(10, 6))
    Latitude = db.Column(db.Numeric(10, 6))
    Type = db.Column(db.String(45))
    IP = db.Column(db.String(45))
    Status = db.Column(db.Integer, nullable=False, default=1)
    CreateTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    ModifyTime = db.Column(db.DateTime)
