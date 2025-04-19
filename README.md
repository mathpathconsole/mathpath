![new2starssign](https://github.com/mathpathconsole/mathpath/assets/116816908/086ff437-e29c-49d9-8ee3-ac6d05150923)

---

<p align="center">
  <a href="https://mathpathconsole.github.io/" target="_blank" style="margin-right: 40px;">
    <img src="https://icons.iconarchive.com/icons/alecive/flatwoken/256/Apps-Libreoffice-Math-B-icon.png" alt="Website" width="60" height="60">
  </a>
  <a href="https://www.youtube.com/@mathpathsolver/shorts" target="_blank" style="margin-right: 40px;">
    <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" alt="YouTube" width="60" height="60">
  </a>
  <a href="https://play.google.com/store/apps/details?id=org.mathconsole_lite.mathconsole_lite&gl=TR" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/888/888857.png" alt="Google Play" width="60" height="60">
  </a>
</p>

## Table of Contents
1. [What is Mathpath Solver](#1-what-is-mathpath-solver)
2. [A brief story of Mathpath](#2-a-brief-story-of-mathpath)
3. [Future of Mathpath](#3-future-of-mathpath)
4. [Advice and Solutions](#4-advice-and-solutions)

## 1. What is Mathpath Solver

*Mathpath: Math solver is an advanced mathematical solver application that running on Windows and Android platforms. The capability to solve problem are algebra to differential equations, vector fields. And 2D + 3D + Dataset graphs{column-line-dot} displays.* **And it does not need any internet connection to solve problems.** *Also Mathpath solver is full open-source project to reach anyone and programming their own solver application.*

*Mathpath uses symbolic computing. (below sample image)*

![image](https://github.com/mathpathconsole/mathpath/assets/116816908/09b14406-cca3-4858-9abb-9afe8bf6be52)

*The mean is, really hard to entry on textbox to draw-hand mathematical problems. Therefore a simple way is creating* **"word functions"** *that representing current mathematical notations.* A sample: **diff(** *f(x), x* **)** represent **d/dx** of *f(x)* function. (look at below)

![image](https://github.com/user-attachments/assets/0caa779c-767c-4926-8229-08e4a01698f9)


*You see on textbox typed* **x^2+y^2** *but* **[In]** *section converted these symbols automatically to math notation. this process takes ~0.3s.* *Anather sample in below, you see,* **[In] - [Out]** *sections converted quickly math notation and gived answer. (on [Out])*

![image](https://github.com/user-attachments/assets/b3cda630-09fb-45d5-ac82-9e22a785aefa)

Mathpath uses 3 important Python libraries.
1. SymPy
2. Matplotlib
3. Kivy and KivyMD

SymPy and Matplotlib for mathematical drivers. Powerful Gui libraries are Kivy and KivyMD for screen design.

Dependencies:
```pip-requirements
kivymd==1.1.1
kivy==2.1.0
sympy==1.10.1
matplotlib==3.5.2
```
> [!NOTE]
> These all dependencies are not for mobile, please look at below`4.2 Edit your buildozer.spec`. Also these dependencies versions you had might different from us but generally it's ok, still mathpath solver will work well.

---

## 2. A brief story of Mathpath

When i was studying in Physics, I met powerful symbolic computation **Maple** *it was fascinated me. Then I decided to develop advanced mathematical solver running on Mobile to reach students free and do not use internet connection.* Then created little group to thrive them about **Python and scientific computing** *future. A few months on summer holiday passed like these. (But some friends gained more experience, not only mathematical solver)  After these holidays I focus more on mathpath solver. Then published demo version to some users (pictures below)*

![image](https://github.com/mathpathconsole/mathpath/assets/116816908/5becb137-2262-427e-8591-a58953c70aad)

Some structures like Vector fields algorithm(in below) re-written.
![image](https://github.com/mathpathconsole/mathpath/assets/116816908/08ff22be-6f5a-47d4-bac9-d5fb593366d3)

A simple structure to shrink equation font if **[In] and [Out]** labels stacked each of other.
![image](https://github.com/mathpathconsole/mathpath/assets/116816908/1a132ff0-96d9-42cc-b95e-641f90a761f1)

And another summer holiday (just focused holidays and free times) published first versions:
![image](https://github.com/mathpathconsole/mathpath/assets/116816908/8a876440-150b-4932-bf01-6c9b7678cbd1)

---

## 3. Future of Mathpath
*Mathpath still under developing (by free times)*
1. AudioMath: Advanced mathematics with sound lost able to sight skill of people.

2. PhotoMath: Like Photomath

3. Geometry: Angles, Lines, geometric shapes...

**AudioMath** demo is running. Like, you say: **"derivative of x square plus five"** And answer gives as audio: **"two x** I hope anyone fork these and would publish own (*more powerful than Mathpath*) application on PlayStore and AppStore. But AI (like ChatGpt) increasing day to day probably handle these in the near future though :) 

---

## 4. Advice and Solutions
Probably you will take some errors. These errors mostly during compile to .apk or .aab file on buildozer. *Also do not hesitate to send us message if you aim to develop scientific tools or get some errors in during this process.*

### 4.1 Kivy Google Groups
Here is: https://groups.google.com/g/kivy-users  
You can always ask to Kivy support group, they will help you, I'm sure. 

### 4.2 Edit your buildozer.spec:
```pip-requirements
source.include_exts = py,png,jpg,kv,atlas,ttf
```
> [!NOTE]
> `.ttf` is monospaced font type. It might be `.otf`

```pip-requirements 
requirements = python3,kivy==2.1.0, kivymd==1.1.1, pillow, sympy, matplotlib
```

### 4.3 mpmath error!
Solution is here: https://stackoverflow.com/a/64597102/18110933
Go your current Python file (on computer) and search `mpmath` then copy this file and paste (represented file in stackoverflow) in `.buildozer`

### 4.4 SymPy file
Normally when you compile with current requirements(above) sympy default version not enough to making all mathematics structures! You got some errors when open your apk file.
you want to try in `buildozer.spec` requirements `sympy==1.10.1` but sometimes this doesn't work. You try manually copy sympy file in computer python files to `.buildozer`

> Just your sympy file in computer copy then past your compile apk work (like mpmath errror):

```.buildozer/android/platform/build-armeabi-v7a/dists/<your named file>/_python_bundle__armeabi-v7a/_python_bundle/site-packages/sympy``` change this `sympy` file in your computer with sympy file version `1.10.1` or more!
> [!NOTE]
> look this path: `/build-armeabi-v7a/` this path might be `/build-arm64-v8a/` or different.

then again run `buildozer android debug deploy run` in shell. You'll see your apk size increase after added sympy file.

## 4.5 monospace font
if you want to display pretty mathematical symbols, you have to use 'mono space font'. Find mathematical monospace font then put in current folder where your `.py` file location. (I shared, `Mathpath solver/dejavusansmono.ttf`)

That's all. If you want more help these steps you don't hesitate to contact us, we love math and developing scientific tools within Open source.
**#Reşat Berk, StarsoftheSky**
