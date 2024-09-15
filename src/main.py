# examples/things_asgi.py

import falcon
import falcon.asgi

from src.media import SERIALIZERS


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource:
    async def on_get(self, req: falcon.Request, resp: falcon.Response):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_JSON  # Default is JSON, so override
        resp.text = (
            "\nTwo things awe me most, the starry sky "
            "above me and the moral law within me.\n"
            "\n"
            "    ~ Immanuel Kant\n\n"
        )


# falcon.asgi.App instances are callable ASGI apps...
# in larger applications the app is created in a separate file
app = falcon.asgi.App()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route("/things", things)


app.req_options.media_handlers.update(SERIALIZERS)
app.resp_options.media_handlers.update(SERIALIZERS)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app)
