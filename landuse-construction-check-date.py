import overpy
from datetime import datetime


def get_building_construction():
    """Run an overpass turbo query"""
    api = overpy.Overpass()
    query = f"""
            area["name"="Ireland"]->.boundaryarea;
            (
            way(area.boundaryarea)[landuse=construction];
            );

            out center;
    """
    result = api.query(query)
    return result


def main():
    """Build a JSON file with points for a leaflet map"""
    buildings = get_building_construction()
    print("[")
    entries = []
    for way in buildings.ways:
        name = way.tags.get('name', '')
        fixme = way.tags.get('fixme', '')
        check_date_tag = way.tags.get('check_date', None)
        if check_date_tag and len(check_date_tag) == 10:
          check_date = datetime.strptime(check_date_tag, '%Y-%m-%d')
          today = datetime.now().date()
          if check_date.date() < today:
            entry = f' {{ "check_date": "{check_date_tag}", "latitude": {way.center_lat}, "longitude": {way.center_lon}, "name": "<a href=\'https://www.openstreetmap.org/way/{way.id}\'>{way.id}</a> {name} {fixme}" }}'
            entries.append(entry)
    output_str = ",\n".join(entries)
    print(output_str)
    print("]")


if __name__ == "__main__":
    main()
