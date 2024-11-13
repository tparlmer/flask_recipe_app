#!/bin/bash

# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install required packages
sudo apt-get install -y python3-pip python3-dev nginx postgresql postgresql-contrib

# Create database and user
sudo -u postgres psql << EOF
CREATE DATABASE recipes_db;
CREATE USER your_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE recipes_db TO your_user;
EOF

# Install Python dependencies
pip3 install -r requirements.txt

# Create systemd service file
sudo tee /etc/systemd/system/recipes.service << EOF
[Unit]
Description=Recipe App
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/your/app
Environment="PATH=/path/to/your/venv/bin"
ExecStart=/path/to/your/venv/bin/python3 app.py

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

# Enable the site
sudo ln -s /etc/nginx/sites-available/recipes /etc/nginx/sites-enabled

# Start services
sudo systemctl start recipes
sudo systemctl enable recipes
sudo systemctl restart nginx
