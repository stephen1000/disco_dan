"""
Docker control bindings
"""

from pathlib import Path

import yaml

import docker
from disco_dan import settings

compose_path = Path(settings.DOCKER_COMPOSE_FILE)
compose = yaml.load(compose_path.read_text(), Loader=yaml.Loader)
client = docker.from_env()


class InvalidContainer(Exception):
    """ I don't like that container """


async def get_container(container_name: str):
    """ Get container with name """
    if container_name not in compose.get("services", []):
        raise InvalidContainer("Container %s does not exist!", container_name)
    containers = client.containers.list()
    containers = [
        c
        for c in containers
        if c.name == container_name
        or c.name == f"{settings.DOCKER_COMPOSE_GROUP}_{container_name}_1"
    ]
    if not containers:
        raise InvalidContainer("Container %s not found!", container_name)
    return containers[0]


async def exec_command(container_name: str, cmd: str):
    """ Execute `cmd` in `container_name` via rcon """
    container = await get_container(container_name)
    result = container.exec_run(f"rcon-cli {cmd}")
    return result.output.decode().strip()