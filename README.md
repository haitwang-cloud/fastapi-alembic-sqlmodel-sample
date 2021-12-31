# fastapi-app-sample

Make an out-of-the-box backend based on FastAPI

```bash
FastAPI + MySQL + Requests+ alembic + SQLmodel + aiohttp + sqlalchemy
```

### Project screen shoot
![](./sample.gif)

### Project API doc

```bash
http://0.0.0.0:8000
```

## Database

Offical
docs: [https://alembic.sqlalchemy.org/en/latest/tutorial.html](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

### Init

```bash
alembic init alembic
```

### Editing the alembic.ini File

```bash
 Please edit configuration/connection/logging settings in './fastapi-app-sample/alembic.ini' before proceeding
```

### Create a Migration Script

```bash
alembic revision -m "create account table"
Generating /path/to/yourproject/alembic/versions/1975ea83b712_create_accoun
t_table.py...done
```

## Docker

### how to build images

```bash
sh docker/build.sh
```

## how to run

```bash
sh docker/run.sh
```

## References

- [https://fastapi.tiangolo.com/tutorial/](https://fastapi.tiangolo.com/tutorial/)
- [https://sqlmodel.tiangolo.com/](https://sqlmodel.tiangolo.com/)
- [https://docs.aiohttp.org/en/stable/](https://docs.aiohttp.org/en/stable/)
- [https://github.com/Delgan/loguru](https://github.com/Delgan/loguru)
- [https://docs.python-requests.org/en/master/](https://docs.python-requests.org/en/master/)
- [https://docs.sqlalchemy.org/en/14/](https://docs.sqlalchemy.org/en/14/)
- [https://github.com/alembic/alembic](https://github.com/alembic/alembic)