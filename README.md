# Data Importer

## Setup

1. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

2. Update the `config/config.yaml` file with your API and database configuration.

3. Run the main script to fetch and store phone data:
    ```sh
    python main.py
    ```

## Configuration

The `config/config.yaml` file should contain the following structure:
```yaml
api:
  url: "https://api.restful-api.dev/objects"

database:
  host: "youhostaddress"
  port: 5432
  user: "username"
  password: "password"
  dbname: "database name"
```

## Logging

Logs are stored in the `data_importer.log` file. You can check this file for detailed logs of the operations performed by the script.

## Testing

Run the tests using:
    ```sh
    python -m unittest discover tests
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.