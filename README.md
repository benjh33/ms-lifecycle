# update docker daemon on ansible hosts

1. add to /etc/docker/daemon.json
  - { "insecure-registries": ["cd:5000"] }
