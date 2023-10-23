# lp_generator

This project is a Way to make my own work easier, so i dont plan in making a visual interface anytime soon
for now works only with the [greatpages](https://www.greatpages.com.br) software, since i dont work with other services i'm not thinking about other plataform updates for now - but i certainly can if needed

# How to use

Create a csv archive with all the info and insert in the './lp_generator/archives/csv' directory, for now the csv has the name test, and this is what the program will lok for, i do plan to change this in the near future
all the info you need to inser in the csv is link,	model,	page_name,	city and	date

## link
this info is the link to the model page you should have in your account, this page will be cloned and edited to add the info you want in it

## model
This is the name of the model, i strongly advise into keeping this into a standard in the program and in the plataform

## page_name
This info is the one you should use to rename the page in the greatpages plataform, again i advise you to have a solid standard for this one

## city
Since i work with events this one is a information that i'm going to insert into the landing page

## date
As City, a info that is going to be inserted in the final model, but also will be organized to be put into the page name for rastreability

# How it Works
Once you have the data correctly organized in the csv archive, you will need a new archive in the './lp_generator/models' folder that will do the work in the page, i personaly use selenium for my automations
so this is what you will see here
when you have all in place, just start the program, make login through the prompt shell tha will pop up and let the program handle the labor for you
