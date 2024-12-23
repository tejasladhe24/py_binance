from pydantic import BaseModel, Field
from typing import Union, Optional, Type


class APIResponse(BaseModel):
    data: Optional[Union[dict, list]] = Field(
        default=None, description="Response data; always in json format."
    )
    error: str = Field(default="", description="Error message if any.")
    status_code: int = Field(default=200, description="Response status_code.")
