from typing import Iterator, List

import pyarrow as pa
from pyarrow.flight import FlightStreamReader


class TableReader(FlightStreamReader):
    """
    A Flight reader implementation that wraps a PyArrow Table.
    This allows a pa.Table to be used in Flight server implementations
    where a FlightStreamReader is expected.

    Args:
        table (pa.Table): The PyArrow Table to wrap.

    Examples:
        >>> # Create a sample table
        >>> import pyarrow as pa
        >>> data = {
        ...     'id': [1, 2, 3],
        ...     'name': ['Alice', 'Bob', 'Charlie'],
        ...     'score': [85.5, 92.0, 78.5]
        ... }
        >>> table = pa.Table.from_pydict(data)
        >>>
        >>> # Create the reader
        >>> reader = TableReader(table)
        >>>
        >>> # Read all data at once
        >>> full_table = reader.read_all()
        >>> print(full_table.to_pandas())
        >>>
    """

    def __init__(self, table: pa.Table) -> None:
        """
        Initialize the reader with a PyArrow Table.
        Converts the table into record batches for streaming access.

        Args:
            table (pa.Table): The source table to read from
        """
        self._table: pa.Table = table
        self._current_batch: int = 0
        self._batches: List[pa.RecordBatch] = table.to_batches()

    def read_all(self) -> pa.Table:
        """
        Read the entire table at once.
        Useful when you need all the data and don't want to stream it.

        Returns:
            pa.Table: The complete table
        """
        return self._table

    def __iter__(self) -> Iterator[pa.RecordBatch]:
        """
        Make the reader iterable.
        Allows using the reader in a for loop.

        Returns:
            Iterator[pa.RecordBatch]: The iterator object
        """
        return self
