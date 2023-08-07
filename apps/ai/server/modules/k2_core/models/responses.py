from typing import Any

from pydantic import BaseModel, Field, confloat

from modules.k2_core.models.entities import SQLGenerationStatus, SQLQueryResult


class NLQueryResponse(BaseModel):
    id: Any | None = Field(alias="_id")
    nl_question_id: Any
    nl_response: str | None = None
    intermediate_steps: list[str] | None = None
    sql_query: str
    sql_query_result: SQLQueryResult | None
    sql_generation_status: SQLGenerationStatus = "NONE"
    exec_time: float | None = None
    total_tokens: int | None = None
    total_cost: float | None = None
    golden_record: bool = False
    confidence_score: float | None = None
    error_message: str | None


class Evaluation(BaseModel):
    id: str | None = Field(alias="_id")
    question_id: str | None = Field(alias="q_id")
    answer_id: str | None = Field(alias="a_id")
    score: confloat(ge=0, le=1) = 0.5
