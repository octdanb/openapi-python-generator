import os
from pathlib import Path

from jinja2 import Environment
from jinja2 import FileSystemLoader, ChoiceLoader


ENUM_TEMPLATE = "enum.jinja2"
MODELS_TEMPLATE = "models.jinja2"
SERVICE_TEMPLATE = "service.jinja2"
HTTPX_TEMPLATE = "httpx.jinja2"
API_CONFIG_TEMPLATE = "apiconfig.jinja2"
TEMPLATE_PATH = Path(__file__).parent / "templates"

JINJA_ENV = Environment(
    loader=(
        ChoiceLoader(
            [
                FileSystemLoader(os.environ["CUSTOM_TEMPLATE_PATH"]),
                FileSystemLoader(TEMPLATE_PATH),
            ]
        )
        if os.environ.get("CUSTOM_TEMPLATE_PATH")
        else FileSystemLoader(TEMPLATE_PATH)
    ),
    autoescape=True,
    trim_blocks=True,
)
