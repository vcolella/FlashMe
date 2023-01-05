# FlashME
#### Video Demo:  <https://youtu.be/5fDHbNKyq_o>
#### Description:
FlashMe is a web application that aims to help you study using the flash card method.

Within the application, you can :

- Create sets of cards with name, description and tags
- Create cards and add them to sets
- Display sets of flash cards

#### Development:

Initially, FlashMe was intended to be a mobile app, but making it a web application made it more accessible to desktop users.

The front-end was created using HTML, some jQuery and the Bootstrap framework for UX.

The back-end relies on Python running Flask with SQlite. When thinking about the mobile application, I started to design a basic API with its endpoints supplying JSON so that any kind of client (mobile or not) could consume its data.

But with that arrangement I wouldn't be able to take advantage of the Bootstrap framework and would have to learn a new technology. So in order to save time, I decided to go with the easier.

The implemented features are very, very simple, but provide a proof of concept, if you may call it that way.

I have some features in mind to be added in the future so that this application might actually interest some user.

If you want to provide a PR with any improvements, I'd be more than happy to review it. 

#### How to use:

1. After registering and loggin in, create a new set by clicking `New Set`.

2. Now add some cards by clicking `New Card`, selecting your *Set* and filling the flash card fields.

3. Done ! Now click `Sets` to list all your sets and start studying with them !

- You can edit a *Set* description and tags by "creating a new set" with the same name !

#### TODO

Future features to be added :

- [ ] Search sets by name, description or tags
- [ ] Randomize set order
- [ ] Edit and remove cards in set
- [ ] Delete sets
- [ ] 