# The math/pow Http Docs

Math/pow takes 2 integers or floats and returns `arg1` to the power of `arg2`.
Representation: arg1^arg2
---------

## Http request format

----

### headers

| name          | type   | example  | description                                  |
|---------------|--------|----------|----------------------------------------------|
| Authorization | String | myAuthID | This is just for authenticating your request |

### body

| name | type         | example | description               |
|------|--------------|---------|---------------------------|
| arg1 | Int \| Float | 5       | This will be the base Int |
| arg2 | Int \| Float | 10      | This will be the exponent |

### example

request

```
Authorization: Bearer SuperSecrectKey!
{
    "arg1": 5,
    "arg2":  10
}
```

response

```
{
    "message":9765625
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