# The math/mul Http Docs

Math/mul takes 2 integers or floats and returns the product of them.
Representation: arg1 * arg2
---------

## Http request format

----

### headers

| name          | type   | example  | description                                  |
|---------------|--------|----------|----------------------------------------------|
| Authorization | String | myAuthID | This is just for authenticating your request |

### body

| name | type         | example | description      |
|------|--------------|---------|------------------|
| arg1 | Int \| Float | 5       | The multiplier   |
| arg2 | Int \| Float | 10      | The multiplicand |

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
    "message": 50
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