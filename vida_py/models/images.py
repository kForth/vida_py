from sqlalchemy import BINARY, Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from vida_py.models import Model


class GraphicCarConfigs(Model):
    __bind_key__ = "images"
    __tablename__ = "GraphicCarConfigs"

    fkCarConfig: Mapped[str] = mapped_column(String(16))
    width: Mapped[int] = mapped_column(Integer, default=0)
    height: Mapped[int] = mapped_column(Integer, default=0)


class GraphicFormats(Model):
    __bind_key__ = "images"
    __tablename__ = "GraphicFormats"

    description: Mapped[str] = mapped_column(String(50))


class Graphics(Model):
    __bind_key__ = "images"
    __tablename__ = "Graphics"

    fkGraphicFormat: Mapped[int] = mapped_column(Integer)
    width: Mapped[int] = mapped_column(Integer)
    height: Mapped[int] = mapped_column(Integer)
    isNavigable: Mapped[bool] = mapped_column(Boolean)
    isLanguageDependent: Mapped[bool] = mapped_column(Boolean)
    isVehicleModel: Mapped[bool] = mapped_column(Boolean)
    isParts: Mapped[bool] = mapped_column(Boolean)


class LocalizedGraphics(Model):
    __bind_key__ = "images"
    __tablename__ = "LocalizedGraphics"

    languageId: Mapped[int] = mapped_column(Integer)
    title: Mapped[str] = mapped_column(String(2000))
    path: Mapped[str] = mapped_column(String(255))
    width: Mapped[int] = mapped_column(Integer)
    height: Mapped[int] = mapped_column(Integer)
    imageData: Mapped[bytes] = mapped_column(BINARY(2147483647))
    isUpdated: Mapped[bool] = mapped_column(Boolean)
