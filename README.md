# kubic
Simple Python wrapper over Kubernetes API objects


The goal of this project is to generate a simple Kubernetes API designed to build Kubernetes manifests.

As the generated API is designed to build manifest (and not to parse manifest), it ignores K8S API only used to consume the Kubernetes REST API.

```python

d = apps.Deployment(name="myapp", namespace="default")

d.spec.min_ready_seconds = spec.get("min_ready_seconds")
d.spec.paused = spec.get("paused")
d.spec.progress_deadline_seconds = spec.get("deployment_progress_deadline_seconds")
d.spec.replicas = spec.get("replicas", 1)
d.spec.revision_history_limit = spec.get("revision_history_limit", 2)
d.spec.strategy = spec.get("update_strategy")

with open("manifest.yaml", "w") as f:
  yaml.dump(d, f, yaml.SafeDumper)

```

## K8S API

This project include most of Kubernetes 1.22 objects.


## CRDs

This project is also designed to generate python API from Kubernetes CRDs. It includes a bunch of common CRDs.
