from datetime import datetime
from typing import List

from sqlalchemy import (
    BINARY,
    DECIMAL,
    NVARCHAR,
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vida_py.models import Model


class T100_EcuVariant(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T100_EcuVariant"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT101_Ecu: Mapped[int] = mapped_column(ForeignKey("T101_Ecu.id"))
    fkT101_Ecu_Gateway: Mapped[int] = mapped_column(ForeignKey("T101_Ecu.id"))
    identifier: Mapped[str] = mapped_column(String(200))
    status: Mapped[int] = mapped_column(Integer)
    inheritance: Mapped[str] = mapped_column(String(1))

    ecu: Mapped["T101_Ecu"] = relationship(
        back_populates="variants", foreign_keys=fkT101_Ecu
    )
    gateway: Mapped["T101_Ecu"] = relationship(foreign_keys=fkT101_Ecu_Gateway)


class T101_Ecu(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T101_Ecu"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT102_EcuType: Mapped[int] = mapped_column(ForeignKey("T102_EcuType.id"))
    identifier: Mapped[str] = mapped_column(String(200))
    name: Mapped[str] = mapped_column(String(200))

    variants: Mapped[list["T100_EcuVariant"]] = relationship(
        foreign_keys="T100_EcuVariant.fkT101_Ecu"
    )
    type: Mapped["T102_EcuType"] = relationship()


class T102_EcuType(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T102_EcuType"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    identifier: Mapped[int] = mapped_column(Integer)
    fkt190_Text: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    description: Mapped[str] = mapped_column(String(100))

    text: Mapped["T190_Text"] = relationship()


class T103_EcuVariant_Project(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T103_EcuVariant_Project"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT100_EcuVariant: Mapped[int] = mapped_column(ForeignKey("T100_EcuVariant.id"))
    fkT104_Project: Mapped[int] = mapped_column(ForeignKey("T104_Project.id"))

    variant: Mapped["T100_EcuVariant"] = relationship()
    project: Mapped["T104_Project"] = relationship()


class T104_Project(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T104_Project"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    modelYear: Mapped[int] = mapped_column(Integer)
    startOfProd: Mapped[str] = mapped_column(String(10))
    serie: Mapped[str] = mapped_column(String(50))
    isProdData: Mapped[bool] = mapped_column(Boolean)
    prodDataFrom: Mapped[datetime] = mapped_column()


class T110_Service_EcuVariant(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T110_Service_EcuVariant"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT111_Service: Mapped[int] = mapped_column(ForeignKey("T111_Service.id"))
    fkT100_EcuVariant: Mapped[int] = mapped_column(ForeignKey("T100_EcuVariant.id"))
    fkt130_Init_Timing_Service: Mapped[int] = mapped_column(ForeignKey("T130_Init.id"))

    service: Mapped["T111_Service"] = relationship()
    ecu_variant: Mapped["T100_EcuVariant"] = relationship()
    init_timing_service: Mapped["T130_Init"] = relationship()


class T111_Service(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T111_Service"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT122_Protocol: Mapped[int] = mapped_column(ForeignKey("T122_Protocol.id"))
    service: Mapped[str] = mapped_column(String(10))
    mode: Mapped[str] = mapped_column(String(10))
    serviceName: Mapped[str] = mapped_column(String(200))
    modeName: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(200))
    definition: Mapped[bytes] = mapped_column(BINARY(2147483647))
    type: Mapped[int] = mapped_column(Integer)
    status: Mapped[int] = mapped_column(Integer)
    fkt130_Init_Timing_Service_Default: Mapped[int] = mapped_column(
        ForeignKey("T130_Init.id")
    )

    protocol: Mapped["T122_Protocol"] = relationship()
    init_timing_service: Mapped["T130_Init"] = relationship()


class T120_Config_EcuVariant(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T120_Config_EcuVariant"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT121_Config: Mapped[int] = mapped_column(ForeignKey("T121_Config.id"))
    fkT100_EcuVariant: Mapped[int] = mapped_column(ForeignKey("T100_EcuVariant.id"))

    config: Mapped["T121_Config"] = relationship()
    ecu_variant: Mapped["T100_EcuVariant"] = relationship()


class T121_Config(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T121_Config"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT123_Bus: Mapped[int] = mapped_column(ForeignKey("T123_Bus.id"))
    fkT122_Protocol: Mapped[int] = mapped_column(ForeignKey("T122_Protocol.id"))
    fkT130_Init_Diag: Mapped[int] = mapped_column(ForeignKey("T130_Init.id"))
    fkT130_Init_Timing: Mapped[int] = mapped_column(ForeignKey("T130_Init.id"))
    physicalAddress: Mapped[str] = mapped_column(String(100))
    functionalAddress: Mapped[str] = mapped_column(String(100))
    canAddress: Mapped[str] = mapped_column(String(100))
    commAddress: Mapped[str] = mapped_column(String(100))
    priority: Mapped[int] = mapped_column(Integer)
    canIdTX: Mapped[str] = mapped_column(String(3))
    canIdRX: Mapped[str] = mapped_column(String(3))
    canIdFunc: Mapped[str] = mapped_column(String(7))
    canIdUUDT: Mapped[str] = mapped_column(String(508))
    busRate: Mapped[str] = mapped_column(String(10))
    addressSize: Mapped[str] = mapped_column(String(10))
    fkT121_Config_Gateway: Mapped[int] = mapped_column(ForeignKey("T121_Config.id"))

    bus: Mapped["T123_Bus"] = relationship()
    protocol: Mapped["T122_Protocol"] = relationship()
    init_diag: Mapped["T130_Init"] = relationship(foreign_keys=[fkT130_Init_Diag])
    init_timing: Mapped["T130_Init"] = relationship(foreign_keys=[fkT130_Init_Timing])
    config: Mapped["T121_Config"] = relationship()


class T122_Protocol(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T122_Protocol"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    identifier: Mapped[str] = mapped_column(String(200))
    version: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(200))


class T123_Bus(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T123_Bus"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT124_Net: Mapped[int] = mapped_column(ForeignKey("T124_Net.id"))
    fkT190_Text: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    identifier: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(200))
    version: Mapped[int] = mapped_column(Integer)

    net: Mapped["T124_Net"] = relationship()
    text: Mapped["T190_Text"] = relationship()


class T124_Net(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T124_Net"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    identifier: Mapped[str] = mapped_column(String(200))
    name: Mapped[str] = mapped_column(String(200))


class T130_Init(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T130_Init"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT133_InitCategory: Mapped[int] = mapped_column(ForeignKey("T133_InitCategory.id"))

    init_category: Mapped["T133_InitCategory"] = relationship()


class T131_InitValue(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T131_InitValue"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT130_Init: Mapped[int] = mapped_column(ForeignKey("T130_Init.id"))
    fkT132_InitValueType: Mapped[int] = mapped_column(ForeignKey("T132_InitValueType.id"))
    initValue: Mapped[str] = mapped_column(String(80))
    sortOrder: Mapped[int] = mapped_column(Integer)

    init: Mapped["T130_Init"] = relationship()
    init_value_type: Mapped["T132_InitValueType"] = relationship()


class T132_InitValueType(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T132_InitValueType"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200))


class T133_InitCategory(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T133_InitCategory"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200))


class T134_InitCategory_Type(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T134_InitCategory_Type"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT133_InitCategory: Mapped[int] = mapped_column(ForeignKey("T133_InitCategory.id"))
    fkT132_InitValueType: Mapped[int] = mapped_column(ForeignKey("T132_InitValueType.id"))

    init_category: Mapped["T133_InitCategory"] = relationship()
    init_value_type: Mapped["T132_InitValueType"] = relationship()


class T136_InitHw_Profile(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T136_InitHw_Profile"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT130_Init: Mapped[int] = mapped_column(ForeignKey("T130_Init.id"))
    fkT161_Profile: Mapped[int] = mapped_column(ForeignKey("T161_Profile.id"))

    init: Mapped["T130_Init"] = relationship()
    profile: Mapped["T161_Profile"] = relationship()


class T137_InitSwdl_Profile(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T137_InitSwdl_Profile"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT130_Init: Mapped[int] = mapped_column(ForeignKey("T130_Init.id"))
    fkT161_Profile: Mapped[int] = mapped_column(ForeignKey("T161_Profile.id"))
    ecuAddress: Mapped[str] = mapped_column(String(100))

    init: Mapped["T130_Init"] = relationship()
    profile: Mapped["T161_Profile"] = relationship()


class T141_Block(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T141_Block"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT142_BlockType: Mapped[int] = mapped_column(ForeignKey("T142_BlockType.id"))
    fkT143_BlockDataType: Mapped[int] = mapped_column(ForeignKey("T143_BlockDataType.id"))
    name: Mapped[str] = mapped_column(String(500))
    fkT190_Text: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    offset: Mapped[int] = mapped_column(Integer)
    length: Mapped[int] = mapped_column(Integer)
    exclude: Mapped[int] = mapped_column(Integer, default=0)
    composite: Mapped[bool] = mapped_column(Boolean)

    type: Mapped["T142_BlockType"] = relationship()
    datatype: Mapped["T143_BlockDataType"] = relationship()
    text: Mapped["T190_Text"] = relationship()


class T142_BlockType(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T142_BlockType"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT142_BlockType_Parent: Mapped[int] = mapped_column(ForeignKey("T142_BlockType.id"))
    identifier: Mapped[str] = mapped_column(String(200))
    metaTable: Mapped[str] = mapped_column(String(200))

    parent: Mapped["T142_BlockType"] = relationship()


class T143_BlockDataType(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T143_BlockDataType"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200))


class T144_BlockChild(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T144_BlockChild"

    fkT100_EcuVariant: Mapped[int] = mapped_column(
        ForeignKey("T100_EcuVariant.id"), primary_key=True
    )
    fkT141_Block_Child: Mapped[int] = mapped_column(
        ForeignKey("T141_Block.id"), primary_key=True
    )
    fkT141_Block_Parent: Mapped[int] = mapped_column(
        ForeignKey("T141_Block.id"), primary_key=True
    )
    SortOrder: Mapped[int] = mapped_column(Integer)

    ecu_variant: Mapped["T100_EcuVariant"] = relationship()
    child: Mapped["T141_Block"] = relationship(foreign_keys=[fkT141_Block_Child])
    parent: Mapped["T141_Block"] = relationship(foreign_keys=[fkT141_Block_Parent])


class T148_BlockMetaPARA(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T148_BlockMetaPARA"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT141_Block: Mapped[int] = mapped_column(ForeignKey("T141_Block.id"))
    fkT100_EcuVariant: Mapped[int] = mapped_column(ForeignKey("T100_EcuVariant.id"))
    asMinRange: Mapped[float] = mapped_column(DECIMAL, default=30)
    asMaxRange: Mapped[float] = mapped_column(DECIMAL, default=30)
    showAsFreezeFrame: Mapped[bool] = mapped_column(Boolean)

    block: Mapped["T141_Block"] = relationship()
    ecu_variant: Mapped["T100_EcuVariant"] = relationship()


class T150_BlockValue(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T150_BlockValue"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT141_Block: Mapped[int] = mapped_column(ForeignKey("T141_Block.id"))
    SortOrder: Mapped[int] = mapped_column(Integer)
    CompareValue: Mapped[str] = mapped_column(String(50))
    Operator: Mapped[int] = mapped_column(Integer)
    fkT190_Text_Value: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    fkT190_Text_Unit: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    fkT155_Scaling: Mapped[int] = mapped_column(ForeignKey("T155_Scaling.id"))
    altDisplayValue: Mapped[str] = mapped_column(String(10))
    fkT190_Text_ppeValue: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    fkT190_Text_ppeUnit: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    fkT155_ppeScaling: Mapped[int] = mapped_column(ForeignKey("T155_Scaling.id"))

    block: Mapped["T141_Block"] = relationship(foreign_keys=[fkT141_Block])
    text_value: Mapped["T190_Text"] = relationship(foreign_keys=[fkT190_Text_Value])
    text_unit: Mapped["T190_Text"] = relationship(foreign_keys=[fkT190_Text_Unit])
    scaling: Mapped["T155_Scaling"] = relationship(foreign_keys=[fkT155_Scaling])
    ppe_text_value: Mapped["T190_Text"] = relationship(
        foreign_keys=[fkT190_Text_ppeValue]
    )
    ppe_text_unit: Mapped["T190_Text"] = relationship(foreign_keys=[fkT190_Text_ppeUnit])
    ppe_scaling: Mapped["T155_Scaling"] = relationship(foreign_keys=[fkT155_ppeScaling])


class T151_BlockValue_Symptom(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T151_BlockValue_Symptom"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT150_BlockValue: Mapped[int] = mapped_column(ForeignKey("T150_BlockValue.Id"))
    fkT157_SymptomConnection: Mapped[int] = mapped_column(
        ForeignKey("T157_SymptomConnection.id")
    )
    SortOrder: Mapped[int] = mapped_column(Integer)

    value: Mapped["T150_BlockValue"] = relationship()
    connection: Mapped["T157_SymptomConnection"] = relationship()


class T152_Symptom(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T152_Symptom"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT153_SymptomCategory: Mapped[int] = mapped_column(
        ForeignKey("T153_SymptomCategory.id")
    )
    fkT190_Text: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    type: Mapped[str] = mapped_column(String(1))

    category: Mapped["T153_SymptomCategory"] = relationship()
    text: Mapped["T190_Text"] = relationship()


class T153_SymptomCategory(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T153_SymptomCategory"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT190_Text: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    fkT156_SymptomSection: Mapped[int] = mapped_column(
        ForeignKey("T156_SymptomSection.id")
    )
    fkT154_SymptomType: Mapped[int] = mapped_column(ForeignKey("T154_SymptomType.Id"))

    text: Mapped["T190_Text"] = relationship()
    section: Mapped["T156_SymptomSection"] = relationship()
    type: Mapped["T154_SymptomType"] = relationship()


class T154_SymptomType(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T154_SymptomType"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT190_Text: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))

    text: Mapped["T190_Text"] = relationship()


class T155_Scaling(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T155_Scaling"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    definition: Mapped[str] = mapped_column(String(254))
    type: Mapped[int] = mapped_column(Integer)


class T156_SymptomSection(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T156_SymptomSection"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT190_Text: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))

    text: Mapped["T190_Text"] = relationship()


class T157_SymptomConnection(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T157_SymptomConnection"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT152_Symptom: Mapped[int] = mapped_column(ForeignKey("T152_Symptom.id"))
    fkT100_EcuVariant: Mapped[int] = mapped_column(ForeignKey("T100_EcuVariant.id"))

    symptom: Mapped["T152_Symptom"] = relationship()
    ecu_variant: Mapped["T100_EcuVariant"] = relationship()


class T158_Symptom_CSC(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T158_Symptom_CSC"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    CSC: Mapped[str] = mapped_column(String(2))
    status: Mapped[str] = mapped_column(String(10))
    fkT190_Text_SymptomType: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    fkT194_FunctionGroup_1: Mapped[int] = mapped_column(
        ForeignKey("T194_FunctionGroup_1.id")
    )
    fkT196_FunctionGroup_2: Mapped[int] = mapped_column(
        ForeignKey("T196_FunctionGroup_2.id")
    )
    fkT190_Text_CompFunc: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    fkT190_Text_Deviation: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    fkT190_Text_Condition_1: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    fkT190_Text_Condition_2: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))
    validFromDate: Mapped[datetime] = mapped_column()

    symptom_type: Mapped["T190_Text"] = relationship(
        foreign_keys=[fkT190_Text_SymptomType]
    )
    function_group_1: Mapped["T194_FunctionGroup_1"] = relationship()
    function_group_2: Mapped["T196_FunctionGroup_2"] = relationship()
    text_comp_func: Mapped["T190_Text"] = relationship(
        foreign_keys=[fkT190_Text_CompFunc]
    )
    text_comp_deviation: Mapped["T190_Text"] = relationship(
        foreign_keys=[fkT190_Text_Deviation]
    )
    text_comp_cond_1: Mapped["T190_Text"] = relationship(
        foreign_keys=[fkT190_Text_Condition_1]
    )
    text_comp_cond_2: Mapped["T190_Text"] = relationship(
        foreign_keys=[fkT190_Text_Condition_2]
    )


class T159_SymptomCSC_SymptomDTC(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T159_SymptomCSC_SymptomDTC"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT158_Symptom_CSC: Mapped[int] = mapped_column(ForeignKey("T158_Symptom_CSC.id"))
    fkT152_Symptom: Mapped[int] = mapped_column(ForeignKey("T152_Symptom.id"))

    csc: Mapped["T158_Symptom_CSC"] = relationship()
    symptom: Mapped["T152_Symptom"] = relationship()


class T160_DefaultEcuVariant(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T160_DefaultEcuVariant"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT161_Profile: Mapped[int] = mapped_column(ForeignKey("T161_Profile.id"))
    fkT100_EcuVariant: Mapped[int] = mapped_column(ForeignKey("T100_EcuVariant.id"))

    profile: Mapped["T161_Profile"] = relationship()
    ecu_variant: Mapped["T100_EcuVariant"] = relationship()


class T161_Profile(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T161_Profile"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    identifier: Mapped[str] = mapped_column(String(100))
    folderLevel: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(500))
    title: Mapped[str] = mapped_column(String(500))
    fkT162_ProfileValue_Model: Mapped[int] = mapped_column(
        ForeignKey("T162_ProfileValue.id")
    )
    fkT162_ProfileValue_Year: Mapped[int] = mapped_column(
        ForeignKey("T162_ProfileValue.id")
    )
    fkT162_ProfileValue_Engine: Mapped[int] = mapped_column(
        ForeignKey("T162_ProfileValue.id")
    )
    fkT162_ProfileValue_Transmission: Mapped[int] = mapped_column(
        ForeignKey("T162_ProfileValue.id")
    )
    fkT162_ProfileValue_Body: Mapped[int] = mapped_column(
        ForeignKey("T162_ProfileValue.id")
    )
    fkT162_ProfileValue_Steering: Mapped[int] = mapped_column(
        ForeignKey("T162_ProfileValue.id")
    )
    fkT162_ProfileValue_Market: Mapped[int] = mapped_column(
        ForeignKey("T162_ProfileValue.id")
    )
    fkT162_ProfileValue_ControlUnit: Mapped[int] = mapped_column(
        ForeignKey("T162_ProfileValue.id")
    )
    fkT162_ProfileValue_ChassisFrom: Mapped[int] = mapped_column(
        ForeignKey("T162_ProfileValue.id")
    )
    fkT162_ProfileValue_ChassisTo: Mapped[int] = mapped_column(
        ForeignKey("T162_ProfileValue.id")
    )

    model: Mapped["T162_ProfileValue"] = relationship(
        foreign_keys=[fkT162_ProfileValue_Model]
    )
    year: Mapped["T162_ProfileValue"] = relationship(
        foreign_keys=[fkT162_ProfileValue_Year]
    )
    engine: Mapped["T162_ProfileValue"] = relationship(
        foreign_keys=[fkT162_ProfileValue_Engine]
    )
    transmission: Mapped["T162_ProfileValue"] = relationship(
        foreign_keys=[fkT162_ProfileValue_Transmission]
    )
    body: Mapped["T162_ProfileValue"] = relationship(
        foreign_keys=[fkT162_ProfileValue_Body]
    )
    steering: Mapped["T162_ProfileValue"] = relationship(
        foreign_keys=[fkT162_ProfileValue_Steering]
    )
    market: Mapped["T162_ProfileValue"] = relationship(
        foreign_keys=[fkT162_ProfileValue_Market]
    )
    control_unit: Mapped["T162_ProfileValue"] = relationship(
        foreign_keys=[fkT162_ProfileValue_ControlUnit]
    )
    chassis_from: Mapped["T162_ProfileValue"] = relationship(
        foreign_keys=[fkT162_ProfileValue_ChassisFrom]
    )
    chassis_to: Mapped["T162_ProfileValue"] = relationship(
        foreign_keys=[fkT162_ProfileValue_ChassisTo]
    )


class T162_ProfileValue(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T162_ProfileValue"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    identifier: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(200))
    fkT163_ProfileValueType: Mapped[int] = mapped_column(
        ForeignKey("T163_ProfileValueType.id")
    )

    type: Mapped["T163_ProfileValueType"] = relationship()


class T163_ProfileValueType(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T163_ProfileValueType"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    identifier: Mapped[str] = mapped_column(String(100))


class T170_SecurityCode_EcuVariant(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T170_SecurityCode_EcuVariant"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT171_SecurityCode: Mapped[int] = mapped_column(ForeignKey("T171_SecurityCode.id"))
    fkT100_EcuVariant: Mapped[int] = mapped_column(ForeignKey("T100_EcuVariant.id"))

    security_code: Mapped["T171_SecurityCode"] = relationship()
    ecu_variant: Mapped["T100_EcuVariant"] = relationship()


class T171_SecurityCode(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T171_SecurityCode"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT172_SecurityCodeType: Mapped[int] = mapped_column(
        ForeignKey("T172_SecurityCodeType.id")
    )
    code: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(250))

    type: Mapped["T172_SecurityCodeType"] = relationship()


class T172_SecurityCodeType(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T172_SecurityCodeType"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    identifier: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(250))


class T190_Text(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T190_Text"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT192_TextCategory: Mapped[int] = mapped_column(ForeignKey("T192_TextCategory.id"))
    status: Mapped[int] = mapped_column(Integer)

    data: Mapped[List["T191_TextData"]] = relationship()
    category: Mapped["T192_TextCategory"] = relationship()


class T191_TextData(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T191_TextData"

    fkT193_Language: Mapped[int] = mapped_column(
        ForeignKey("T193_Language.id"), primary_key=True
    )
    fkT190_Text: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"), primary_key=True)
    status: Mapped[int] = mapped_column(Integer)
    data: Mapped[str] = mapped_column(NVARCHAR(500))

    language: Mapped["T193_Language"] = relationship()
    text: Mapped["T190_Text"] = relationship(back_populates="data")


class T192_TextCategory(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T192_TextCategory"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    identifier: Mapped[str] = mapped_column(String(5))
    description: Mapped[str] = mapped_column(String(200))


class T193_Language(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T193_Language"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    identifier: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(80))


class T194_FunctionGroup_1(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T194_FunctionGroup_1"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT190_Text: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))

    text: Mapped["T190_Text"] = relationship()


class T196_FunctionGroup_2(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T196_FunctionGroup_2"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkT194_FunctionGroup_1: Mapped[int] = mapped_column(
        ForeignKey("T194_FunctionGroup_1.id")
    )
    fkT190_Text: Mapped[int] = mapped_column(ForeignKey("T190_Text.id"))

    function_group_1: Mapped["T194_FunctionGroup_1"] = relationship()
    text: Mapped["T190_Text"] = relationship()


class T199_ControlTable(Model):
    __bind_key__ = "carcom"
    __tablename__ = "T199_ControlTable"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    controlId: Mapped[str] = mapped_column(String(20))
    controlValue: Mapped[str] = mapped_column(String(200))
    controlDescription: Mapped[str] = mapped_column(String(200))
    modified: Mapped[datetime] = mapped_column(DateTime())
    modifiedBy: Mapped[str] = mapped_column(String(12))
