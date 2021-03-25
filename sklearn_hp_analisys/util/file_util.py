# Copyright (c) Aniskov N.
import json
import os
from typing import List


def read_file_to_string(filename: str) -> str:
    with open(filename) as f:
        content = f.read()
    return content


def get_all_src_files_from_dir(dirname: str) -> List[str]:
    result = []
    for entry in os.listdir(dirname):
        if entry.endswith('.py') and entry != '__init__.py':
            sample_filename = os.path.join(dirname, entry)
            result.append(sample_filename)
    return result


def write_json_to_file(result, out_filename):

    with open(out_filename, 'w') as out_f:
        json.dump(result, out_f)