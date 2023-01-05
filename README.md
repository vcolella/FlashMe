# FlashME
#### Video Demo:  <https://youtu.be/5fDHbNKyq_o>
#### Description:
FlashMe is a web application that aims to help you study using the flash card method.

Within the application, you can :

- Create sets of cards with name, description and tags
- Create cards and add them to sets
- Display sets of flash cards

## Development:

Initially, FlashMe was intended to be a mobile app, but making it a web application made it more accessible to desktop users.

The front-end was created using HTML, some jQuery and the Bootstrap framework for UX.

The back-end relies on Python running Flask with SQLite. When thinking about the mobile application, I started to design a basic API with its endpoints supplying JSON so that any kind of client (mobile or not) could consume its data.

But with that arrangement I wouldn't be able to take advantage of the Bootstrap framework and would have to learn a new technology. So in order to save time, I decided to go with the easier.

The implemented features are very, very simple, but provide a proof of concept, if you may call it that way.

I have some features in mind to be added in the future so that this application might actually interest some user.

If you want to provide a PR with any improvements, I'd be more than happy to review it. 

#### TODO

Future features to be added :

- [ ] Search sets by name, description or tags
- [ ] Randomize set order
- [ ] Edit and remove cards in set
- [ ] Delete sets
- [ ] 

## How to use:

1. After registering and loggin in, create a new set by clicking `New Set`.

2. Now add some cards by clicking `New Card`, selecting your *Set* and filling the flash card fields.

3. Done ! Now click `Sets` to list all your sets and start studying with them !

- You can edit a *Set* description and tags by "creating a new set" with the same name !


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```



# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Just clone the repo with HTTPS:

```
git clone https://github.com/vcolella/FlashMe.git
```

or with SSH:

```
git clone git@github.com:vcolella/FlashMe.git
```


### Prerequisites

Everything you need to run is an updated Web Browser, an updated distribution of Python and the modules listed in the [requirements](/requirements.txt) file, so in your project directory run:

```
pip install -r ./requirements.txt
```


### Coding style

Not much thought was given to code style besides some basic readability. In future updates of the codebase, some standards should probably be used.

## Deployment

Just push it to your branch and create a PR in Github.

## Built With

* [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Back-End
* [Bootstrap](https://getbootstrap.com/) - Front-End
* [SQLite](https://www.sqlite.org/index.html) - Used for the databases

## Versioning

I use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/vcolella/FlashMe/tags). 

## Authors

* **Victor Colella** - *Initial work* - [vcolella](https://github.com/vcolella)

See also the list of [contributors](https://github.com/vcolella/FlashMe/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used (CS50 staff)
