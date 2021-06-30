# White Bear Finder

### API server

post request to /api/

request:

```
{
    "src": "{image bytes}",
    "width": {image width, number}, 
    "height": {image height, number}
}
```
response:
```
{
    "src": "{image bytes}",
    "width": {image width, number}, 
    "height": {image height, number}
}
```
return clean JSON if error has occurred
