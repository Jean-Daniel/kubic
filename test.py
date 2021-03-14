import json

from k8s.api import Deployment, Container, DeploymentStrategy

deployment = Deployment("nginx", "default")
deployment.spec.paused = False
deployment.spec.min_ready_seconds = 10
deployment.spec.template.metadata.name = "nginx"
deployment.spec.template.metadata.labels["app"] = "nginx"
deployment.spec.template.spec.containers.append(Container(name="nginx"))

default_strategy = {
    "type": "RollingUpdate",
    "rolling_update": {
        "max_surge": "25%",
        "max_unavailable": "25%"
    }
}
deployment.spec.strategy = default_strategy

print(json.dumps(deployment, indent="  "))


obj = DeploymentStrategy.from_dict(default_strategy)
print(json.dumps(obj, indent="  "))
