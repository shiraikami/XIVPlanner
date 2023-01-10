# XIVPlanner

## API List
- https://xivapi.com/ - This will be used to search up the gear the user wants to save. Also comes with a lot more data that comes from the game’s data.

- https://articles.fflogs.com/help/api-documentation - This is a third party website that essentially parses the logs from the game and ranks the damage you did in raid. It has combat analysis and statistics over a large range of raids and ranks the damage you do. I will use this to get the data for a specific character and how well they did in a raid.

### Instructions
- Set up a new client from the client management page from the FFLogs API docs provided above. Get a client_id and client_secret and add both as variables ("CLIENT_ID",  "CLIENT_SECRET") to a new file called "authenticate.py" in the root of the folder.
- Download the packages from requirements.txt.
- Create a new postgresql database: "xivplanner".
- Run the seed.py. 
- Can run the server with "flask run".
