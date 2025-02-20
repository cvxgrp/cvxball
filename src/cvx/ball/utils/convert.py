from typing import Dict

import numpy as np
import pyarrow as pa


def np_2_pa(data: Dict[str, np.ndarray]) -> pa.Table:
    """
    Convert a dictionary of NumPy arrays into a PyArrow Table.
    Each array is stored as a structured array containing the flattened data and its original shape.

    Args:
        data (Dict[str, np.ndarray]): Dictionary where keys are column names and values are NumPy arrays
            of any shape.

    Returns:
        pa.Table: PyArrow Table where each column contains structured arrays with 'data' and 'shape' fields.

    Examples:
        >>> # Single array
        >>> import numpy as np
        >>> data = {'array1': np.array([[1, 2], [3, 4]])}
        >>> table = np_2_pa(data)
        >>> print(table.schema)
        array1: struct<data: list<item: int64>, shape: list<item: int64>>

        >>> # Multiple arrays of different shapes
        >>> data = {
        ...     'matrix': np.array([[1, 2], [3, 4]]),
        ...     'vector': np.array([5, 6, 7]),
        ...     'scalar': np.array(42)
        ... }
        >>> table = np_2_pa(data)

        >>> # Working with complex data
        >>> arr = table.column('matrix')[0].as_py()
        >>> original_shape = tuple(arr['shape'])
        >>> restored_array = np.array(arr['data']).reshape(original_shape)
    """

    def _f(value: np.ndarray) -> pa.Array:
        arr = np.asarray(value)

        # Create a dictionary with the flattened data and shape
        arr_dict = {"data": arr.flatten(), "shape": np.array(arr.shape, dtype=np.int64)}

        return pa.array([arr_dict])

    return pa.Table.from_pydict({key: _f(value) for key, value in data.items() if value is not None})


def pa_2_np(table: pa.Table) -> dict[str, np.ndarray]:
    """
    Convert a PyArrow Table back to a dictionary of NumPy arrays.
    This is the inverse operation of np_2_pa.

    Args:
        table (pa.Table): PyArrow Table

    Returns:
        Dict[str, np.ndarray]: Dictionary where keys are column names and values are NumPy arrays
            with their original shapes restored.
    """

    def _f(col_name: str) -> np.ndarray:
        struct_arr = table.column(col_name)[0].as_py()
        # Reconstruct the original array
        data = np.asarray(struct_arr["data"])
        shape = tuple(struct_arr["shape"])
        return data.reshape(shape)

    return {name: _f(name) for name in table.column_names}
