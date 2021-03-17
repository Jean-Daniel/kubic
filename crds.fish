#!/usr/local/bin/fish

set CRDS certificates.cert-manager.io \
        ciliumclusterwidenetworkpolicies.cilium.io \
        ciliumnetworkpolicies.cilium.io \
        podmonitors.monitoring.coreos.com \
        probes.monitoring.coreos.com \
        prometheusrules.monitoring.coreos.com \
        sealedsecrets.bitnami.com \
        servicemonitors.monitoring.coreos.com \
        verticalpodautoscaler.autoscaling.k8s.io \


for crd in $CRDS;
  echo "  Processing $crd"
  python3 src/kubegen.py --schemas ./schemas -o src/kubic/crds/ $crd
end

# for crd in (kubectl get crds -o name);
#   set crd (string replace -r 'customresourcedefinition.apiextensions.k8s.io/' '' $crd)
#   set name (string split --max 1 '.' $crd)[1]
#   echo "  Processing $crd"
#  python3 kubegen.py -o k8s/{$name}.py $crd
# end

black src
