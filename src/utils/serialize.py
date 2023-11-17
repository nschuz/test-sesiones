from typing import List, Any, Dict
from sqlalchemy.orm import class_mapper
from utils.types import sqlalchemy_to_python_types

def sqlalchemy_to_dict(obj: Any, exclude_keys: List[str] = []) -> Dict[str, Any]:
        """
        Convert an SQLAlchemy object to a dictionary.

        Args:
            obj (Any): The SQLAlchemy object to convert.
            exclude_keys (List[str], optional): The list of keys to exclude from the conversion. Defaults to [].

        Returns:
            Dict[str, Any]: The dictionary representation of the SQLAlchemy object.
        """
        mapper = class_mapper(obj.__class__)
        columns = [column.key for column in mapper.columns]

        data: Dict[str, Any] = {}
        for column in columns:
            if column in exclude_keys:
                continue

            try:
                column_value = getattr(obj, column)
                if isinstance(column_value, (str, int, float, bool, dict, list)):
                    data[column] = column_value
                else:
                    data[column] = (
                        sqlalchemy_to_python_types.get(type(column_value))(column_value)
                        if column_value
                        else None
                    )
            except Exception:
                continue

        return data
