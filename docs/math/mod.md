# The math/mod Http Docs

Math/mod takes 2 integers or floats and returns the modulo remainder of `arg1` divided by `arg2`.
Representation: 10 % 4
---------

## Http request format

----

### headers

| name          | type   | example  | description                                  |
|---------------|--------|----------|----------------------------------------------|
| Authorization | String | myAuthID | This is just for authenticating your request |

### body

| name | type         | example | description   |
|------|--------------|---------|---------------|
| arg1 | Int \| Float | 10      | The  dividend |
| arg2 | Int \| Float | 4       | The dividend  |

### example

request

```
Authorization: Bearer SuperSecrectKey!
{
    "arg1": 10,
    "arg2":  4
}
```

response

```
{
    "message": 2
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