import typing as t

import httpx
from attrs import define, field

from ..enums import Method
from .request import ResolveHint

__all__ = ("Rest",)


@define
class Rest:
    client: httpx.AsyncClient = field(
        init=True, repr=False, default=httpx.AsyncClient()
    )

    async def send(
        self, method: Method, delta: t.Callable[..., ResolveHint]
    ) -> httpx.Response:
        return await self.client.request(method=method.name, **delta.resolve())
