from sqlalchemy import Result, text
from sqlalchemy.orm import Session


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
