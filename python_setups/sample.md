## Setting up project with uv 

### Initializing project 
    use -- uv init 
### Installing a single package
    use -- uv add <package-name>
### Installing from an existing requirements.txt
    use -- uv add -r requirements.txt 
### Running code 
    use -- uv run <file-name>.py 
### Generating requiremnets.txt 
    use -- uv pip compile pyproject.toml -o requirements.txt
