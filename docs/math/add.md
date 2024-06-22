# The math/add Http Docs

Math/add takes 2 integers or floats and returns the addition of them.

---------

## Http request format

----

### headers

| name          | type   | example  | description                                  |
|---------------|--------|----------|----------------------------------------------|
| Authorization | String | myAuthID | This is just for authenticating your request |

### body

| name | type         | example | description                       |
|------|--------------|---------|-----------------------------------|
| arg1 | Int \| Float | 5       | The first number you want to add  |
| arg2 | Int \| Float | 10      | The second number you want to add |

### example

request

```
Authorization: SuperSecrectKey!
{
    "arg1": 5,
    "arg2":  10
}
```

response

```
{
    "answer":15
}
```

---

## Http Errors

---

| status | trigger                      |
|--------|------------------------------|
| 200    | a successful operation       |
| 400    | a missing header or argument |
| 401    | a user being unauthorized    |