from pydantic import BaseModel
from typing import Optional
import json


class Task(BaseModel):
    theme_id: int
    description: list[str]
    input: list[str]
    output: list[str]

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value

    class Config:
        extra = 'allow'


class TaskUpdate(BaseModel):
    description: Optional[list[str]] = None
    input: Optional[list[str]] = None
    output: Optional[list[str]] = None

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value

    class Config:
        extra = 'allow'


class TaskAnswer(BaseModel):
    code: str
    language: str
