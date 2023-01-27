#until curl --output /dev/null --silent --head --fail https://github.com/piotrmiskiewicz/gactions/releases/download/1.0.3/template.yaml; do
#            echo 'waiting...'
#            sleep 10
#done

found=false
while [ $found == "false" ]
do
  found=$(skopeo list-tags docker://europe-docker.pkg.dev/kyma-project/prod/unsigned/component-descriptors/kyma.project.io/module/btp-operator | jq '.Tags|any(. == "0.0.14")')
  sleep 10
  echo "..."
done