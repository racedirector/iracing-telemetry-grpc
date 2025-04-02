# iracing-telemetry-grpc

A gRPC server for iRacing telemetry data. Uses `pyirsdk` under the hood.

Allows for messaging to the iRacing simulation, and querying for telmetry data.

## Running the server

Clone the repo and create the environment file:

```bash
cp .env.template .env
```

Then, install the dependencies:

```bash
make install
```

Run the server:

```bash
make run
```

## Development

Make changes to the `proto` files in the `proto` directory and run:

```bash
make protoc
```

To generate the gRPC code.
