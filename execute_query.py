from sqlmodel import select, Session
from beerlog.models import Beer
from beerlog.database import engine
import warnings

warnings.filterwarnings("ignore", ".*Class SelectOfScalar will not make use of SQL compilation *")

with Session(engine) as session:
    # beer = Beer(name="Bewdog", style="NEIPA", flavor=6, image=8, cost=8)
    # beer = Beer(name="Two Chefs", style="QPA", flavor=5, image=6, cost=6)
    # session.add(beer)
    # session.commit()

    sql = select(Beer)
    results = session.exec(sql)
    for beer in results:
        print(beer.name)

