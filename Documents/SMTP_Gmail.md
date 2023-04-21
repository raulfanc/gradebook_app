1. create a google account for test purpose
2. go to `google account`, then `Security`, turn on `2-step Verification`
3. and create a **APP Password** (google changed the policy to use this you have to enable `2-step Verification`)
4. Generate a `APP password` copy and paste
5. then go to `settings.py`, 
```python
# Email backend with Gmail SMTP  
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587  
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')  
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  
EMAIL_USE_TLS = True
```
6. use [.env](/Enviroment_Variables) to store confidentials (this file need to add into `.gitignore`)
```
EMAIL_HOST_USER=<the test email address> 
EMAIL_HOST_PASSWORD=<the generated APP password>
```
used this previously when setting up with PostgreSQL's confidentials.
