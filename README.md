# White Bear Finder

### API server

post request to /api/

get:

```
{
    "src": "{image bytes in base64}"
}
```
return:
```
{
    "count": {count bears, number},
    "data": "{image bytes in base64 (new image)}"
}
```
> return clean JSON if error has occurred
