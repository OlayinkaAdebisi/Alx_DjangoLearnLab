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