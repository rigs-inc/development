# author: @noizee
#
# Create a Git bare repository
#
# Replace the following tags with your data:
# - {{server_ip}}, ex: 127.0.0.1
# - {{repository_root}}, ex: /var/repo/app.git
# - {{application_root}}, ex: /var/www/app
#

server_ip={{server_ip}}
repository_source={{repository_root}}.git
application_source={{application_root}}
post_receive_webhook=$repository_source/hooks/post-receive

# Create bare repository...
git --bare init $repository_source || echo "Error"; exit

# Creating post-receive hook
{
  printf "#!/bin/sh
  git --work-tree=${application_source} --git-dir=${repository_source} checkout -f" > $post_receive_webhook
} || {
  echo "Error" 
  exit
}

sudo chmod +x $post_receive_webhook &&
sudo chown git -R $repository_source &&
sudo chown git -R $application_source

printf '''
Git Bare Repository

Application: ${application_source}
Repository: ${repository_source}
SSH: ssh://git@${server_ip}${repository_source}
'''
