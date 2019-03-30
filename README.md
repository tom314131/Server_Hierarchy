# Server_Hierarchy
Creating a UDP local server that know answering questions.
The client send a message to the local server and ask ip the ip of a url adress and the server return him the answer by looking in his cache mapping file. (map between ip and url)
If the server doesn't know the answer it goes to his parent server and ask him,(The parent server has all the urls and their ip).
The parent server return the right ip of the url and send it to the local server, and the server returns it to the client. Meanwhile the local server save the url an the ip in his cahce so the next time the client request the ip of the same url the local server won't need to turn to the parent server.
