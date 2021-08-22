#!/usr/bin/env bash

az login

az account list-locations -o table

az group create --name "resource-group-west" --location "westus2"
