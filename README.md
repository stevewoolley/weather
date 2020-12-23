# weather
A Single Page Application for displaying the current weather in a selected city. 
The weather information is provided by [Open Weather Map](http://openweathermap.org) and their wonderful API.

### Architecture
AWS API Gateway referencing an AWS Lambda. 
The AWS Lambda calls out to the Open Weather API and retrieves info based on location specified on the url query parameter (location).

### Query Parameters
- *location* - The city to retrieve weather. Best results it in format city,state, country
- *scale* - Specifies temperature scale (K for Kelvin, C for Celsius, and F for Fahrenheit). 
  If not specified, will default to Fahrenheit.
- *wind_scale* - The speed scale of the wind (ms for meters/sec, mph for miles per hour).
Defaults to mph.

### Examples
#### Weather for Tulsa,OK
http://snerted.com.s3-website-us-east-1.amazonaws.com/?location=Tulsa,OK,US
#### Weather for Apex,NC in Celcius
http://snerted.com.s3-website-us-east-1.amazonaws.com/?location=Apex,NC,US&scale=C
#### Weather for Orlando,FL with wind in meters/sec
http://snerted.com.s3-website-us-east-1.amazonaws.com/?location=Orlando,FL,US&speed_scale=ms

