import json
import os
from typing import List, Dict, Any


class BaseRepository:
    def __init__(self, file_path: str):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        self.file_path = os.path.join(base_dir, file_path)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def _read_json(self) -> List[Dict[str, Any]]:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def _write_json(self, data: List[Dict[str, Any]]) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def get_all(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save_all(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def get_next_id(self, data):
        if data:
            last_id = max(item['id'] for item in data)
            return last_id + 1
        return 1

    def save(self, new_data: Dict[str, Any]) -> None:
        data = self._read_json()
        data.append(new_data)
        self._write_json(data)

