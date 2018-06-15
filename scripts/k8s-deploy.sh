#!/bin/bash

./scripts/az login --service-principal --username $AZURE_APP_ID --password $AZURE_PASSWORD --tenant $AZURE_TENANT_ID
./scripts/az aks get-credentials --resource-group $AZURE_RESOURCE_GROUP --name $AZURE_CLUSTER_NAME

curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl

NAMESPACE="${PROJECT_NAME}-${TAG//./-}"

if ! ./kubectl get namespace "${NAMESPACE}"; then
    ./kubectl create namespace "${NAMESPACE}"
fi

# Change version
sed -ie 's/0.0.1/'"${TAG}"'/g' k8s/dev/conta-api/3.conta-api-deployment.yml

# Change domain name
sed -ie 's/conta-api\.dev\.fernandoe\.com/'"${NAMESPACE}"'.dev.fernandoe.com/g' k8s/dev/conta-api/4.certificate.yml
sed -ie 's/conta-api\.dev\.fernandoe\.com/'"${NAMESPACE}"'.dev.fernandoe.com/g' k8s/dev/conta-api/5.ingress.yml

./kubectl apply --recursive -f ./k8s/dev/ -n ${NAMESPACE}

./kubectl scale -n ${NAMESPACE} --replicas=0 deploy/conta-api
./kubectl scale -n ${NAMESPACE} --replicas=1 deploy/conta-api
