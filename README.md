# Medredirect

Meddirect is a script based on python3, filter ip's with country Names and block them after many times access for 12h.

### Installation

Medredirect requires [python](https://fr.wikipedia.org/wiki/Python_(langage)) v3 to run.

Install python & pip git.

```sh
$ sudo apt install python3
$ sudo apt install python3-pip
$ sudo apt install git
```

Install modules ...

```sh
$ pip3 install flask
```

Download script ...

```sh
$ git clone https://github.com/medsouaidi/Medredirect.git
$ cd Medredirect
```

Install script ...

```sh
$ sudo bash ./install.sh 
```


### Run server

To run server using port http and many times is 10 :
```sh
$ sudo med.py run 80 10
```
Out put:
```sh
[x] Running Port : 80 | Many's : 10
nohup: appending output to 'nohup.out'
```
Out server address in your preferred browser.

```sh
http://DOMAIN.COM/goto?href=http://google.com/&contry=MA
```
```sh
Params : href = http://google.com / #REPLACE GOOGLE TO YOUR OFFRE CPA OR REDIRECT
Params Contry = MA / #REPLACE MA TO CONTRY WANNA ACCESS TO OFFRE CPA
```

To run server using port HTTPS and many times is 5 :
```sh
https://DOMAIN.COM/goto?href=http://google.com/&contry=MA
```
To run server using port 7070 and many times is 77 :
```sh
http://DOMAIN.COM:7070/goto?href=http://google.com/&contry=MA
```
### Update server

To update port from any port to 8080 and any many times to 10 :
```sh
$ sudo med.py update 8080 10
```
Out put :
```sh
[x] Killed 
[x] Updated Port  8080 | Many's  10
nohup: appending output to 'nohup.out'
```

### Kill server

To Kill script (provider) :
```sh
$ sudo med.py kill
```
Out put :
```sh
[x] KILLED
```


**Contact!**
   [Facebook]: <https://www.facebook.com/M0h4mm33d/>
   [Twitter]: <https://twitter.com/M0h4mm33d/>
   [Mail]: <medmedsouaidi@gmail.com>
