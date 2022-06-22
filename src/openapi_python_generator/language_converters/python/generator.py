from typing import List, Optional, Union
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from openapi_schema_pydantic import OpenAPI, Components, Schema, Reference

from src.openapi_python_generator.language_converters.python.model_generator import generate_models
from src.openapi_python_generator.language_converters.python.service_generator import generate_services
from src.openapi_python_generator.models import ConversionResult, Model

def generator(data: OpenAPI) -> ConversionResult:
    """
    Generate Python code from an OpenAPI 3.0 specification.
    """

    models = generate_models(data.components)
    services = generate_services(data.paths)

    return ConversionResult(
        models=models,
        services=[],
    )
