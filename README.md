This program generates a proper DNS query response, it does not send it. This was mainly an exercise in understanding dns queries and being able to decode and encode reponses in bits/bytes
To run this program, run it regularly on terminal to start the server. Then, open another terminal window to act as the client and enter 'dig "WEBSITE_OF_CHOICE" @127.0.0.1'
A dns query will be sent to the program, the information will be printed 3 times in an attempt from the client to get a response, but it will disconnect because a response will not be received.
This program can be added on to in the future to send responses and can be turned into a functioning dns server. This code is predominantly based on a youtube tutorial from 'HowCode'.

Link to code tutorial: https://www.youtube.com/watch?v=HdrPWGZ3NRo&list=PLBOh8f9FoHHhvO5e5HF_6mYvtZegobYX2

This has served as a phenomenal learning experience in working with dns queries, sockets, ports, receiving data (and understanding its formatting) as well as bit compression
and decompression.