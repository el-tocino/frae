# What 

A wrapper for google's vision api run on a raspberry pi with an attached pi camera. 

# How

Via PiCamera, snap a picture. Generate a hash from resulting pic (sha256), upload file to GCP storage named after the hash. Call the Vision label API, return what it lists. 

# Future

Separate the steps into individual pieces to limit memory footprint of each piece and make them more granularly usable (ie, batch jobs, delayed labeling, etc). 

