darshan lal

1001667684

Python is used to code the program

The program contains an expand function 
when input is provided through the console the program fetches the file and takes out the details into a dictionary.
Then source is pushed into the fringe and then expand function is called
Expand function uses the heap queue as well as the heuristics(if provided) to find an optimal path

To execute the program version5.py

	write this command on the terminal
		python version5.py
	Then provide the input
		ex: 1) With heuristics: 
		find_route input1.txt Bremen Kassel h_kassel.txt
		    2) Without heuristics: 
		find_route input1.txt Bremen Kassel 
		    3) Input with no path between the cities
		find_route input1.txt London Kassel

Note: The program uses heap queue to pop the node with lowest cost that is why if the input without heuristics is provided then the number of nodes may be less than what is expected where as for the inputs with heuristics everything is fine 