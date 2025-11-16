# Quick Guide on Post Permissions
In this app we got some custom permisions like can_view, can_create, can_edit and can_delete.  
Django creates them automaticly wen you run makemigraitons and migrate.  
To give a user or group access, just go to the admin panel and add the permisions.  
You can also do it in code using Permission.objects.get(codename="can_edit") but dont forget to import.  
If a user dont have can_create, they cant add new posts, simple as that.  
For templates, check with {% if perms.appname.can_edit %} so the edit button will show.  
Inside views, you can use @permission_required("appname.can_view") to prevent unapproved users.  
Sometimes restart the surver after adding new groups, Django can act weird.  
The permisions just control who can do what, its pretty simple.  
That’s basically it, follow these steps and everything should work fine.  

# Force all HTTP traffic to HTTPS
# Ensures encrypted communication between client and server
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
# Tells browsers to only use HTTPS for 1 year
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply to all subdomains
SECURE_HSTS_PRELOAD = True             # Allow browser preload lists

# Cookies should only be sent over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Prevent clickjacking by denying iframe embedding
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-sniffing responses
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser XSS filter
SECURE_BROWSER_XSS_FILTER = True

SSL/TLS Certificate:
 Provider: Let's Encrypt (free) or purchased SSL certificate
Certificate paths configured in Nginx/Apache