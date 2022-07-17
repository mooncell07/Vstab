import typing as t

from attrs import define, field
from rfc3986 import builder

__all__ = ("ResolveHint", "Request")


class ResolveHint(t.TypedDict):
    url: str
    headers: dict[str, str]


@define
class Request:

    base: str = field(repr=True, init=False, default="https://api.twitter.com/2/")
    path: str
    headers: dict[str, t.Any]
    queries: dict[str, t.Any] = field(repr=True, init=True, default={})

    def append_queries(self, queries: dict[str, str]) -> None:
        self.queries = queries

    def resolve(self) -> ResolveHint:
        url = (
            builder.URIBuilder.from_uri(self.base)
            .extend_path(self.path)
            .add_query_from(self.queries)
            .finalize()
            .unsplit()
        )
        return {"url": url, "headers": self.headers}
