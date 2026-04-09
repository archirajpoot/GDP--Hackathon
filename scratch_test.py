import json
try:
    from openenv.core.client_types import TaskInfo
    print(TaskInfo.schema_json() if hasattr(TaskInfo, 'schema_json') else TaskInfo.model_json_schema())
except Exception as e:
    import traceback
    traceback.print_exc()
