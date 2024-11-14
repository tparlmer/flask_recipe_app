#!/bin/bash

# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install required packages
sudo apt-get install -y python3-pip python3-dev nginx sqlite3

# Install Python dependencies
pip3 install -r requirements.txt

# Create systemd service file
sudo tee /etc/systemd/system/recipes.service << EOF
[Unit]
Description=Recipe App
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/recipes
Environment="PATH=/usr/local/bin"
ExecStart=/usr/bin/python3 app.py

[Install]
WantedBy=multi-user.target
EOF

# Configure Nginx
sudo tee /etc/nginx/sites-available/recipes << EOF
server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

# Create application directory
sudo mkdir -p /var/www/recipes
sudo chown www-data:www-data /var/www/recipes

# Enable the site
sudo ln -s /etc/nginx/sites-available/recipes /etc/nginx/sites-enabled
sudo rm -f /etc/nginx/sites-enabled/default  # Remove default site

# Start services
sudo systemctl start recipes
sudo systemctl enable recipes
sudo systemctl restart nginx
