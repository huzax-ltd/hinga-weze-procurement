## Instalation ##

```bash
[sudo] apt-get install stunnel
```

## Configuration ##

```bash
cd path/to/django/project
mkdir stunnel
cd stunnel
```

Create the key:

```bash
openssl genrsa 1024 > stunnel.key
openssl req -new -x509 -nodes -sha1 -days 365 -key stunnel.key > stunnel.cert
cat stunnel.key stunnel.cert > stunnel.pem
```

Create the `dev_https` file with:

```bash
pid=

cert = stunnel/stunnel.pem
sslVersion = SSLv3
foreground = yes
output = stunnel.log

[https]
accept=8443
connect=8001
TIMEOUTclose=1
```

Now go to project root and create a `runserver` file:

```bash
stunnel4 stunnel/dev_https &
python manage.py runserver&
```

Sets the permission:

```bash
chmod a+x runserver
```

The SSL works in:


```
https://localhost:8443 
```

##### REF #####

http://stackoverflow.com/questions/8023126/how-can-i-test-https-connections-with-django-as-easily-as-i-can-non-https-connec