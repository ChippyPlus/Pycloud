# The storage/createBucket Http Docs

Creates bucket with the name of `bucket`

---------

## Http request format

----

### headers

| name          | type   | example  | description                                  |
|---------------|--------|----------|----------------------------------------------|
| Authorization | String | myAuthID | This is just for authenticating your request |

### body

| name | type   | example       | description            |
|------|--------|---------------|------------------------|
| arg1 | String | "zoo_backend" | The name of the bucket |

### example

request

```
Authorization: Bearer SuperSecrectKey!
{
    "arg1":  "zoo_backend"
}
```

response

```
201
```

---

## Http Errors

---

| status | trigger                      |
|--------|------------------------------|
| 200    | a successful operation       |
| 400    | a missing header or argument |
| 401    | a user being unauthorized    |