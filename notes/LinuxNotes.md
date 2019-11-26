Some knowledge about linux

## Commands

- Check if the `port` has already been used
```
# netstat -anp | grep port_number
```

## Web server

### Change index page

If you want to change the default index page, you can change the `/var/www/html/index.html` file like:
```html
<meta http-equiv="refresh" content="0; url=/web">
```

After `url` is the path of your own website.

You can also visit [this link](https://blog.csdn.net/LEE18254290736/article/details/51901725) for more information.
