<img src="https://telegra.ph/file/110ca1738ab92da7483c0.jpg" align="right" width="200" height="200"/>

# Shasa Music Bot <img src="https://img.shields.io/github/v/release/MdNoor786/ShasaVcPlayer?color=black&logo=github&logoColor=black&style=social" alt="LICENSE">

[Shasa Music Bot](https://github.com/MdNoor786/ShasaVcPlayer) is a Powerful Telegram Music+Video Bot written in Python using Pyrogram and Py-Tgcalls by which you can stream songs, video and even live streams in your group calls via various sources.

* Youtube, Soundcloud, Apple Music, Spotify, Resso and Telegram Audios & Videos support.
* Written from scratch, making it stable and less crashes.
* Attractive thumbnails, fonts and images,  making experience more user-friendly and interactive.
* Loop, Shuffle, Specific Skip, Playlists etc support
* Global, Users, Chats Top 10 played tracks stats
* Multi-Language support


# 🔗 An Overview

Here's a brief high-level overview of the Shasa Music Bot:

This project is based on [Pyrogram](https://github.com/pyrogram) and [Py-Tgcalls](https://github.com/pytgcalls/pytgcalls) . Pyrogram is a modern, elegant and asynchronous MTProto API framework. 

* For database, Shasa uses the MongoDB to store data and keys. [MongoDB](https://www.mongodb.com/) is a document database with the scalability and flexibility that you want with the querying and indexing that you need.
* Project uses the bs4 web scrapping for getting many platform details. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is a Python library for pulling data out of HTML and XML files.
* The project uses the font [`Poppins`](../assets/font.ttf) as its main font for the thumbnails.
* The projects uses attractive images and icons which you cen get in [assets](../assets/) directory.

For more information on the technologies that power the Shasa Music Bot, check out the [Docs](https://notreallyshikhar.gitbook.io/ShasaVcPlayer/).



# ⚡️ Getting Started
    
> If you want to start working with Shasa Music Bot you can either fork or import repo .
> The official [documentation site](https://notreallyshikhar.gitbook.io/ShasaVcPlayer/) contains a lot of information. The best place to start is from the deployment section.
> If you'd like to talk to us, join us on our [Telegram Group](https://t.me/LionXsupport)


## 🖇 Prerequisites
    
> In order to avoid conflicts in your project, you must have/installed

- [Python3.9](https://www.python.org/downloads/release/python-390/)
- [Telegram API Key](https://docs.pyrogram.org/intro/setup#api-keys)
- [Telegram Bot Token](https://t.me/botfather)
- [MongoDB URI](https://telegra.ph/How-To-get-Mongodb-URI-04-06)
- [Pyrogram String Session](https://notreallyshikhar.gitbook.io/ShasaVcPlayer/deployment/string-session)
    

## 🖇 Generating Pyrogram String Session

- Generate a Pyrogram String Session via [Replit](https://replit.com/@NotReallyShikhar/Shasa-Music-String-Gen)

- Generate a Pyrogram String Session via [Telegram String Generation Bot](https://t.me/LionXStringbot)
    
    
## 🖇 Heroku Deployment
    
<h4>Click the button below to deploy Shasa on Heroku!</h4>    
<a href="https://Shasa.tech/deploy/"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a>
    
> Click on buttons below to expand and  detailed explanation process. !

 
<details>
    <summary><b> Detailed Heroku Depoyment Process » </b></summary>

<img src="https://telegra.ph/file/672efa7b8160ed39c6e86.jpg" align="right" width="350" height="700"/>
    
### 🚀 Deploy Process
- Click on the deploy button above and login to your [heroku account](https://heroku.com/login) .
- Fill your values there.
- If you don't know how to get config vars : [Please refer here](../config/README.md)
- Make sure you fill correct values.
- Click on **Deploy** button.
- Please wait till the app gets deployed on heroku. Deploying can take upto **2-3 mins**..
- When your app is successfully deployed, click on **Manage App** button.
 
    
### 🚀 Booting Process
- Search for **Resources** Tab inside your app. ( Check Image for more details) 
- Click on the **Pencil Icon** under resources section.
- Turn **on** the **switch** present there near pencil icon.
- Congrats your Music Bot is now **Booting**.

    
### 🚀 Checking Logs
- After Turning on your booting .
- Click on the **More Button** present at top right corner .
- Click on the **View Logs** button from the drop down menu.
- You check your logs there! 
- Click on save button there at bottom to save your logs and forward it to us on [@LionXsupport](https://t.me/LionXsupport) if you face any problem
    
</details>
    
## 🖇 VPS Deployment
    
> Checkout [Docs](https://notreallyshikhar.gitbook.io/ShasaVcPlayer/deployment/local-hosting-or-vps) for Detailed Explanation on VPS Deploy
    

```console
shikhar@MacBook~ $ git clone https://github.com/notreallyshikhar/ShasaVcPlayer
shikhar@MacBook~ $ cd ShasaVcPlayer
shikhar@MacBook~ $ sudo bash setup
```
> Setup will install each and every requirement, nodejs and pip packages automatically. After successfull installation of requirements , setup will ask you to input your vars. 
> Please input your vars correctly.
    
```console
shikhar@MacBook~ $ bash start
```

> Not Getting VPS Method? [Watch Tutorial](https://t.me/LionXsupport/2275)
    
    
<img src="https://telegra.ph/file/6b75b57da50ef1183fcdc.jpg" align="center">


## 🏷 Support

Reach out to the maintainer at one of the following places:

- [GitHub Issues](https://github.com/MdNoor786/ShasaVcPlayer/issues/new?assignees=&labels=question&template=SUPPORT_QUESTION.md&title=support%3A+)
- Contact options listed on [this GitHub profile](https://github.com/MdNoor786)
- [Telegram Support](https://t.me/LionXsupport)

## 🎗 Project assistance

If you want to say **thank you** or/and support active development of ShasaVcPlayer:

- Add a [GitHub Star](https://github.com/MdNoor786/ShasaVcPlayer) to the project.
- Fork the Repo :)
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or your personal blog.

PS: You can buy me a coffee too :) 
<p><a href="https://www.buymeacoffee.com/notreallysy" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 35px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a></p>

Together, we can make ShasaVcPlayer **better**!

## ✍🏻 Contributing

First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.

Please read [our contribution guidelines](CONTRIBUTING.md), and thank you for being involved!

## 👨🏻‍💻 Authors & contributors

The original setup of this repository is by [Team Shasa](https://github.com/MdNoor786).

For a full list of all authors and contributors, see [the contributors page](https://github.com/MdNoor786/ShasaVcPlayer/contributors).

## ⚠️ Security

ShasaVcPlayer follows good practices of security, but 100% security cannot be assured. ShasaVcPlayer is provided **"as is"** without any **warranty**. Use at your own risk.

For more information and to report security issues, please refer to our [`SECURITY.md`](SECURITY.md)


## 🗂 License

This project is licensed under the **GNU General Public License v3**. All designs were created by [@NotReallyShikhar](https://github.com/NotReallyShikhar) .

See [LICENSE](../LICENSE) for more information.

## 📑 Acknowledgements

Special thanks to these amazing projects/people which/who vchelp power Shasa Music Bot:

- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [Py-Tgcalls](https://github.com/pytgcalls/pytgcalls)
- [CallsMusic Team](https://github.com/Callsmusic)
- [TheHamkerCat](https://github.com/TheHamkerCat)
- [Charon Baglari](https://github.com/XCBv021)





Reminder that you are great, you are enough, and your presence is valued. If you are struggling with your mental health, please reach out to someone you love and consult a professional.
  
  
