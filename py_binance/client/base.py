import requests
from ..models.response import APIResponse
from urllib.parse import urlencode
import json as _json
from typing import Literal, Optional, Any, Dict


class BaseClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers if headers else {}

    def request(
        self,
        method: Literal["GET", "POST", "PATCH", "PUT", "DELETE"],
        path: str,
        params: Optional[Dict] = None,
        json: Optional[Dict] = None,
        body: Optional[Any] = None,
        headers: Optional[Dict] = None,
    ):
        url = f"{self.base_url}{path}"
        request_headers = self.headers.copy()
        if headers:
            request_headers.update(headers)

        if params:
            url += "?" + urlencode(
                {
                    k: _json.dumps(v) if isinstance(v, (list, dict)) else v
                    for k, v in params.items()
                }
            )

        try:
            response = requests.request(
                method=method,
                url=url,
                json=json,
                data=body,
                headers=request_headers,
            )

            response.raise_for_status()
            return APIResponse(data=response.json(), status_code=response.status_code)

        except Exception as e:
            return APIResponse(error=str(e), status_code=response.status_code)
