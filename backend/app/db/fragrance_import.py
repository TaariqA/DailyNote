'''
import argparse
import json
from pathlib import Path

from backend.app.db.base import Base
from backend.app.db.session import sessionLocal, engine
from backend.app.models.fragrance import Fragrance

def import_fragrances(limit: int | None = None) -> int:
    input_file = Path(__file__).with_name("perfumes.jsonl")
    imported = 0

    with input_file.open(encoding="utf-8") as file, sessionLocal.begin() as db:
        for line in file:
            if limit is not None and imported >= limit:
                break

            pulled_frag = json.loads(line)
            seasons = pulled_frag["seasons"]
            preferred_season = max(seasons, key=seasons.get)

            db.add(
                Fragrance(
                    id=pulled_frag["id"],
                    slug=pulled_frag["slug"],
                    name=pulled_frag["name"],
                    brand=pulled_frag["brand"],
                    gender=pulled_frag["gender"],
                    description=pulled_frag["description"],
                    picture=pulled_frag["picture"],
                    top_notes=pulled_frag["notes"]["tiered"]["top"],
                    middle_notes=pulled_frag["notes"]["tiered"]["middle"],
                    base_notes=pulled_frag["notes"]["tiered"]["base"],
                    notes_flat=pulled_frag["notes"]["flat"],
                    longevity=pulled_frag["longevity"]["average"],
                    sillage=pulled_frag["sillage"]["average"],
                    season=preferred_season,
                )
            )
            imported += 1

    return imported


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, help="Import only this many records")
    args = parser.parse_args()

    Base.metadata.create_all(bind=engine, tables=[Fragrance.__table__])

    print(f"Imported {import_fragrances(args.limit)} fragrances")


if __name__ == "__main__":
    main()
'''