from sqlalchemy import Result, text
from sqlalchemy.orm import Session


def run_script(session: Session, script: str, **kwargs) -> Result:
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


def run_func(session: Session, script: str, *args) -> Result:
    kwargs = {str(i): e for i, e in enumerate(args)}
    return session.execute(
        text(
            "\n".join(
                [
                    f"SELECT * FROM [dbo].[{script}] (",
                    "\n,".join(f":{k}" for k in kwargs),
                    ")",
                ]
            )
        ),
        kwargs,
    )
