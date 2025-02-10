
{
  "name": "Python Development Environment",
  "image": "mcr.microsoft.com/vscode/devcontainers/python:3.9",
  "settings": {
    "terminal.integrated.shell.linux": "/bin/bash"
  },
  "extensions": [
    "ms-python.python",
    "ms-python.vscode-pylance"
  ],
  "postCreateCommand": "pip install -r requirements.txt"
}
