# Python-tools
Useful tools implemented with Python in 200 lines or less.

### [中文版本](./README_cn.md)

This repository is a collection of various Python scripts I've written since I began to use Python in 2018. You can use these tools to improve efficiency, or, you can use them as small projects to practice Python :)

These tools are very lightweight. Each has only one single Python file with around **100 lines** of code and very few third-party libraries. The tools are made for various purposes, such as build a **free ip pool** for crawlers:globe_with_meridians:, **increase page views**:eyeglasses:, **record the computer screen**:movie_camera:, **monitor net speed**:satellite:, **hide files**:books:, **sync files**:file_folder: and so on. Hope you can find something you like.:heart:

Welcome to contribute!

(PS: *The usage of each tool is explained in their .py file*)

### Screen Recorder:movie_camera: -- [simple-screen-recorder](simple_screen_recorder.py)

> Record the computer screen using python and ffmpeg. (Graphical User Interface)

Functions：

- Self-define save path. Self-define **frame** and **resolution**.
- Automatically save settings, and load the previous settings when opened the next time.
- A 3-second hint before recording.
- Press F10 to stop recording.

<div align="center">
<img src="_v_images/20191220185122289_8134.png" width="390px">
</div>

（[Click here to download](https://github.com/wolverinn/Python-tools/releases/tag/v1.0) executable）

### Build your own free ip pool:globe_with_meridians: -- [free-ip-pool](free_ip_pool.py)

> Self-made ip pool stored in SQLite3, crawling free proxies from websites that offer them.

Functions：

- Crawls ip from 3 websites that offer free high-anomonous ip and stores them in SQLite3.
- Validate the ip and delete invalid ip.

### Monitor computer net speed:satellite: -- [simple-net-speed-monitor](net_speed_monitor.pyw)

> A simple net speed monitor using python3 tkinter library. (Graphical User Interface)

A simple net speed monitor that shows the upload and download speed of a computer in real time.

<div align="center">
<img src="_v_images/20191220203803479_15260.png" width="360px">
</div>

Right-click menu functions:

- Adjust position (and auto-save the setting)
- Adjust transparency (auto-save)
- Re-start monitoring

<div align="center">
<img src="_v_images/20191220204054677_12422.png" width="360px">
</div>

（[Click here to download](https://github.com/wolverinn/Python-tools/releases/tag/v1.1) executable）

### Increase page views:eyeglasses:

Input an URL, the script will view this page continuously to increase page views. Implemented with selenium. Can be used to increase the views of blogs.

- Increase views by page views：[power-views](power_views.py)

    Implemented by using incognito mode to view the webpage.

- Increase views by unique users：[ip-pool-browse](ip_pool_browse.py)

    Implemented with ip pool.

### File sync:file_folder: -- [portable-sync](portable_sync.py)

> A tool to sync the files in the computer to the portable devices, including auto-update and deletion.

This is a handy synchronization tool that can automatically synchronize folders on your computer to a portable device (U disk / mobile hard disk ...). You can customize the folders you want to sync (you can choose multiple), the suffixes of files that you don't want to synchronize will be automatically blocked, and you can choose what to do when the files are updated or deleted.

Personally, I think it's a fragile way to sync your files on clouds and a more reliable way is to sync files to portable devices. However, when copying files on Windows, first, it won't check whether the file has been changed. It either skips or overwrites. Besides, it can't delete files when you copy, which is far from the demands of synchronization. So I wrote this simple Python tool.

<div align="center">
<img src="_v_images/20191220204416988_4614.jpg" width="700px">
</div>

### Simple tool to hide files:books: -- [hide-file](hide_file.py)

Hide files/folders in Windows (haven't tried Linux). Protect files in a simple way.

When hidden, others won't be able to see the files/folders in explorer, and won't see it using ```ls``` command either, which is enough for normal needs.

<div align="center">
<img src="_v_images/20191220191832613_15118.png" width="390px">
</div>

### Edit "send to" menu -- [send-to-editor](send_to_editor.py)

Delete content in "send to" menu. Add a path or an application to send-to.

<div align="center">
<img src="_v_images/20191220193145179_20665.png" width="390px">
</div>

### Get all Windows Focus images on your computer with one click -- [windows-focus](windows_focus.py)

Windows focus images are beautiful and are updated frequently on your computer. However, saving them is a hassle:

- The picture storage path is too complicated, you must write it down in Notepad, copy and paste it when you use it;
- After entering the image storage path, you will find that all files have no suffix, you must manually add the ``` .jpg ``` suffix to view the image;
- After making it to a picture format, you will find that many pictures are actually only a part of a complete picture, such as size ```488x216```. it will take a long time to find the one you really want.

This small tool can scan the path directly, remove those incomplete pictures, and save other pictures to the current directory. It's very trouble-free.

### zhihu video downloader:beginner: -- [zhihu-video-downloader](zhihu_video_downloader.py)

> Download videos from zhihu.com using python3 and ffmpeg. (Graphical User Interface)

<div align="center">
<img src="_v_images/20191220190307589_28533.png" width="390px">
</div>

（[Click here to download](https://github.com/wolverinn/Python-tools/releases/tag/v1.0) executable.）

### Crawls zhihu answers and generate wordcloud:book: -- [zhihu-answer-wordcloud](zhihu_answer_wordcloud.py)

### Save a web page to markdown -- [web2md](web2md.py)

Calls a third-party library, and saves the web page as markdown, which is suitable for relatively simple web pages, such as some articles.  Complicated webpages cannot guarantee the typesetting of the saved markdown. The advantage of saving a web page as markdown instead of PDF is that it is small and easier to modify。

### Run any py -- [run_any_py](run_any_py.py)

Useful when there're a lot of Python files in a directory. You can simply input a number to run a Python script and you can do it over and over again. It's a lot easier than inputting ```python3 XXX.py```

### Get an English name -- [ename](ename.py)

Generate an English name based on Chinese name and gender. Using the API provided by shanbay.

### Get random UserAgent -- [random-userAgents](random_userAgents.py)

Get a random User Agent, useful for web crawling.

*Inspired by [GitHub - geekcomputers/Python: My Python Examples](https://github.com/geekcomputers/Python)*
