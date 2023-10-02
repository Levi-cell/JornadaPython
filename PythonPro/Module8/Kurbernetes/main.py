from kubernetes import client, config

# Carrega a configuração do kubernetes do arquivo ~/.kube/config
config.load_kube_config()

# Cria um objeto do tipo Deployment
deployment = client.ExtensionsV1beta1Deployment()

# Configura os atributos do Deployment
metadata = client.V1ObjectMeta(name="my-deployment")
spec = client.ExtensionsV1beta1DeploymentSpec(
    replicas=3,
template=client.V1PodTemplateSpec(
    metadata=client.V1ObjectMeta(labels={"app": "my-app"}),
    spec=client.V1PodSpec(
        containers=[
            client.V1Container(
                name="my-container",
                image="nginx:latest",
                ports=[client.V1ContainerPort(container_port=80)],
            )
        ]
    )
)
)