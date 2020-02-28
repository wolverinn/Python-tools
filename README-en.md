# Python-tools
Useful tools implemented with Python in 200 lines or less.

这个 repository 收集了我从 2018 年开始用 Python 以来，写的一些小工具，涵盖了爬虫、系统操作等方面。你可以使用这些工具来解决一些问题，提高生产效率；或者，也可以将它们作为小项目练习 Python 这门语言~

我编写的这些工具都比较轻量级，只有一个 Python 文件，**100行**左右的代码，并且只调用了很少的第三方库或者只需要内置库就OK。这些工具涉及到的方面很多，包括建立爬虫的**免费IP池**:globe_with_meridians:，**刷网页浏览量**:eyeglasses:，**爬取知乎答案**:book:，**下载知乎视频**:beginner:；**屏幕录制**:movie_camera:，**网速监测**:satellite:工具，**文件隐藏**:books:，文件**同步工具**:file_folder:等等。希望你能从中找到自己喜欢的:heart:

如果你有新的想法，或者对代码的优化，欢迎提 issues 或者 pull request ！

(PS: *每个工具的用法都写在了对应的.py文件中，部分工具我生成了exe文件可以直接运行*)

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

这是一个小巧的同步工具，可以自动将电脑上的文件夹同步到移动设备（U盘/移动硬盘...）上。可以自定义想要同步的文件夹（可以选多个），对不想同步的文件后缀会自动屏蔽，还可以选择当文件发生更新或删除时如何处理。

之所以写这样一个同步工具，是因为个人觉得将东西同步在云盘上其实是一个很脆弱的做法，就算是自己搭建的云盘，也说不准就崩了，觉得最稳妥的还是同步到自己的移动硬盘或者U盘。然后试了试，发现Windows复制文件夹的时候，首先不会检测文件是否有变化，要么跳过，要么选择替换，效率很低，而且多余的文件不会删除，相当于是合并，这显然和同步的要求相去甚远，所以只好自己写一个简单的同步的 Python 工具。既可以方便快速地访问，又保证了一定的个人信息安全。

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

Windows聚焦的图片比较漂亮，会经常在电脑上更新。但是，保存Windows聚焦的图片是一件很麻烦的事情：

- Windows聚焦的图片存储路径太复杂，必须记在记事本上，用的时候复制粘贴一遍；
- 进入了图片的存储路径之后，会发现全都是没有后缀名的文件，必须手动添加```.jpg```的后缀才能得到图片；
- 变成图片格式之后，才会发现很多图片其实只是某一张完整图片的一个部分，比如```488x216```这种大小，找了好久才找到真正要的那张

这个小工具可以直接扫描该路径，剔除掉那些并不完整的图，把其它图片保存到当前目录，非常省心。

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
