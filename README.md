# SecWatcher
A simple Raspberry Pi script that can be used for a basic security system. 

This code has no warranty, and I'm not responsible for what you do with it. Do not use unless you agree to hold me harmless. Feel free to copy/steal/etc.

You should read the code and modify it to fit your needs, but it defaults to use Raspberry PI pin 19 turning on to trigger the email. You'll need to modify the "sendEmail()" function with your email needs (email addresses, server names).

Here's the wiring diagram that I used: 

```
___________________
| Raspberry Pi     |
|pin #2 (+5V power)|------(fuse)-------(switch)------[LD33V]-----|  
|   pin #6 (ground)|------------------------------------^        | 
|   pin #19 (GPIO) |---------------------------------------------|
|                  |
|__________________|        
```

I used the 5v power with the LD33V 3.3v regulator to get more voltage for my long (~35 foot) run from my switch location to where I have the PI. (Check the wiring diagram for the LD33V; make sure Vout is going to the GPIO.) There are probably better ways to do this.

For example, a SPDT switch with the other pin grounding it out would have been better but I already ran two-pole bell wire from one side of my house and didn't want to go back and do it again for another wire.

Also, adding a small capcitor to debounce the switch (pin #6 to pin #19), and a protective resistor before pin #19 would probably be a good idea: https://hackaday.com/2015/12/09/embed-with-elliot-debounce-your-noisy-buttons-part-i/. The fuse may not be needed, but I was running this wire a long ways and didn't want to take any risks.

For a switch, you can use pretty much anything you want here; I'm using an momentary contact switch, but a magnetic switch or even a photosensor (more circuitry needed) would work too. You could even do something like rigging it up to your doorbell using a relay.

Please note, that the is expandable, you can have different GPIO pins do different things. I'm using the same Raspberry Pi board to control a relay, and listen for other switches flipping (for controlling lights).

Use this wisely; don't hurt yourself or anyone else.
