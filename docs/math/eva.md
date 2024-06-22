# The math/eva Http Docs

Math/eva takes 1 string and returns an evaluation of the string from `arg1` in a mathematical context.
Representation: eval(arg1)
---------

## Http request format

----

### headers

| name          | type   | example  | description                                  |
|---------------|--------|----------|----------------------------------------------|
| Authorization | String | myAuthID | This is just for authenticating your request |

### body

| name | type   | example               | description            |
|------|--------|-----------------------|------------------------|
| arg1 | String | "10 * 5 - 30 / 3 + 5" | The string to evaluate |

### example

request

```
Authorization: Bearer SuperSecrectKey!
{
    "arg1": "10 * 5 - 30 / 3 + 5",
}
```

response

```
{
    "message": 45
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