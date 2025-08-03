# HTTPS Deployment Guide

## 1. SSL Certificate Setup
Obtain certificates from Let's Encrypt:
```bash
sudo certbot certonly --nginx -d yourdomain.com -d www.yourdomain.com
```

## 2. Nginx Configuration
`/etc/nginx/sites-available/yourdomain.com`:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com www.yourdomain.com;
    
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    # Other Django proxy settings...
}
```