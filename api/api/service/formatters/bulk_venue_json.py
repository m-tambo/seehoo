def bulk_venue_json_formatter(record):
    return {
        "name": record["displayName"]["text"],
        "address": record["formattedAddress"],
        "latitude": record["location"]["latitude"],
        "longitude": record["location"]["longitude"],
        "type": record.get("primaryType", None),
        "website": record.get("websiteUri", None)
    }
