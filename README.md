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