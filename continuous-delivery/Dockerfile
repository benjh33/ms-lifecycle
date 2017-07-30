FROM  ubuntu:latest
MAINTAINER bjameshunter@gmail.com

# bootstrap ansible
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y software-properties-common python-pip && \
    apt-add-repository ppa:ansible/ansible && \
    apt-get update && \
    apt-get install -y --allow-remove-essential --allow-downgrades ansible \
      docker docker-compose

RUN pip install docker-py

RUN echo "[defaults] \n\
callback_plugins=/etc/ansible/callback_plugins/\n\
host_key_checking=False\n\
deprecation_warnings=False\n\
\n\
[privilege_escalation]\n\
become=True\n\
become_method=sudo\n\
become_user=root" > /etc/ansible/ansible.cfg

RUN useradd dt && \
    mkdir /home/dt && \
    chown -R dt /home/dt
USER dt
WORKDIR /home/dt/

EXPOSE 22
