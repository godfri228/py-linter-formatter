from typing import Dict, Any, List, Union

def format_linter_error(error: Dict[str, Any]) -> Dict[str, Union[int, str]]:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(path: str, errors: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "path": path,
        "status": "failed" if errors else "passed",
        "errors": [
            {
                "line": e["line_number"],
                "column": e["column_number"],
                "message": e["text"],
                "name": e["code"],
                "source": "flake8"
            }
            for e in errors
        ]
    }


def format_linter_report(errors: Dict[str, List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    return [
        {
            "path": path,
            "status": "failed" if file_errors else "passed",
            "errors": [
                {
                    "line": e["line_number"],
                    "column": e["column_number"],
                    "message": e["text"],
                    "name": e["code"],
                    "source": "flake8"
                }
                for e in file_errors
            ]
        }
        for path, file_errors in errors.items()
    ]
