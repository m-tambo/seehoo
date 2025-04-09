import requests
from datetime import datetime
from .database import Database as DB
from .google import Google as Goo
from .formatters.bulk_venue_json import bulk_venue_json_formatter
from .openai import ai
from bs4 import BeautifulSoup

from ..schema.Venue import Venue
from .crawler import Crawler

class Gather:
    @classmethod
    def venues(cls, lat, lon, radius):
        res = Goo.search_places(lat, lon, radius).json()
        records = DB.bulk_upsert(
            Venue, 
            res['places'], 
            index=['name'], 
            formatter=bulk_venue_json_formatter
        )
        return records

    @classmethod
    def show(cls, venue, date=datetime.now()):
        datetime_str = date.strftime('%Y-%m-%d')
        links = Crawler.get(venue.website).find_all('a')
        links = [l.get('href') if l.get('href') else '' for l in links]
        next_url = ai.message(
            f"Given the following links, which is most likely to lead to a page with events? Only answer with the link, no explanation necessary, thank you: ```{links}```"
        ).output_text
        events_page = str(Crawler.get(next_url).find('body'))
        events = ai.message(f'Please give me a python list (just a value) of events happening according to this HTML document. List items should include the band, date, time and ticket link. Please clean this data of any HTML tags and line breaks - Only the data, no explanation necessary, thank you. If there are none, please give me an empty list: ```{events_page}```').output_text

        return events
