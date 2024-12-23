from .base import BaseClient
from typing import Optional
from ..models import SymbolStatus, Interval
from typing import Any, Literal, Union
from ..utils import get_timezone_offset_relative_to_utc


class UtilsClient(BaseClient):
    def __init__(self, base_url: str):
        super().__init__(base_url=base_url)

    def __repr__(self):
        return f"UtilsClient(base_url={self.base_url})"

    def __str__(self):
        return f"UtilsClient(base_url={self.base_url})"

    def ping(self) -> Any:
        res = self.request(method="GET", path="/api/v3/ping")
        if res.error:
            raise RuntimeError(res.error)

        return res.data

    def get_server_time(self) -> int:
        res = self.request(method="GET", path="/api/v3/time")
        if res.error:
            raise RuntimeError(res.error)

        return res.data["serverTime"]


class MarketClient(BaseClient):
    def __init__(
        self,
        base_url: str = "https://api.binance.com/",
    ):
        super().__init__(base_url=base_url)

    def __repr__(self):
        return f"MarketClient(base_url={self.base_url})"

    def __str__(self):
        return f"MarketClient(base_url={self.base_url})"

    def get_exchange_info(
        self,
        symbols: Optional[list[str]] = None,
        permissions: Optional[list[str]] = None,
        showPermissionSets: Optional[bool] = True,
        symbolStatus: Optional[SymbolStatus] = None,
    ) -> dict:
        params = {
            "symbols": symbols,
            "showPermissionSets": "true" if showPermissionSets else "false",
        }

        if permissions:
            params["permissions"] = permissions

        if symbolStatus:
            params["symbolStatus"] = symbolStatus.value

        res = self.request(
            method="GET",
            path="/api/v3/exchangeInfo",
            params=params,
        )

        if res.error:
            raise RuntimeError(res.error)

        return res.data

    def get_order_book(
        self,
        symbol: str,
        limit: int = 100,
    ) -> dict:
        res = self.request(
            method="GET",
            path="/api/v3/depth",
            params={
                "symbol": symbol,
                "limit": limit,
            },
        )
        if res.error:
            raise RuntimeError(res.error)

        return res.data

    def get_recent_trades(
        self,
        symbol: str,
        limit: int = 100,
    ) -> dict:
        res = self.request(
            method="GET",
            path="/api/v3/trades",
            params={
                "symbol": symbol,
                "limit": limit,
            },
        )
        if res.error:
            raise RuntimeError(res.error)

        return res.data

    def get_historical_trades(
        self,
        symbol: str,
        fromId: int,
        limit: int = 100,
    ) -> dict:
        res = self.request(
            method="GET",
            path="/api/v3/historicalTrades",
            params={
                "symbol": symbol,
                "fromId": fromId,
                "limit": limit,
            },
        )
        if res.error:
            raise RuntimeError(res.error)

        return res.data

    def get_aggregate_trades(
        self,
        symbol: str,
        fromId: int,
        startTime: int,
        endTime: int,
        limit: int = 100,
    ) -> dict:
        res = self.request(
            method="GET",
            path="/api/v3/aggTrades",
            params={
                "symbol": symbol,
                "fromId": fromId,
                "startTime": startTime,
                "endTime": endTime,
                "limit": limit,
            },
        )
        if res.error:
            raise RuntimeError(res.error)

        return res.data

    def get_klines(
        self,
        symbol: str,
        interval: Interval = Interval._1_DAY,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
        timeZone: str = get_timezone_offset_relative_to_utc(),
        limit: int = 100,
    ) -> dict:
        res = self.request(
            method="GET",
            path="/api/v3/klines",
            params={
                "symbol": symbol,
                "interval": interval.value,
                "startTime": startTime,
                "endTime": endTime,
                "timeZone": timeZone,
                "limit": limit,
            },
        )
        if res.error:
            raise RuntimeError(res.error)

        return res.data

    def get_uiKlines(
        self,
        symbol: str,
        interval: Interval = Interval._1_DAY,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
        timeZone: str = get_timezone_offset_relative_to_utc(),
        limit: int = 100,
    ) -> dict:
        res = self.request(
            method="GET",
            path="/api/v3/klines",
            params={
                "symbol": symbol,
                "interval": interval.value,
                "startTime": startTime,
                "endTime": endTime,
                "timeZone": timeZone,
                "limit": limit,
            },
        )
        if res.error:
            raise RuntimeError(res.error)

        return res.data

    def get_average_price(self, symbol: str):
        res = self.request(
            method="GET",
            path="/api/v3/avgPrice",
            params={
                "symbol": symbol,
            },
        )
        if res.error:
            raise RuntimeError(res.error)

        return res.data


__resources = {
    "market": MarketClient,
    "utils": UtilsClient,
}


def create_client(
    resource: Literal["market", "utils"], *args, **kwargs
) -> Union[MarketClient, UtilsClient]:
    if resource not in __resources:
        raise ValueError(f"Invalid resource: {resource}")
    try:
        return __resources[resource](*args, **kwargs)
    except Exception as e:
        raise RuntimeError(e)


__all__ = [create_client]
