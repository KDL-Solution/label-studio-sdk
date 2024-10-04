# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from ..utilities import validate_response


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = [
        {
            "title": "title",
            "parent_model": 1,
            "model_provider_connection": 1,
            "prompt": "prompt",
            "provider": "OpenAI",
            "provider_model_id": "provider_model_id",
            "created_by": 1,
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-15T09:30:00Z",
            "organization": 1,
        }
    ]
    expected_types: typing.Any = (
        "list",
        {
            0: {
                "title": None,
                "parent_model": "integer",
                "model_provider_connection": "integer",
                "prompt": None,
                "provider": None,
                "provider_model_id": None,
                "created_by": "integer",
                "created_at": "datetime",
                "updated_at": "datetime",
                "organization": "integer",
            }
        },
    )
    response = client.prompts.versions.list(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.prompts.versions.list(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "title": "title",
        "parent_model": 1,
        "model_provider_connection": 1,
        "prompt": "prompt",
        "provider": "OpenAI",
        "provider_model_id": "provider_model_id",
        "created_by": 1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "organization": 1,
    }
    expected_types: typing.Any = {
        "title": None,
        "parent_model": "integer",
        "model_provider_connection": "integer",
        "prompt": None,
        "provider": None,
        "provider_model_id": None,
        "created_by": "integer",
        "created_at": "datetime",
        "updated_at": "datetime",
        "organization": "integer",
    }
    response = client.prompts.versions.create(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.prompts.versions.create(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "title": "title",
        "parent_model": 1,
        "model_provider_connection": 1,
        "prompt": "prompt",
        "provider": "OpenAI",
        "provider_model_id": "provider_model_id",
        "created_by": 1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "organization": 1,
    }
    expected_types: typing.Any = {
        "title": None,
        "parent_model": "integer",
        "model_provider_connection": "integer",
        "prompt": None,
        "provider": None,
        "provider_model_id": None,
        "created_by": "integer",
        "created_at": "datetime",
        "updated_at": "datetime",
        "organization": "integer",
    }
    response = client.prompts.versions.get(id=1, version_id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.prompts.versions.get(id=1, version_id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.prompts.versions.delete(id=1, version_id=1) is None  # type: ignore[func-returns-value]

    assert await async_client.prompts.versions.delete(id=1, version_id=1) is None  # type: ignore[func-returns-value]


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "title": "title",
        "parent_model": 1,
        "model_provider_connection": 1,
        "prompt": "prompt",
        "provider": "OpenAI",
        "provider_model_id": "provider_model_id",
        "created_by": 1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "organization": 1,
    }
    expected_types: typing.Any = {
        "title": None,
        "parent_model": "integer",
        "model_provider_connection": "integer",
        "prompt": None,
        "provider": None,
        "provider_model_id": None,
        "created_by": "integer",
        "created_at": "datetime",
        "updated_at": "datetime",
        "organization": "integer",
    }
    response = client.prompts.versions.update(id=1, version_id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.prompts.versions.update(id=1, version_id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_get_refined_prompt(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "title": "title",
        "reasoning": "reasoning",
        "prompt": "prompt",
        "refinement_job_id": "refinement_job_id",
        "refinement_status": "Pending",
    }
    expected_types: typing.Any = {
        "title": None,
        "reasoning": None,
        "prompt": None,
        "refinement_job_id": None,
        "refinement_status": None,
    }
    response = client.prompts.versions.get_refined_prompt(
        prompt_id=1, version_id=1, refinement_job_id="refinement_job_id"
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.prompts.versions.get_refined_prompt(
        prompt_id=1, version_id=1, refinement_job_id="refinement_job_id"
    )
    validate_response(async_response, expected_response, expected_types)


async def test_refine_prompt(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "title": "title",
        "reasoning": "reasoning",
        "prompt": "prompt",
        "refinement_job_id": "refinement_job_id",
        "refinement_status": "Pending",
    }
    expected_types: typing.Any = {
        "title": None,
        "reasoning": None,
        "prompt": None,
        "refinement_job_id": None,
        "refinement_status": None,
    }
    response = client.prompts.versions.refine_prompt(prompt_id=1, version_id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.prompts.versions.refine_prompt(prompt_id=1, version_id=1)
    validate_response(async_response, expected_response, expected_types)
