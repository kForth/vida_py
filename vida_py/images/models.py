"""SQLAlchemy ORM models for the images VIDA database."""

# ruff: noqa: N815

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import BINARY, Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class _Model(DeclarativeBase):
    __bind_key__ = "images"


class GraphicCarConfigs(_Model):
    __tablename__ = "GraphicCarConfigs"

    fkGraphic: Mapped[str] = mapped_column(String(16), primary_key=True)
    fkCarConfig: Mapped[str] = mapped_column(String(16), primary_key=True)
    width: Mapped[int] = mapped_column(Integer, default=0, primary_key=True)
    height: Mapped[int] = mapped_column(Integer, default=0, primary_key=True)


class GraphicFormats(_Model):
    __tablename__ = "GraphicFormats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String(50))


class Graphics(_Model):
    __tablename__ = "Graphics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkGraphicFormat: Mapped[int] = mapped_column(Integer)
    width: Mapped[int] = mapped_column(Integer, primary_key=True)
    height: Mapped[int] = mapped_column(Integer, primary_key=True)
    isNavigable: Mapped[bool] = mapped_column(Boolean)
    isLanguageDependent: Mapped[bool] = mapped_column(Boolean)
    isVehicleModel: Mapped[bool] = mapped_column(Boolean)
    isParts: Mapped[bool] = mapped_column(Boolean)


class LocalizedGraphics(_Model):
    __tablename__ = "LocalizedGraphics"

    fkGraphic: Mapped[str] = mapped_column(String(16), primary_key=True)
    languageId: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(2000))
    path: Mapped[str] = mapped_column(String(255))
    width: Mapped[int] = mapped_column(Integer, primary_key=True)
    height: Mapped[int] = mapped_column(Integer, primary_key=True)
    imageData: Mapped[bytes] = mapped_column(BINARY(2147483647))
    isUpdated: Mapped[bool] = mapped_column(Boolean)
