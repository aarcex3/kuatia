from typing import Annotated

from msgspec import Meta

RUC = Annotated[int, Meta(gt=1_000_000)]
PRICE = Annotated[float, Meta(ge=0.0)]
VAT = Annotated[float, Meta(ge=0.0)]
