"""大江工具箱 · Qwen 提示词优化节点。"""

import importlib.util
from pathlib import Path

_PACKAGE_DIR = Path(__file__).resolve().parent
_NODES_DIR = _PACKAGE_DIR / "nodes"

WEB_DIRECTORY = "./web"

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

for _file_path in sorted(_NODES_DIR.glob("*.py")):
    if _file_path.name == "__init__.py":
        continue
    _spec = importlib.util.spec_from_file_location(
        f"dj_qwenprompt.nodes.{_file_path.stem}", _file_path
    )
    _module = importlib.util.module_from_spec(_spec)
    try:
        _spec.loader.exec_module(_module)
    except Exception as _error:
        print(f"[DJ_QwenPrompt] 节点模块加载失败 {_file_path.name}: {_error}")
        continue
    NODE_CLASS_MAPPINGS.update(getattr(_module, "NODE_CLASS_MAPPINGS", {}))
    NODE_DISPLAY_NAME_MAPPINGS.update(getattr(_module, "NODE_DISPLAY_NAME_MAPPINGS", {}))

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

print(
    f"\033[92m[DJ_QwenPrompt]\033[0m "
    f"\033[93m{len(NODE_CLASS_MAPPINGS)} nodes\033[0m loaded | "
    f"\033[94m大江工具箱\033[0m"
)
