# Project Title

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

## Deployment

I deploy this application on [Elastic Beanstalk on Amazon Web Services](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html). Therefore, if you want to deploy on AWS, you can follow the steps on its website. Or, you can try other popular IaaS provider such as, [Google Cloud Platform](cloud.google.com), [Microsoft Azure](https://azure.microsoft.com/zh-tw/free/), [Digital Ocean](www.digitalocean.com).

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
