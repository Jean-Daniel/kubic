#!/usr/local/bin/fish

for crd in schemas/crds/*;
  echo "  Processing $crd"
  python3 src/kubegen.py crd --api_module="..api" -o src/kubic/crds/ $crd
end

# for crd in (kubectl get crds -o name);
#   set crd (string replace -r 'customresourcedefinition.apiextensions.k8s.io/' '' $crd)
#   set name (string split --max 1 '.' $crd)[1]
#   echo "  Processing $crd"
#  python3 kubegen.py -o k8s/{$name}.py $crd
# end

black src/kubic
