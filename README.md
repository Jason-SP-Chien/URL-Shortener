# URL Shortener

This is a simple application which acts like popular websites offering URL shortening services.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

First, you will need to setup the Environments.

* [Python](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Sqlite](https://www.sqlite.org/)

Following the installation steps of websites above, before running your program, your should need to create your own database.
```
sqlite3 DatabaseName.db
```
And then, to exit sqlite3, you can enter the command:
```
.quit
```
After your database is created, your program should be able to work; however, if you want to use web UI, you should build your own html template in the templates folder.

## Running the tests

Test your application on localhost. 
```
python your_main.py
```

Then, if you are using the web UI version, you can open a webpage in your browser, and the localhost address is:
```
http://127.0.0.1:5000/
```
Enter the URL in the box and submit.

Also, if you are trying to use command line version, you can enter the command below:
```
curl -d "url=http://www.example.com/" "http:/127.0.0.1:5000/"
```
P.S. The web UI version of application.py is on master; on the other hand, the command line version of application.py is on the branch.

## Deployment

I deploy this application on [Elastic Beanstalk on Amazon Web Services](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html). Therefore, if you want to deploy on AWS, you can follow the steps on its website. Or, you can try other popular IaaS provider such as, [Google Cloud Platform](cloud.google.com), [Microsoft Azure](https://azure.microsoft.com/zh-tw/free/), [Digital Ocean](www.digitalocean.com).

## My URL Shortener on AWS

For web UI users, you can go to [URL Shortener web UI](http://url-shortener-web.xpjahimgtj.us-east-2.elasticbeanstalk.com/).

For command line users, you can send your requests by curl:
```
curl -d "url=http://www.example.com/" "http://url-shortener-cmd.xpjahimgtj.us-east-2.elasticbeanstalk.com/"
```

The results will be displayed after the requests.

P.S. Remember to enter a valid website, and the scheme is essential too. (Like http, https, etc.)

## Acknowledgments and References

* Huge thanks to [narenaryan](https://github.com/narenaryan/Pyster) and his/her [blog](https://impythonist.wordpress.com/2015/10/31/building-your-own-url-shortening-service-with-python-and-flask/), most codes are based on his/her program.
* Also, to start on flask [TAIKER'S BLOG](https://blog.taiker.space/python-shi-yong-python-he-flask-she-ji-restful-api/) helps me a lot.
* Thanks to [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#file-readme-template-md) for the readme template.
* Last but not least, every information and problem I encounter can be found on Google, Flask, Sqlite3, AWS's documentations, which give me a big hand.
