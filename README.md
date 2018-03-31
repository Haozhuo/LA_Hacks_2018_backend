End-point documentation:
1. GET http://167.99.161.100:8000/api/start_trip/\[username\]
   This end-point is used when the user click the start trip button. It creates a new trip under this user in the database.
   Return a JSON object like this:
   {"data":"1"}

   If there is a backend error, the value would be "-1". If not, the value would be "1"

2. GET http://167.99.161.100:8000/api/end_trip/\[username\]
   This end-point is used when the user click the end trip button.
   Return a JSON object that returns all data points for this trip

   NOTE: This is not implemented yet

3. GET http://167.99.161.100:8000/api/send_data/\[username\]?v1=\[value1\]&v2=\[value2\]&v3=\[value3\]&v4=\[value4\]

   This end-point is used when the mobile side wants to send signalsto the backend.
   Return A JSON object like this:
   {"status": "1"} or {"status": "-1"}

    in which "-1" indicates the driver needs to be awaken and "1" indicates everything is fine.
   
