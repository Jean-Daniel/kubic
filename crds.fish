#!/usr/local/bin/fish

for crd in (kubectl get crds -o name);
  set crd (string replace -r 'customresourcedefinition.apiextensions.k8s.io/' '' $crd)
  set name (string split --max 1 '.' $crd)[1]
  echo "  Processing $crd"
  python3 kubegen.py -o k8s/{$name}.py $crd
end

black k8s
