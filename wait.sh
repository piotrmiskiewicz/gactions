until curl --output /dev/null --silent --head --fail https://github.com/piotrmiskiewicz/gactions/releases/download/1.0.3/template.yaml; do
            echo 'waiting...'
            sleep 10
done