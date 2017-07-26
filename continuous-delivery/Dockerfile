FROM  phusion/baseimage:latest
MAINTAINER bjameshunter@gmail.com

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y software-properties-common && \
    apt-add-repository ppa:ansible/ansible && \
    apt-get update && \
    apt-get install -y --allow-remove-essential --allow-downgrades ansible

RUN echo "[defaults] \n\
callback_plugins=/etc/ansible/callback_plugins/\n\
host_key_checking=False\n\
deprecation_warnings=False\n\
\n\
[privilege_escalation]\n\
become=True\n\
become_method=sudo\n\
become_user=root" > /etc/ansible/ansible.cfg

EXPOSE 22
