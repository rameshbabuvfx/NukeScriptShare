# NukeShareScript

The NukeScriptShare tool makes it simple to share nuke nodes within a connected network. Artists can quickly paste the received nodes and use them.
This tool is storing data in the MongoDB database.

After two days, the data is automatically deleted from the database to free up space. Add to favourites if you want to save nodes for a long time. Deleting the favourites option is available.

![share nodes01](https://user-images.githubusercontent.com/73053972/147654988-c0b58a32-71be-4bc0-bda2-18d0694679f6.png)

## Requirements

* MongoDB Database.
* Database management tool.
  `Preferred :MongoDB Compass, Robo 3T`.
* Database with `nuke_script_share`.
* Collection `nuke_scripts`.
* Common server in local network.

## Configuration of the database

* Download MongoDB from this [link](https://www.mongodb.com/try/download/community).

```
https://www.mongodb.com/try/download/community
```

* Install the MongoDB in common server which is local connected to network.
* Download MongoDB Compass.

```
https://www.mongodb.com/try/download/compass
```

* Start the Mongodb server uding mongo command.
* Launch MongoDB Compass connect to `localhost:27017` server.
* Create `nuke_script_share` database.
* And create `nuke_scripts` collection in `nuke_script_share` database.

