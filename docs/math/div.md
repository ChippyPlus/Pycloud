# The math/div Http Docs

Math/div takes 2 integers or floats and returns `arg1` divided by `arg2`.  
Representation: arg1 / arg2

---------

## Http request format

----

### headers

| name          | type   | example  | description                                  |
|---------------|--------|----------|----------------------------------------------|
| Authorization | String | myAuthID | This is just for authenticating your request |

### body

| name | type         | example | description  |
|------|--------------|---------|--------------|
| arg1 | Int \| Float | 10      | The dividend |
| arg2 | Int \| Float | 5       | The dividend |

### example

request

```
Authorization: Bearer SuperSecrectKey!
{
    "arg1": 10,
    "arg2":  5
}
```

response

```
{
    "message":2
}
200
```

---

## Http Errors

---

| status | trigger                      |
|--------|------------------------------|
| 200    | a successful operation       |
| 400    | a missing header or argument |
| 401    | a user being unauthorized    |