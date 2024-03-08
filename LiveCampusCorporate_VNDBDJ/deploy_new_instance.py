import docker

def deploy_new_instance():
    client = docker.from_env()

    container = client.containers.run(
        'projet_web',
        detach=True,
        ports={'8080/tcp': 8081},
        volumes={'logs': {'bind': '/var/log/app', 'mode': 'rw'}}
    )

    print("Nouvelle instance de l'application web démarrée avec succès!")
    print("ID du conteneur:", container.id)

if __name__ == "__main__":
    deploy_new_instance()
