from pyodbc import Cursor, Row


def get_profiles_fuzzy(
    cursor: Cursor,
    year: int,
    market: int,
    steering: int,
    transmission: int,
    engine: int,
    model: int,
):
    return [
        {
            "id": e.id,
            "identifier": e.identifier,
            "folderLevel": e.folderLevel,
            "description": e.description,
            "title": e.title,
            "model": e.fkT162_ProfileValue_Model,
            "year": e.fkT162_ProfileValue_Year,
            "engine": e.fkT162_ProfileValue_Engine,
            "transmission": e.fkT162_ProfileValue_Transmission,
            "body": e.fkT162_ProfileValue_Body,
            "steering": e.fkT162_ProfileValue_Steering,
            "market": e.fkT162_ProfileValue_Market,
            "control_init": e.fkT162_ProfileValue_ControlUnit,
            "chassis_from": e.fkT162_ProfileValue_ChassisFrom,
            "chassis_to": e.fkT162_ProfileValue_ChassisTo,
        }
        for e in cursor.execute(
            f"""
            SELECT [id]
                ,[identifier]
                ,[folderLevel]
                ,[description]
                ,[title]
                ,[fkT162_ProfileValue_Model]
                ,[fkT162_ProfileValue_Year]
                ,[fkT162_ProfileValue_Engine]
                ,[fkT162_ProfileValue_Transmission]
                ,[fkT162_ProfileValue_Body]
                ,[fkT162_ProfileValue_Steering]
                ,[fkT162_ProfileValue_Market]
                ,[fkT162_ProfileValue_ControlUnit]
                ,[fkT162_ProfileValue_ChassisFrom]
                ,[fkT162_ProfileValue_ChassisTo]
            FROM [carcom].[dbo].[T161_Profile]
            WHERE (fkT162_ProfileValue_Year = {year} OR fkT162_ProfileValue_Year IS NULL)
            AND (fkT162_ProfileValue_Market = {market} OR fkT162_ProfileValue_Market IS NULL)
            AND (fkT162_ProfileValue_Steering = {steering} OR fkT162_ProfileValue_Steering IS NULL)
            AND (fkT162_ProfileValue_Transmission = {transmission} OR fkT162_ProfileValue_Transmission IS NULL)
            AND (fkT162_ProfileValue_Engine = {engine} OR fkT162_ProfileValue_Engine IS NULL)
            AND (fkT162_ProfileValue_Model = {model} OR fkT162_ProfileValue_Model IS NULL)
            ORDER BY id ASC
            """
        ).fetchall()
    ]


def get_profile_ecus(cursor: Cursor, profile: int) -> list[int]:
    cursor.execute(
        f"""
        SELECT [fkT100_EcuVariant]
        FROM [carcom].[dbo].[T160_DefaultEcuVariant]
        WHERE fkT161_Profile = {profile}
        """
    )
    return [r.fkT100_EcuVariant for r in cursor.fetchall()]


def get_scaling(cursor: Cursor, scaling: int) -> dict:
    r = cursor.execute(
        f"""
        SELECT [id]
        ,[definition]
        ,[type]
        FROM [carcom].[dbo].[T155_Scaling]
        WHERE [id] = {scaling}
        """
    ).fetchone()
    return {
        "id": r.id,
        "definition": r.definition,
        "type": r.type,
    }


def get_text(cursor: Cursor, id: int, language: int) -> dict:
    t = cursor.execute(
        f"""
        SELECT [fkT192_TextCategory], [status]
        FROM [carcom].[dbo].[T190_Text]
        WHERE [id] = {id}
        """
    ).fetchone()
    d = cursor.execute(
        f"""
        SELECT [status], [data]
        FROM [carcom].[dbo].[T191_TextData]
        WHERE [fkT190_Text] = {id}
        AND [fkT193_Language] = {language}
        """
    ).fetchone()
    c = cursor.execute(
        f"""
        SELECT [id], [identifier], [description]
        FROM [carcom].[dbo].[T192_TextCategory]
        WHERE [id] = {t.fkT192_TextCategory}
        """
    ).fetchone()
    return {
        "id": id,
        "status": d.status,
        "data": d.data,
        "category": {
            "id": c.id,
            "identifier": c.identifier,
            "description": c.description,
        },
    }


def get_block(cursor: Cursor, id: int, language: int) -> dict:
    b = cursor.execute(
        f"""
            SELECT [id]
            ,[fkT142_BlockType]
            ,[fkT143_BlockDataType]
            ,[name]
            ,[fkT190_Text]
            ,[offset]
            ,[length]
            ,[exclude]
            ,[composite]
        FROM [carcom].[dbo].[T141_Block]
        WHERE [id] = {id}
        """
    ).fetchone()
    if b is None:
        return None
    meta = get_block_meta(cursor, id)
    v = get_block_value(cursor, id)
    block = {
        "id": id,
    }
    if b is not None:
        block.update(
            {
                "fkT142_BlockType": b.fkT142_BlockType,
                "fkT143_BlockDataType": b.fkT143_BlockDataType,
                "name": b.name,
                "text": get_text(cursor, b.fkT190_Text, language),
                "offset": b.offset,
                "length": b.length,
                "exclude": b.exclude,
                "composite": b.composite,
            }
        )
    if meta is not None:
        block.update(
            {
                "ecu_variant": meta.fkT100_EcuVariant,
                "min_range": (
                    float(meta.asMinRange) if meta.asMinRange is not None else None
                ),
                "max_range": (
                    float(meta.asMaxRange) if meta.asMaxRange is not None else None
                ),
                "freeze_frame": meta.showAsFreezeFrame,
            }
        )
    if v is not None:
        block.update(
            {
                "sort_order": v.SortOrder,
                "compare_value": v.CompareValue,
                "operator": v.Operator,
                "text_value": get_text(cursor, v.fkT190_Text_Value, language),
                "text_unit": get_text(cursor, v.fkT190_Text_Unit, language),
                "scaling": get_scaling(cursor, v.fkT155_Scaling),
                "alt_displat_value": v.altDisplayValue,
                "text_ppe_value": get_text(cursor, v.fkT190_Text_ppeValue, language),
                "text_ppe_unit": get_text(cursor, v.fkT190_Text_ppeUnit, language),
                "ppe_scaling": get_scaling(cursor, v.fkT155_ppeScaling),
            }
        )
    return block


def get_block_metas(cursor: Cursor, ecu: int) -> list[Row]:
    return cursor.execute(
        f"""
        SELECT [fkT141_Block]
            ,[fkT100_EcuVariant]
            ,[asMinRange]
            ,[asMaxRange]
            ,[showAsFreezeFrame]
        FROM [carcom].[dbo].[T148_BlockMetaPARA]
        WHERE [fkT100_EcuVariant] = {ecu}
        """
    ).fetchall()


def get_block_meta(cursor: Cursor, block: int) -> Row:
    return cursor.execute(
        f"""
        SELECT [fkT141_Block]
            ,[fkT100_EcuVariant]
            ,[asMinRange]
            ,[asMaxRange]
            ,[showAsFreezeFrame]
        FROM [carcom].[dbo].[T148_BlockMetaPARA]
        WHERE [fkT141_Block] = {block}
        """
    ).fetchone()


def get_block_value(cursor: Cursor, block: int) -> Row:
    return cursor.execute(
        f"""
        SELECT [SortOrder]
            ,[CompareValue]
            ,[Operator]
            ,[fkT190_Text_Value]
            ,[fkT190_Text_Unit]
            ,[fkT155_Scaling]
            ,[altDisplayValue]
            ,[fkT190_Text_ppeValue]
            ,[fkT190_Text_ppeUnit]
            ,[fkT155_ppeScaling]
        FROM [carcom].[dbo].[T150_BlockValue]
        WHERE [fkT141_Block] = {block}
        """
    ).fetchone()


def get_blocks(cursor: Cursor, ecu: int, language: int) -> list[dict]:
    return [get_block(cursor, e, language) for e in get_block_metas(cursor, ecu)]


def get_block_children(cursor: Cursor, ecu: int) -> list[dict]:
    return [
        {
            "ecu_variant": e.fkT100_EcuVariant,
            "child_id": e.fkT141_Block_Child,
            "parent_id": e.fkT141_Block_Parent,
            "sort_order": e.SortOrder,
        }
        for e in cursor.execute(
            f"""
            SELECT [fkT100_EcuVariant]
                ,[fkT141_Block_Child]
                ,[fkT141_Block_Parent]
                ,[SortOrder]
            FROM [carcom].[dbo].[T144_BlockChild]
            WHERE [fkT100_EcuVariant] = {ecu}
            """
        )
    ]
