# LPR Checker

This project is to perform the following:
1. Detect vehicle license plates with a LPR model
2. Matches them with the database
3. Returns result of LPR and information from database (if exist)

>Note: Disclaimer -- this is a pet project, use at your own risk.

## Checklist

-   [X] List of commands
-   [ ] Dockerize the application
-   [ ] Create CI/CD for this project


## Commands

The commands to run this project are listed in the `Makefile`. To run a command from the `Makefile`:

```bash
# Replace [your_command_here] with your desired command
make [your_command_here]
```

For development purposes, it is recommended to enter into the venv first with:
```
source .venv/bin/activate
```

### List of commands

1.  Initial setup
    ```bash
    make start-setup
    ```

2.  Enter venv
    ```bash
    make start-venv
    ```

3.  Start Django development server
    ```bash
    make start-server
    ```

