
# Server Port Checker

This code will check if a certain port of a server is open, if it is it will print "Server is Online" if it isnt it will print "Server is Offline" I couldnt find one that used a API So I created my own


## Installation

Install the requirements for running the API

```bash
    pip install uvicorn requests fastapi
```
    
## Deployment

To deploy this API, go to https://render.com/, sign up, and verify email.





![App Screenshot](https://cdn.discordapp.com/attachments/1087714570291904522/1087714658296795227/image.png)

Then create a "Web Services" connect your github, and connect the repo that you forked or created, once done edit the settings to whatever you want until you get up to here !

![App Screenshot](https://cdn.discordapp.com/attachments/1075750867640258560/1087729112992460903/image.png)

Within the **Build Command** place 
```
    pip install uvicorn requests fastapi
```
and within the **Start Command** place (be sure to change 'main' with the version u are using e.g uvicorn setipandport:app --host 0.0.0.0)
```
    uvicorn main:app --host 0.0.0.0
```
Select the tier u want and then deploy it, wait for everything to setup **Around 5-10 mins** then visit the url given to you, you should see a response like this

![App Screenshot](https://cdn.discordapp.com/attachments/1082433859687284756/1087719869262336100/image.png)

The response will change according to if the port is open or not

For any help contact me on Discord AX200M#9061
