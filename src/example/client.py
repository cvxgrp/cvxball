import numpy as np
import pyarrow as pa
import pyarrow.flight as fl
from loguru import logger


def numpy2pyarrow(data):
    return pa.array([{"data": data.flatten(), "shape": data.shape}])


def compute(client, data, logger=None):
    table = pa.table({"input": numpy2pyarrow(data)})
    logger.info("Created example data.")

    # Upload data
    command = "compute_ball"
    descriptor = fl.FlightDescriptor.for_command(command)

    logger.info(f"Uploading data with command: {command}")
    writer, _ = client.do_put(descriptor, table.schema)
    writer.write_table(table)
    writer.close()

    # Retrieve result
    ticket = fl.Ticket(command)  # Create a Ticket with the command
    reader = client.do_get(ticket)

    result_table = reader.read_all()
    logger.info("Result retrieved successfully.")

    results = {name: result_table.column(name)[0].as_py() for name in result_table.schema.names}
    logger.info(f"Results: {results}")
    return results


def main():
    # Connect to the server
    client = fl.connect("grpc+tcp://127.0.0.1:5006")
    logger.info("Connected to the server.")

    # Example data
    data = np.random.rand(10000, 20)  # 10000 points in 20D space
    compute(client, data, logger=logger)


if __name__ == "__main__":
    main()
