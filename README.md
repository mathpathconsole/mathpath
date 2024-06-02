![new2starssign](https://github.com/mathpathconsole/mathpath/assets/116816908/086ff437-e29c-49d9-8ee3-ac6d05150923)

Welcome to **Stars of the sky, Mathpath: Math solver** application development information segment.

# What is the Mathpath: Math solver

*Mathpath: Math solver is an advanced mathematical solver application that running on Windows and Android platforms. The capability to solve problem are algebra to differential equations, vector fields. And 2D + 3D + Dataset graphs{column-line-dot} displays.* **And it does not need any internet connection to solve problems.** *Also Mathpath solver is widely open-source project to reach anyone and programming their own solver application.*

*Mathpath uses symbolic computing. (below sample image)*

![image](https://github.com/mathpathconsole/mathpath/assets/116816908/09b14406-cca3-4858-9abb-9afe8bf6be52)

*The mean is, really hard to entry on textbox to draw-hand mathematical problems. Therefore a simple way is creating* **"word functions"** *that representing current mathematical notations.* A sample: **diff(** *f(x), x* **)** represent **d/dx** of *f(x)* function. (look at below)

![diff_sample](https://github.com/mathpathconsole/mathpath/assets/116816908/08cb20fa-0005-45f4-aa16-87eb61a17433)

*You see on textbox typed* **x^2+y^2** *but* **[In]** *section converted these symbols automatically to math notation. this process takes ~0.3s.* *Anather sample in below, you see,* **[In] - [Out]** *sections converted quickly math notation and gived answer. (on [Out])*

![image](https://github.com/mathpathconsole/mathpath/assets/116816908/34ea759b-ae82-4250-a4ce-ca357d623f87)

![image](https://github.com/mathpathconsole/mathpath/assets/116816908/59676bba-06fc-444e-8837-ca284b306117)



# A brief story of Mathpath

When i was studying in Physics, I met powerful symbolic computation **Maple** *it was fascinated me. Then I decided to develop advanced mathematical solver running on Mobile to reach students free and do not use internet connection.* Then created little group to thrive them about **Python and scientific computing** *future. A few months on summer holiday passed like these. (But some friends gained more experience, not only mathematical solver)  After these holidays I focus more on mathpath solver. Then published demo version to some users (pictures below)*

![image](https://github.com/mathpathconsole/mathpath/assets/116816908/5becb137-2262-427e-8591-a58953c70aad)

Some structures like Vector fields algorithm(in below) re-written.
![image](https://github.com/mathpathconsole/mathpath/assets/116816908/08ff22be-6f5a-47d4-bac9-d5fb593366d3)

A simple structure to shrink equation font if **[In] and [Out]** labels stacked each of other.
![image](https://github.com/mathpathconsole/mathpath/assets/116816908/1a132ff0-96d9-42cc-b95e-641f90a761f1)

And another summer holiday (just focused holidays and free times) published first versions:
![image](https://github.com/mathpathconsole/mathpath/assets/116816908/8a876440-150b-4932-bf01-6c9b7678cbd1)




# Future of Mathpath
*Mathpath still under developing (by free times)*
1. AudioMath: Advanced mathematics with sound lost able to sight skill of people.

2. PhotoMath: Like Photomath

3. Geometry: Angles, Lines, geometric shapes...

**AudioMath** demo is running. Like, you say: **"derivative of x square plus five"** And answer gives as audio: **"two x** I hope anyone fork these and would publish own (*more powerful than Mathpath*) application on PlayStore and AppStore. But AI (like ChatGpt) increasing day to day probably handle these in the near future though :) 

# More help and videos

https://github.com/mathpathconsole/mathpath/assets/116816908/d835cb7a-bd6b-44ec-bd35-a13181a6a9f5

Now I share our sample code as GUI and Backend for if anyone working mathematics with Python-Kivy. I hope this helps developing more scientific tools on mobile and desktop platforms that using Python. 
1. **Look more info** https://mathpathconsole.github.io/ 
2. **Google Play Store** https://play.google.com/store/apps/details?id=org.mathconsole_lite.mathconsole_lite&pli=1
3. **Youtube** https://www.youtube.com/@mathpathsolver/shorts

https://github.com/mathpathconsole/mathpath/assets/116816908/6b6314fc-74d1-4243-9344-a11722e6715d

Mathpath uses 3 important Python libraries.
1. SymPy
2. Matplotlib
3. Kivy and KivyMD

SymPy and Matplotlib for mathematical drivers. Powerful Gui libraries are Kivy and KivyMD for screen design. 

https://github.com/mathpathconsole/mathpath/assets/116816908/3ae7f065-4c06-4728-b3a6-dc999e181782

https://github.com/mathpathconsole/mathpath/assets/116816908/7b8b9ec5-a371-4c68-a37d-e5e2c914dbf1

Look file content for mathpath sample design and mathematical backend.

https://github.com/mathpathconsole/mathpath/assets/116816908/61009bc8-7dc5-4c52-9c07-be32556f19dc


# ADVICE and SOLUTION OF ERRORS
Probably you will take some errors. These errors mostly during compile to .apk or .aab file on buildozer. *Also do not hesitate to send us message if you aim to develop scientific tools or get some errors in during this process.*

## Buildozer.spec
Open your Buildozer.spec file and find "below pieces" in it. Ooops. If you ask me what is Buildozer, please search on your browser and look "kivy buildozer" or send message **Google Groups Kivy users support**  Here is: https://groups.google.com/g/kivy-users  **By the way** you can always ask Kivy support group, they help you, I'm sure. 

### Edit your buildozer.spec like:
> *# (list) Source files to include (let empty to include all the files)*
*source.include_exts = py,png,jpg,kv,atlas,**ttf** |||**ttf** **or otf**

> #(list) Application requirements*
> #comma separated e.g. requirements = sqlite3,kivy*
> requirements = python3,kivy==2.1.0, **kivymd==1.1.1, pillow, sympy, matplotlib**

## 1st error: mpmath error!
Solution is here: https://stackoverflow.com/a/64597102/18110933
Go your current Python file and search 'mpmath' then copy this file and paste (represented file in stackoverflow) in .buildozer

## 2nd Advice: SymPy file
Normally when you compile with current requirements(at over) sympy default version not enough to making mathematics! you got some errors when open your apk file.
you want to try in buildozer.spec requirements sympy==1.10.1 but sometimes this doesn't work. You try manually copy sympy file in computer python files to .buildozer 
> like 1st error: mpmath errror! Just your sympy file in computer copy then past your compile apk work: **.buildozer/android/platform/build-armeabi-v7a/dists/<your named file>/_python_bundle__armeabi-v7a/_python_bundle/site-packages/sympy** ->change this sympy file in your computer sympy file version 1.10.1 or more!

> look this path: **/build-armeabi-v7a/** this path might be **/build-arm64-v8a/** or different.

> then again run **'buildozer android debug deploy run'** in shell. You'll see your apk size increase after added sympy file.

## 3rd Advice: monospace font
if you want to display pretty mathematical symbols, you have to use 'mono space font' find mathematical monospace font then put in current file your .py file location. (I shared an example about it) look **example.py and menu_screen.kv** file.

That's all. If you want more help these steps you don't hesitate to contact us, we love math and developing scientific tools within Open source.
**#Reşat Berk, StarsoftheSky**
