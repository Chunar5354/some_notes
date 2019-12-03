## Build-in bluetooth

Raspberry pi has a build-in blurtooth application `bluetoothctl`, type this command:
```
# sudo bluetoothctl
```
Then you will be in `bluetooth` command line, something like this:
```
[bluetooth] ...
```

And there are some commands you can use to operate bluetooth:
```
list                    // show available controllers
power on/off            // Set controller power
discoverable on/off     // Set controller discoverable mode
devices                 // show devices available to connect
pair [device_id]        // pair with the device
trust [device_id]       // Trust the device
connect [device_id]     // connect with the device
quit                    // quit bluetooth
```

You can using `devices` to find your phone and use `pair`+`trust`+`connect` to connect with your phone. 
There is a [reference](http://www.mamicode.com/info-detail-1887112.html)

But this appliction seems it can't deal with `data transmission`.

## hci something

I can use my phone bluetooth to connect with the `build-in bluetooth`, but I can't use a blurtooth-serial app to connect it.

There is a way to connect by an app.

- 1. Edit this file`/etc/systemd/system/dbus-org.bluez.service`, change this line:
```
ExecStart=/usr/lib/bluetooth/bluetoothd --compat
```

And under this line, type a new line:
```
ExecStartPost=/usr/bin/sdptool add Sp
```

Save and quit.

- 2. Restart bluetooth:
```
# sudo systemctl daemon-reload
# sudo systemctl restart bluetooth
```
Then change permissions on `/var/run/sdp`:
```
# sudo chmod 777 /var/run/sdp
```

- 3. Test

Now when you type the command:
```
# Sdptool browse local
```
you will see some information on the screen.

- 4. Pair

Type this to let other devices can find raspberry pi
```
# sudo hciconfig hci0 piscan
```

Then you can open your phone to get pair with raspiberry pi

If your phone can't find raspiberry pi, you can try this:
```
# bt-adapter --set Discoverable 1
```

- 5. Connect

Add pi to user group
```
# sudo usermod -G bluetooth -a pi
```

Then type this to get raspberry pi ready
```
# sudo rfcomm watch hci0
```

By this way, I can get my app connect with raspberrypi.
