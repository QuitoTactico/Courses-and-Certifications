La idea es que el volumen del container (su almacenamiento) no sea el default de él mismo, sino que sea un mapeo del local nuestro. Y le dijimos a nuestro flask que se autoactualizara.

# MAC/Linux Command:
`docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api`

# Windows command

## PowerShell

`docker run -dp 5000:5000 -w //app -v "$(Get-Location)://app" flask-smorest-api`

## Git Bash

`docker run -dp 5000:5000 -w //app -v "//$(pwd)://app" flask-smorest-api`

## Command Prompt (CMD)

`docker run -dp 5000:5000 -w //app -v "%cd%://app" flask-smorest-api`

# Explanation:

- `-dp 5000:5000` - same as before. Run in detached (background) mode and create a port mapping.
- `-w /app` - sets the container's present working directory where the command will run from.
- `-v "$(pwd):/app"` - bind mount (link) the host's present directory to the container's /app directory. Note: Docker requires absolute paths for binding mounts, so in this example we use pwd for printing the absolute path of the working directory instead of typing it manually.
- `flask-smorest-api` - the image to use.