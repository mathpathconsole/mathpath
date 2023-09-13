![new2starssign](https://github.com/mathpathconsole/mathpath/assets/116816908/086ff437-e29c-49d9-8ee3-ac6d05150923)

Welcome to **Stars of the sky, Mathpath: Math solver** application development information segment.


https://github.com/mathpathconsole/mathpath/assets/116816908/d835cb7a-bd6b-44ec-bd35-a13181a6a9f5

Now I share our sample code as GUI and Backend for if anyone working mathematics with Python-Kivy. I hope this helps developing more scientific tools on mobile and desktop platforms that using Python. When I was studying physics at the college, getting symbolic calculating lesson with Maple software, **it was fascinated me.** 
That the time, I knew Python language as basic. In a while later my scientific computing feelings was soar. I wanted to any student use advanced application (algebra to differential equation) to solve their problems with free and without internet connection. Then I created little group (some still testing or giving feedback) to inspire "thrive spirit"... **Look more info** https://mathpathconsole.github.io/ and on **Google Play Store** https://play.google.com/store/apps/details?id=org.mathconsole_lite.mathconsole_lite&pli=1 

https://github.com/mathpathconsole/mathpath/assets/116816908/6b6314fc-74d1-4243-9344-a11722e6715d

Mathpath uses 3 important Python libraries.

  1- SymPy
  
  2- Matplotlib
  
  3- Kivy and KivyMD

SymPy and Matplotlib for mathematical drivers. Powerful Gui libraries Kivy and KivyMD for screen design. Here is there are sample code each of them in here.

[SymPy source] https://docs.sympy.org/latest/index.html 

[Matplotlib source] https://matplotlib.org/stable/

[Kivy source] https://kivy.org/doc/stable/

[KivyMD source] https://kivymd.readthedocs.io/en/1.1.1/

https://github.com/mathpathconsole/mathpath/assets/116816908/3ae7f065-4c06-4728-b3a6-dc999e181782

https://github.com/mathpathconsole/mathpath/assets/116816908/7b8b9ec5-a371-4c68-a37d-e5e2c914dbf1

Look file content for mathpath sample design and mathematical backend.

https://github.com/mathpathconsole/mathpath/assets/116816908/61009bc8-7dc5-4c52-9c07-be32556f19dc


**ADVICE and SOLUTION OF ERRORS**
Probably you will take some errors. These errors mostly during compile to .apk or .aab file on buildozer

**Buildozer.spec**

**Edit your buildozer.spec like:**
*# (list) Source files to include (let empty to include all the files)*
*source.include_exts = py,png,jpg,kv,atlas,ttf*
---add ttf or otf---

*# (list) Application requirements*
*# comma separated e.g. requirements = sqlite3,kivy*
*requirements = python3,kivy==2.1.0, kivymd==1.1.1, pillow, sympy, matplotlib*
---add requirements like this---

**1st error: mpmath error!**
Solution is here: https://stackoverflow.com/a/64597102/18110933
Go your current Python file and search 'mpmath' then copy this file and paste (represented file in stackoverflow) in .buildozer

**2nd Advice: SymPy file**
Normally when you compile with current requirements(at over) sympy default version not enough to making mathematics! you got some errors when open your apk file.
you want to try in buildozer.spec requirements sympy==1.10.1 but sometimes this doesn't work. You try manually copy sympy file in computer python files to .buildozer 
like __1st error: mpmath errror!__. just your sympy file in computer copy then past your compile apk work: **.buildozer/android/platform/build-armeabi-v7a/dists/<your named file>/_python_bundle__armeabi-v7a/_python_bundle/site-packages/sympy** ->change this sympy file in your computer sympy file version 1.10.1 or more!

[*]look this path: **/build-armeabi-v7a/** this path might be **/build-arm64-v8a/** or different.

then again run **'buildozer android debug deploy run'** in shell. You'll see your apk size increase after added sympy file.

**3rd Advice: monospace font**
if you want to display pretty mathematical symbols, you have to use 'mono space font' find mathematical monospace font then put in current file your .py file location. (I shared an example about it) look example.py and menu_screen.kv file.

That's all. If you want more help these steps you don't hesitate to contact us, we love math and developing scientific tools within Open source.
**#Reşat Berk, StarsoftheSky**
