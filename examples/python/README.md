## Flux Enterprise Object Python Client

This is the Flux Enterprise Object example Python client. This client retrieves 
information from the Enterprise Objects API and stores it into a local json file
to be consumed by other processes.

### To Set up the Client
Create a virtualenv:
```
$ python3 -m venv .venv
```
After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.
```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:
```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.
```
$ pip install -r requirements.txt
```

Retrieve Asset
```
$ python3 enterprise-object-client.py -c <client-id> -s <client-secret> -a <assetId>
```

Search Asset
```
$ python3 enterprise-object-client.py -c <client-id> -s <client-secret> -s <searchTerm>
```