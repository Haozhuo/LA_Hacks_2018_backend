This is the backend implementation for the LA Hacks project for my team. The project is an iOS app that aims to monitor drivers' brainwaves when they're driving and alter them when the driver is likely to be tired.

End-point documentation:
1. GET http://some_ip_address/api/start_trip/[username]
   This end-point is used when the user click the start trip button. It creates a new trip under this user in the database.
   Return a JSON object like this:
   {"data":"1"}

   If there is a backend error, the value would be "-1". If not, the value would be "1"

2. GET http://some_ip_address/api/end_trip/[username]
   This end-point is used when the user click the end trip button.
   Return a JSON object that returns all data points for this trip. The time is sorted from earliest to latest.

[
    {
        time: "2018-03-31 23:17:12",
        avg_alpha: 0.12
    },
    {
        time: "2018-03-31 23:17:15",
        avg_alpha: 0.20
    },
    {
        time: "2018-03-31 23:17:17",
        avg_alpha: 0.30
    },
    {
        time: "2018-03-31 23:17:20",
        avg_alpha: 0.50
    }
]

3. GET http://some_ip_address/api/send_data/[username]?v1=[value1]&v2=[value2]&v3=[value3]&v4=[value4]

   This end-point is used when the mobile side wants to send signals to the backend.
   Return A JSON object like this:
   {"status": "1"} or {"status": "-1"}

    in which "-1" indicates the driver needs to be awaken and "1" indicates everything is fine.
   
