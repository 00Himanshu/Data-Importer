# Data Importer

## About

The Data Importer project is designed to fetch phone data from a specified API and store it in a PostgreSQL database. This project is useful for applications that need to regularly import and store data from external APIs for further processing or analysis.

## Use Case

The primary use case for this project is to automate the process of importing phone data from an external API into a PostgreSQL database. This can be useful for data analysis, reporting, or integrating with other systems that require up-to-date phone data.

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
  host: "yourhostaddress"
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

## Code Structure

The project is organized as follows:

- `main.py`: The main script that orchestrates the data fetching and storing process.
- `db.py`: Contains functions for connecting to the database, creating tables, and inserting data.
- `config/config.yaml`: Configuration file for API and database settings.
- `requirements.txt`: Lists the required Python packages.
- `tests/`: Directory containing unit tests for the project.
- `data_importer.log`: Log file for recording the operations performed by the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.