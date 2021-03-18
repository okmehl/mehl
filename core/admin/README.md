Mehl Admin container
====================

![admin-docker](https://github.com/okmehl/mehl/workflows/admin-docker/badge.svg)

This is the web-based administrative interface for the Mehl containerized
mail server.


Development
-----------

1. Install prerequisites: `apt install python3-dev default-libmysqlclient-dev libpq-dev`
2. Create virtual environment: `python3 -m venv .venv`
3. Activate environment: `source .venv/bin/activate`
4. Install requirements: `pip3 install -r requirements.txt`
5. Create launch configuration for python and start start.py
6. Install frontend: `npm i`
7. Run webpack: `npm run dev`
8. Create symbolic link for static folder: `ln -s mailu/static static`
9. Open browser with `localhost`


Multi-Arch build on Ubuntu amd64
--------------------------------

```bash
docker run --privileged --rm tonistiigi/binfmt --install all
docker buildx build --platform linux/arm/v7 -t admin:multi --load .
```

Resources
---------

 * [Report issues](https://github.com/Mailu/Mailu/issues) and
    [send Pull Requests](https://github.com/Mailu/Mailu/pulls)
    in the [main Mailu repository](https://github.com/Mailu/Mailu)
