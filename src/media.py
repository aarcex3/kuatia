from falcon import media
from msgspec import json

JSONHANDLER = media.JSONHandler(
    dumps=json.encode,
    loads=json.decode,
)
SERIALIZERS = {
    "application/json": JSONHANDLER,
}
