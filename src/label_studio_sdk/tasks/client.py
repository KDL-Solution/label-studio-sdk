# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pagination import AsyncPager, SyncPager
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..types.base_task import BaseTask
from ..types.project_import import ProjectImport
from ..types.task import Task
from .types.tasks_list_request_fields import TasksListRequestFields
from .types.tasks_list_response import TasksListResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TasksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_many_status(
        self, id: int, import_pk: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectImport:
        """
        Get information about an async project import operation. This can be especially useful to monitor status, as large import jobs can take time.

        You will need the project ID and the unique ID of the import operation.

        The project ID can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list).

        The import ID is returned as part of the response when you call [Import tasks](import-tasks).

        Parameters
        ----------
        id : int
            The project ID.

        import_pk : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectImport


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.tasks.create_many_status(
            id=1,
            import_pk="import_pk",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/imports/{jsonable_encoder(import_pk)}/",
            method="GET",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ProjectImport, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_all_tasks(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete all tasks from a specific project.

        The project ID can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list).

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.tasks.delete_all_tasks(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/tasks/", method="DELETE", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        view: typing.Optional[int] = None,
        project: typing.Optional[int] = None,
        resolve_uri: typing.Optional[bool] = None,
        fields: typing.Optional[TasksListRequestFields] = None,
        review: typing.Optional[bool] = None,
        include: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[Task]:
        """
        Retrieve a list of tasks.

        You can use the query parameters to filter the list by project and/or view (a tab within the Data Manager). You can also optionally add pagination to make the response easier to parse.

        The project ID can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list). The view ID can be found using [List views](../views/list).

        Parameters
        ----------
        page : typing.Optional[int]
            A page number within the paginated result set.

        page_size : typing.Optional[int]
            Number of results to return per page.

        view : typing.Optional[int]
            View ID

        project : typing.Optional[int]
            Project ID

        resolve_uri : typing.Optional[bool]
            Resolve task data URIs using Cloud Storage

        fields : typing.Optional[TasksListRequestFields]
            Set to "all" if you want to include annotations and predictions in the response

        review : typing.Optional[bool]
            Get tasks for review

        include : typing.Optional[str]
            Specify which fields to include in the response

        query : typing.Optional[str]
            Additional query to filter tasks. It must be JSON encoded string of dict containing one of the following parameters: `{"filters": ..., "selectedItems": ..., "ordering": ...}`

            - **filters**: dict with `"conjunction"` string (`"or"` or `"and"`) and list of filters in `"items"` array. Each filter is a dictionary with keys: `"filter"`, `"operator"`, `"type"`, `"value"`. [Read more about available filters](https://labelstud.io/sdk/data_manager.html)<br/> Example: `{"conjunction": "or", "items": [{"filter": "filter:tasks:completed_at", "operator": "greater", "type": "Datetime", "value": "2021-01-01T00:00:00.000Z"}]}`
            - **selectedItems**: dictionary with keys: `"all"`, `"included"`, `"excluded"`. If "all" is `false`, `"included"` must be used. If "all" is `true`, `"excluded"` must be used.<br/> Examples: `{"all": false, "included": [1, 2, 3]}` or `{"all": true, "excluded": [4, 5]}`
            - **ordering**: list of fields to order by. Currently, ordering is supported by only one parameter. <br/>
              Example: `["completed_at"]`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Task]
            List of Tasks

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.tasks.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/tasks/",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "view": view,
                "project": project,
                "resolve_uri": resolve_uri,
                "fields": fields,
                "review": review,
                "include": include,
                "query": query,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            _parsed_response = pydantic_v1.parse_obj_as(TasksListResponse, _response.json())  # type: ignore
            _has_next = True
            _get_next = lambda: self.list(
                page=page + 1 if page is not None else 1,
                page_size=page_size,
                view=view,
                project=project,
                resolve_uri=resolve_uri,
                fields=fields,
                review=review,
                include=include,
                query=query,
                request_options=request_options,
            )
            _items = _parsed_response.tasks
            return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        project: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseTask:
        """
        Create a new labeling task in Label Studio.

        The data you provide depends on your labeling config and data type.

        You will also need to provide a project ID. The project ID can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list).

        Parameters
        ----------
        data : typing.Optional[typing.Dict[str, typing.Any]]
            Task data dictionary with arbitrary keys and values

        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseTask
            Created task

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.tasks.create(
            data={"image": "https://example.com/image.jpg", "text": "Hello, world!"},
            project=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/tasks/",
            method="POST",
            json={"data": data, "project": project},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseTask, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> BaseTask:
        """
        Get task data, metadata, annotations and other attributes for a specific labeling task by task ID.
        The task ID is available from the Label Studio URL when viewing the task, or you can retrieve it programmatically with [Get task list](list).

        Parameters
        ----------
        id : str
            Task ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseTask
            Task

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.tasks.get(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/tasks/{jsonable_encoder(id)}/", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseTask, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a task in Label Studio.

        You will need the task ID. This is available from the Label Studio URL when viewing the task, or you can retrieve it programmatically with [Get task list](list).

        <Warning>This action cannot be undone.</Warning>

        Parameters
        ----------
        id : str
            Task ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.tasks.delete(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/tasks/{jsonable_encoder(id)}/", method="DELETE", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: str,
        *,
        data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        project: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseTask:
        """
        Update the attributes of an existing labeling task.

        You will need the task ID. This is available from the Label Studio URL when viewing the task, or you can retrieve it programmatically with [Get task list](list).

        Parameters
        ----------
        id : str
            Task ID

        data : typing.Optional[typing.Dict[str, typing.Any]]
            Task data dictionary with arbitrary keys and values

        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseTask
            Updated task

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.tasks.update(
            id="id",
            data={"image": "https://example.com/image.jpg", "text": "Hello, world!"},
            project=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/tasks/{jsonable_encoder(id)}/",
            method="PATCH",
            json={"data": data, "project": project},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseTask, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTasksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_many_status(
        self, id: int, import_pk: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectImport:
        """
        Get information about an async project import operation. This can be especially useful to monitor status, as large import jobs can take time.

        You will need the project ID and the unique ID of the import operation.

        The project ID can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list).

        The import ID is returned as part of the response when you call [Import tasks](import-tasks).

        Parameters
        ----------
        id : int
            The project ID.

        import_pk : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectImport


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.tasks.create_many_status(
            id=1,
            import_pk="import_pk",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/imports/{jsonable_encoder(import_pk)}/",
            method="GET",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ProjectImport, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_all_tasks(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete all tasks from a specific project.

        The project ID can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list).

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.tasks.delete_all_tasks(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/tasks/", method="DELETE", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        view: typing.Optional[int] = None,
        project: typing.Optional[int] = None,
        resolve_uri: typing.Optional[bool] = None,
        fields: typing.Optional[TasksListRequestFields] = None,
        review: typing.Optional[bool] = None,
        include: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[Task]:
        """
        Retrieve a list of tasks.

        You can use the query parameters to filter the list by project and/or view (a tab within the Data Manager). You can also optionally add pagination to make the response easier to parse.

        The project ID can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list). The view ID can be found using [List views](../views/list).

        Parameters
        ----------
        page : typing.Optional[int]
            A page number within the paginated result set.

        page_size : typing.Optional[int]
            Number of results to return per page.

        view : typing.Optional[int]
            View ID

        project : typing.Optional[int]
            Project ID

        resolve_uri : typing.Optional[bool]
            Resolve task data URIs using Cloud Storage

        fields : typing.Optional[TasksListRequestFields]
            Set to "all" if you want to include annotations and predictions in the response

        review : typing.Optional[bool]
            Get tasks for review

        include : typing.Optional[str]
            Specify which fields to include in the response

        query : typing.Optional[str]
            Additional query to filter tasks. It must be JSON encoded string of dict containing one of the following parameters: `{"filters": ..., "selectedItems": ..., "ordering": ...}`

            - **filters**: dict with `"conjunction"` string (`"or"` or `"and"`) and list of filters in `"items"` array. Each filter is a dictionary with keys: `"filter"`, `"operator"`, `"type"`, `"value"`. [Read more about available filters](https://labelstud.io/sdk/data_manager.html)<br/> Example: `{"conjunction": "or", "items": [{"filter": "filter:tasks:completed_at", "operator": "greater", "type": "Datetime", "value": "2021-01-01T00:00:00.000Z"}]}`
            - **selectedItems**: dictionary with keys: `"all"`, `"included"`, `"excluded"`. If "all" is `false`, `"included"` must be used. If "all" is `true`, `"excluded"` must be used.<br/> Examples: `{"all": false, "included": [1, 2, 3]}` or `{"all": true, "excluded": [4, 5]}`
            - **ordering**: list of fields to order by. Currently, ordering is supported by only one parameter. <br/>
              Example: `["completed_at"]`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Task]
            List of Tasks

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.tasks.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/tasks/",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "view": view,
                "project": project,
                "resolve_uri": resolve_uri,
                "fields": fields,
                "review": review,
                "include": include,
                "query": query,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            _parsed_response = pydantic_v1.parse_obj_as(TasksListResponse, _response.json())  # type: ignore
            _has_next = True
            _get_next = lambda: self.list(
                page=page + 1 if page is not None else 1,
                page_size=page_size,
                view=view,
                project=project,
                resolve_uri=resolve_uri,
                fields=fields,
                review=review,
                include=include,
                query=query,
                request_options=request_options,
            )
            _items = _parsed_response.tasks
            return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        project: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseTask:
        """
        Create a new labeling task in Label Studio.

        The data you provide depends on your labeling config and data type.

        You will also need to provide a project ID. The project ID can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list).

        Parameters
        ----------
        data : typing.Optional[typing.Dict[str, typing.Any]]
            Task data dictionary with arbitrary keys and values

        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseTask
            Created task

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.tasks.create(
            data={"image": "https://example.com/image.jpg", "text": "Hello, world!"},
            project=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/tasks/",
            method="POST",
            json={"data": data, "project": project},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseTask, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> BaseTask:
        """
        Get task data, metadata, annotations and other attributes for a specific labeling task by task ID.
        The task ID is available from the Label Studio URL when viewing the task, or you can retrieve it programmatically with [Get task list](list).

        Parameters
        ----------
        id : str
            Task ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseTask
            Task

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.tasks.get(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/tasks/{jsonable_encoder(id)}/", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseTask, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a task in Label Studio.

        You will need the task ID. This is available from the Label Studio URL when viewing the task, or you can retrieve it programmatically with [Get task list](list).

        <Warning>This action cannot be undone.</Warning>

        Parameters
        ----------
        id : str
            Task ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.tasks.delete(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/tasks/{jsonable_encoder(id)}/", method="DELETE", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: str,
        *,
        data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        project: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseTask:
        """
        Update the attributes of an existing labeling task.

        You will need the task ID. This is available from the Label Studio URL when viewing the task, or you can retrieve it programmatically with [Get task list](list).

        Parameters
        ----------
        id : str
            Task ID

        data : typing.Optional[typing.Dict[str, typing.Any]]
            Task data dictionary with arbitrary keys and values

        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseTask
            Updated task

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.tasks.update(
            id="id",
            data={"image": "https://example.com/image.jpg", "text": "Hello, world!"},
            project=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/tasks/{jsonable_encoder(id)}/",
            method="PATCH",
            json={"data": data, "project": project},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseTask, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
