from sqlalchemy import Result, text
from sqlalchemy.orm import Session


def runScript(session: Session, script: str, **kwargs) -> Result:
    return session.execute(
        text(
            "\n".join(
                [
                    "DECLARE @RC int",
                    f"EXECUTE @RC = [dbo].[{script}]",
                    "\n,".join(f"@{k} = :{k}" for k in kwargs),
                    "SELECT @RC",
                ]
            )
        ),
        kwargs,
    )
