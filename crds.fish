#!/usr/local/bin/fish

set CRDS sealedsecrets.bitnami.com \
         verticalpodautoscaler.autoscaling.k8s.io \
         schemas/cilium.crds.yaml \
         schemas/cert-manager.crds.yaml \
         schemas/prometheus-operator.crds.yaml\
         schemas/victoriametrics-operator.crds.yaml


for crd in schemas/crds/*;
  echo "  Processing $crd"
  python3 src/kubegen.py --schemas ./schemas -o src/kubic/crds/ $crd
end

# for crd in (kubectl get crds -o name);
#   set crd (string replace -r 'customresourcedefinition.apiextensions.k8s.io/' '' $crd)
#   set name (string split --max 1 '.' $crd)[1]
#   echo "  Processing $crd"
#  python3 kubegen.py -o k8s/{$name}.py $crd
# end

black src/kubic
