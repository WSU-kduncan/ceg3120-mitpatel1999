Part 2

1. vim etc/hosts, Type content like IP, filename, and name.
2. ssh -i /home/mitpatel/ceg3120.aws-vm.pem ubuntu@privte IP
3. 
 - Modified: /etc/haproxy/haproxy.cfg 
 - Config: 
global
   
    maxconn 50000
    log /dev/log local0
    user haproxy
    group haproxy
    stats socket /run/haproxy/admin.sock user haproxy group haproxy mode 660 level admin

defaults
    # defaults here
    timeout connect 10s
    timeout client 30s
    timeout server 30s
    log global
    mode http
    option httplog
    maxconn 3000


frontend
    # a frontend that accepts requests from clients
    


backend
    # servers that fulfill the requests
    balence roundrobin
    server WedServ1 172.31.88.100:80
    server WedServ2 172.31.80.177:80

- Restart: sudo systemctl restart haproxy
- Source: https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/

4. 
- Modified:
- Config: 
- Restart: sudo systemctl restart apache2
- Source: https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04

