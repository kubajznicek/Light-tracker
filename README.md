# Light tracker



***Why would I use it?***

You’ll get an ability to draw by hand without mouse. You just need to
hold any LED light in front of your webcam.

***Are there any other features?***

Yes, besides tracking light, you can:

* Choose from many colours in menu.

* Select the the thickness you’d like.

* Erase stuff that you no longer want.

* Save your masterpiece in .JPG

***What’s going on?***

It’s a program, that is able to track the whitest colour in focused
area.

>You will need an LED light, see below.

**Instalation**

> Note for windows users: It is python, it should work but I haven’t tested it.

**Linux:**

1. open Console and write
```bash
git clone https://github.com/kubajznicek/kresleni.git
```

2.  Navigate yourself to the folder using CD comand.

```
cd kresleni
```
3. Create and activate python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```
4. Install required modules

```bash
pip install opencv-python
```

5. To run the program type 
```bash
python3 camera.py
```

***Usage***

hotkeys

- [ b ] blue
- [ r ] red
- [ g ] green
- [ w ] white
- [ c ] clear screen
- [ e ] eraser
- [ s ] save
- [ 1 ] thickness 1
- [ 2 ] thickness 2
- [ 3 ] thickness 3

Note: numbers don't work on numpad.

***Camera resolution***

Depending on what camera you have and what resolution it supports you can change it in the program. Open _camera.py_ and look for this code .
```python
resolution_x = 1280
resolution_y = 720
```
> Recommended frame rate it at least 15 fps.

***Troubleshooting***

For correct light detection **camera shutter** needs to be set to low value and **auto exposure** must be turn off. Program does that but in case it didn't work you can set the values manualy using similar commands like this:
```bash
v4l2-ctl -d /dev/video0 --set-ctrl=exposure_auto=1
v4l2-ctl -d /dev/video0 --set-ctrl=exposure_absolute=250
```

If it is not detecting your LED make sure that you are in a room with no **direct light**. Soft light is much better.

***Hardware***

Any basic LED light should work fine. For better funcionality you can optionally wrap protruding LED by a small paper cylinder.

![simple LED light](https://zlepsovak.cz/1-large_default/led-klicenka-cerna.jpg "simple LED light")


***Feedback***

If you spot any bug or have an idea for improvment, please, crate github issue.