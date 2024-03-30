# Product Requirements Documentation

**Summary**

| Field        | Detail                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------ |
| Project Name | Bill Tracker                                                                                     |
| Description  | A database where users can enter their bill details and show their catalog of bills |
| Developers   | Rachel Yang                                                                     |
| Live Website |                                                                                                  |
| Repo-back    | https://github.com/LilyX2023/Mini-project-bill-tracker-backend                                                  |
| Repo-front   | https://github.com/LilyX2023/Mini-project-bill-tracker                                                 |

## Problem Being Solved and Target Market

This app can track all type of bills. Ac

## User Stories

- Users should be able to see the site on desktop and mobile
- Users can create a new entry
- Users can see all their bill on the dashboard
- Users can see a detail page of selected bill
- Users can update the bill
- Users can delete the bill

## Route Tables

Server url: 

| Endpoint          | Method | Response                                        | Other                               |
| ----------------- | ------ | ----------------------------------------------- | ----------------------------------- |
| /bills     | GET    | JSON of all items                               |                                     |
| /bils     | POST   | Create new item return JSON of new item         | body must include data for new item |
| /bills/:id | GET    | JSON of item with matching id number            |                                     |
| /bills/:id | PUT    | update item with matching idea, return its JSON | body must include updated data      |
| /bills/:id | DELETE | delete the item with the matching id            |                                     |