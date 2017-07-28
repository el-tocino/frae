# What 

A wrapper for google's vision api run on a raspberry pi with an attached pi camera. 

# How

Via PiCamera, snap a picture. Generate a hash from resulting pic (sha256), upload file to GCP storage named after the hash. Call the Vision label API, return what it lists. 

# Future

Separate the steps into individual pieces to limit memory footprint of each piece and make them more granularly usable (ie, batch jobs, delayed labeling, etc). 

# Things

Setup your GCP account over at https://console.cloud.google.com/
Sign up for free trial and/or create a project.
Check api manager to make sure cloud storage is enabled. This appears to be the default.

# Stuff 

Google's gcloud and gsutil tools can be run on a pi, though they no longer package them for ARM architecture.

 - sudo pip install google-cloud
 - mkdir ~/tmp
 - cd ~/tmp
(versions will change this was just the current as of whenever this was created)
 - wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-164.0.0-linux-x86.tar.gz
 - tar xfz google-cloud-sdk-164.0.0-linux-x86.tar.gz
 - cd google-cloud-sdk

To run without constantly authenticating, use the following:
 - python lib/gcloud.py components install beta app-engine-python
 - python lib/gcloud.py auth login
 - python lib/gcloud.py beta auth application-default login
 - python lib/gcloud.py config set project $PROJECT_NAME_FROM_ABOVE

