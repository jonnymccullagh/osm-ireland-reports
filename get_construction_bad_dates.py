import overpy
from datetime import datetime


def get_building_construction():
    """Run an overpass turbo query for recycling facilities in a location"""
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
    """Import the CSV file and check if each node already exists on OSM"""
    buildings = get_building_construction()
    print("[")
    entries = []
    for way in buildings.ways:
        name = way.tags.get('name', '')
        fixme = way.tags.get('fixme', '')
        check_date_tag = way.tags.get('check_date', None)
        # Validation of user date input
        if check_date_tag:
            entry = f' {{ "check_date": {check_date_tag} ,"latitude": {way.center_lat}, "longitude": {way.center_lon}, "name": "<a href=\'https://www.openstreetmap.org/way/{way.id}\'>{way.id}</a> {name} {fixme}" }}'
            entries.append(entry)
            output_str = ",\n".join(entries)
    print(output_str)
    print("]")


if __name__ == "__main__":
    main()
