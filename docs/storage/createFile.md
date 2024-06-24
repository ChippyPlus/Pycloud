# The storage/createFile Http Docs

Creates a file at the given `path` within the specified `bucket`

---------

## Http request format

----

### headers

| name          | type   | example  | description                                  |
|---------------|--------|----------|----------------------------------------------|
| Authorization | String | myAuthID | This is just for authenticating your request |

### body

| name | type   | example                      | description     |
|------|--------|------------------------------|-----------------|
| arg1 | String | "/data/logs/countedDogs.log" | the file path   |
| arg2 | String | "zoo_backend"                | the bucket name |

### example

request

```
Authorization: Bearer SuperSecrectKey!
{
    "arg1": "/data/logs/countedDogs.log" ,
    "arg2":  "zoo_backend"
}
```

response

```
201
```

---

## Http Errors

---

| status | trigger                                                     |
|--------|-------------------------------------------------------------|
| 200    | a successful operation                                      |
| 400    | a missing header or argument                                |
| 401    | a user being unauthorized                                   |
| 404    | if part of the path does not exist or bucket does not exist |